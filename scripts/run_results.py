#!/usr/bin/env python3
"""Generate NanoGT match reports for the reproducible 40-disease cohort.

Usage from the repo root:
    uv run python run_results.py

The main CLI can still be used for any single Orphanet disease ID:
    uv run nanogt match ORPHA:1946 --top 5 -o output
"""
from __future__ import annotations

import csv
import pathlib
import sys

# Allow running from repo root without install
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "src"))

from nanogt.db import setup
from nanogt.disease import fetch_disease
from nanogt.gene import GeneInfo, fetch_gene
from nanogt.mechanism import lookup_mechanism
from nanogt.report import MatchResult, save_report
from nanogt.scoring import rank_programs

ROOT = pathlib.Path(__file__).parent.parent
OUTPUT = ROOT / "output"
COHORT_CSV = ROOT / "data" / "disease_cohort_46.csv"


def load_cohort() -> list[dict[str, str]]:
    """Load the poster/reproducibility cohort from data/disease_cohort_46.csv."""
    with COHORT_CSV.open(newline="") as f:
        return list(csv.DictReader(f))


def main() -> None:
    print("Initialising database...")
    conn = setup()
    n_programs = conn.execute("SELECT COUNT(*) FROM gt_programs").fetchone()[0]
    n_vectors = conn.execute("SELECT COUNT(*) FROM vectors").fetchone()[0]
    print(f"  {n_vectors} vectors, {n_programs} GT programs loaded.\n")

    cohort = load_cohort()
    # clean_generated_reports(OUTPUT)  # skipped: mounted fs may be read-only on old reports
    results: list[MatchResult] = []
    cohort_kind_by_id = {
        row["orphanet_id"].replace("ORPHA:", ""): row["cohort_role"] for row in cohort
    }

    for row in cohort:
        orpha_id = row["orphanet_id"]
        print(f"Processing {orpha_id}...")
        disease = fetch_disease(orpha_id)
        if not disease:
            print("  WARN: not found, skipping")
            continue

        gene_sym = row.get("gene") or (disease.gene_symbols[0] if disease.gene_symbols else None)
        if gene_sym:
            gene = fetch_gene(gene_sym)
        else:
            gene = GeneInfo("unknown", None, None, None, None, False, [], [], [], [])

        scores = rank_programs(disease, gene, conn)
        result = MatchResult(disease=disease, gene=gene, scores=scores, top_n=5)
        results.append(result)

        path = save_report(result, OUTPUT)
        top = next((s for s in scores if s.confidence != "fail"), None)
        if top:
            print(
                f"  {disease.name}: top match = {top.program_name} "
                f"({top.composite_score:.1f}/10 [{top.confidence}])"
            )
        else:
            print(f"  {disease.name}: no compatible precedent after hard gates")
        print(f"  Report saved to {path}\n")

    write_summary(results, OUTPUT, cohort_kind_by_id)
    print(f"\nDone. Reports written to {OUTPUT}")
    print("Open output/SUMMARY.md for the cross-disease overview.")


def clean_generated_reports(output_dir: pathlib.Path) -> None:
    """Remove stale generated match reports before writing a fresh cohort run."""
    if not output_dir.exists():
        return
    for path in output_dir.glob("match_*.md"):
        path.unlink()


def write_summary(
    results: list[MatchResult],
    output_dir: pathlib.Path,
    cohort_kind_by_id: dict[str, str],
) -> None:
    lines = [
        "# NanoGT Results: 46-Disease GT Precedent Matching Cohort",
        "",
        "**Algorithm:** 14-dimension heuristic scoring (v2): packaging fit, tissue tropism, protein class, pathway similarity, mechanism/modality compatibility, inheritance compatibility, approval precedent, vector immunogenicity, therapeutic window, cross-correction, immune privilege, promoter availability, route-of-administration feasibility, and organelle targeting feasibility. Raw max = 21; composite normalised to /10.",
        "",
        "**Interpretation:** The framework ranks which existing clinical gene-therapy program is the closest development precedent for the query disease. It does not claim the top precedent is directly reusable without disease-specific validation, vector engineering, toxicology, and regulatory review.",
        "",
        "## Summary Table",
        "",
        "| Cohort role | Disease | ORPHA | Gene | Mechanism | Gene-addition fit | CDS (bp) | #1 Precedent | Vector | Score | Confidence |",
        "|-------------|---------|-------|------|-----------|-------------------|----------|--------------|--------|-------|------------|",
    ]
    for r in results:
        valid = [s for s in r.scores if s.confidence != "fail"]
        m1 = valid[0] if valid else None
        kind = cohort_kind_by_id.get(r.disease.orphanet_id.replace("ORPHA:", ""), "discovery")
        mechanism = lookup_mechanism(r.disease.orphanet_id, r.gene.symbol)
        # Determine no-result reason: mechanism gate vs packaging gate
        if not m1:
            if mechanism.gene_addition_compatibility == "incompatible":
                no_result_label = "mechanism_hard_fail"
            else:
                no_result_label = "packaging_hard_fail"
        lines.append(
            f"| {kind} | {r.disease.name} | {r.disease.orphanet_id} | {r.gene.symbol} "
            f"| {mechanism.mechanism_category} "
            f"| {mechanism.gene_addition_compatibility} "
            f"| {r.gene.cds_length_bp or '?'} "
            f"| {m1.program_name if m1 else '—'} "
            f"| {m1.vector if m1 else '—'} "
            f"| {f'{m1.composite_score:.1f}/10' if m1 else '—'} "
            f"| {m1.confidence if m1 else no_result_label} |"
        )

    lines += [
        "",
        "---",
        "",
        "## Disease Sections",
        "",
    ]
    for r in results:
        append_disease_section(lines, r)

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "SUMMARY.md").write_text("\n".join(lines))


def append_disease_section(lines: list[str], r: MatchResult) -> None:
    lines.append(f"### {r.disease.name} ({r.disease.orphanet_id})")
    lines.append(
        f"**Gene:** {r.gene.symbol} | "
        f"**Mechanism:** {lookup_mechanism(r.disease.orphanet_id, r.gene.symbol).mechanism_category} | "
        f"**CDS:** {r.gene.cds_length_bp or '?'} bp | "
        f"**Inheritance:** {', '.join(r.disease.inheritance) or 'unknown'} | "
        f"**Tissues:** {', '.join(r.disease.affected_tissues) or 'unknown'}"
    )
    lines.append("")
    mechanism = lookup_mechanism(r.disease.orphanet_id, r.gene.symbol)
    lines.append(
        f"**Mechanism evidence:** {mechanism.evidence_summary} "
        f"Source: {mechanism.evidence_citation}"
        + (f" ({mechanism.evidence_url})" if mechanism.evidence_url else "")
    )
    lines.append("")
    valid = [s for s in r.scores if s.confidence != "fail"][:5]
    if not valid:
        lines.append(
            "No single-vector precedent survived the packaging hard gate. For this disease, the likely development route requires an oversized-cargo strategy such as micro-gene design, dual-vector delivery, ex vivo/lentiviral delivery if tissue-appropriate, or non-viral/editing approaches outside the current v0.1 catalog."
        )
    for i, s in enumerate(valid, 1):
        lines.append(
            f"{i}. **{s.program_name}** ({s.vector}) — {s.composite_score:.1f}/10 [{s.confidence}]"
        )
    lines.append("")


if __name__ == "__main__":
    main()
