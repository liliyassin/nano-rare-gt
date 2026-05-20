# cli.py — Nano-rare GT Framework CLI
"""Typer CLI entry point."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from nanogt.db import DB
from nanogt.models import Disease, Gene, Protein, ScoreBreakdown, Vector
from nanogt.report import ReportRenderer

app = typer.Typer(help="Nano-Rare Gene Therapy Matching Framework")
console = Console()

DEFAULT_DB = Path.home() / ".nanogt" / "nanogt.db"


def _ensure_db(db_path: Path) -> DB:
    if not db_path.exists():
        db_path.parent.mkdir(parents=True, exist_ok=True)
        db = DB(db_path)
        db.seed_vectors()
        console.print(f"[dim]Initialized {db_path}[/dim]")
    return DB(db_path)


def _load_rogdi_data() -> tuple[Disease, Gene, Protein, Vector, ScoreBreakdown]:
    """Load the source-audited ROGDI/KTS deep-dive dataset."""
    disease = Disease(
        orphanet_id="ORPHA:1946",
        name="Kohlsch\u00fctter-T\u00f6nz syndrome / amelocerebrohypohidrotic syndrome",
        omim_id="226750",
        prevalence="<1 / 1,000,000",
        morbidity_flag=True,
        inheritance="autosomal recessive",
        active_gt_trials=0,
        phenotype_terms=[
            "amelogenesis imperfecta",
            "early-onset epilepsy",
            "severe developmental delay / intellectual disability / regression",
            "spasticity",
            "hypohidrosis",
            "nephrocalcinosis reported in some cases",
        ],
    )
    gene = Gene(
        symbol="ROGDI",
        aliases=["KIAA0267", "FLJ22386", "RAV2"],
        omim_id="614574",
        uniprot_id="Q9GZN7",
        chromosome="16p12.1",
        exon_count=11,
        cds_length_bp=861,
        aa_length=287,
        molecular_weight_da=32254.0,
    )
    protein = Protein(
        uniprot_id="Q9GZN7",
        name="Protein rogdi homolog",
        domains=["RAVE2/Rogdi", "Rogdi_lz", "atypical leucine zipper-like scaffold"],
        go_terms=[
            "nuclear envelope",
            "presynapse",
            "axon",
            "perikaryon",
            "dendrite",
            "synaptic vesicle",
            "Rabconnectin-3 complex interaction",
            "V-ATPase assembly/regulation",
        ],
        keywords=[
            "3D-structure",
            "Amelogenesis imperfecta",
            "Cytoplasmic vesicle",
            "Epilepsy",
            "Nucleus",
            "Reference proteome",
            "Synapse",
            "Rabconnectin-3",
            "V-ATPase",
        ],
        subcellular_location=[
            "nuclear envelope",
            "presynapse",
            "axon",
            "perikaryon",
            "dendrite",
            "synaptic vesicle",
            "lysosomal fraction / acidic perinuclear lysosome context",
        ],
        is_secreted=False,
        afdb_id="Q9GZN7",
        afdb_url="https://alphafold.ebi.ac.uk/entry/Q9GZN7",
    )
    vector = Vector(
        serotype="AAV9",
        cargo_limit_bp=4700,
        tissue_tropism=["CNS", "heart", "liver", "muscle", "retina"],
        cns_tropic=True,
        retinal_tropic=True,
        hepatic_tropic=True,
        muscle_tropic=True,
        clinical_precedents=25,
        freely_available=True,
    )
    # First-pass scores for corrected ROGDI biology (v0.2 source-audited)
    scores = ScoreBreakdown(
        structural_homology=0.50,
        sequence_identity=0.35,
        domain_similarity=0.55,
        size_compatibility=0.98,
        tissue_tropism=0.45,
        roa_precedent=0.80,
        promoter_match=0.70,
        localization_match=0.45,
        immunogenicity=0.60,
        therapeutic_window=0.55,
        codon_optimization=0.85,
        platform_depth=0.70,
    )
    return disease, gene, protein, vector, scores


@app.command()
def init(
    db_path: Annotated[Path, typer.Option("--db", help="Database path")] = DEFAULT_DB,
) -> None:
    """Initialize the local database."""
    _ensure_db(db_path)
    console.print(f"[green]Database ready at {db_path}[/green]")


@app.command()
def match(
    disease: Annotated[str, typer.Option("--disease", help="Orphanet ID e.g. ORPHA:1946")],
    output: Annotated[Path, typer.Option("--output", "-o", help="Output markdown path")] = Path("report.md"),
    db_path: Annotated[Path, typer.Option("--db", help="Database path")] = DEFAULT_DB,
    deep_dive: Annotated[bool, typer.Option("--deep-dive", help="Generate full protocol with analysis")] = False,
) -> None:
    """Run the matching pipeline for a single disease."""
    db = _ensure_db(db_path)

    # v0.2: Hardcoded source-audited ROGDI path for the primary case study
    if disease == "ORPHA:1946":
        disease_obj, gene, protein, vector, scores = _load_rogdi_data()
    else:
        row = db.get_disease_by_orphanet(disease)
        if row is None:
            console.print(f"[red]Disease {disease} not yet supported in v0.2. Only ORPHA:1946 (ROGDI/KTS) is available for deep-dive.[/red]")
            raise typer.Exit(1)
        # Placeholder for future diseases
        disease_obj = Disease.model_validate(row)
        gene = Gene(symbol="UNKNOWN", aliases=[])
        protein = Protein(uniprot_id="UNKNOWN")
        vector = Vector(serotype="UNKNOWN")
        scores = ScoreBreakdown()

    renderer = ReportRenderer()
    if deep_dive:
        renderer.render_protocol(disease_obj, gene, protein, vector, scores, output)
        console.print(f"[green]✓ Standardised Gene Therapy Protocol generated:[/green] {output}")
    else:
        # Quick summary table
        table = Table(title=f"Match Summary for {disease_obj.name}")
        table.add_column("Dimension", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_row("Gene", gene.symbol)
        table.add_row("CDS", f"{gene.cds_length_bp} bp")
        table.add_row("AAV Fit", f"{(gene.cds_length_bp or 0) <= vector.cargo_limit_bp}")
        table.add_row("Vector", vector.serotype)
        table.add_row("Status", "[yellow]Use --deep-dive for full protocol[/yellow]")
        console.print(table)
        console.print("\n[dim]Run with --deep-dive to generate the full protocol.[/dim]")


@app.command()
def status(
    db_path: Annotated[Path, typer.Option("--db", help="Database path")] = DEFAULT_DB,
) -> None:
    """Check database health."""
    if not db_path.exists():
        console.print(f"[red]Database not found: {db_path}[/red]")
        raise typer.Exit(1)
    _db = DB(db_path)
    console.print(f"[green]Database OK[/green]: {db_path}")


if __name__ == "__main__":
    app()
