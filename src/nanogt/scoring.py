"""
12-dimension scoring engine.

For a given (disease, gene, target tissues) tuple, scores each GT program
in the catalog as a potential precedent/surrogate.

Dimensions:
  1.  packaging_fit         — gene CDS vs. vector cargo limit
  2.  tropism_match         — vector tissue tropism vs. disease target tissues
  3.  protein_class         — same lysosomal/secreted/membrane/intracellular class
  4.  inheritance           — AR/XL/AD compatibility
  5.  pathway_similarity    — same biological pathway
  6.  approval_weight       — approved programs score higher
  7.  immunogenicity        — pre-existing neutralising antibody seroprevalence for vector
  8.  therapeutic_window    — can intervention occur before irreversible damage?
  9.  cross_correction      — can transduced cells rescue untransduced neighbours?
  10. immune_privilege      — immunological privilege of the target tissue
  11. promoter_availability — validated tissue-specific promoters exist for target
  12. roa_feasibility       — accessible, established delivery route to target tissue
"""

# ── What this file is ──────────────────────────────────────────────────────
# THE ALGORITHM. This is the intellectual core of the dissertation.
# It takes one disease + one gene and scores every GT program in the catalog
# across 12 dimensions. Raw scores are normalized to a composite out of 10.
# Highest composite = best precedent match.
#
# Max raw scores per dimension:
#   packaging_fit         → max 2.0
#   tropism_match         → max 2.0
#   protein_class         → max 2.0
#   pathway_similarity    → max 2.0
#   inheritance_match     → max 1.0
#   approval_weight       → max 1.0
#   immunogenicity        → max 2.0
#   therapeutic_window    → max 2.0
#   cross_correction      → max 1.0
#   immune_privilege      → max 1.0
#   promoter_availability → max 1.0
#   roa_feasibility       → max 1.0
#   ─────────────────────────────
#   RAW TOTAL MAX         = 18.0
#   NORMALIZED (× 10/18)  = 10.0

from __future__ import annotations
import json
from dataclasses import dataclass, field
from typing import Optional
import sqlite3

from .disease import DiseaseInfo
from .gene import GeneInfo

_RAW_MAX = 18.0  # ← total of all dimension maxima; used for normalization


@dataclass
class ScoreBreakdown:
    # ← One row of results: all scores + metadata for ONE program comparison.
    program_name: str          # ← name of the GT program, e.g. "Zolgensma"
    program_disease: str       # ← disease the program was originally designed for
    vector: str                # ← vector used, e.g. "AAV9"
    tissue_target: str         # ← where the program delivers the gene, e.g. "CNS/motor neuron"
    approval_status: str       # ← "approved", "phase2", etc.
    composite_score: float     # ← FINAL SCORE out of 10 (normalized from raw 18)
    confidence: str            # ← "high" (≥7.5), "medium" (≥5.0), "low" (<5.0), "fail" (packaging impossible)

    # ── Original 6 dimensions ─────────────────────────────────────────────
    packaging_fit: float       # ← 0–2: does the gene fit in the vector?
    tropism_match: float       # ← 0–2: does the vector reach the right tissue?
    protein_class_match: float # ← 0–2: same type of protein (lysosomal/secreted/membrane)?
    inheritance_match: float   # ← 0–1: same inheritance pattern (AR/XL)?
    pathway_similarity: float  # ← 0–2: same biological pathway?
    approval_weight: float     # ← 0–1: how far along in trials/approval?

    # ── 6 new dimensions ──────────────────────────────────────────────────
    immunogenicity: float = 0.0
    # ← 0–2: how likely are patients to have pre-existing antibodies against this vector?
    #   Low seroprevalence = high score (more patients can receive treatment)
    #   Source: published seroprevalence studies (Boutin et al. 2010, Calcedo et al. 2011)

    therapeutic_window: float = 0.0
    # ← 0–2: can gene therapy be administered before irreversible damage occurs?
    #   Adult/chronic onset = wide window (2.0); neonatal rapid progression = narrow (0.5)
    #   Inferred from HPO terms: "neonatal", "progressive", "adult onset", etc.

    cross_correction: float = 0.0
    # ← 0–1: can transduced cells secrete the protein to correct untransduced neighbours?
    #   Secreted/lysosomal proteins can; intracellular proteins cannot.
    #   High cross-correction → fewer cells need gene delivery → safer, lower dose

    immune_privilege: float = 0.0
    # ← 0–1: does the target tissue have immunological privilege?
    #   Retina and CNS (blood-retinal/brain barriers) and liver (tolerogenic) = privileged
    #   Higher privilege → lower risk of immune-mediated transgene silencing over time

    promoter_availability: float = 0.0
    # ← 0–1: do validated, tissue-specific promoters exist for the target tissue?
    #   Liver and retina have the most (used in approved programs); kidney has the fewest
    #   Critical for both efficacy (right cells express the gene) and safety (others don't)

    roa_feasibility: float = 0.0
    # ← 0–1: is there an accessible, established route to deliver to the target tissue?
    #   Liver/muscle = easy (IV/IM); CNS = harder (intrathecal or high-dose IV); retina = injection

    notes: list[str] = field(default_factory=list)  # ← plain-English explanation of each score


# ══════════════════════════════════════════════════════════════════════════════
# DIMENSION 1: PACKAGING FIT (max 2.0)
# ══════════════════════════════════════════════════════════════════════════════
def score_packaging(
    disease_gene: GeneInfo,
    program_cds: int,      # ← size of the gene in the precedent program (base pairs)
    vector_cargo: int,     # ← maximum size the vector can carry (base pairs)
) -> tuple[float, list[str]]:
    # ← Returns (score, [explanation notes])

    gene_cds = disease_gene.cds_length_bp or program_cds  # ← if we don't know the disease gene size, use the program's as a proxy

    if gene_cds > vector_cargo:
        # ← HARD FAIL: gene literally cannot fit → score 0, entire program rejected
        return 0.0, [f"Gene CDS ({gene_cds}bp) exceeds vector cargo ({vector_cargo}bp) — hard fail"]

    ratio = gene_cds / vector_cargo  # ← what fraction of the vector's capacity is used

    # ← Smaller = better: leaves more room, less risk of packaging problems
    if ratio <= 0.3:
        score = 2.0   # ← gene uses ≤30% of capacity → perfect fit
    elif ratio <= 0.6:
        score = 1.5   # ← 30–60% → good fit
    elif ratio <= 0.85:
        score = 1.0   # ← 60–85% → tight but workable
    else:
        score = 0.5   # ← 85–100% → dangerously close to limit

    return score, [f"Gene CDS {gene_cds}bp / cargo {vector_cargo}bp ({ratio:.0%} utilized)"]


# ══════════════════════════════════════════════════════════════════════════════
# DIMENSION 2: TISSUE TROPISM (max 2.0)
# ══════════════════════════════════════════════════════════════════════════════
def score_tropism(
    disease_tissues: list[str],        # ← tissues affected by the query disease, e.g. ["CNS", "muscle"]
    vector_tropism: list[str],         # ← tissues the vector naturally reaches, e.g. ["CNS", "liver"]
    program_tissue_target: str | None = None,  # ← where the precedent program actually delivers to
) -> tuple[float, list[str]]:

    if not disease_tissues:
        return 1.0, ["No tissue data — neutral score"]  # ← no data → neutral, not a penalty

    disease_set = set(t.lower() for t in disease_tissues)   # ← set = unique items, lowercase for matching
    vector_set = set(t.lower() for t in vector_tropism)
    overlap = disease_set & vector_set  # ← "&" = intersection: tissues in BOTH sets

    target = (program_tissue_target or "").lower()

    def target_mentions(tissue: str) -> bool:
        # ← checks if the precedent program's tissue target description mentions this tissue
        if tissue == "cns":
            return any(word in target for word in ("cns", "brain", "spinal", "motor neuron", "neuron"))
        return tissue in target

    direct_target = sorted(tissue for tissue in disease_set if target_mentions(tissue))
    # ← list of disease tissues that are directly mentioned in the precedent program's target

    if direct_target and overlap:
        return 2.0, [
            f"Vector tropism plus precedent target match: {', '.join(direct_target)}"
        ]   # ← BEST: vector reaches the tissue AND precedent program targets it too
    if direct_target:
        return 1.5, [f"Precedent target match: {', '.join(direct_target)}"]
        # ← precedent targets the right tissue even if vector tropism doesn't perfectly match
    if len(overlap) >= 2:
        return 1.5, [f"Vector tropism overlap: {', '.join(sorted(overlap))}"]
        # ← vector covers 2+ of the disease's affected tissues
    if len(overlap) == 1:
        return 1.0, [
            f"Vector tropism overlaps {', '.join(sorted(overlap))}, but precedent target is {program_tissue_target or 'unspecified'}"
        ]   # ← partial match: vector hits one tissue but not where the precedent programme specifically aimed
    return 0.3, [f"No tissue overlap (disease: {disease_tissues}, vector: {vector_tropism})"]
    # ← WORST: completely different tissues


# ══════════════════════════════════════════════════════════════════════════════
# DIMENSION 3: PROTEIN CLASS (max 2.0)
# ══════════════════════════════════════════════════════════════════════════════
def score_protein_class(
    gene_info: GeneInfo,     # ← the query disease's gene
    program_class: str,      # ← protein class of the precedent program, e.g. "lysosomal", "secreted"
) -> tuple[float, list[str]]:
    # ← Protein class matters because the delivery mechanism works differently:
    #   - Secreted proteins: one cell makes the protein, neighbours benefit too ("cross-correction")
    #   - Lysosomal proteins: similar cross-correction principle (cells share via endocytosis)
    #   - Membrane/intracellular: each cell needs its own copy → harder to treat

    kws = [k.lower() for k in gene_info.keywords]            # ← UniProt keywords in lowercase
    locs = [l.lower() for l in gene_info.subcellular_location]  # ← where in the cell the protein lives

    is_secreted_gene = gene_info.is_secreted or any("secret" in l for l in locs)   # ← released outside the cell
    is_lysosomal_gene = any("lysosom" in l for l in locs) or "lysosome" in kws     # ← lives in the lysosome
    is_membrane_gene = any("membran" in l for l in locs)                           # ← sits in a cell membrane

    pc = program_class.lower()

    if "lysosomal" in pc and is_lysosomal_gene:
        return 2.0, ["Both lysosomal proteins — cross-correction likely"]
    if "secreted" in pc and is_secreted_gene:
        return 2.0, ["Both secreted proteins — systemic delivery viable"]
    if "intracellular" in pc and not is_secreted_gene and not is_lysosomal_gene and not is_membrane_gene:
        return 1.5, ["Both intracellular proteins"]
    if "membrane" in pc and is_membrane_gene:
        return 1.5, ["Both membrane proteins"]
    if is_secreted_gene or is_lysosomal_gene:
        return 1.0, ["Partial match: extracellular/secreted component present"]
    return 0.5, ["Protein class mismatch"]


# ══════════════════════════════════════════════════════════════════════════════
# DIMENSION 4: INHERITANCE COMPATIBILITY (max 1.0)
# ══════════════════════════════════════════════════════════════════════════════
def score_inheritance(
    disease_inheritance: list[str],  # ← e.g. ["Autosomal recessive"]
    program_inheritance: str,        # ← e.g. "AR", "XL"
) -> tuple[float, list[str]]:
    # ← Why inheritance matters: AR and XL recessive diseases = loss-of-function (LOF)
    #   Gene replacement therapy is the natural fix for LOF diseases.
    #   Dominant diseases are harder — you may need to silence a bad gene, not just add a good one.

    if not disease_inheritance:
        return 0.5, ["Unknown inheritance"]

    di_lower = [d.lower() for d in disease_inheritance]
    pi = program_inheritance.lower()

    ar_match = "autosomal recessive" in di_lower and "ar" in pi
    xl_match = any("x-linked" in d for d in di_lower) and "xl" in pi

    if ar_match or xl_match:
        return 1.0, [f"Inheritance match ({disease_inheritance[0]} <-> {program_inheritance})"]

    any_lof = any("recessive" in d for d in di_lower) or any("x-linked" in d for d in di_lower)
    prog_lof = "ar" in pi or "xl" in pi

    if any_lof and prog_lof:
        return 0.7, ["LOF inheritance — compatible for gene replacement"]

    return 0.3, ["Inheritance mismatch (dominant/mitochondrial — higher complexity)"]


# ══════════════════════════════════════════════════════════════════════════════
# DIMENSION 5: PATHWAY SIMILARITY (max 2.0)
# ══════════════════════════════════════════════════════════════════════════════
_PATHWAY_GROUPS: dict[str, set[str]] = {
    "lysosomal_storage": {"lysosomal_storage", "leukodystrophy", "glycogen_storage"},
    "leukodystrophy": {"leukodystrophy", "lysosomal_storage", "peroxisomal"},
    "peroxisomal": {"peroxisomal", "leukodystrophy", "lipid_metabolism"},
    "coagulation": {"coagulation"},
    "motor_neuron": {"motor_neuron", "myopathy"},
    "myopathy": {"myopathy", "motor_neuron", "glycogen_storage"},
    "retinal": {"retinal_visual_cycle", "retinal_phototransduction", "mitochondrial_complex"},
    "retinal_visual_cycle": {"retinal_visual_cycle", "retinal_phototransduction"},
    "retinal_phototransduction": {"retinal_phototransduction", "retinal_visual_cycle"},
    "mitochondrial_complex": {"mitochondrial_complex", "retinal_visual_cycle", "amino_acid_metabolism"},
    "amino_acid_metabolism": {"amino_acid_metabolism", "urea_cycle", "mitochondrial_complex"},
    "urea_cycle": {"urea_cycle", "amino_acid_metabolism"},
    "glycogen_storage": {"glycogen_storage", "myopathy", "lysosomal_storage"},
    "immune_hematopoietic": {"immune_hematopoietic"},
    "lipid_metabolism": {"lipid_metabolism", "peroxisomal"},
}


def _infer_pathway(disease: DiseaseInfo, gene: GeneInfo) -> str:
    """Infer disease pathway from gene keywords and disease tissues."""
    kws = " ".join(gene.keywords).lower() + " " + " ".join(gene.go_terms).lower()
    locs = " ".join(gene.subcellular_location).lower()
    hpo = " ".join(disease.hpo_terms).lower()

    if "leukodystrophy" in hpo or "white matter" in hpo:
        return "leukodystrophy"
    if "peroxisom" in kws or "peroxisom" in locs or "peroxisom" in hpo:
        return "peroxisomal"
    if "lysosom" in locs or "lysosom" in hpo:
        return "lysosomal_storage"
    if "glycogen" in kws or "glycogen" in hpo:
        return "glycogen_storage"
    if "coagulat" in kws or "coagulat" in hpo:
        return "coagulation"
    if "retina" in " ".join(disease.affected_tissues).lower() or "retina" in hpo or "phototransduction" in kws:
        return "retinal_phototransduction"
    if "motor neuron" in hpo or "spinal cord" in hpo:
        return "motor_neuron"
    if "muscul" in hpo or "myopat" in hpo or "dystrophy" in hpo:
        return "myopathy"
    if "immunodeficiency" in hpo or "lymphopenia" in hpo or "hematopoietic" in hpo:
        return "immune_hematopoietic"
    if "amino acid" in kws or "phenylalan" in kws or "methylmalonic" in hpo:
        return "amino_acid_metabolism"
    if "urea" in kws or "urea" in hpo or "nitrogen" in kws or "hyperammonemia" in hpo:
        return "urea_cycle"
    if "mitochondri" in kws or "mitochondri" in locs or "mitochondri" in hpo:
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

    prog_group = _PATHWAY_GROUPS.get(program_pathway, {program_pathway})
    if inferred in prog_group or program_pathway in group:
        return 1.5, [f"Related pathway ({inferred} ~ {program_pathway})"]

    if inferred != "unknown":
        return 0.5, [f"Different pathway ({inferred} vs {program_pathway})"]

    return 1.0, ["Unknown pathway — neutral score"]


# ══════════════════════════════════════════════════════════════════════════════
# DIMENSION 6: APPROVAL WEIGHT (max 1.0)
# ══════════════════════════════════════════════════════════════════════════════
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


# ══════════════════════════════════════════════════════════════════════════════
# DIMENSION 7: IMMUNOGENICITY — VECTOR SEROPREVALENCE (max 2.0)
# ══════════════════════════════════════════════════════════════════════════════
#
# Pre-existing neutralising antibodies (NAbs) in the general population are one
# of the biggest clinical blockers in AAV gene therapy. Patients with NAb titres
# above a threshold are excluded from trials. High seroprevalence means fewer
# eligible patients and greater trial complexity.
#
# Sources: Boutin et al. (2010) J Infect Dis; Calcedo et al. (2011) Hum Gene Ther;
#          Mingozzi & High (2013) Nat Rev Genet
#
# Values represent approximate population seroprevalence (fraction 0–1):
_SEROPREVALENCE: dict[str, float] = {
    "AAV1":    0.20,   # ← 15–30%; moderate
    "AAV2":    0.55,   # ← 40–70%; HIGHEST — AAV2 is the oldest, most encountered naturally
    "AAV5":    0.09,   # ← 3–15%; LOW — favourable immunogenicity profile
    "AAV8":    0.30,   # ← 20–40%; moderate
    "AAV9":    0.22,   # ← 15–30%; moderate; neonatal dosing in SMA trials mitigates this
    "AAVrh10": 0.10,   # ← 5–15%; low — primate-derived, less historical human exposure
    "AAV2/6":  0.17,   # ← 10–25%; low-moderate hybrid
    "LV":      0.02,   # ← <5%; lentiviral vectors are immunologically distinct from AAVs
}


def score_immunogenicity(vector_serotype: str) -> tuple[float, list[str]]:
    """Score based on pre-existing neutralising antibody seroprevalence for this vector.

    Lower seroprevalence = fewer patients excluded = higher score.
    """
    sero = _SEROPREVALENCE.get(vector_serotype, 0.25)

    if sero < 0.10:
        score = 2.0
        label = f"low (~{sero:.0%}) — most patients eligible; minimal screening burden"
    elif sero < 0.20:
        score = 1.5
        label = f"moderate (~{sero:.0%}) — significant proportion may require pre-screening or exclusion"
    elif sero < 0.40:
        score = 1.0
        label = f"high (~{sero:.0%}) — substantial patient exclusion expected; immunodepletion protocols may be needed"
    else:
        score = 0.5
        label = f"very high (~{sero:.0%}) — majority of patients may be ineligible; major trial design challenge"

    return score, [f"Vector immunogenicity ({vector_serotype}): {label}"]


# ══════════════════════════════════════════════════════════════════════════════
# DIMENSION 8: THERAPEUTIC WINDOW (max 2.0)
# ══════════════════════════════════════════════════════════════════════════════
#
# Gene therapy can only help if administered before target cells are irreversibly
# damaged. A wide therapeutic window allows straightforward trial design; a very
# narrow window may require neonatal or in utero delivery, significantly increasing
# trial complexity and cost.
#
# Inferred from HPO symptom terms and disease name.
#
def score_therapeutic_window(disease: DiseaseInfo) -> tuple[float, list[str]]:
    """Score the disease's amenability to GT from a natural-history/timing perspective."""
    combined = (" ".join(disease.hpo_terms) + " " + disease.name).lower()

    neonatal = any(t in combined for t in [
        "neonatal onset", "neonatal crisis", "congenital", "in utero", "fetal", "antenatal",
        "hydrops", "stillbirth",
    ])
    rapidly_fatal = any(t in combined for t in [
        "death in infancy", "infantile death", "lethal", "fatal in infancy",
    ])
    progressive = any(t in combined for t in [
        "neurodegenerat", "progressive", "brain atrophy", "white matter",
    ])
    early_childhood = any(t in combined for t in [
        "early-onset", "infantile", "childhood onset", "pediatric",
    ])
    adult_onset = any(t in combined for t in [
        "adult onset", "late onset", "adolescent onset",
    ])
    chronic = any(t in combined for t in [
        "chronic", "slowly progressive", "episodic", "relapsing",
    ])
    irreversible = any(t in combined for t in [
        "intellectual disability", "neurodegenerat", "cirrhosis", "fibrosis", "brain atrophy",
    ])

    if adult_onset or (chronic and not irreversible):
        return 2.0, [
            "Wide therapeutic window — adult or chronic onset; GT can be administered at multiple "
            "timepoints; irreversible damage has not yet occurred at typical diagnosis age"
        ]
    elif progressive and not neonatal:
        return 1.5, [
            "Moderate therapeutic window — progressive disease with childhood onset; "
            "early intervention strongly recommended; newborn screening integration beneficial"
        ]
    elif early_childhood and not neonatal and not rapidly_fatal:
        return 1.2, [
            "Moderate-to-narrow window — early childhood onset; "
            "newborn screening integration would significantly improve outcomes"
        ]
    elif neonatal and not rapidly_fatal:
        return 0.8, [
            "Narrow therapeutic window — neonatal onset requires delivery within weeks of birth; "
            "trial design must incorporate newborn screening programmes"
        ]
    else:
        return 0.5, [
            "Very narrow therapeutic window — congenital or rapidly fatal early onset; "
            "in utero or immediate neonatal GT required; substantially increases trial complexity"
        ]


# ══════════════════════════════════════════════════════════════════════════════
# DIMENSION 9: CROSS-CORRECTION POTENTIAL (max 1.0)
# ══════════════════════════════════════════════════════════════════════════════
#
# Cross-correction is the ability of a transduced cell to secrete the therapeutic
# protein and thereby correct neighbouring, untransduced cells. This dramatically
# amplifies the effective reach of gene therapy — a minority of transduced cells
# can rescue the majority.
#
# Mechanism:
#   Secreted proteins  → diffuse through extracellular space / bloodstream
#   Lysosomal enzymes  → secreted and taken up via mannose-6-phosphate (M6P) receptor
#   Intracellular      → cannot leave the cell; no cross-correction
#   Membrane-bound     → anchored; no cross-correction
#
def score_cross_correction(gene: GeneInfo) -> tuple[float, list[str]]:
    """Score the cross-correction potential of the query gene's protein."""
    locs = [l.lower() for l in gene.subcellular_location]
    kws = [k.lower() for k in gene.keywords]

    is_secreted = gene.is_secreted or any("secret" in l or "extracell" in l for l in locs)
    is_lysosomal = any("lysosom" in l for l in locs) or "lysosome" in kws

    if is_secreted and is_lysosomal:
        return 1.0, [
            "Secreted lysosomal enzyme — maximum cross-correction via M6P receptor pathway; "
            "high therapeutic efficiency; substantially lower required transduction rate"
        ]
    elif is_secreted:
        return 1.0, [
            "Secreted protein — systemic cross-correction via bloodstream; "
            "all cells can benefit from a minority of transduced cells"
        ]
    elif is_lysosomal:
        return 0.8, [
            "Lysosomal enzyme (non-secreted) — moderate cross-correction via M6P pathway; "
            "neighbouring cells can benefit but uptake efficiency is lower than fully secreted"
        ]
    else:
        return 0.2, [
            "Intracellular or membrane-bound protein — no cross-correction possible; "
            "each target cell must individually receive the vector; "
            "requires high transduction efficiency and therefore a higher or more targeted dose"
        ]


# ══════════════════════════════════════════════════════════════════════════════
# DIMENSION 10: IMMUNE PRIVILEGE OF TARGET TISSUE (max 1.0)
# ══════════════════════════════════════════════════════════════════════════════
#
# Immunologically privileged tissues are partially sequestered from the systemic
# immune system by physical barriers or local immunosuppressive signals. In GT:
#   High privilege → lower risk of cytotoxic T-lymphocytes clearing transduced cells
#                 → lower risk of inflammation destroying the therapeutic effect
#                 → more durable long-term transgene expression
#
# Retina: blood-retinal barrier + FasL expression + TGF-β2 → highest privilege
# CNS:    blood-brain barrier limits T-cell access → high privilege
# Liver:  tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1) → moderate-high
# Muscle: moderate immune surveillance
# Haematopoietic: immune cells reside here → lowest privilege
#
_IMMUNE_PRIVILEGE_SCORES: dict[str, tuple[float, str]] = {
    "retina":        (1.0, "highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk"),
    "cns":           (0.9, "high privilege — blood-brain barrier severely limits T-cell access; durable expression expected"),
    "liver":         (0.8, "moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)"),
    "muscle":        (0.6, "moderate immune surveillance — standard immunosuppression protocols typically sufficient"),
    "heart":         (0.6, "moderate privilege; similar immune access to muscle"),
    "kidney":        (0.5, "moderate-low privilege; renal immune surveillance is significant"),
    "hematopoietic": (0.3, "low privilege — immune cells reside here; robust conditioning and monitoring required"),
}


def score_immune_privilege(disease_tissues: list[str]) -> tuple[float, list[str]]:
    """Score immune privilege based on the disease's primary target tissue(s)."""
    if not disease_tissues:
        return 0.5, ["No tissue data — neutral immune privilege score applied"]

    best_score = 0.0
    best_note = ""
    for tissue in disease_tissues:
        score, note = _IMMUNE_PRIVILEGE_SCORES.get(
            tissue.lower(), (0.5, f"Standard immune surveillance assumed for {tissue}")
        )
        if score > best_score:
            best_score = score
            best_note = note

    return best_score, [f"Immune privilege: {best_note}"]


# ══════════════════════════════════════════════════════════════════════════════
# DIMENSION 11: PROMOTER AVAILABILITY (max 1.0)
# ══════════════════════════════════════════════════════════════════════════════
#
# The promoter controls where and how much the therapeutic gene is expressed.
# A validated, tissue-specific promoter is essential for:
#   1. Efficacy: sufficient protein production in the target cell type
#   2. Safety: preventing off-target expression in non-target tissues
#   3. Regulatory confidence: prior clinical validation reduces approval hurdles
#
# Liver and retina have the richest catalogue of validated promoters; kidney
# has almost none in clinical use.
#
_PROMOTER_DATA: dict[str, tuple[float, str]] = {
    "liver":         (1.0, "ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301"),
    "retina":        (1.0, "VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1"),
    "cns":           (0.8, "Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies"),
    "muscle":        (0.8, "MHCK7, CK8, Desmin — validated in Elevidys (DMD) and SMA programs"),
    "hematopoietic": (0.7, "EFS, PGK, SFFV — validated in lentiviral ex vivo programs (ADA-SCID, beta-thalassaemia)"),
    "heart":         (0.6, "CMV/CAG ubiquitous promoters most common; cardiac troponin T (cTnT) available but limited clinical use"),
    "kidney":        (0.4, "Very few validated kidney-specific promoters in clinical use; AQP2 and NPHS2 in research only"),
}


def score_promoter_availability(disease_tissues: list[str]) -> tuple[float, list[str]]:
    """Score based on availability of validated, tissue-specific promoters."""
    if not disease_tissues:
        return 0.5, ["No tissue data — neutral promoter availability score applied"]

    best_score = 0.0
    best_note = ""
    for tissue in disease_tissues:
        score, note = _PROMOTER_DATA.get(
            tissue.lower(), (0.5, f"Limited clinical-grade promoters validated for {tissue}")
        )
        if score > best_score:
            best_score = score
            best_note = note

    return best_score, [f"Promoter availability: {best_note}"]


# ══════════════════════════════════════════════════════════════════════════════
# DIMENSION 12: ROUTE OF ADMINISTRATION FEASIBILITY (max 1.0)
# ══════════════════════════════════════════════════════════════════════════════
#
# The route of administration (RoA) is how the vector reaches the target tissue.
# Feasibility depends on tissue accessibility, procedural invasiveness, and
# whether the RoA has been used in prior approved programs.
#
# Liver/muscle: IV or IM — simple, well-established
# CNS: intrathecal/ICV — invasive but used in OAV101-IT, RGX-121
# Retina: subretinal/intravitreal injection — specialist procedure; used in Luxturna
# Haematopoietic: ex vivo HSC — complex but highly precise
# Kidney: no established clinical route yet
#
_ROA_DATA: dict[str, tuple[float, str]] = {
    "liver":         (1.0, "IV systemic — established, minimally invasive; used in all hepatic GT programs"),
    "muscle":        (0.9, "IV systemic or intramuscular injection — well established; used in SMA, DMD, Glybera"),
    "hematopoietic": (0.9, "Ex vivo HSC delivery — technically complex but highly precise; gold standard for blood disorders"),
    "retina":        (0.8, "Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010"),
    "cns":           (0.7, "Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk"),
    "heart":         (0.6, "Intracoronary infusion or IV systemic; cardiac-specific delivery is technically demanding"),
    "kidney":        (0.4, "No well-established kidney-specific GT delivery route in clinical programs; renal artery infusion in early research"),
}


def score_roa_feasibility(disease_tissues: list[str]) -> tuple[float, list[str]]:
    """Score the feasibility and precedent of the required delivery route."""
    if not disease_tissues:
        return 0.5, ["No tissue data — neutral RoA feasibility score"]

    best_score = 0.0
    best_note = ""
    for tissue in disease_tissues:
        score, note = _ROA_DATA.get(
            tissue.lower(), (0.5, f"Delivery route to {tissue} not well established in clinical programs")
        )
        if score > best_score:
            best_score = score
            best_note = note

    return best_score, [f"Route of administration: {best_note}"]


# ══════════════════════════════════════════════════════════════════════════════
# MAIN SCORING FUNCTION: combines all 12 dimensions for one program
# ══════════════════════════════════════════════════════════════════════════════
def score_program(
    disease: DiseaseInfo,   # ← the query disease
    gene: GeneInfo,         # ← its causal gene
    program: dict,          # ← one GT program from the catalog (e.g. Zolgensma row)
    vector: dict,           # ← the vector used by that program (e.g. AAV9 row)
) -> ScoreBreakdown:

    notes: list[str] = []

    # ── Step 1: Packaging (hard gate) ─────────────────────────────────────
    pkg, pkg_notes = score_packaging(gene, program["cds_bp"], vector["cargo_limit_bp"])
    notes.extend(pkg_notes)

    if pkg == 0.0:
        # ← Gene doesn't fit → immediate fail, skip all other scoring
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
            immunogenicity=0.0,
            therapeutic_window=0.0,
            cross_correction=0.0,
            immune_privilege=0.0,
            promoter_availability=0.0,
            roa_feasibility=0.0,
            notes=notes,
        )

    # ── Step 2: Tropism ───────────────────────────────────────────────────
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

    # ── Step 3: Protein class ─────────────────────────────────────────────
    prc, prc_notes = score_protein_class(gene, program["protein_class"])
    notes.extend(prc_notes)

    # ── Step 4: Inheritance ───────────────────────────────────────────────
    inh, inh_notes = score_inheritance(disease.inheritance, program["inheritance"])
    notes.extend(inh_notes)

    # ── Step 5: Pathway ───────────────────────────────────────────────────
    pth, pth_notes = score_pathway(disease, gene, program["pathway"])
    notes.extend(pth_notes)

    # ── Step 6: Approval ──────────────────────────────────────────────────
    apv, apv_notes = score_approval(program["approval_status"])
    notes.extend(apv_notes)

    # ── Step 7: Immunogenicity ────────────────────────────────────────────
    # ← uses the vector serotype to look up published seroprevalence rates
    imm, imm_notes = score_immunogenicity(program["vector"])
    notes.extend(imm_notes)

    # ── Step 8: Therapeutic window ────────────────────────────────────────
    # ← uses the disease's HPO terms to infer how wide the treatment window is
    # ← same score for all precedent programs (it's a property of the query disease)
    tw, tw_notes = score_therapeutic_window(disease)
    notes.extend(tw_notes)

    # ── Step 9: Cross-correction ──────────────────────────────────────────
    # ← uses the gene's protein localisation to determine cross-correction capacity
    # ← same for all precedent programs (it's a property of the query gene)
    cc, cc_notes = score_cross_correction(gene)
    notes.extend(cc_notes)

    # ── Step 10: Immune privilege ─────────────────────────────────────────
    # ← uses the disease's target tissues to score immunological privilege
    ip, ip_notes = score_immune_privilege(disease.affected_tissues)
    notes.extend(ip_notes)

    # ── Step 11: Promoter availability ────────────────────────────────────
    # ← scores whether validated tissue-specific promoters exist for target tissues
    pa, pa_notes = score_promoter_availability(disease.affected_tissues)
    notes.extend(pa_notes)

    # ── Step 12: Route of administration feasibility ──────────────────────
    # ← scores how accessible the target tissue is via established delivery routes
    roa, roa_notes = score_roa_feasibility(disease.affected_tissues)
    notes.extend(roa_notes)

    # ── Final composite score ─────────────────────────────────────────────
    # Raw sum across all 12 dimensions (max = 18.0)
    # Normalized to out of 10 for consistent interpretation.
    raw_sum = pkg + trp + prc + pth + inh + apv + imm + tw + cc + ip + pa + roa
    composite = round((raw_sum / _RAW_MAX) * 10.0, 2)

    confidence = "high" if composite >= 7.5 else "medium" if composite >= 5.0 else "low"

    return ScoreBreakdown(
        program_name=program["name"],
        program_disease=program["disease"],
        vector=program["vector"],
        tissue_target=program["tissue_target"],
        approval_status=program["approval_status"],
        composite_score=composite,
        confidence=confidence,
        packaging_fit=pkg,
        tropism_match=trp,
        protein_class_match=prc,
        inheritance_match=inh,
        pathway_similarity=pth,
        approval_weight=apv,
        immunogenicity=imm,
        therapeutic_window=tw,
        cross_correction=cc,
        immune_privilege=ip,
        promoter_availability=pa,
        roa_feasibility=roa,
        notes=notes,
    )


# ══════════════════════════════════════════════════════════════════════════════
# RANK ALL PROGRAMS: runs score_program() on every GT program in the database
# ══════════════════════════════════════════════════════════════════════════════
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
            vec = {"cargo_limit_bp": 4700, "tissue_tropism": "[]"}
        scores.append(score_program(disease, gene, prog, vec))

    scores.sort(key=lambda s: (-s.composite_score, s.program_name))
    return scores
