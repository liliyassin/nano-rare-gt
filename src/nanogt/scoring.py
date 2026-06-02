"""
6-dimension scoring engine.

For a given (disease, gene, target tissues) tuple, scores each GT program
in the catalog as a potential precedent/surrogate.

Dimensions:
  1. packaging_fit      — gene CDS vs. vector cargo limit
  2. tropism_match      — vector tissue tropism vs. disease target tissues
  3. protein_class      — same lysosomal/secreted/membrane class
  4. inheritance        — AR/XL/AD compatibility
  5. pathway_similarity — same biological pathway
  6. approval_weight    — approved programs score higher
"""

from __future__ import annotations
import json
from dataclasses import dataclass, field
from typing import Optional
import sqlite3

from .disease import DiseaseInfo
from .gene import GeneInfo


@dataclass
class ScoreBreakdown:
    program_name: str
    program_disease: str
    vector: str
    tissue_target: str
    approval_status: str
    composite_score: float      # 0–10
    confidence: str             # high / medium / low
    packaging_fit: float        # 0–2
    tropism_match: float        # 0–2
    protein_class_match: float  # 0–2
    inheritance_match: float    # 0–1
    pathway_similarity: float   # 0–2
    approval_weight: float      # 0–1
    notes: list[str] = field(default_factory=list)


def score_packaging(
    disease_gene: GeneInfo,
    program_cds: int,
    vector_cargo: int,
) -> tuple[float, list[str]]:
    gene_cds = disease_gene.cds_length_bp or program_cds  # use program as proxy if unknown
    if gene_cds > vector_cargo:
        return 0.0, [f"Gene CDS ({gene_cds}bp) exceeds vector cargo ({vector_cargo}bp) — hard fail"]
    ratio = gene_cds / vector_cargo
    if ratio <= 0.3:
        score = 2.0
    elif ratio <= 0.6:
        score = 1.5
    elif ratio <= 0.85:
        score = 1.0
    else:
        score = 0.5
    return score, [f"Gene CDS {gene_cds}bp / cargo {vector_cargo}bp ({ratio:.0%} utilized)"]


def score_tropism(
    disease_tissues: list[str],
    vector_tropism: list[str],
    program_tissue_target: str | None = None,
) -> tuple[float, list[str]]:
    if not disease_tissues:
        return 1.0, ["No tissue data — neutral score"]

    disease_set = set(t.lower() for t in disease_tissues)
    vector_set = set(t.lower() for t in vector_tropism)
    overlap = disease_set & vector_set

    target = (program_tissue_target or "").lower()

    def target_mentions(tissue: str) -> bool:
        if tissue == "cns":
            return any(word in target for word in ("cns", "brain", "spinal", "motor neuron", "neuron"))
        return tissue in target

    direct_target = sorted(tissue for tissue in disease_set if target_mentions(tissue))

    if direct_target and overlap:
        return 2.0, [
            f"Vector tropism plus precedent target match: {', '.join(direct_target)}"
        ]
    if direct_target:
        return 1.5, [f"Precedent target match: {', '.join(direct_target)}"]
    if len(overlap) >= 2:
        return 1.5, [f"Vector tropism overlap: {', '.join(sorted(overlap))}"]
    if len(overlap) == 1:
        return 1.0, [
            f"Vector tropism overlaps {', '.join(sorted(overlap))}, but precedent target is {program_tissue_target or 'unspecified'}"
        ]
    return 0.3, [f"No tissue overlap (disease: {disease_tissues}, vector: {vector_tropism})"]


def score_protein_class(
    gene_info: GeneInfo,
    program_class: str,
) -> tuple[float, list[str]]:
    # Map gene features to protein class
    kws = [k.lower() for k in gene_info.keywords]
    locs = [l.lower() for l in gene_info.subcellular_location]

    is_secreted_gene = gene_info.is_secreted or any("secret" in l for l in locs)
    is_lysosomal_gene = any("lysosom" in l for l in locs) or "lysosome" in kws
    is_membrane_gene = any("membran" in l for l in locs)

    pc = program_class.lower()

    if "lysosomal" in pc and is_lysosomal_gene:
        return 2.0, ["Both lysosomal proteins — cross-correction likely"]
    if "secreted" in pc and is_secreted_gene:
        return 2.0, ["Both secreted proteins — systemic delivery viable"]
    if "intracellular" in pc and not is_secreted_gene and not is_lysosomal_gene and not is_membrane_gene:
        return 1.5, ["Both intracellular proteins"]
    if "membrane" in pc and is_membrane_gene:
        return 1.5, ["Both membrane proteins"]
    # Partial credit: secreted vs lysosomal both have extracellular components
    if is_secreted_gene or is_lysosomal_gene:
        return 1.0, ["Partial match: extracellular/secreted component present"]
    return 0.5, ["Protein class mismatch"]


def score_inheritance(
    disease_inheritance: list[str],
    program_inheritance: str,
) -> tuple[float, list[str]]:
    if not disease_inheritance:
        return 0.5, ["Unknown inheritance"]
    di_lower = [d.lower() for d in disease_inheritance]
    pi = program_inheritance.lower()
    # LOF diseases (AR/XL recessive) suit gene replacement
    ar_match = "autosomal recessive" in di_lower and "ar" in pi
    xl_match = any("x-linked" in d for d in di_lower) and "xl" in pi
    if ar_match or xl_match:
        return 1.0, [f"Inheritance match ({disease_inheritance[0]} <-> {program_inheritance})"]
    # AR vs XL still both LOF
    any_lof = any("recessive" in d for d in di_lower) or any("x-linked" in d for d in di_lower)
    prog_lof = "ar" in pi or "xl" in pi
    if any_lof and prog_lof:
        return 0.7, ["LOF inheritance — compatible for gene replacement"]
    return 0.3, ["Inheritance mismatch (dominant/mitochondrial — higher complexity)"]


# Pathway similarity lookup
_PATHWAY_GROUPS: dict[str, set[str]] = {
    "lysosomal_storage": {"lysosomal_storage"},
    "coagulation": {"coagulation"},
    "motor_neuron": {"motor_neuron", "myopathy"},  # neuromuscular
    "myopathy": {"myopathy", "motor_neuron"},
    "retinal": {"retinal_visual_cycle", "retinal_phototransduction", "mitochondrial_complex"},
    "retinal_visual_cycle": {"retinal_visual_cycle", "retinal_phototransduction"},
    "retinal_phototransduction": {"retinal_phototransduction", "retinal_visual_cycle"},
    "mitochondrial_complex": {"mitochondrial_complex", "retinal_visual_cycle"},
    "amino_acid_metabolism": {"amino_acid_metabolism", "urea_cycle"},
    "urea_cycle": {"urea_cycle", "amino_acid_metabolism"},
    "lipid_metabolism": {"lipid_metabolism"},
}


def _infer_pathway(disease: DiseaseInfo, gene: GeneInfo) -> str:
    """Infer disease pathway from gene keywords and disease tissues."""
    kws = " ".join(gene.keywords).lower() + " " + " ".join(gene.go_terms).lower()
    locs = " ".join(gene.subcellular_location).lower()
    hpo = " ".join(disease.hpo_terms).lower()

    if "lysosom" in locs or "lysosom" in hpo:
        return "lysosomal_storage"
    if "coagulat" in kws or "coagulat" in hpo:
        return "coagulation"
    if "retina" in " ".join(disease.affected_tissues).lower() or "retina" in hpo:
        return "retinal_visual_cycle"
    if "motor neuron" in hpo or "spinal cord" in hpo:
        return "motor_neuron"
    if "muscul" in hpo or "myopat" in hpo:
        return "myopathy"
    if "amino acid" in kws or "phenylalan" in kws:
        return "amino_acid_metabolism"
    if "urea" in kws or "nitrogen" in kws:
        return "urea_cycle"
    if "mitochondri" in kws:
        return "mitochondrial_complex"
    return "unknown"


def score_pathway(
    disease: DiseaseInfo,
    gene: GeneInfo,
    program_pathway: str,
) -> tuple[float, list[str]]:
    inferred = _infer_pathway(disease, gene)
    group = _PATHWAY_GROUPS.get(inferred, {inferred})
    if program_pathway in group:
        return 2.0, [f"Pathway match: {program_pathway}"]
    # Close-enough groupings
    prog_group = _PATHWAY_GROUPS.get(program_pathway, {program_pathway})
    if inferred in prog_group or program_pathway in group:
        return 1.5, [f"Related pathway ({inferred} ~ {program_pathway})"]
    if inferred != "unknown":
        return 0.5, [f"Different pathway ({inferred} vs {program_pathway})"]
    return 1.0, ["Unknown pathway — neutral score"]


_APPROVAL_SCORES = {
    "approved": 1.0,
    "withdrawn": 0.7,
    "phase3": 0.8,
    "phase2/3": 0.7,
    "phase2": 0.6,
    "phase1/2": 0.5,
    "phase1": 0.4,
}


def score_approval(status: str) -> tuple[float, list[str]]:
    s = _APPROVAL_SCORES.get(status.lower(), 0.3)
    return s, [f"Approval status: {status}"]


def score_program(
    disease: DiseaseInfo,
    gene: GeneInfo,
    program: dict,
    vector: dict,
) -> ScoreBreakdown:
    notes: list[str] = []

    pkg, pkg_notes = score_packaging(gene, program["cds_bp"], vector["cargo_limit_bp"])
    notes.extend(pkg_notes)
    if pkg == 0.0:
        # Hard fail — packaging not possible
        return ScoreBreakdown(
            program_name=program["name"],
            program_disease=program["disease"],
            vector=program["vector"],
            tissue_target=program["tissue_target"],
            approval_status=program["approval_status"],
            composite_score=0.0,
            confidence="fail",
            packaging_fit=0.0,
            tropism_match=0.0,
            protein_class_match=0.0,
            inheritance_match=0.0,
            pathway_similarity=0.0,
            approval_weight=0.0,
            notes=notes,
        )

    v_tropism = (
        json.loads(vector["tissue_tropism"])
        if isinstance(vector.get("tissue_tropism"), str)
        else vector.get("tissue_tropism", [])
    )
    trp, trp_notes = score_tropism(
        disease.affected_tissues,
        v_tropism,
        program.get("tissue_target"),
    )
    notes.extend(trp_notes)

    prc, prc_notes = score_protein_class(gene, program["protein_class"])
    notes.extend(prc_notes)

    inh, inh_notes = score_inheritance(disease.inheritance, program["inheritance"])
    notes.extend(inh_notes)

    pth, pth_notes = score_pathway(disease, gene, program["pathway"])
    notes.extend(pth_notes)

    apv, apv_notes = score_approval(program["approval_status"])
    notes.extend(apv_notes)

    # Composite: packaging(2) + tropism(2) + protein_class(2) + pathway(2) + inheritance(1) + approval(1) = max 10
    composite = pkg + trp + prc + pth + inh + apv
    confidence = "high" if composite >= 7.5 else "medium" if composite >= 5.0 else "low"

    return ScoreBreakdown(
        program_name=program["name"],
        program_disease=program["disease"],
        vector=program["vector"],
        tissue_target=program["tissue_target"],
        approval_status=program["approval_status"],
        composite_score=round(composite, 2),
        confidence=confidence,
        packaging_fit=pkg,
        tropism_match=trp,
        protein_class_match=prc,
        inheritance_match=inh,
        pathway_similarity=pth,
        approval_weight=apv,
        notes=notes,
    )


def rank_programs(
    disease: DiseaseInfo,
    gene: GeneInfo,
    conn: sqlite3.Connection,
) -> list[ScoreBreakdown]:
    """Score all GT programs and return ranked list (highest first)."""
    programs = [dict(r) for r in conn.execute("SELECT * FROM gt_programs").fetchall()]
    vectors_by_sero = {
        r["serotype"]: dict(r)
        for r in conn.execute("SELECT * FROM vectors").fetchall()
    }

    scores: list[ScoreBreakdown] = []
    for prog in programs:
        vec = vectors_by_sero.get(prog["vector"])
        if vec is None:
            # Unknown vector — use generic AAV params
            vec = {"cargo_limit_bp": 4700, "tissue_tropism": "[]"}
        scores.append(score_program(disease, gene, prog, vec))

    # Sort by composite score descending; hard fails at bottom
    scores.sort(key=lambda s: (-s.composite_score, s.program_name))
    return scores
