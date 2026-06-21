"""nanogt CLI — gene therapy precedent matching for rare diseases."""

# This is the command-line interface.
# When you type `nanogt match ORPHA:324` in the terminal, this file runs.
#
# Three commands available:
#   nanogt init                        → set up the database
#   nanogt match ORPHA:xxx             → score one disease
#   nanogt batch ORPHA:xxx ORPHA:yyy   → score multiple diseases at once

from __future__ import annotations
from dataclasses import replace
import pathlib
from typing import Optional

import typer  # Typer = library that turns Python functions into terminal commands
from rich.console import Console  # Rich = library for pretty coloured terminal output
from rich.table import Table  # makes formatted tables in the terminal
from rich import print as rprint  # coloured print (replaces normal print)

from .db import setup, get_db_path  # database setup functions
from .disease import fetch_disease  # fetches disease info from Orphanet
from .gene import fetch_gene, GeneInfo  # fetches gene info from UniProt
from .mechanism import lookup_mechanism
from .scoring import rank_programs  # THE ALGORITHM (scoring.py)
from .report import (
    MatchResult,
    generate_report,
    save_report,
)  # turns scores into markdown reports

app = typer.Typer(
    name="nanogt",
    help="Gene therapy precedent matching for rare diseases.",
    add_completion=False,
)
console = Console()  # the Rich console object used for all terminal output


def _require_db():
    """Return a ready DB connection (init + seed if needed)."""
    # every command calls this first to make sure the database exists and is populated
    return setup()


# PROBLEM --> _require_db() always calls setup() with no custom path. If a user wants match or batch to use a custom database path, this function currently does not expose that option. To fix this, we could modify _require_db to accept an optional db_path argument, and then pass that through to setup(). Then the match and batch commands would also need to accept a --db-path option and pass it to _require_db. This way, users can specify a custom database path for all commands, not just init.
# ══════════════════════════════════════════════════════════════════════════════
# COMMAND 1: nanogt init
# ══════════════════════════════════════════════════════════════════════════════
@app.command()  # @app.command() = "register this function as a terminal command"
def init(
    db_path: Optional[pathlib.Path] = typer.Option(None, help="Path to SQLite DB"),
    # optional flag: --db-path /custom/location.db (otherwise uses default ~/.nanogt/nanogt.db)
):
    """Initialise the database and seed vector/program catalog."""
    # creates the SQLite database and loads VECTORS + GT_PROGRAMS from catalog.py
    conn = setup(db_path)
    n_programs = conn.execute("SELECT COUNT(*) FROM gt_programs").fetchone()[0]
    n_vectors = conn.execute("SELECT COUNT(*) FROM vectors").fetchone()[0]
    console.print(f"[green]Database ready at [bold]{get_db_path()}[/bold][/green]")
    console.print(f"  {n_vectors} vectors, {n_programs} GT programs loaded.")


# ══════════════════════════════════════════════════════════════════════════════
# COMMAND 2: nanogt match ORPHA:xxx
# ══════════════════════════════════════════════════════════════════════════════
@app.command()
def match(
    disease: str = typer.Argument(..., help="Orphanet ID, e.g. ORPHA:324"),
    # required positional argument: the Orphanet ID to query
    top: int = typer.Option(5, help="Number of top matches to show"),
    # optional: --top 3 to show only top 3 (default = 5)
    output: Optional[pathlib.Path] = typer.Option(
        None, "-o", help="Save report to directory"
    ),
    # optional: -o /path/to/dir to save the report somewhere specific
    gene_symbol: Optional[str] = typer.Option(
        None, "--gene", help="Override gene symbol"
    ),
    # optional: --gene SMN1 to override which gene is used (normally auto-detected)
    all_genes: bool = typer.Option(
        False, "--all-genes", help="Score every listed causal gene as a separate molecular subtype"
    ),
    # optional: --all-genes runs subtype-level scoring for diseases with multiple causal genes
    primary_tissue: Optional[str] = typer.Option(
        None, "--primary-tissue", help="Score around one declared primary target tissue"
    ),
    # optional: --primary-tissue CNS narrows multi-system tissue scoring to one clinical objective
):
    """Match a disease to the best gene therapy precedents."""
    conn = _require_db()

    # ── Step 1: Look up the disease ───────────────────────────────────────
    with console.status(f"[bold]Looking up {disease}...[/bold]"):
        # shows a loading spinner while fetching
        disease_info = fetch_disease(
            disease
        )  # calls Orphanet API (or uses fallback data)

    if disease_info is None:
        console.print(f"[red]Disease not found: {disease}[/red]")
        raise typer.Exit(1)  # exits with error code 1

    # print disease summary to terminal
    console.print(f"\n[bold]{disease_info.name}[/bold] ({disease_info.orphanet_id})")
    console.print(f"  Genes: {', '.join(disease_info.gene_symbols) or 'none found'}")
    console.print(f"  Tissues: {', '.join(disease_info.affected_tissues) or 'unknown'}")
    console.print(
        f"  Inheritance: {', '.join(disease_info.inheritance) or 'unknown'}\n"
    )

    source_tissues = list(disease_info.affected_tissues)
    scoring_disease = disease_info
    if primary_tissue:
        scoring_disease = replace(disease_info, affected_tissues=[primary_tissue])
        console.print(
            "[yellow]Primary tissue override — scoring "
            f"{primary_tissue} as the therapeutic objective; original tissues: "
            f"{', '.join(source_tissues) or 'unknown'}[/yellow]"
        )

    if all_genes and gene_symbol:
        console.print("[red]Use either --all-genes or --gene, not both.[/red]")
        raise typer.Exit(1)

    if all_genes:
        if not disease_info.gene_symbols:
            console.print("[red]No genes found for subtype scoring.[/red]")
            raise typer.Exit(1)

        subtype_table = Table(
            title=f"Subtype GT Precedents for {disease_info.name}",
            show_lines=True,
        )
        subtype_table.add_column("Gene", style="bold")
        subtype_table.add_column("Top Program")
        subtype_table.add_column("Vector", width=10)
        subtype_table.add_column("Score", justify="right")
        subtype_table.add_column("Confidence")
        subtype_table.add_column("Flags", justify="right")

        output_dir = output or pathlib.Path("output")
        for subtype_gene in disease_info.gene_symbols:
            with console.status(f"Scoring subtype {subtype_gene}..."):
                gene_info = fetch_gene(subtype_gene)
                scores = rank_programs(scoring_disease, gene_info, conn)
            top_match = next((s for s in scores if s.confidence != "fail"), None)
            if top_match:
                subtype_table.add_row(
                    subtype_gene,
                    top_match.program_name,
                    top_match.vector,
                    f"{top_match.composite_score:.1f}/10",
                    f"{top_match.confidence}",
                    str(len(top_match.review_flags)),
                )
            else:
                subtype_table.add_row(subtype_gene, "none", "-", "0.0/10", "fail", "-")

            result = MatchResult(
                disease=scoring_disease,
                gene=gene_info,
                scores=scores,
                top_n=top,
                primary_tissue=primary_tissue,
                source_tissues=source_tissues,
            )
            save_report(result, output_dir)

        console.print(subtype_table)
        console.print(f"\n[green]Subtype reports saved to {output_dir}[/green]")
        return

    # ── Step 2: Get gene info ─────────────────────────────────────────────
    target_gene_sym = gene_symbol or (
        disease_info.gene_symbols[0] if disease_info.gene_symbols else None
    )
    # use --gene override if given, otherwise take the first gene from the disease record

    if not gene_symbol and len(disease_info.gene_symbols) > 1:
        console.print(
            "[yellow]Multiple genes listed — using "
            f"{target_gene_sym} by default. Re-run with --gene to score each molecular subtype.[/yellow]"
        )

    if not target_gene_sym:
        console.print("[yellow]No gene found — using generic scoring[/yellow]")
        gene_info = GeneInfo(
            symbol="unknown",
            uniprot_id=None,
            protein_name=None,
            cds_length_bp=None,
            aa_length=None,
            is_secreted=False,
            subcellular_location=[],
            go_terms=[],
            keywords=[],
            domains=[],
        )
        # creates an empty gene record so scoring still runs (with neutral scores)
    else:
        with console.status(f"Fetching gene info for {target_gene_sym}..."):
            gene_info = fetch_gene(
                target_gene_sym
            )  # calls UniProt API (or uses fallback)

    mechanism = lookup_mechanism(disease_info.orphanet_id, gene_info.symbol)
    console.print(
        "  Mechanism: "
        f"{mechanism.short_label} "
        f"({mechanism.evidence_status}; {mechanism.evidence_citation})"
    )

    # ── Step 3: Run the scoring algorithm ────────────────────────────────
    with console.status("Scoring GT programs..."):
        scores = rank_programs(scoring_disease, gene_info, conn)
        # calls scoring.py → returns all 18 programs ranked by composite score

    # ── Step 4: Display results table in terminal ─────────────────────────
    table = Table(title=f"Top GT Precedents for {disease_info.name}", show_lines=True)
    table.add_column("Rank", style="dim", width=5)
    table.add_column("Program", style="bold")
    table.add_column("Vector", width=10)
    table.add_column("Score", justify="right")
    table.add_column("Confidence")
    table.add_column("Status")

    emoji = {"high": "🟢", "medium": "🟡", "low": "🔴", "fail": "⛔"}
    shown = [s for s in scores if s.confidence != "fail"][:top]
    # filter out hard fails, take only the top N

    for i, s in enumerate(shown, 1):  # enumerate adds row number, starting from 1
        table.add_row(
            str(i),
            s.program_name,
            s.vector,
            f"{s.composite_score:.1f}/10",  # format score to 1 decimal place
            f"{emoji.get(s.confidence, '')} {s.confidence}",
            s.approval_status,
        )

    console.print(table)

    # ── Step 5: Save the markdown report ─────────────────────────────────
    result = MatchResult(
        disease=scoring_disease,
        gene=gene_info,
        scores=scores,
        top_n=top,
        primary_tissue=primary_tissue,
        source_tissues=source_tissues,
    )

    if output:
        path = save_report(result, output)
    else:
        path = save_report(
            result, pathlib.Path("output")
        )  # default: saves to ./output/ folder
    console.print(f"\n[green]Report saved to {path}[/green]")


# ══════════════════════════════════════════════════════════════════════════════
# COMMAND 3: nanogt batch ORPHA:70 ORPHA:306 ORPHA:324 ...
# ══════════════════════════════════════════════════════════════════════════════
@app.command()
def batch(
    diseases: list[str] = typer.Argument(..., help="Space-separated Orphanet IDs"),
    # accepts multiple Orphanet IDs in one go
    output: pathlib.Path = typer.Option(
        pathlib.Path("output"), "-o", help="Output directory"
    ),
    top: int = typer.Option(3, help="Top N matches per disease"),
):
    """Run match for multiple diseases and generate a summary report."""
    # same as running `nanogt match` for each disease one at a time,
    #   but also writes a combined SUMMARY.md at the end
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
                "unknown",
                None,
                None,
                None,
                None,
                False,
                [],
                [],
                [],
                [],
            )

        scores = rank_programs(disease_info, gene_info, conn)
        r = MatchResult(disease=disease_info, gene=gene_info, scores=scores, top_n=top)
        results.append(r)
        path = save_report(r, output)
        console.print(f"  [green]{disease_info.name} -> {path.name}[/green]")

    _write_summary(results, output, top)  # generates the SUMMARY.md overview table
    console.print(f"\n[bold green]Batch complete.[/bold green] Reports in {output}/")


def _write_summary(
    results: list[MatchResult],
    output_dir: pathlib.Path,
    top: int,
) -> None:
    # generates SUMMARY.md: an overview table + per-disease top-match lists
    lines = [
        "# NanoGT Batch Summary",
        "",
        f"Ran on {len(results)} diseases.",
        "",
        "| Disease | Orphanet ID | Gene | Mechanism | Gene-addition fit | Top Match | Score | Confidence |",
        "|---------|------------|------|-----------|-------------------|-----------|-------|-----------|",
    ]
    for r in results:
        top_match = next((s for s in r.scores if s.confidence != "fail"), None)
        # next(...) = get first non-fail result (i.e. the top match)
        if top_match:
            mechanism = lookup_mechanism(r.disease.orphanet_id, r.gene.symbol)
            lines.append(
                f"| {r.disease.name} | {r.disease.orphanet_id} | {r.gene.symbol} "
                f"| {mechanism.mechanism_category} | {mechanism.gene_addition_compatibility} "
                f"| {top_match.program_name} | {top_match.composite_score:.1f}/10 "
                f"| {top_match.confidence} |"
            )
    lines += ["", "---", ""]

    for r in results:
        lines.append(f"## {r.disease.name}")
        mechanism = lookup_mechanism(r.disease.orphanet_id, r.gene.symbol)
        lines.append(
            f"Mechanism: {mechanism.short_label}. Evidence: "
            f"{mechanism.evidence_citation}"
            + (f" ({mechanism.evidence_url})" if mechanism.evidence_url else "")
        )
        top_matches = [s for s in r.scores if s.confidence != "fail"][:top]
        for i, s in enumerate(top_matches, 1):
            lines.append(
                f"{i}. **{s.program_name}** ({s.vector}) — {s.composite_score:.1f}/10 [{s.confidence}]"
            )
        lines.append("")

    output_dir.mkdir(
        parents=True, exist_ok=True
    )  # create output folder if it doesn't exist
    (output_dir / "SUMMARY.md").write_text(
        "\n".join(lines)
    )  # write all lines to SUMMARY.md


if __name__ == "__main__":
    app()  # entry point: runs the CLI when this file is executed directly
