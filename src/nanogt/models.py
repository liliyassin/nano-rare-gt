"""Pydantic models for the nano-rare gene therapy matching framework."""

# ── What this file is ──────────────────────────────────────────────────────
# Defines the "data shapes" used everywhere in the project.
# Think of each class as a template / form with labelled fields.
# Pydantic = a library that checks the data is the right type automatically.

from __future__ import annotations

from pydantic import BaseModel, Field  # BaseModel = the template; Field = labels each slot


class Disease(BaseModel):
    """A rare disease entry from Orphanet / OMIM."""
    # ← One disease record. Filled in by disease.py when you query Orphanet.

    orphanet_id: str = Field(..., description="Orphanet ID, e.g. ORPHA:1946")      # ← the unique disease code, e.g. "ORPHA:324" for Fabry
    name: str = Field(..., description="Disease name")                              # ← human-readable name
    omim_id: str | None = Field(None, description="OMIM ID, e.g. 226750")          # ← another disease database ID (optional)
    prevalence: str | None = Field(None, description="Prevalence class")           # ← how rare it is, e.g. "1-5/10000"
    morbidity_flag: bool = Field(False, description="High-morbidity flag")         # ← True if disease causes severe suffering
    inheritance: str | None = Field(None, description="AR, AD, XL, etc.")          # ← how it's inherited: AR=autosomal recessive, XL=X-linked
    active_gt_trials: int = Field(0, description="Count of active gene therapy trials")  # ← number of ongoing GT trials for this disease
    phenotype_terms: list[str] = Field(default_factory=list)                       # ← list of HPO symptom terms, e.g. ["Seizures", "Liver failure"]


class Gene(BaseModel):
    """A gene and its basic properties."""
    # ← One gene record. Filled in by gene.py when you query UniProt.

    symbol: str = Field(..., description="HGNC symbol, e.g. ROGDI")               # ← the gene's short name, e.g. "SMN1", "GLA"
    aliases: list[str] = Field(default_factory=list, description="Alternative symbols")  # ← other names the gene is known by
    omim_id: str | None = Field(None, description="OMIM gene ID")                  # ← OMIM database ID for this gene
    uniprot_id: str | None = Field(None, description="UniProt accession, e.g. Q9GZN7")   # ← UniProt database ID for the protein it makes
    chromosome: str | None = Field(None, description="Cytogenetic location")       # ← where on which chromosome, e.g. "Xq22"
    exon_count: int | None = Field(None)                                           # ← how many exons (coding segments) the gene has
    cds_length_bp: int | None = Field(None, description=" Coding sequence length in bp")  # ← crucial for packaging: how many base pairs need to fit in the vector
    aa_length: int | None = Field(None, description="Protein length in amino acids")      # ← protein size; CDS ÷ 3 = amino acids
    molecular_weight_da: float | None = Field(None)                                # ← protein weight in daltons


class Protein(BaseModel):
    """Protein-level annotations."""
    # ← Detailed protein data from UniProt. Used to determine protein class (secreted/lysosomal/etc.)

    uniprot_id: str = Field(..., description="UniProt accession")                  # ← UniProt ID
    name: str | None = Field(None)                                                 # ← protein full name
    sequence: str | None = Field(None, description="Amino acid sequence")         # ← the actual protein sequence (letters = amino acids)
    domains: list[str] = Field(default_factory=list, description="Pfam / InterPro domains")  # ← functional regions within the protein
    go_terms: list[str] = Field(default_factory=list)                             # ← Gene Ontology terms: what the protein does biologically
    keywords: list[str] = Field(default_factory=list)                             # ← UniProt keyword tags e.g. "Lysosome", "Secreted"
    subcellular_location: list[str] = Field(
        default_factory=list, description="GO cellular components"
    )                                                                              # ← where in the cell the protein lives, e.g. "Lysosome", "Nucleus"
    is_secreted: bool = Field(False)                                               # ← True if protein is released outside the cell (important for cross-correction)
    afdb_id: str | None = Field(None, description="AlphaFold DB identifier")      # ← AlphaFold structure ID (3D protein shape prediction)
    afdb_url: str | None = Field(None, description="AlphaFold structure URL")     # ← link to the 3D structure


class Vector(BaseModel):
    """An AAV vector serotype and its properties."""
    # ← One viral vector. Defines how big a gene it can carry and which tissues it targets.

    serotype: str = Field(..., description="e.g. AAV9, AAV-DJ, AAV8, AAVrh.10")  # ← vector name/type, e.g. "AAV9"
    cargo_limit_bp: int = Field(4700, description="Packaging limit in base pairs")  # ← max gene size it can carry (~4700 bp for most AAVs)
    tissue_tropism: list[str] = Field(default_factory=list)                       # ← which tissues it naturally infects, e.g. ["CNS", "muscle"]
    cns_tropic: bool = Field(False, description="Crosses blood-brain barrier")    # ← True = can reach the brain/spinal cord
    retinal_tropic: bool = Field(False)                                           # ← True = targets the retina
    hepatic_tropic: bool = Field(False)                                           # ← True = targets the liver
    muscle_tropic: bool = Field(False)                                            # ← True = targets muscle tissue
    clinical_precedents: int = Field(0, description="Number of clinical programs")  # ← how many clinical trials have used this vector (more = more trust)
    freely_available: bool = Field(
        True, description="Unencumbered by active patents"
    )                                                                             # ← True = no patent blocking use; False = licencing needed


class ScoreBreakdown(BaseModel):
    """Per-dimension match scores (0.0–1.0)."""
    # ← Stores the score for each of the 12 possible scoring dimensions.
    # Note: scoring.py only uses 6 of these — the others are defined here for future use.

    structural_homology: float = Field(0.0)    # ← 3D protein structure similarity (not yet active)
    sequence_identity: float = Field(0.0)      # ← DNA/protein sequence % match (not yet active)
    domain_similarity: float = Field(0.0)      # ← whether same protein domains are present (not yet active)
    size_compatibility: float = Field(0.0)     # ← gene fits inside the vector (ACTIVE — called "packaging_fit" in scoring.py)
    tissue_tropism: float = Field(0.0)         # ← vector targets the right tissue (ACTIVE)
    roa_precedent: float = Field(0.0)          # ← route of administration match (not yet active)
    promoter_match: float = Field(0.0)         # ← same promoter type used (not yet active)
    localization_match: float = Field(0.0)     # ← protein goes to same cell compartment (not yet active)
    immunogenicity: float = Field(0.0)         # ← immune response risk (not yet active)
    therapeutic_window: float = Field(0.0)     # ← how precise the dosing needs to be (not yet active)
    codon_optimization: float = Field(0.0)     # ← whether gene is optimised for human expression (not yet active)
    platform_depth: float = Field(0.0)         # ← how much clinical experience exists (not yet active)

    @property
    def must_pass_gates(self) -> dict[str, bool]:
        """Hard gates: any False flags an automatic reject."""
        # ← "Gate" = a hard pass/fail check before scoring even starts.
        # If the gene is too big for the vector, score = 0 regardless of anything else.
        return {
            "size_compatibility": self.size_compatibility >= 0.5,  # ← gene must be < 50% of cargo limit to pass
        }


class Match(BaseModel):
    """A single disease-to-surrogate match result."""
    # ← The final output for one disease + one GT program comparison.
    # Combines disease info, gene info, vector info, and the scores.

    disease: Disease                                      # ← the query disease
    gene: Gene                                            # ← the causal gene for that disease
    vector: Vector                                        # ← the AAV vector used in the precedent program
    surrogate_program: str = Field(
        ..., description="Name of precedent program or platform"
    )                                                     # ← name of the precedent GT program, e.g. "Zolgensma"
    scores: ScoreBreakdown = Field(default_factory=ScoreBreakdown)  # ← all dimension scores for this match
    composite_score: float = Field(0.0)                  # ← final total score out of 10
    confidence: str = Field("low", description="low / medium / high")  # ← ≥7.5 = high, ≥5.0 = medium, <5.0 = low
    notes: list[str] = Field(default_factory=list)        # ← human-readable explanation of why each score was given
    protocol_sections: dict[str, str] = Field(
        default_factory=dict,
        description="Auto-generated GT protocol parts",
    )                                                     # ← text blocks that go into the generated GT protocol report


class Report(BaseModel):
    """Top-level output for a matching run."""
    # ← The full output object for one disease query: contains all matches, the top match, timing, warnings.

    query_disease: Disease                               # ← the disease that was queried
    matches: list[Match] = Field(default_factory=list)  # ← all GT programs ranked by score
    top_match: Match | None = Field(None)               # ← the single best matching program
    generated_at: str | None = Field(None)              # ← timestamp of when the report was generated
    query_time_s: float = Field(0.0)                    # ← how many seconds the whole run took
    warnings: list[str] = Field(default_factory=list)  # ← any issues encountered, e.g. "API not reachable, used fallback"
