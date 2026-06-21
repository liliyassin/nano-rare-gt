"""Markdown report generator."""

# ── What this file is ──────────────────────────────────────────────────────
# Takes the scores from scoring.py and turns them into a human-readable
# markdown report. Think of it as the "print results" step.
#
# Two functions:
#   generate_report() → builds the markdown text as a string
#   save_report()     → writes that string to a .md file in the output/ folder

from __future__ import annotations
import json
from dataclasses import dataclass, field
from typing import Optional
import pathlib

from .catalog import GT_PROGRAMS, VECTORS
from .disease import DiseaseInfo
from .gene import GeneInfo
from .mechanism import MechanismEvidence, lookup_mechanism
from .scoring import ScoreBreakdown


@dataclass
class MatchResult:
    # ← bundles everything needed to generate a report into one object
    disease: DiseaseInfo              # ← the query disease
    gene: GeneInfo                    # ← its causal gene
    scores: list[ScoreBreakdown]      # ← full ranked list of all GT programs (from scoring.py)
    top_n: int = 5                    # ← how many top matches to include in the report (default 5)
    primary_tissue: str | None = None
    # ← optional user-declared target tissue for multi-system diseases.
    source_tissues: list[str] = field(default_factory=list)
    # ← original disease tissue list when scoring was narrowed to primary_tissue.


def _confidence_emoji(c: str) -> str:
    # ← converts confidence string to a coloured circle emoji for visual clarity
    return {"high": "🟢", "medium": "🟡", "low": "🔴", "fail": "⛔"}.get(c, "⬜")


def _portfolio_interpretation(top: list[ScoreBreakdown]) -> list[str]:
    """Summarise what the ranked list means clinically."""
    if not top:
        return [
            "No packagable precedent was found in the current catalog.",
            "Treat this disease as out-of-scope for single-vector precedent matching until an alternative modality or engineered construct is defined.",
        ]

    best = top[0]
    if best.confidence == "high":
        lines = [
            "At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.",
        ]
    elif best.confidence == "medium":
        lines = [
            "No high-confidence vector precedent was found; the best result is medium-confidence and should be treated as manual-review territory.",
        ]
    else:
        lines = [
            "Only low-confidence precedents were found; this is weak support for clinical translation with the current catalog and assumptions.",
        ]

    flags: list[str] = []
    for score in top:
        for flag in score.review_flags:
            if flag not in flags:
                flags.append(flag)
    if flags:
        lines.append("Main review flags: " + "; ".join(flags[:3]) + ".")

    return lines


def _mentions_tissue(text: str, tissue: str) -> bool:
    target = text.lower()
    tissue_l = tissue.lower()
    if tissue_l == "cns":
        return any(word in target for word in ("cns", "brain", "spinal", "motor neuron", "neuron"))
    return tissue_l in target


def _catalog_bias_notes(disease: DiseaseInfo) -> list[str]:
    """Describe catalog coverage limits so scores are interpreted as catalog-relative."""
    disease_tissues = [t for t in disease.affected_tissues if t]
    direct_programs = [
        p for p in GT_PROGRAMS
        if any(_mentions_tissue(p.get("tissue_target", ""), tissue) for tissue in disease_tissues)
    ]
    covering_vectors = []
    for vector in VECTORS:
        tropism = vector.get("tissue_tropism", [])
        if isinstance(tropism, str):
            tropism = json.loads(tropism)
        if {t.lower() for t in tropism} & {t.lower() for t in disease_tissues}:
            covering_vectors.append(vector["serotype"])

    notes = [
        f"Catalog-relative ranking: current catalog contains {len(GT_PROGRAMS)} precedent programs and {len(VECTORS)} vectors, so absence of a strong match is not proof that no therapy is possible.",
        "Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.",
    ]
    if disease_tissues and not direct_programs:
        notes.append(
            "No catalog program directly targets the annotated disease tissue(s); ranking is extrapolating from indirect precedents."
        )
    elif disease_tissues and len(direct_programs) <= 2:
        notes.append(
            f"Only {len(direct_programs)} catalog program(s) directly target the annotated disease tissue(s); tissue evidence is sparse."
        )
    if disease_tissues and not covering_vectors:
        notes.append(
            "No catalog vector naturally covers the annotated disease tissue(s); consider non-catalog vectors or alternative modalities."
        )
    elif disease_tissues and len(covering_vectors) <= 2:
        notes.append(
            "Few catalog vectors cover the annotated disease tissue(s): " + ", ".join(covering_vectors) + "."
        )

    return notes


def _endpoint_feasibility_notes(disease: DiseaseInfo) -> list[str]:
    """Flag whether a plausible clinical endpoint package is obvious from tissue/HPO data."""
    tissues = {t.lower() for t in disease.affected_tissues}
    hpo = " ".join(disease.hpo_terms).lower()
    notes: list[str] = []

    if "retina" in tissues:
        notes.append(
            "Endpoint readiness: retinal diseases often have measurable endpoints such as OCT, ERG, visual acuity, visual fields, or mobility testing, but genotype-specific progression still needs confirmation."
        )
    if "liver" in tissues:
        notes.append(
            "Endpoint readiness: liver/metabolic targets may have biochemical biomarkers, but biomarker correction must be linked to clinical benefit."
        )
    if "cns" in tissues or "neuro" in hpo or "intellectual disability" in hpo:
        notes.append(
            "Endpoint risk: CNS/neurodevelopmental outcomes may require natural-history data, age-stratified endpoints, and long follow-up because short-term clinical change can be hard to interpret."
        )
    if "muscle" in tissues or "heart" in tissues:
        notes.append(
            "Endpoint risk: muscle/cardiac diseases may need functional, respiratory, imaging, or cardiac endpoints that progress slowly and vary by age/stage."
        )
    if len(tissues) > 1:
        notes.append(
            "Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit."
        )
    if not notes:
        notes.append(
            "Endpoint readiness unclear from available annotations; identify biomarkers, natural-history measures, and patient-relevant outcomes before trial prioritisation."
        )

    return notes


def _mechanism_lines(mechanism: MechanismEvidence) -> list[str]:
    """Render source-linked disease mechanism evidence."""
    source = (
        f"[{mechanism.evidence_citation}]({mechanism.evidence_url})"
        if mechanism.evidence_url
        else mechanism.evidence_citation
    )
    return [
        f"**Molecular mechanism:** {mechanism.mechanism_category.replace('_', ' ')}  ",
        f"**Mechanistic detail:** {mechanism.mechanism_detail}  ",
        f"**Gene-addition compatibility:** {mechanism.gene_addition_compatibility}  ",
        f"**Preferred modality class:** {mechanism.preferred_modality.replace('_', ' ')}  ",
        f"**Evidence level/status:** {mechanism.evidence_level} / {mechanism.evidence_status}  ",
        f"**Evidence summary:** {mechanism.evidence_summary}  ",
        f"**Evidence source:** {source}  ",
    ]


def generate_report(result: MatchResult) -> str:
    # ← builds the full markdown report as a text string
    d = result.disease
    g = result.gene
    top = [s for s in result.scores if s.confidence != "fail"][:result.top_n]
    # ← filter out hard fails (gene too big for vector), keep only top N
    source_tissues = result.source_tissues or d.affected_tissues
    mechanism = lookup_mechanism(d.orphanet_id, g.symbol)

    # ── Header ────────────────────────────────────────────────────────────
    lines = [
        f"# NanoGT Match Report: {d.name}",
        f"",
        f"**Disease:** {d.name} ({d.orphanet_id})  ",
        f"**Primary gene:** {g.symbol}  ",
        f"**Gene CDS:** {g.cds_length_bp or 'unknown'} bp  ",
        f"**Inheritance:** {', '.join(d.inheritance) if d.inheritance else 'unknown'}  ",
        f"**Target tissues scored:** {', '.join(d.affected_tissues) if d.affected_tissues else 'unknown'}  ",
    ]
    if result.primary_tissue:
        lines.append(
            f"**Primary tissue assumption:** {result.primary_tissue} selected from original tissue list ({', '.join(source_tissues) or 'unknown'}).  "
        )
    if len(d.gene_symbols) > 1:
        lines.append(
            f"**Gene selection note:** this disease has multiple listed genes ({', '.join(d.gene_symbols)}); "
            f"this report scores {g.symbol} only.  "
        )
    lines += [
        f"",
        f"---",
        f"",
        f"## Interpretation",
        f"",
    ]
    for line in _portfolio_interpretation(top):
        lines.append(f"- {line}")
    lines += [
        "",
        "### Disease Mechanism Evidence",
        "",
    ]
    lines.extend(_mechanism_lines(mechanism))
    lines += [
        "",
        "### Study-Level Limitations",
        "",
    ]
    for line in _catalog_bias_notes(d) + _endpoint_feasibility_notes(d):
        lines.append(f"- {line}")

    lines += [
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
            f"| Modality compatibility | {s.modality_compatibility:.2f} | 2.0 | Disease mechanism supports gene-addition precedent |",
            f"| Inheritance compatibility | {s.inheritance_match:.2f} | 1.0 | AR/XL loss-of-function pattern match |",
            f"| Approval precedent | {s.approval_weight:.2f} | 1.0 | Regulatory approval / trial stage |",
            f"| Immunogenicity | {s.immunogenicity:.2f} | 2.0 | Pre-existing NAb seroprevalence for this vector |",
            f"| Therapeutic window | {s.therapeutic_window:.2f} | 2.0 | Can GT be given before irreversible damage? |",
            f"| Cross-correction | {s.cross_correction:.2f} | 1.0 | Can transduced cells rescue untransduced neighbours? |",
            f"| Immune privilege | {s.immune_privilege:.2f} | 1.0 | Immunological protection of target tissue |",
            f"| Promoter availability | {s.promoter_availability:.2f} | 1.0 | Validated tissue-specific promoters exist |",
            f"| Route of administration | {s.roa_feasibility:.2f} | 1.0 | Established delivery route to target tissue |",
            f"| **TOTAL (normalised)** | **{s.composite_score:.2f}** | **10.0** | Raw sum / 20 × 10 |",
            f"",
            f"### Rationale",
            f"",
        ]
        for note in s.notes:
            lines.append(f"- {note}")  # ← each note explains one dimension's score in plain English
        if s.review_flags:
            lines += [
                "",
                "### Manual Review Flags",
                "",
            ]
            for flag in s.review_flags:
                lines.append(f"- {flag}")
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
    gene_suffix = f"_{result.gene.symbol.lower()}" if len(result.disease.gene_symbols) > 1 else ""
    tissue_suffix = f"_{result.primary_tissue.lower()}" if result.primary_tissue else ""
    path = output_dir / f"match_{slug}_{result.disease.name.lower().replace(' ', '_')[:30]}{gene_suffix}{tissue_suffix}.md"
    # ← filename format: match_ORPHA324_fabry_disease.md (name truncated to 30 chars)

    path.write_text(generate_report(result))  # ← generate the markdown text and write to file
    return path
