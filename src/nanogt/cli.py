"""nanogt CLI — gene therapy precedent matching for rare diseases."""
from __future__ import annotations
import pathlib
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table
from rich import print as rprint

from .db import setup, get_db_path
from .disease import fetch_disease
from .gene import fetch_gene, GeneInfo
from .scoring import rank_programs
from .report import MatchResult, generate_report, save_report

app = typer.Typer(
    name="nanogt",
    help="Gene therapy precedent matching for rare diseases.",
    add_completion=False,
)
console = Console()


def _require_db():
    """Return a ready DB connection (init + seed if needed)."""
    return setup()


@app.command()
def init(
    db_path: Optional[pathlib.Path] = typer.Option(None, help="Path to SQLite DB"),
):
    """Initialise the database and seed vector/program catalog."""
    conn = setup(db_path)
    n_programs = conn.execute("SELECT COUNT(*) FROM gt_programs").fetchone()[0]
    n_vectors = conn.execute("SELECT COUNT(*) FROM vectors").fetchone()[0]
    console.print(f"[green]Database ready at [bold]{get_db_path()}[/bold][/green]")
    console.print(f"  {n_vectors} vectors, {n_programs} GT programs loaded.")


@app.command()
def match(
    disease: str = typer.Argument(..., help="Orphanet ID, e.g. ORPHA:324"),
    top: int = typer.Option(5, help="Number of top matches to show"),
    output: Optional[pathlib.Path] = typer.Option(None, "-o", help="Save report to directory"),
    gene_symbol: Optional[str] = typer.Option(None, "--gene", help="Override gene symbol"),
):
    """Match a disease to the best gene therapy precedents."""
    conn = _require_db()

    with console.status(f"[bold]Looking up {disease}...[/bold]"):
        disease_info = fetch_disease(disease)

    if disease_info is None:
        console.print(f"[red]Disease not found: {disease}[/red]")
        raise typer.Exit(1)

    console.print(f"\n[bold]{disease_info.name}[/bold] ({disease_info.orphanet_id})")
    console.print(f"  Genes: {', '.join(disease_info.gene_symbols) or 'none found'}")
    console.print(f"  Tissues: {', '.join(disease_info.affected_tissues) or 'unknown'}")
    console.print(f"  Inheritance: {', '.join(disease_info.inheritance) or 'unknown'}\n")

    # Pick gene to score on
    target_gene_sym = gene_symbol or (disease_info.gene_symbols[0] if disease_info.gene_symbols else None)
    if not target_gene_sym:
        console.print("[yellow]No gene found — using generic scoring[/yellow]")
        gene_info = GeneInfo(
            symbol="unknown", uniprot_id=None, protein_name=None,
            cds_length_bp=None, aa_length=None, is_secreted=False,
            subcellular_location=[], go_terms=[], keywords=[], domains=[],
        )
    else:
        with console.status(f"Fetching gene info for {target_gene_sym}..."):
            gene_info = fetch_gene(target_gene_sym)

    with console.status("Scoring GT programs..."):
        scores = rank_programs(disease_info, gene_info, conn)

    # Print table
    table = Table(title=f"Top GT Precedents for {disease_info.name}", show_lines=True)
    table.add_column("Rank", style="dim", width=5)
    table.add_column("Program", style="bold")
    table.add_column("Vector", width=10)
    table.add_column("Score", justify="right")
    table.add_column("Confidence")
    table.add_column("Status")

    emoji = {"high": "🟢", "medium": "🟡", "low": "🔴", "fail": "⛔"}
    shown = [s for s in scores if s.confidence != "fail"][:top]
    for i, s in enumerate(shown, 1):
        table.add_row(
            str(i),
            s.program_name,
            s.vector,
            f"{s.composite_score:.1f}/10",
            f"{emoji.get(s.confidence, '')} {s.confidence}",
            s.approval_status,
        )

    console.print(table)

    result = MatchResult(disease=disease_info, gene=gene_info, scores=scores, top_n=top)

    if output:
        path = save_report(result, output)
        console.print(f"\n[green]Report saved to {path}[/green]")
    else:
        # Auto-save to ./output/
        path = save_report(result, pathlib.Path("output"))
        console.print(f"\n[green]Report saved to {path}[/green]")


@app.command()
def batch(
    diseases: list[str] = typer.Argument(..., help="Space-separated Orphanet IDs"),
    output: pathlib.Path = typer.Option(pathlib.Path("output"), "-o", help="Output directory"),
    top: int = typer.Option(3, help="Top N matches per disease"),
):
    """Run match for multiple diseases and generate a summary report."""
    conn = _require_db()
    results: list[MatchResult] = []

    for disease_id in diseases:
        console.print(f"\n[bold]Processing {disease_id}...[/bold]")
        disease_info = fetch_disease(disease_id)
        if disease_info is None:
            console.print("  [yellow]Skipping — not found[/yellow]")
            continue
        gene_sym = disease_info.gene_symbols[0] if disease_info.gene_symbols else None
        if gene_sym:
            gene_info = fetch_gene(gene_sym)
        else:
            gene_info = GeneInfo(
                "unknown", None, None, None, None, False, [], [], [], [],
            )

        scores = rank_programs(disease_info, gene_info, conn)
        r = MatchResult(disease=disease_info, gene=gene_info, scores=scores, top_n=top)
        results.append(r)
        path = save_report(r, output)
        console.print(f"  [green]{disease_info.name} -> {path.name}[/green]")

    # Generate summary
    _write_summary(results, output, top)
    console.print(f"\n[bold green]Batch complete.[/bold green] Reports in {output}/")


def _write_summary(
    results: list[MatchResult],
    output_dir: pathlib.Path,
    top: int,
) -> None:
    lines = [
        "# NanoGT Batch Summary",
        "",
        f"Ran on {len(results)} diseases.",
        "",
        "| Disease | Orphanet ID | Gene | Top Match | Score | Confidence |",
        "|---------|------------|------|-----------|-------|-----------|",
    ]
    for r in results:
        top_match = next((s for s in r.scores if s.confidence != "fail"), None)
        if top_match:
            lines.append(
                f"| {r.disease.name} | {r.disease.orphanet_id} | {r.gene.symbol} "
                f"| {top_match.program_name} | {top_match.composite_score:.1f}/10 "
                f"| {top_match.confidence} |"
            )
    lines += ["", "---", ""]
    for r in results:
        lines.append(f"## {r.disease.name}")
        top_matches = [s for s in r.scores if s.confidence != "fail"][:top]
        for i, s in enumerate(top_matches, 1):
            lines.append(
                f"{i}. **{s.program_name}** ({s.vector}) — {s.composite_score:.1f}/10 [{s.confidence}]"
            )
        lines.append("")

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "SUMMARY.md").write_text("\n".join(lines))


if __name__ == "__main__":
    app()
