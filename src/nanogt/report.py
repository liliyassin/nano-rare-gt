"""Markdown report generator."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import pathlib

from .disease import DiseaseInfo
from .gene import GeneInfo
from .scoring import ScoreBreakdown


@dataclass
class MatchResult:
    disease: DiseaseInfo
    gene: GeneInfo
    scores: list[ScoreBreakdown]   # full ranked list
    top_n: int = 5


def _confidence_emoji(c: str) -> str:
    return {"high": "🟢", "medium": "🟡", "low": "🔴", "fail": "⛔"}.get(c, "⬜")


def generate_report(result: MatchResult) -> str:
    d = result.disease
    g = result.gene
    top = [s for s in result.scores if s.confidence != "fail"][:result.top_n]

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

    for i, s in enumerate(top, 1):
        lines += [
            f"## Match #{i}: {s.program_name}",
            f"",
            f"**Precedent disease:** {s.program_disease}  ",
            f"**Vector:** {s.vector}  ",
            f"**Tissue target:** {s.tissue_target}  ",
            f"**Composite score:** {s.composite_score:.1f} / 10  ",
            f"",
            f"### Score Breakdown",
            f"",
            f"| Dimension | Score | Max |",
            f"|-----------|-------|-----|",
            f"| Packaging fit | {s.packaging_fit:.1f} | 2.0 |",
            f"| Tissue tropism | {s.tropism_match:.1f} | 2.0 |",
            f"| Protein class | {s.protein_class_match:.1f} | 2.0 |",
            f"| Pathway similarity | {s.pathway_similarity:.1f} | 2.0 |",
            f"| Inheritance compatibility | {s.inheritance_match:.1f} | 1.0 |",
            f"| Approval precedent | {s.approval_weight:.1f} | 1.0 |",
            f"",
            f"### Rationale",
            f"",
        ]
        for note in s.notes:
            lines.append(f"- {note}")
        lines.append("")

    # Packaging fail log
    fails = [s for s in result.scores if s.confidence == "fail"]
    if fails:
        lines += [
            "---",
            "",
            "## Excluded Programs (Packaging Failure)",
            "",
            "| Program | Vector | Gene CDS Issue |",
            "|---------|--------|----------------|",
        ]
        for s in fails[:5]:
            reason = s.notes[0] if s.notes else "CDS too large"
            lines.append(f"| {s.program_name} | {s.vector} | {reason} |")
        lines.append("")

    return "\n".join(lines)


def save_report(result: MatchResult, output_dir: pathlib.Path) -> pathlib.Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    slug = result.disease.orphanet_id.replace("ORPHA:", "ORPHA")
    path = output_dir / f"match_{slug}_{result.disease.name.lower().replace(' ', '_')[:30]}.md"
    path.write_text(generate_report(result))
    return path
