#!/usr/bin/env python3
"""Score the 12 new diseases added to the 46-disease cohort.

Generates match_ORPHA*.md files in output/ for each new disease,
then appends their rows and sections to the existing output/SUMMARY.md.

Usage from repo root:
    uv run python score_new_diseases.py
"""
from __future__ import annotations

import csv
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "src"))

from nanogt.db import setup
from nanogt.disease import fetch_disease
from nanogt.gene import GeneInfo, fetch_gene
from nanogt.mechanism import lookup_mechanism
from nanogt.report import MatchResult, save_report
from nanogt.scoring import rank_programs

ROOT = pathlib.Path(__file__).parent
OUTPUT = ROOT / "output"
COHORT_CSV = ROOT / "data" / "disease_cohort_46.csv"
SUMMARY_MD = OUTPUT / "SUMMARY.md"

# The 12 new disease ORPHA IDs (not yet scored)
NEW_IDS = {
    "ORPHA:98878",   # Hemophilia A
    "ORPHA:586",     # Cystic fibrosis
    "ORPHA:141",     # Canavan disease
    "ORPHA:79241",   # Biotinidase deficiency
    "ORPHA:845",     # Tay-Sachs disease
    "ORPHA:905",     # Wilson disease
    "ORPHA:213",     # Nephropathic cystinosis
    "ORPHA:618891",  # ASMD / Niemann-Pick A/B
    "ORPHA:646",     # Niemann-Pick disease type C
    "ORPHA:912",     # Zellweger syndrome
    "ORPHA:93598",   # Primary hyperoxaluria type 1
    "ORPHA:886",     # Usher syndrome type 1B
}


def load_new_cohort_rows() -> list[dict[str, str]]:
    with COHORT_CSV.open(newline="") as f:
        return [r for r in csv.DictReader(f) if r["orphanet_id"] in NEW_IDS]


def build_table_row(r: MatchResult, kind: str) -> str:
    valid = [s for s in r.scores if s.confidence != "fail"]
    m1 = valid[0] if valid else None
    mechanism = lookup_mechanism(r.disease.orphanet_id, r.gene.symbol)
    if not m1:
        no_result_label = (
            "mechanism_hard_fail"
            if mechanism.gene_addition_compatibility == "incompatible"
            else "packaging_hard_fail"
        )
    return (
        f"| {kind} | {r.disease.name} | {r.disease.orphanet_id} | {r.gene.symbol} "
        f"| {mechanism.mechanism_category} "
        f"| {mechanism.gene_addition_compatibility} "
        f"| {r.gene.cds_length_bp or '?'} "
        f"| {m1.program_name if m1 else '—'} "
        f"| {m1.vector if m1 else '—'} "
        f"| {f'{m1.composite_score:.1f}/10' if m1 else '—'} "
        f"| {m1.confidence if m1 else no_result_label} |"
    )


def build_disease_section(r: MatchResult) -> str:
    mechanism = lookup_mechanism(r.disease.orphanet_id, r.gene.symbol)
    lines = [
        f"### {r.disease.name} ({r.disease.orphanet_id})",
        (
            f"**Gene:** {r.gene.symbol} | "
            f"**Mechanism:** {mechanism.mechanism_category} | "
            f"**CDS:** {r.gene.cds_length_bp or '?'} bp | "
            f"**Inheritance:** {', '.join(r.disease.inheritance) or 'unknown'} | "
            f"**Tissues:** {', '.join(r.disease.affected_tissues) or 'unknown'}"
        ),
        "",
        (
            f"**Mechanism evidence:** {mechanism.evidence_summary} "
            f"Source: {mechanism.evidence_citation}"
            + (f" ({mechanism.evidence_url})" if mechanism.evidence_url else "")
        ),
        "",
    ]
    valid = [s for s in r.scores if s.confidence != "fail"][:5]
    if not valid:
        lines.append(
            "No single-vector precedent survived the packaging hard gate. "
            "For this disease, the likely development route requires an oversized-cargo "
            "strategy such as micro-gene design, dual-vector delivery, ex vivo/lentiviral "
            "delivery if tissue-appropriate, or non-viral/editing approaches outside the "
            "current v0.1 catalog."
        )
    for i, s in enumerate(valid, 1):
        lines.append(f"{i}. **{s.program_name}** ({s.vector}) — {s.composite_score:.1f}/10 [{s.confidence}]")
    lines.append("")
    return "\n".join(lines)


def append_to_summary(new_results: list[tuple[MatchResult, str]]) -> None:
    summary = SUMMARY_MD.read_text()

    # 1. Remove the pending note (we now have real results)
    summary = re.sub(
        r"\n> \*\*Note:\*\* 12 new diseases.*?\n\n",
        "\n",
        summary,
        flags=re.DOTALL,
    )

    # 2. Insert new table rows just before the closing --- separator
    new_rows = "\n".join(build_table_row(r, kind) for r, kind in new_results)
    summary = summary.replace("\n---\n\n## Disease Sections", f"\n{new_rows}\n\n---\n\n## Disease Sections")

    # 3. Append new disease sections at the end
    new_sections = "\n".join(build_disease_section(r) for r, _ in new_results)
    summary = summary.rstrip() + "\n\n" + new_sections

    SUMMARY_MD.write_text(summary)
    print(f"  SUMMARY.md updated ({len(new_results)} diseases appended)")


def main() -> None:
    print("Initialising database...")
    conn = setup()
    n_programs = conn.execute("SELECT COUNT(*) FROM gt_programs").fetchone()[0]
    n_vectors = conn.execute("SELECT COUNT(*) FROM vectors").fetchone()[0]
    print(f"  {n_vectors} vectors, {n_programs} GT programs loaded.\n")

    cohort_rows = load_new_cohort_rows()
    print(f"Scoring {len(cohort_rows)} new diseases...\n")

    results: list[tuple[MatchResult, str]] = []

    for row in cohort_rows:
        orpha_id = row["orphanet_id"]
        kind = row["cohort_role"]
        print(f"Processing {orpha_id} ({row['disease_name']})...")

        disease = fetch_disease(orpha_id)
        if not disease:
            print("  WARN: not found, skipping")
            continue

        gene_sym = row.get("gene") or (disease.gene_symbols[0] if disease.gene_symbols else None)
        gene = fetch_gene(gene_sym) if gene_sym else GeneInfo("unknown", None, None, None, None, False, [], [], [], [])

        scores = rank_programs(disease, gene, conn)
        result = MatchResult(disease=disease, gene=gene, scores=scores, top_n=5)
        results.append((result, kind))

        path = save_report(result, OUTPUT)
        top = next((s for s in scores if s.confidence != "fail"), None)
        if top:
            print(f"  → {top.program_name} ({top.vector}) {top.composite_score:.1f}/10 [{top.confidence}]")
        else:
            print(f"  → no compatible precedent after hard gates")
        print(f"  Report: {path.name}\n")

    if results:
        append_to_summary(results)

    print(f"\nDone. {len(results)} new disease reports written to {OUTPUT}/")
    print("Run regenerate_match_pdfs.py to build PDFs for the new reports.")


if __name__ == "__main__":
    main()
