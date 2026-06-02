#!/usr/bin/env python3
"""
Standalone runner — generates GT match results for all target diseases.

Usage (from repo root):
    pip install -e . --quiet
    python run_results.py

Or with the existing venv:
    source .venv_\(my_python_environment\)/bin/activate
    pip install typer requests rich jinja2 pydantic --quiet
    python run_results.py
"""
import pathlib
import sys

# Allow running from repo root without install
sys.path.insert(0, str(pathlib.Path(__file__).parent / "src"))

from nanogt.db import setup
from nanogt.disease import fetch_disease
from nanogt.gene import fetch_gene, GeneInfo
from nanogt.scoring import rank_programs
from nanogt.report import MatchResult, save_report, generate_report

OUTPUT = pathlib.Path("output")

# ── Validation diseases (approved GT exists — positive controls) ──────────
VALIDATION_DISEASES = [
    "ORPHA:70",     # Spinal Muscular Atrophy       → Zolgensma (approved)
    "ORPHA:306",    # Hemophilia B                  → Hemgenix (approved)
]

# ── Discovery diseases (NO approved/late-stage GT trial) ─────────────────
DISCOVERY_DISEASES = [
    "ORPHA:1946",   # Kohlschütter-Tönz syndrome    (ROGDI, CNS)
    "ORPHA:578",    # Mucolipidosis type IV          (MCOLN1, CNS/retina)
    "ORPHA:61",     # Alpha-mannosidosis             (MAN2B1, CNS/liver)
    "ORPHA:511",    # Maple syrup urine disease      (BCKDHA, liver/CNS)
    "ORPHA:309",    # Salla disease                  (SLC17A5, CNS)
    # Previously analysed (partial precedent, no approved GT):
    "ORPHA:324",    # Fabry disease                  (GLA, lysosomal)
    "ORPHA:79269",  # Sanfilippo A                   (SGSH, CNS lysosomal)
    "ORPHA:1060",   # Crigler-Najjar type I          (UGT1A1, liver)
]

DISEASES = VALIDATION_DISEASES + DISCOVERY_DISEASES

def main():
    print("Initialising database...")
    conn = setup()
    n_programs = conn.execute("SELECT COUNT(*) FROM gt_programs").fetchone()[0]
    n_vectors  = conn.execute("SELECT COUNT(*) FROM vectors").fetchone()[0]
    print(f"  {n_vectors} vectors, {n_programs} GT programs loaded.\n")

    results = []
    for orpha_id in DISEASES:
        print(f"Processing {orpha_id}...")
        disease = fetch_disease(orpha_id)
        if not disease:
            print(f"  WARN: not found, skipping")
            continue

        gene_sym = disease.gene_symbols[0] if disease.gene_symbols else None
        if gene_sym:
            gene = fetch_gene(gene_sym)
        else:
            gene = GeneInfo("unknown", None, None, None, None, False, [], [], [], [])

        scores = rank_programs(disease, gene, conn)
        result = MatchResult(disease=disease, gene=gene, scores=scores, top_n=5)
        results.append(result)

        path = save_report(result, OUTPUT)
        top = next((s for s in scores if s.confidence != "fail"), None)
        print(f"  {disease.name}: top match = {top.program_name if top else 'none'} "
              f"({top.composite_score:.1f}/10 [{top.confidence}])" if top else "  no match")
        print(f"  Report saved to {path}\n")

    # Write summary
    _write_summary(results, OUTPUT)
    print(f"\nDone! All reports in ./{OUTPUT}/")
    print(f"  Open output/SUMMARY.md for the cross-disease overview.")

def _write_summary(results, output_dir):
    validation_ids = {d.replace("ORPHA:", "") for d in VALIDATION_DISEASES}
    lines = [
        "# NanoGT Results: Cross-Disease GT Precedent Matching",
        "",
        "**Algorithm:** 6-dimension scoring (packaging fit, tissue tropism, protein class,",
        "pathway similarity, inheritance compatibility, approval precedent). Max score = 10.",
        "",
        "## Summary Table",
        "",
        "| Type | Disease | ORPHA | Gene | CDS (bp) | #1 Precedent | Score | Confidence |",
        "|------|---------|-------|------|----------|--------------|-------|-----------|",
    ]
    for r in results:
        valid = [s for s in r.scores if s.confidence != "fail"]
        m1 = valid[0] if valid else None
        kind = "Validation ✓" if r.disease.orphanet_id.replace("ORPHA:", "") in validation_ids else "Discovery"
        lines.append(
            f"| {kind} | {r.disease.name} | {r.disease.orphanet_id} | {r.gene.symbol} "
            f"| {r.gene.cds_length_bp or '?'} "
            f"| {m1.program_name if m1 else '-'} "
            f"| {f'{m1.composite_score:.1f}/10' if m1 else '-'} "
            f"| {m1.confidence if m1 else '-'} |"
        )
    lines += ["", "---", "", "## Validation Results (positive controls)", ""]
    for r in results:
        if r.disease.orphanet_id.replace("ORPHA:", "") not in validation_ids:
            continue
        _append_disease_section(lines, r)
    lines += ["", "---", "", "## Discovery Results (no approved GT)", ""]
    for r in results:
        if r.disease.orphanet_id.replace("ORPHA:", "") in validation_ids:
            continue
        _append_disease_section(lines, r)

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "SUMMARY.md").write_text("\n".join(lines))

def _finalise_summary(lines, output_dir):
    pass  # kept for compatibility

def _append_disease_section(lines, r):
    lines.append(f"### {r.disease.name} ({r.disease.orphanet_id})")
    lines.append(
        f"**Gene:** {r.gene.symbol} | "
        f"**CDS:** {r.gene.cds_length_bp or '?'} bp | "
        f"**Inheritance:** {', '.join(r.disease.inheritance) or 'unknown'} | "
        f"**Tissues:** {', '.join(r.disease.affected_tissues) or 'unknown'}"
    )
    lines.append("")
    valid = [s for s in r.scores if s.confidence != "fail"][:5]
    for i, s in enumerate(valid, 1):
        lines.append(f"{i}. **{s.program_name}** ({s.vector}) — "
                     f"{s.composite_score:.1f}/10 [{s.confidence}]")
    lines.append("")

def _finalise_summary(lines, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "SUMMARY.md").write_text("\n".join(lines))

if __name__ == "__main__":
    main()
