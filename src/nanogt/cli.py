# cli.py — Nano-rare GT Framework CLI
"""Typer CLI entry point."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from nanogt.db import DB

app = typer.Typer(help="Nano-rare Gene Therapy Matching Framework")
console = Console()

DEFAULT_DB = Path.home() / ".nanogt" / "nanogt.db"


@app.command()
def init(
    db_path: Annotated[Path, typer.Option("--db", help="Database path")] = DEFAULT_DB,
) -> None:
    """Initialize the local database."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    db = DB(db_path)
    db.seed_vectors()
    console.print(f"[green]Initialized {db_path}[/green]")


@app.command()
def match(
    disease: Annotated[str, typer.Option("--disease", help="Orphanet ID e.g. ORPHA:916")],
    output: Annotated[Path, typer.Option("--output", "-o", help="Output markdown path")] = Path("report.md"),
    db_path: Annotated[Path, typer.Option("--db", help="Database path")] = DEFAULT_DB,
) -> None:
    """Run the matching pipeline for a single disease."""
    if not db_path.exists():
        console.print(f"[red]Database not found at {db_path}. Run `nanogt init` first.[/red]")
        raise typer.Exit(1)

    db = DB(db_path)
    disease_row = db.get_disease_by_orphanet(disease)
    if disease_row is None:
        console.print(f"[yellow]Disease {disease} not in local DB. Querying APIs... (not yet implemented)[/yellow]")

    # ROGDI quick-facts placeholder for v0.1 PoC
    table = Table(title=f"Match Report for {disease}")
    table.add_column("Dimension", style="cyan")
    table.add_column("Value", style="magenta")
    table.add_row("Gene", "ROGDI (GMPR2)")
    table.add_row("UniProt", "Q9P2T1")
    table.add_row("AA length", "348")
    table.add_row("CDS (bp)", "~1044")
    table.add_row("AAV fit", "YES (well under 4.7 kb)")
    table.add_row("CNS target", "Hippocampal neurons (presynaptic)")
    table.add_row("Dental target", "Ameloblasts")
    table.add_row("Status", "[yellow]Full pipeline v0.1 WIP[/yellow]")
    console.print(table)
    console.print(f"\n[dim]Full report will be written to {output} in v0.1[/dim]")


@app.command()
def status(
    db_path: Annotated[Path, typer.Option("--db", help="Database path")] = DEFAULT_DB,
) -> None:
    """Check database health."""
    if not db_path.exists():
        console.print(f"[red]Database not found: {db_path}[/red]")
        raise typer.Exit(1)
    db = DB(db_path)
    console.print(f"[green]Database OK[/green]: {db_path}")


if __name__ == "__main__":
    app()
