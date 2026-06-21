"""
14-dimension scoring engine.

For a given (disease, gene, target tissues) tuple, scores each GT program
in the catalog as a potential precedent/surrogate.

Dimensions:
  1.  packaging_fit         — gene CDS vs. vector cargo limit
  2.  tropism_match         — vector tissue tropism vs. disease target tissues
  3.  protein_class         — same lysosomal/secreted/membrane/intracellular class
  4.  inheritance           — AR/XL/AD compatibility
  5.  pathway_similarity    — same biological pathway
  6.  modality_compatibility — disease mechanism supports gene-addition precedent
  7.  approval_weight       — approved programs score higher
  8.  immunogenicity        — pre-existing neutralising antibody seroprevalence for vector
  9.  therapeutic_window    — can intervention occur before irreversible damage?
  10. cross_correction      — can transduced cells rescue untransduced neighbours?
  11. immune_privilege      — immunological privilege of the target tissue
  12. promoter_availability — validated tissue-specific promoters exist for target
  13. roa_feasibility       — accessible, established delivery route to target tissue
  14. organelle_targeting   — can standard nuclear AAV delivery produce protein at
                              the correct subcellular compartment? (NEW — v2)

CHANGELOG v2:
  - Dimension 3 (protein_class): now distinguishes lysosomal MEMBRANE proteins
    (channels/transporters, e.g. MCOLN1, SLC17A5) from lysosomal ENZYMES.
    Cross-correction via the M6P receptor pathway requires a SOLUBLE, secretable
    enzyme; it is physically impossible for a membrane-anchored channel or
    transporter. Previously these proteins received an inflated protein-class
    score (2.0) and cross-correction score (0.8) matching lysosomal enzyme
    programs. They now receive 1.0 and 0.0 respectively.
  - Dimension 10 (cross_correction): lysosomal membrane proteins now correctly
    return 0.0 (no cross-correction possible) instead of 0.8.
  - Dimension 14 (organelle_targeting) ADDED: penalises diseases where standard
    nuclear AAV delivery cannot produce a functional protein at the correct
    subcellular location. Scores: cytoplasmic/nuclear/secreted → 1.0; peroxisomal
    → 0.7; mitochondrial matrix (nuclear-encoded) → 0.5; mitochondrial DNA gene
    (MT-*) → 0.0 (allotopic expression required, a fundamentally different
    strategy not represented in this catalog).
  - RAW_MAX updated from 20.0 → 21.0 to accommodate the new dimension.
  - build_review_flags(): added specific flags for lysosomal membrane proteins,
    mitochondrial matrix enzymes, mtDNA genes, unresolved disease biology,
    multi-subunit enzyme complexes, and neuronopathic disease subtypes.
"""

# ── What this file is ──────────────────────────────────────────────────────
# THE ALGORITHM. This is the intellectual core of the dissertation.
# It takes one disease + one gene and scores every GT program in the catalog
# across 14 dimensions. Raw scores are normalized to a composite out of 10.
# Highest composite = best precedent match.
#
# Max raw scores per dimension:
#   packaging_fit         → max 2.0
#   tropism_match         → max 2.0
#   protein_class         → max 2.0
#   pathway_similarity    → max 2.0
#   modality_compatibility → max 2.0
#   inheritance_match     → max 1.0
#   approval_weight       → max 1.0
#   immunogenicity        → max 2.0
#   therapeutic_window    → max 2.0
#   cross_correction      → max 1.0
#   immune_privilege      → max 1.0
#   promoter_availability → max 1.0
#   roa_feasibility       → max 1.0
#   organelle_targeting   → max 1.0   ← NEW in v2
#   ─────────────────────────────
#   RAW TOTAL MAX         = 21.0      ← updated from 20.0
#   NORMALIZED (× 10/21)  = 10.0

from __future__ import annotations
import json
from dataclasses import dataclass, field, replace
from typing import Optional
import sqlite3

from .disease import DiseaseInfo
from .gene import GeneInfo
from .mechanism import lookup_mechanism, score_gene_addition_compatibility

_RAW_MAX = 21.0  # ← total of all dimension maxima; updated to 21.0 in v2 (added organelle_targeting dim)


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
    modality_compatibility: float  # ← 0–2: does disease mechanism support gene addition?
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

    organelle_targeting: float = 0.0
    # ← 0–1: can standard nuclear AAV delivery produce a functional protein at the
    #   correct subcellular compartment?  (NEW dimension, v2)
    #
    #   AAV delivers a transgene to the NUCLEUS. The gene is transcribed normally and
    #   the protein is translated by cytoplasmic ribosomes. This works directly for
    #   cytoplasmic, nuclear, secreted, and lysosomal proteins.
    #
    #   It requires additional validated steps for:
    #     0.7 — Peroxisomal proteins: PTS1/PTS2 targeting signal must be preserved
    #     0.5 — Mitochondrial matrix/inner-membrane proteins (nuclear-encoded):
    #            the N-terminal mitochondrial targeting sequence (MTS) must be preserved
    #            and functional in the delivered construct for post-translational import
    #     0.0 — Mitochondrial DNA-encoded genes (MT-*): these are transcribed by
    #            mitochondrial ribosomes using a non-standard genetic code;
    #            nuclear AAV delivery CANNOT produce these proteins without allotopic
    #            expression (a fundamentally different, disease-specific approach not
    #            represented in this catalog; GS010/Lumevoq for LHON is one example)
    #
    #   Rationale: Without this dimension, diseases like LHON (MT-ND4) and MMA (MUT)
    #   received scores built on false analogies to nuclear gene addition programs.
    #   This dimension makes the incompatibility explicit and numerically visible.

    notes: list[str] = field(default_factory=list)  # ← plain-English explanation of each score
    review_flags: list[str] = field(default_factory=list)
    # ← translational caveats that should be reviewed after ranking.
    # These are deliberately separate from confidence: a program can be the
    # best catalog precedent and still need manual clinical/scientific review.


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


def _packaging_gene_for_program(
    disease_gene: GeneInfo,
    program: dict,
) -> tuple[GeneInfo, list[str]]:
    """Return the construct to use for packaging checks.

    Most programs must package the query disease gene itself. A small number of
    precedents use engineered mini/micro transgenes for oversized genes, where
    the clinically relevant question is not "does native CDS fit?" but "is
    there a precedent for a shortened construct strategy?"
    """
    program_symbol = str(program.get("gene_symbol", ""))
    program_symbol_l = program_symbol.lower()
    disease_symbol_l = disease_gene.symbol.lower()
    engineered_markers = ("micro", "mini", "truncated")

    is_engineered_same_gene = (
        disease_symbol_l
        and disease_symbol_l in program_symbol_l
        and program_symbol_l != disease_symbol_l
        and any(marker in program_symbol_l for marker in engineered_markers)
    )

    if not is_engineered_same_gene:
        return disease_gene, []

    notes = [
        f"Native {disease_gene.symbol} CDS ({disease_gene.cds_length_bp or 'unknown'}bp) "
        f"is oversized; scoring engineered {program_symbol} construct "
        f"({program['cds_bp']}bp) as a micro/mini-transgene strategy, not full-length replacement"
    ]
    return (
        replace(
            disease_gene,
            symbol=program_symbol,
            cds_length_bp=program["cds_bp"],
            aa_length=None,
        ),
        notes,
    )


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
def _classify_gene_protein(gene_info: GeneInfo) -> tuple[bool, bool, bool, bool]:
    """Return (is_secreted, is_lysosomal_enzyme, is_lysosomal_membrane, is_membrane) for a gene.

    The critical distinction added in v2 is between:
      - lysosomal ENZYMES  (e.g. ARSA, IDUA, GBA): soluble, secretable, can cross-correct
                            via the mannose-6-phosphate (M6P) receptor uptake pathway
      - lysosomal MEMBRANE proteins (e.g. MCOLN1/mucolipin-1, SLC17A5/sialin): anchored
                            in the lysosomal membrane; cannot be secreted; cannot cross-correct;
                            every target cell must individually receive the vector

    Before v2, both classes were treated as "lysosomal" and received the same 2.0 protein-
    class score when matched against lysosomal-enzyme precedent programs (Libmeldy, etc.).
    This inflated scores for MCOLN1 (ML-IV, 9.1/10) and SLC17A5 (Salla disease, 8.8/10)
    because the cross-correction mechanism of those precedents does not apply.
    """
    kws = [k.lower() for k in (gene_info.keywords or [])]
    locs = [l.lower() for l in (gene_info.subcellular_location or [])]

    is_secreted = gene_info.is_secreted or any(
        "secret" in l or "extracell" in l for l in locs
    )
    is_lysosomal = any("lysosom" in l for l in locs) or "lysosome" in kws

    # A lysosomal protein is a MEMBRANE protein if it sits in the lysosomal membrane
    # (transmembrane anchor) OR if it is a channel/transporter/pump.
    # These cannot be secreted and therefore cannot be taken up by neighbouring cells.
    is_lysosomal_membrane = is_lysosomal and (
        any("membran" in l for l in locs)          # explicit membrane location
        or any(
            term in k
            for k in kws
            for term in ("channel", "transport", "pump", "antiport", "symport", "ion")
        )
        or any(
            term in l
            for l in locs
            for term in ("membrane",)
        )
    )
    is_lysosomal_enzyme = is_lysosomal and not is_lysosomal_membrane

    # General membrane flag (non-lysosomal)
    is_membrane = (
        any("membran" in l or "sarcolemma" in l for l in locs)
        or any("membran" in k for k in kws)
    )

    return is_secreted, is_lysosomal_enzyme, is_lysosomal_membrane, is_membrane


def score_protein_class(
    gene_info: GeneInfo,     # ← the query disease's gene
    program_class: str,      # ← protein class of the precedent program, e.g. "lysosomal", "secreted"
) -> tuple[float, list[str]]:
    # ← Protein class matters because the delivery mechanism works differently:
    #   - Secreted proteins: one cell makes the protein, neighbours benefit too ("cross-correction")
    #   - Lysosomal ENZYMES: similar cross-correction via M6P receptor uptake pathway
    #   - Lysosomal MEMBRANE proteins: cell-autonomous — CANNOT cross-correct (v2 fix)
    #   - Membrane/intracellular: each cell needs its own copy → harder to treat

    is_secreted, is_lysosomal_enzyme, is_lysosomal_membrane, is_membrane = (
        _classify_gene_protein(gene_info)
    )
    pc = program_class.lower()

    # ── Lysosomal matches (most common in this catalog) ───────────────────
    if "lysosomal" in pc and is_lysosomal_enzyme:
        # Both are soluble lysosomal proteins → cross-correction via M6P pathway is viable
        return 2.0, ["Both lysosomal enzymes — cross-correction via M6P receptor pathway likely"]

    if "lysosomal" in pc and is_lysosomal_membrane:
        # BUG FIX (v2): lysosomal membrane protein matched against a lysosomal-enzyme
        # precedent (e.g. MCOLN1 vs Libmeldy or SLC17A5 vs Libmeldy).
        # The pathway is shared (lysosome) but the MECHANISM is incompatible:
        # Libmeldy/Skysona work because ARSA/ABCD1 enzymes are secreted by HSC-derived
        # microglia and taken up by neurons. A membrane channel or transporter cannot
        # be secreted; it must be delivered to every individual cell.
        return 1.0, [
            "Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE "
            "protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated "
            "cross-correction mechanism of the matched precedent is not applicable. "
            "Direct per-cell vector delivery to every target neuron is required."
        ]

    # ── Other protein classes ──────────────────────────────────────────────
    if "secreted" in pc and is_secreted:
        return 2.0, ["Both secreted proteins — systemic delivery viable"]
    if "intracellular" in pc and not is_secreted and not is_lysosomal_enzyme and not is_lysosomal_membrane and not is_membrane:
        return 1.5, ["Both intracellular proteins"]
    if "membrane" in pc and is_membrane:
        return 1.5, ["Both membrane proteins"]
    if is_secreted or is_lysosomal_enzyme:
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
    """Score the cross-correction potential of the query gene's protein.

    v2 fix: lysosomal membrane proteins (channels/transporters) now correctly
    receive 0.0 instead of 0.8.

    Cross-correction requires that the therapeutic protein can LEAVE the producing
    cell and be TAKEN UP by neighbouring cells. This applies to:
      - Secreted proteins (diffuse through extracellular space / bloodstream)
      - Soluble lysosomal enzymes (secreted via M6P-tagged vesicles, recaptured
        by M6P receptors on neighbouring lysosomes)

    It does NOT apply to:
      - Lysosomal MEMBRANE channels/transporters (anchored in the membrane;
        cannot be exocytosed as soluble cargo; e.g. MCOLN1, SLC17A5)
      - Intracellular proteins (stay inside the producing cell)
      - Membrane-bound structural proteins (e.g. dystrophin)
    """
    is_secreted, is_lysosomal_enzyme, is_lysosomal_membrane, _ = (
        _classify_gene_protein(gene)
    )

    if is_secreted and is_lysosomal_enzyme:
        return 1.0, [
            "Secreted lysosomal enzyme — maximum cross-correction via M6P receptor pathway; "
            "high therapeutic efficiency; substantially lower required transduction rate"
        ]
    elif is_secreted:
        return 1.0, [
            "Secreted protein — systemic cross-correction via bloodstream; "
            "all cells can benefit from a minority of transduced cells"
        ]
    elif is_lysosomal_membrane:
        # BUG FIX (v2): previously returned 0.8 as "lysosomal enzyme (non-secreted)".
        # Lysosomal membrane proteins (channels, transporters) are ANCHORED in the
        # lysosomal membrane and cannot be secreted or taken up by neighbouring cells.
        # Each target cell must individually be transduced — no bystander rescue.
        return 0.0, [
            "Lysosomal MEMBRANE protein (channel/transporter) — no cross-correction possible. "
            "The protein is anchored in the lysosomal membrane and cannot be released as "
            "soluble cargo. Every target cell must individually receive the vector. "
            "HSC-based lentiviral programs (Libmeldy) depend on secreted enzyme cross-"
            "correction and are not applicable as direct strategies for this protein class."
        ]
    elif is_lysosomal_enzyme:
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
# DIMENSION 14: ORGANELLE TARGETING FEASIBILITY (max 1.0)  ← NEW in v2
# ══════════════════════════════════════════════════════════════════════════════
#
# Standard AAV gene therapy delivers the transgene to the NUCLEUS, where it is
# transcribed by the cell's RNA polymerase and translated by cytoplasmic ribosomes.
# The resulting protein is functional without further targeting for most disease genes.
#
# However, some proteins must reach specific organelles AFTER translation:
#   Mitochondrial matrix proteins (nuclear-encoded): the mature protein is produced
#     in the cytoplasm and imported post-translationally into the mitochondria via an
#     N-terminal mitochondrial targeting sequence (MTS). Standard AAV is theoretically
#     feasible, but the MTS in the therapeutic construct must be intact and functional.
#     Example: MUT (methylmalonyl-CoA mutase) in methylmalonic acidemia (ORPHA:27).
#
#   Mitochondrial DNA-encoded proteins (MT-* genes): these genes reside in the
#     mitochondrial genome, use a non-standard genetic code, and are translated by
#     mitochondrial ribosomes inside the organelle. Nuclear AAV cannot produce these
#     proteins. The only nuclear gene-therapy approach requires "allotopic expression":
#     the gene is recoded for cytoplasmic translation, given an artificial MTS, and
#     the import/assembly is re-engineered. This is a disease-specific, specialist
#     strategy NOT represented in this precedent catalog.
#     Example: MT-ND4 in Leber hereditary optic neuropathy (ORPHA:104).
#     Real-world precedent: GS010/Lumevoq uses this allotopic approach (Phase 3 completed;
#     EMA MAA voluntarily withdrawn April 2023 after primary endpoint not met vs sham).
#
#   Peroxisomal proteins: targeted via PTS1/PTS2 signal; AAV is feasible but the
#     peroxisomal targeting signal must be preserved in the construct.
#     Example: ABCD1 (X-linked adrenoleukodystrophy, ORPHA:43).
#
# WHY THIS MATTERS FOR SCORING:
#   Without this dimension, LHON (MT-ND4) received a composite score of 6.8/10 based
#   on comparisons to nuclear gene-addition programs — a category error.
#   MMA (MUT) received 7.8/10 without any flag that the mitochondrial import step is
#   an unvalidated prerequisite. This dimension makes these gaps numerically explicit.
#
def score_organelle_targeting(
    gene: GeneInfo,
    disease: DiseaseInfo,
) -> tuple[float, list[str]]:
    """Score whether standard nuclear AAV delivery can produce a functional protein
    at the correct subcellular compartment for the query disease gene.
    """
    symbol = (gene.symbol or "").upper()
    locs = [l.lower() for l in (gene.subcellular_location or [])]
    kws = [k.lower() for k in (gene.keywords or [])]

    # ── 1. Mitochondrial DNA-encoded genes (MT-*) ────────────────────────────
    # These are the most severe case: the gene lives in mtDNA, not the nucleus.
    # Standard nuclear AAV delivery is fundamentally inapplicable without allotopic
    # expression engineering.
    #
    # Detection: gene symbol starts with "MT-" (HGNC convention for mitochondrial genes)
    # OR the disease has mitochondrial inheritance (maternally inherited).
    is_mtdna_gene = symbol.startswith("MT-") and len(symbol) > 3
    has_mito_inheritance = any(
        "mitochondri" in i.lower() for i in (disease.inheritance or [])
    )

    if is_mtdna_gene or has_mito_inheritance:
        return 0.0, [
            f"ORGANELLE TARGETING: INCOMPATIBLE — {symbol} is a mitochondrial DNA-encoded "
            "gene. Standard nuclear AAV delivery cannot produce a functional protein at the "
            "mitochondrial target site. Treatment requires allotopic expression: cytoplasmic "
            "recoding of the gene using the standard genetic code plus an artificial "
            "mitochondrial targeting sequence (MTS). This strategy is disease-specific and "
            "fundamentally different from the nuclear gene-addition programs in this catalog. "
            "All precedent scores for this disease should be treated as cross-paradigm "
            "comparisons only, not direct development templates. "
            "(Real-world precedent: GS010/Lumevoq for MT-ND4/LHON; Phase 3 completed, EMA MAA withdrawn April 2023.)"
        ]

    # ── 2. Nuclear-encoded mitochondrial matrix/inner-membrane proteins ──────
    # The gene is in the nucleus (AAV can deliver it), but after cytoplasmic translation
    # the protein must be imported into mitochondria via an N-terminal MTS.
    # AAV gene therapy is theoretically viable, but MTS integrity is not verified
    # by any other dimension in this framework.
    is_mito_matrix = any(
        "mitochondri" in l and ("matrix" in l or "inner membrane" in l) for l in locs
    )
    is_mito_protein = (
        any("mitochondri" in l for l in locs)
        or "mitochondrion" in kws
        or any("mitochondri" in k for k in kws)
    )

    if is_mito_matrix:
        return 0.5, [
            f"ORGANELLE TARGETING: CONDITIONAL — {symbol} is a nuclear-encoded "
            "mitochondrial matrix protein. Nuclear AAV delivery is theoretically feasible "
            "(the gene is in the nuclear genome) but the N-terminal mitochondrial targeting "
            "sequence (MTS) must be preserved intact in the therapeutic construct for correct "
            "post-translational import into the mitochondrial matrix. MTS functionality is not "
            "validated by any other dimension in this framework. Confirm import efficiency "
            "with disease-specific in vitro/in vivo data before treating vector precedent "
            "scores as directly transferable."
        ]

    if is_mito_protein:
        # Mitochondrial but not explicitly matrix — could be outer membrane, IMS, etc.
        # Lower penalty than matrix; flagged but not heavily penalised.
        return 0.6, [
            f"ORGANELLE TARGETING: VERIFY — {symbol} has mitochondrial localisation. "
            "Nuclear AAV delivery is feasible for nuclear-encoded mitochondrial proteins, "
            "but confirm that targeting signals in the construct are intact and that the "
            "protein reaches the correct mitochondrial sub-compartment."
        ]

    # ── 3. Peroxisomal proteins ──────────────────────────────────────────────
    # Targeted via PTS1 (C-terminal SKL tripeptide) or PTS2 (N-terminal signal).
    # AAV delivery is feasible; the targeting signal must be preserved.
    # Examples: ABCD1 (X-ALD), PEX genes.
    is_peroxisomal = (
        any("peroxisom" in l for l in locs)
        or "peroxisome" in kws
        or any("peroxisom" in k for k in kws)
    )
    if is_peroxisomal:
        return 0.7, [
            f"ORGANELLE TARGETING: VERIFY — {symbol} is a peroxisomal protein. "
            "Nuclear AAV delivery is feasible; the peroxisomal targeting signal (PTS1/PTS2) "
            "must be preserved in the construct for correct organelle import."
        ]

    # ── 4. Standard localisation ─────────────────────────────────────────────
    # Cytoplasmic, nuclear, secreted, lysosomal, ER membrane, plasma membrane:
    # nuclear AAV delivery directly produces functional protein at the correct location.
    return 1.0, [
        f"ORGANELLE TARGETING: COMPATIBLE — {symbol} standard subcellular localisation; "
        "nuclear AAV delivery directly produces functional protein at the correct "
        "cellular compartment with no additional organelle-import steps required."
    ]


def _normalised_tissue_set(tissues: list[str]) -> set[str]:
    """Normalize tissue labels for comparison."""
    return {t.lower() for t in tissues if t}


def _is_gene_replacement_friendly(disease: DiseaseInfo) -> bool:
    inheritance = " ".join(disease.inheritance or []).lower()
    return "recessive" in inheritance or "x-linked" in inheritance


def build_review_flags(
    disease: DiseaseInfo,
    gene: GeneInfo,
    vector_tropism: list[str],
    vector_serotype: str,
    tropism_score: float,
    cross_correction_score: float,
    therapeutic_window_score: float,
    strategy_notes: list[str],
    organelle_targeting_score: float = 1.0,  # ← new parameter (v2); default 1.0 = no issue
) -> list[str]:
    """Generate translational review flags that are not captured by rank alone.

    v2 additions:
      - Lysosomal membrane protein flag (MCOLN1, SLC17A5 class)
      - Mitochondrial DNA gene flag (MT-* class; allotopic expression required)
      - Mitochondrial matrix enzyme flag (MUT, BCKDHA, OTC class; MTS validation needed)
      - Unresolved disease biology flag (ROGDI class)
      - Multi-subunit enzyme complex flag (BCKDHA/MSUD class)
      - Neuronopathic subtype ambiguity flag (GBA/Gaucher class)
      - Defensive None-guards on all list accesses to prevent crashes on unknown diseases
    """
    flags: list[str] = []
    disease_tissues = _normalised_tissue_set(disease.affected_tissues or [])
    vector_tissues = _normalised_tissue_set(vector_tropism or [])
    uncovered = sorted(disease_tissues - vector_tissues)

    # ── Protein biology flags (NEW in v2) ────────────────────────────────────
    locs_l = [l.lower() for l in (gene.subcellular_location or [])]
    kws_l = [k.lower() for k in (gene.keywords or [])]
    symbol = (gene.symbol or "").upper()

    # Flag A: Lysosomal membrane proteins
    # These are physically incapable of cross-correction via M6P receptor uptake.
    # Scores from HSC/LV programs (Libmeldy, Skysona) are platform comparisons only.
    gene_is_lysosomal = any("lysosom" in l for l in locs_l) or "lysosome" in kws_l
    gene_is_lysosomal_membrane = gene_is_lysosomal and (
        any("membran" in l for l in locs_l)
        or any(
            term in k
            for k in kws_l
            for term in ("channel", "transport", "pump", "antiport", "symport", "ion")
        )
    )
    if gene_is_lysosomal_membrane:
        flags.append(
            f"LYSOSOMAL MEMBRANE PROTEIN ({symbol}): the disease gene encodes a lysosomal "
            "membrane channel or transporter, NOT a soluble secretable enzyme. "
            "The HSC-lentiviral cross-correction strategy of precedent programs such as "
            "Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from "
            "microglia and M6P receptor-mediated uptake by neurons — a mechanism that is "
            "physically impossible for a membrane-anchored protein. "
            "Direct in vivo AAV delivery to individual target neurons is required. "
            "Precedent scores from HSC/LV programs compare delivery platform only, "
            "not therapeutic mechanism."
        )

    # Flag B: Mitochondrial DNA-encoded genes (MT-*)
    is_mtdna_gene = symbol.startswith("MT-") and len(symbol) > 3
    has_mito_inheritance = any(
        "mitochondri" in i.lower() for i in (disease.inheritance or [])
    )
    if is_mtdna_gene or has_mito_inheritance:
        flags.append(
            f"MITOCHONDRIAL DNA GENE ({symbol}): this gene is encoded in the mitochondrial "
            "genome, translated by mitochondrial ribosomes using a non-standard genetic code. "
            "Standard nuclear AAV gene addition CANNOT produce this protein. "
            "Treatment requires allotopic expression: the gene must be recoded for "
            "cytoplasmic translation and given an artificial MTS — a strategy "
            "fundamentally different from every program in this catalog. "
            "All precedent scores are cross-paradigm comparisons. "
            "See: GS010/Lumevoq (Gensight Biologics) as a real-world allotopic precedent."
        )

    # Flag C: Nuclear-encoded mitochondrial matrix enzymes (MTS validation required)
    is_mito_matrix = any(
        "mitochondri" in l and ("matrix" in l or "inner membrane" in l) for l in locs_l
    )
    if is_mito_matrix and not is_mtdna_gene and not has_mito_inheritance:
        flags.append(
            f"MITOCHONDRIAL MATRIX ENZYME ({symbol}): nuclear-encoded but the protein must "
            "be imported into the mitochondrial matrix post-translation via its N-terminal "
            "mitochondrial targeting sequence (MTS). Nuclear AAV delivery is theoretically "
            "feasible, but the therapeutic construct must preserve the intact MTS. "
            "MTS functionality is not captured by any other scoring dimension — this is an "
            "additional disease-specific development step requiring experimental validation."
        )

    # Flag D: Multi-subunit enzyme complexes
    # Gene addition of one subunit of a multi-gene complex may be insufficient alone.
    gene_name_lower = (gene.protein_name or "").lower()
    is_multisubunit = (
        any(
            term in kws_l or term in gene_name_lower
            for term in ("subunit alpha", "subunit beta", "e1 alpha", "e1 beta", "subunit a")
        )
        or (any("subunit" in k for k in kws_l) and any("complex" in k for k in kws_l))
    )
    if is_multisubunit:
        flags.append(
            f"MULTI-SUBUNIT ENZYME ({symbol}): the disease gene encodes one subunit of a "
            "multi-polypeptide enzyme complex. Scoring addresses this subunit only. "
            "Confirm whether restoring this single subunit reconstitutes full enzymatic "
            "activity, or whether co-delivery of other complex subunits is required."
        )

    # Flag E: Unresolved disease biology
    # Detect when the mechanism evidence states that gene function is not fully characterised.
    mechanism = lookup_mechanism(disease.orphanet_id, gene.symbol)
    mech_detail_lower = (mechanism.mechanism_detail or "").lower()
    if any(
        phrase in mech_detail_lower
        for phrase in ("not fully resolved", "not well understood", "poorly characterised",
                       "biology is not fully", "not been established")
    ):
        flags.append(
            f"UNRESOLVED DISEASE BIOLOGY ({symbol}): the molecular function of the gene "
            "product is not fully characterised in the literature. Scoring assumes a "
            "standard LOF mechanism compatible with gene addition, but this assumption "
            "has not been experimentally validated. Do not use this score as evidence of "
            "gene therapy tractability without independent confirmation of gene function, "
            "target cell type, and expected therapeutic benefit."
        )

    # Flag F: Neuronopathic vs non-neuronopathic disease subtypes
    disease_name_lower = (disease.name or "").lower()
    neuronopathic_cases = [
        ("gaucher", "Gaucher disease has non-neuronopathic (type 1) and neuronopathic "
         "(types 2/3) subtypes requiring fundamentally different GT strategies. "
         "Specify subtype before applying these scores."),
        ("niemann-pick", "Niemann-Pick disease encompasses mechanistically distinct subtypes "
         "(types A/B: SMPD1; type C: NPC1/NPC2). Confirm gene and subtype before use."),
        ("fabry", "Fabry disease has classic and late-onset phenotypes with different "
         "tissue involvement. CNS/cardiac delivery requirements vary by phenotype."),
    ]
    for keyword, message in neuronopathic_cases:
        if keyword in disease_name_lower:
            flags.append(f"DISEASE HETEROGENEITY: {message}")
            break

    # ── Existing flags (updated for v2 robustness) ───────────────────────────

    if len(disease.gene_symbols or []) > 1:
        flags.append(
            "Multiple causal genes listed; score is gene-specific and should be repeated for each molecular subtype"
        )

    if len(disease_tissues) >= 3:
        flags.append(
            "Multi-system disease; define a primary therapeutic target tissue before selecting route/vector"
        )
    elif len(disease_tissues) == 2 and {"cns", "heart"} & disease_tissues:
        flags.append(
            "Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints"
        )

    if uncovered and disease_tissues:
        flags.append(
            "Vector does not naturally cover all annotated disease tissues: "
            + ", ".join(uncovered)
        )

    if tropism_score <= 0.3:
        flags.append(
            "No direct tissue overlap; treat this as weak precedent unless route or modality is changed"
        )
    elif tropism_score < 1.5:
        flags.append(
            "Only partial tissue match; verify target-cell transduction and delivery route manually"
        )

    if cross_correction_score <= 0.2 and len(disease_tissues) > 1:
        flags.append(
            "Cell-autonomous protein across multiple tissues; high transduction coverage may be required"
        )

    if therapeutic_window_score <= 0.8:
        flags.append(
            "Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility"
        )
    elif therapeutic_window_score < 1.5:
        flags.append(
            "Therapeutic window is not wide; natural-history timing and irreversible damage should be reviewed"
        )

    if gene.cds_length_bp and gene.cds_length_bp > 4700:
        flags.append(
            "Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy"
        )

    if strategy_notes:
        flags.append(
            "Engineered mini/micro-transgene strategy scored; not equivalent to full-length native gene replacement"
        )

    if not _is_gene_replacement_friendly(disease):
        flags.append(
            "Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology"
        )

    compatibility = mechanism.gene_addition_compatibility.lower()
    if mechanism.evidence_status == "missing":
        flags.append(
            "No curated disease-mechanism evidence; do not infer gene-addition suitability from inheritance alone"
        )
    elif compatibility == "conditional":
        flags.append(
            "Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable"
        )
    elif compatibility in {"uncertain", "incompatible"}:
        flags.append(
            "Mechanism evidence does not cleanly support simple gene addition; consider RNA, editing, silencing, mitochondrial, or other non-catalog modalities"
        )

    # Combined text for catch-all pattern checks — use safe joins
    combined_mechanism_text = " ".join([
        " ".join(disease.inheritance or []),
        " ".join(disease.hpo_terms or []),
        " ".join(gene.keywords or []),
        " ".join(gene.subcellular_location or []),
    ]).lower()

    # Only add generic mitochondrial flag if NOT already covered by specific flags B or C above
    if "mitochondri" in combined_mechanism_text and not is_mtdna_gene and not is_mito_matrix and not has_mito_inheritance:
        flags.append(
            "Mitochondrial biology flagged; confirm whether gene is nuclear-encoded "
            "(feasible for AAV) or mtDNA-encoded (requires allotopic expression)"
        )
    if "dominant" in combined_mechanism_text:
        flags.append(
            "Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition"
        )

    if gene.cds_length_bp is None or not gene.subcellular_location:
        flags.append(
            "Gene annotation incomplete; packaging, protein class, and localization scores need manual confirmation"
        )

    if (vector_serotype or "").upper().startswith("AAV"):
        flags.append(
            "AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone"
        )

    return flags


# ══════════════════════════════════════════════════════════════════════════════
# MAIN SCORING FUNCTION: combines all 14 dimensions for one program
# ══════════════════════════════════════════════════════════════════════════════
def score_program(
    disease: DiseaseInfo,   # ← the query disease
    gene: GeneInfo,         # ← its causal gene
    program: dict,          # ← one GT program from the catalog (e.g. Zolgensma row)
    vector: dict,           # ← the vector used by that program (e.g. AAV9 row)
) -> ScoreBreakdown:

    notes: list[str] = []

    # ── Step 1: Packaging (hard gate) ─────────────────────────────────────
    packaging_gene, strategy_notes = _packaging_gene_for_program(gene, program)
    notes.extend(strategy_notes)
    pkg, pkg_notes = score_packaging(
        packaging_gene,
        program["cds_bp"],
        vector["cargo_limit_bp"],
    )
    notes.extend(pkg_notes)

    if pkg == 0.0:
        # ← Gene doesn't fit → immediate fail, skip all other scoring
        # Organelle targeting still scored on hard-fail so the flag appears in the report
        ot_fail, ot_fail_notes = score_organelle_targeting(gene, disease)
        notes.extend(ot_fail_notes)
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
            modality_compatibility=0.0,
            approval_weight=0.0,
            immunogenicity=0.0,
            therapeutic_window=0.0,
            cross_correction=0.0,
            immune_privilege=0.0,
            promoter_availability=0.0,
            roa_feasibility=0.0,
            organelle_targeting=ot_fail,
            notes=notes,
            review_flags=build_review_flags(
                disease=disease,
                gene=gene,
                vector_tropism=[],
                vector_serotype=program["vector"],
                tropism_score=0.0,
                cross_correction_score=0.0,
                therapeutic_window_score=0.0,
                strategy_notes=strategy_notes,
                organelle_targeting_score=ot_fail,
            ),
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

    # ── Step 6: Modality compatibility ────────────────────────────────────
    # ← uses source-linked disease mechanism evidence instead of assuming
    # ← inheritance always equals loss-of-function gene-addition suitability.
    mechanism = lookup_mechanism(disease.orphanet_id, gene.symbol)
    mod, mod_notes = score_gene_addition_compatibility(mechanism)
    notes.extend(mod_notes)

    if mechanism.gene_addition_compatibility.lower() == "incompatible":
        # ← Mechanism hard gate: gain-of-function, dominant-negative, RNA toxic GOF,
        #   and gene duplication/overexpression diseases are fundamentally incompatible
        #   with gene addition. Adding more gene copies would not help and may worsen
        #   disease. Exclude from ranking entirely, same as the packaging hard-fail.
        notes.append(
            f"Mechanism hard-fail: {mechanism.mechanism_category} — "
            f"{mechanism.mechanism_detail}"
        )
        ot_mfail, ot_mfail_notes = score_organelle_targeting(gene, disease)
        notes.extend(ot_mfail_notes)
        return ScoreBreakdown(
            program_name=program["name"],
            program_disease=program["disease"],
            vector=program["vector"],
            tissue_target=program["tissue_target"],
            approval_status=program["approval_status"],
            composite_score=0.0,
            confidence="fail",
            packaging_fit=pkg,
            tropism_match=0.0,
            protein_class_match=0.0,
            inheritance_match=0.0,
            pathway_similarity=0.0,
            modality_compatibility=0.0,
            approval_weight=0.0,
            immunogenicity=0.0,
            therapeutic_window=0.0,
            cross_correction=0.0,
            immune_privilege=0.0,
            promoter_availability=0.0,
            roa_feasibility=0.0,
            organelle_targeting=ot_mfail,
            notes=notes,
            review_flags=build_review_flags(
                disease=disease,
                gene=gene,
                vector_tropism=[],
                vector_serotype=program["vector"],
                tropism_score=0.0,
                cross_correction_score=0.0,
                therapeutic_window_score=0.0,
                strategy_notes=strategy_notes,
                organelle_targeting_score=ot_mfail,
            ),
        )

    # ── Step 7: Approval ──────────────────────────────────────────────────
    apv, apv_notes = score_approval(program["approval_status"])
    notes.extend(apv_notes)

    # ── Step 8: Immunogenicity ────────────────────────────────────────────
    # ← uses the vector serotype to look up published seroprevalence rates
    imm, imm_notes = score_immunogenicity(program["vector"])
    notes.extend(imm_notes)

    # ── Step 9: Therapeutic window ────────────────────────────────────────
    # ← uses the disease's HPO terms to infer how wide the treatment window is
    # ← same score for all precedent programs (it's a property of the query disease)
    tw, tw_notes = score_therapeutic_window(disease)
    notes.extend(tw_notes)

    # ── Step 10: Cross-correction ─────────────────────────────────────────
    # ← uses the gene's protein localisation to determine cross-correction capacity
    # ← same for all precedent programs (it's a property of the query gene)
    cc, cc_notes = score_cross_correction(gene)
    notes.extend(cc_notes)

    # ── Step 11: Immune privilege ─────────────────────────────────────────
    # ← uses the disease's target tissues to score immunological privilege
    ip, ip_notes = score_immune_privilege(disease.affected_tissues)
    notes.extend(ip_notes)

    # ── Step 12: Promoter availability ────────────────────────────────────
    # ← scores whether validated tissue-specific promoters exist for target tissues
    pa, pa_notes = score_promoter_availability(disease.affected_tissues)
    notes.extend(pa_notes)

    # ── Step 13: Route of administration feasibility ──────────────────────
    # ← scores how accessible the target tissue is via established delivery routes
    roa, roa_notes = score_roa_feasibility(disease.affected_tissues)
    notes.extend(roa_notes)

    # ── Step 14: Organelle targeting feasibility (NEW in v2) ──────────────
    # ← scores whether standard nuclear AAV delivery can produce a functional
    # ← protein at the correct subcellular compartment.
    # ← This is the same for all precedent programs — it is a property of the
    # ← query disease gene, not of the precedent (so it is computed once here,
    # ← not per-program). It will lower composite scores for MT-* genes (0.0),
    # ← mitochondrial matrix enzymes (0.5), and peroxisomal proteins (0.7).
    ot, ot_notes = score_organelle_targeting(gene, disease)
    notes.extend(ot_notes)

    # ── Final composite score ─────────────────────────────────────────────
    # Raw sum across all 14 dimensions (max = 21.0 from v2 onwards).
    # Normalized to out of 10 for consistent interpretation.
    raw_sum = pkg + trp + prc + pth + mod + inh + apv + imm + tw + cc + ip + pa + roa + ot
    composite = round((raw_sum / _RAW_MAX) * 10.0, 2)

    confidence = "high" if composite >= 7.5 else "medium" if composite >= 5.0 else "low"
    review_flags = build_review_flags(
        disease=disease,
        gene=gene,
        vector_tropism=v_tropism,
        vector_serotype=program["vector"],
        tropism_score=trp,
        cross_correction_score=cc,
        therapeutic_window_score=tw,
        strategy_notes=strategy_notes,
        organelle_targeting_score=ot,
    )

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
        modality_compatibility=mod,
        approval_weight=apv,
        immunogenicity=imm,
        therapeutic_window=tw,
        cross_correction=cc,
        immune_privilege=ip,
        promoter_availability=pa,
        roa_feasibility=roa,
        organelle_targeting=ot,
        notes=notes,
        review_flags=review_flags,
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
