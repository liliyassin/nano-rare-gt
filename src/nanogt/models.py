"""Pydantic models for the nano-rare gene therapy matching framework."""

from __future__ import annotations


from pydantic import BaseModel, Field


class Disease(BaseModel):
    """A rare disease entry from Orphanet / OMIM."""

    orphanet_id: str = Field(..., description="Orphanet ID, e.g. ORPHA:1946")
    name: str = Field(..., description="Disease name")
    omim_id: str | None = Field(None, description="OMIM ID, e.g. 226750")
    prevalence: str | None = Field(None, description="Prevalence class")
    morbidity_flag: bool = Field(False, description="High-morbidity flag")
    inheritance: str | None = Field(None, description="AR, AD, XL, etc.")
    active_gt_trials: int = Field(0, description="Count of active gene therapy trials")
    phenotype_terms: list[str] = Field(default_factory=list)


class Gene(BaseModel):
    """A gene and its basic properties."""

    symbol: str = Field(..., description="HGNC symbol, e.g. ROGDI")
    aliases: list[str] = Field(default_factory=list, description="Alternative symbols")
    omim_id: str | None = Field(None, description="OMIM gene ID")
    uniprot_id: str | None = Field(None, description="UniProt accession, e.g. Q9GZN7")
    chromosome: str | None = Field(None, description="Cytogenetic location")
    exon_count: int | None = Field(None)
    cds_length_bp: int | None = Field(None, description=" Coding sequence length in bp")
    aa_length: int | None = Field(None, description="Protein length in amino acids")
    molecular_weight_da: float | None = Field(None)


class Protein(BaseModel):
    """Protein-level annotations."""

    uniprot_id: str = Field(..., description="UniProt accession")
    name: str | None = Field(None)
    sequence: str | None = Field(None, description="Amino acid sequence")
    domains: list[str] = Field(default_factory=list, description="Pfam / InterPro domains")
    go_terms: list[str] = Field(default_factory=list)
    keywords: list[str] = Field(default_factory=list)
    subcellular_location: list[str] = Field(
        default_factory=list, description="GO cellular components"
    )
    is_secreted: bool = Field(False)
    afdb_id: str | None = Field(None, description="AlphaFold DB identifier")
    afdb_url: str | None = Field(None, description="AlphaFold structure URL")


class Vector(BaseModel):
    """An AAV vector serotype and its properties."""

    serotype: str = Field(..., description="e.g. AAV9, AAV-DJ, AAV8, AAVrh.10")
    cargo_limit_bp: int = Field(4700, description="Packaging limit in base pairs")
    tissue_tropism: list[str] = Field(default_factory=list)
    cns_tropic: bool = Field(False, description="Crosses blood-brain barrier")
    retinal_tropic: bool = Field(False)
    hepatic_tropic: bool = Field(False)
    muscle_tropic: bool = Field(False)
    clinical_precedents: int = Field(0, description="Number of clinical programs")
    freely_available: bool = Field(
        True, description="Unencumbered by active patents"
    )


class ScoreBreakdown(BaseModel):
    """Per-dimension match scores (0.0–1.0)."""

    structural_homology: float = Field(0.0)
    sequence_identity: float = Field(0.0)
    domain_similarity: float = Field(0.0)
    size_compatibility: float = Field(0.0)
    tissue_tropism: float = Field(0.0)
    roa_precedent: float = Field(0.0)
    promoter_match: float = Field(0.0)
    localization_match: float = Field(0.0)
    immunogenicity: float = Field(0.0)
    therapeutic_window: float = Field(0.0)
    codon_optimization: float = Field(0.0)
    platform_depth: float = Field(0.0)

    @property
    def must_pass_gates(self) -> dict[str, bool]:
        """Hard gates: any False flags an automatic reject."""
        return {
            "size_compatibility": self.size_compatibility >= 0.5,
        }


class Match(BaseModel):
    """A single disease-to-surrogate match result."""

    disease: Disease
    gene: Gene
    vector: Vector
    surrogate_program: str = Field(
        ..., description="Name of precedent program or platform"
    )
    scores: ScoreBreakdown = Field(default_factory=ScoreBreakdown)
    composite_score: float = Field(0.0)
    confidence: str = Field("low", description="low / medium / high")
    notes: list[str] = Field(default_factory=list)
    protocol_sections: dict[str, str] = Field(
        default_factory=dict,
        description="Auto-generated GT protocol parts",
    )


class Report(BaseModel):
    """Top-level output for a matching run."""

    query_disease: Disease
    matches: list[Match] = Field(default_factory=list)
    top_match: Match | None = Field(None)
    generated_at: str | None = Field(None)
    query_time_s: float = Field(0.0)
    warnings: list[str] = Field(default_factory=list)
