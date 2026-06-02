"""Markdown report generator."""

# ── What this file is ──────────────────────────────────────────────────────
# Takes the scores from scoring.py and turns them into a human-readable
# markdown report. Think of it as the "print results" step.
#
# Two functions:
#   generate_report() → builds the markdown text as a string
#   save_report()     → writes that string to a .md file in the output/ folder

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import pathlib

from .disease import DiseaseInfo
from .gene import GeneInfo
from .scoring import ScoreBreakdown


@dataclass
class MatchResult:
    # ← bundles everything needed to generate a report into one object
    disease: DiseaseInfo              # ← the query disease
    gene: GeneInfo                    # ← its causal gene
    scores: list[ScoreBreakdown]      # ← full ranked list of all GT programs (from scoring.py)
    top_n: int = 5                    # ← how many top matches to include in the report (default 5)


def _confidence_emoji(c: str) -> str:
    # ← converts confidence string to a coloured circle emoji for visual clarity
    return {"high": "🟢", "medium": "🟡", "low": "🔴", "fail": "⛔"}.get(c, "⬜")


def generate_report(result: MatchResult) -> str:
    # ← builds the full markdown report as a text string
    d = result.disease
    g = result.gene
    top = [s for s in result.scores if s.confidence != "fail"][:result.top_n]
    # ← filter out hard fails (gene too big for vector), keep only top N

    # ── Header ────────────────────────────────────────────────────────────
    lines = [
        f"# NanoGT Match Report: {d.name}",
        f"",
        f"**Disease:** {d.name} ({d.orphanet_id})  ",
        f"**Primary gene:** {g.symbol}  ",
        f"**Gene CDS:** {g.cds_length_bp or 'unknown'} bp  ",
        f"**Inheritance:** {', '.join(d.inheritance) if d.inheritance else 'unknown'}  ",
        f"**Target tissues:** {', '.join(d.affected_tissues) if d.affected_tissues else 'unknown'}  ",
        f"",
        f"---",
        f"",
        # ── Summary table ─────────────────────────────────────────────────
        f"## Top {len(top)} GT Precedent Matches",
        f"",
        f"| Rank | Program | Vector | Score | Confidence | Approval |",
        f"|------|---------|--------|-------|-----------|----------|",
    ]
    for i, s in enumerate(top, 1):
        lines.append(
            f"| {i} | {s.program_name} | {s.vector} | {s.composite_score:.1f}/10 "
            f"| {_confidence_emoji(s.confidence)} {s.confidence.capitalize()} | {s.approval_status} |"
        )

    lines += ["", "---", ""]

    # ── Per-match detailed breakdown ──────────────────────────────────────
    for i, s in enumerate(top, 1):
        lines += [
            f"## Match #{i}: {s.program_name}",
            f"",
            f"**Precedent disease:** {s.program_disease}  ",     # ← what disease the precedent program was designed for
            f"**Vector:** {s.vector}  ",
            f"**Tissue target:** {s.tissue_target}  ",
            f"**Composite score:** {s.composite_score:.1f} / 10  ",
            f"",
            f"### Score Breakdown",
            f"",
            f"| Dimension | Score | Max | What it measures |",
            f"|-----------|-------|-----|-----------------|",
            f"| Packaging fit | {s.packaging_fit:.2f} | 2.0 | Gene CDS size vs vector cargo capacity |",
            f"| Tissue tropism | {s.tropism_match:.2f} | 2.0 | Vector naturally reaches disease target tissue |",
            f"| Protein class | {s.protein_class_match:.2f} | 2.0 | Same secreted/lysosomal/membrane/intracellular class |",
            f"| Pathway similarity | {s.pathway_similarity:.2f} | 2.0 | Same or related biological pathway |",
            f"| Inheritance compatibility | {s.inheritance_match:.2f} | 1.0 | AR/XL loss-of-function pattern match |",
            f"| Approval precedent | {s.approval_weight:.2f} | 1.0 | Regulatory approval / trial stage |",
            f"| Immunogenicity | {s.immunogenicity:.2f} | 2.0 | Pre-existing NAb seroprevalence for this vector |",
            f"| Therapeutic window | {s.therapeutic_window:.2f} | 2.0 | Can GT be given before irreversible damage? |",
            f"| Cross-correction | {s.cross_correction:.2f} | 1.0 | Can transduced cells rescue untransduced neighbours? |",
            f"| Immune privilege | {s.immune_privilege:.2f} | 1.0 | Immunological protection of target tissue |",
            f"| Promoter availability | {s.promoter_availability:.2f} | 1.0 | Validated tissue-specific promoters exist |",
            f"| Route of administration | {s.roa_feasibility:.2f} | 1.0 | Established delivery route to target tissue |",
            f"| **TOTAL (normalised)** | **{s.composite_score:.2f}** | **10.0** | Raw sum / 18 × 10 |",
            f"",
            f"### Rationale",
            f"",
        ]
        for note in s.notes:
            lines.append(f"- {note}")  # ← each note explains one dimension's score in plain English
        lines.append("")

    # ── Packaging failures log (at the bottom) ────────────────────────────
    fails = [s for s in result.scores if s.confidence == "fail"]
    if fails:
        lines += [
            "---",
            "",
            "## Excluded Programs (Packaging Failure)",
            # ← programs where the gene was simply too big for the vector → shown for transparency
            "",
            "| Program | Vector | Gene CDS Issue |",
            "|---------|--------|----------------|",
        ]
        for s in fails[:5]:  # ← show up to 5 failures
            reason = s.notes[0] if s.notes else "CDS too large"
            lines.append(f"| {s.program_name} | {s.vector} | {reason} |")
        lines.append("")

    return "\n".join(lines)  # ← joins all lines with newline characters into one big string


def save_report(result: MatchResult, output_dir: pathlib.Path) -> pathlib.Path:
    # ← writes the report to a .md file and returns the file path
    output_dir.mkdir(parents=True, exist_ok=True)  # ← create output folder if it doesn't exist

    slug = result.disease.orphanet_id.replace("ORPHA:", "ORPHA")
    # ← turns "ORPHA:324" into "ORPHA324" for use in the filename
    path = output_dir / f"match_{slug}_{result.disease.name.lower().replace(' ', '_')[:30]}.md"
    # ← filename format: match_ORPHA324_fabry_disease.md (name truncated to 30 chars)

    path.write_text(generate_report(result))  # ← generate the markdown text and write to file
    return path
