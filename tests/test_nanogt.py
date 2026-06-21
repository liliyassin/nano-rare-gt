"""Tests for the current NanoGT v0.1 proof-of-concept flow."""

from __future__ import annotations

import json
import sqlite3
from dataclasses import replace
from pathlib import Path

import pytest
from typer.testing import CliRunner

import nanogt.disease as disease_module
import nanogt.gene as gene_module
from nanogt.catalog import GT_PROGRAMS, VECTORS
from nanogt.cli import app
from nanogt.db import setup
from nanogt.disease import DiseaseInfo, fetch_disease
from nanogt.gene import fetch_gene
from nanogt.mechanism import lookup_mechanism, score_gene_addition_compatibility
from nanogt.models import Disease, Gene, ScoreBreakdown as ModelScoreBreakdown
from nanogt.report import MatchResult, generate_report, save_report
from nanogt.scoring import rank_programs, score_packaging

DATA_DIR = Path(__file__).parent.parent / "data"


@pytest.fixture(autouse=True)
def offline_sources(monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep tests deterministic and independent of external APIs."""
    disease_module._CACHE.clear()
    gene_module._CACHE.clear()
    monkeypatch.setattr(
        disease_module,
        "_fetch_from_orphanet",
        lambda orpha_num: disease_module._fallback_disease(orpha_num),
    )
    monkeypatch.setattr(
        gene_module,
        "_search_uniprot",
        lambda gene_symbol, organism="human": None,
    )


class TestModels:
    """Validate the stable Pydantic models used by docs and fixtures."""

    def test_disease_model(self) -> None:
        disease = Disease(
            orphanet_id="ORPHA:1946",
            name="Kohlschutter-Tonz syndrome",
            omim_id="226750",
            inheritance="AR",
        )
        assert disease.orphanet_id == "ORPHA:1946"
        assert disease.inheritance == "AR"

    def test_gene_model_tracks_rogdi_identity(self) -> None:
        gene = Gene(
            symbol="ROGDI",
            aliases=["KIAA0267", "FLJ22386", "RAV2"],
            omim_id="614574",
            uniprot_id="Q9GZN7",
            cds_length_bp=861,
            aa_length=287,
        )
        assert gene.symbol == "ROGDI"
        assert gene.uniprot_id == "Q9GZN7"
        assert gene.cds_length_bp in {861, 864}

    def test_score_breakdown_must_pass_gate(self) -> None:
        passing = ModelScoreBreakdown(size_compatibility=0.6)
        failing = ModelScoreBreakdown(size_compatibility=0.3)
        assert passing.must_pass_gates["size_compatibility"] is True
        assert failing.must_pass_gates["size_compatibility"] is False


class TestROGDIFixture:
    """Validate the hand-audited ROGDI facts remain corrected."""

    def test_rogdi_fixture_values(self) -> None:
        data = json.loads((DATA_DIR / "rogdi_test_fixture.json").read_text())
        assert data["gene"] == "ROGDI"
        assert data["orphanet_id"] == "ORPHA:1946"
        assert data["omim_id"] == "226750"
        assert data["omim_gene_id"] == "614574"
        assert data["uniprot_id"] == "Q9GZN7"
        assert data["aa_length"] == 287
        assert data["cds_length_bp"] in {861, 864}
        assert data["protein_name"] == "Protein rogdi homolog"
        assert data["aav_compatible"] is True
        assert data["is_secreted"] is False
        assert data["active_gt_trials"] == 0

        serialized = json.dumps(data).lower()
        for obsolete_term in ("q9p2t1", "gmpr2", "gmp reductase", "impdh"):
            assert obsolete_term not in serialized

    def test_current_clients_have_offline_rogdi_fallbacks(self) -> None:
        disease = fetch_disease("ORPHA:1946")
        gene = fetch_gene("ROGDI")

        assert isinstance(disease, DiseaseInfo)
        assert disease.name.startswith("Kohlschutter-Tonz")
        assert disease.omim_ids == ["226750"]
        assert disease.gene_symbols == ["ROGDI"]
        assert "Autosomal recessive" in disease.inheritance
        assert "CNS" in disease.affected_tissues

        assert gene.symbol == "ROGDI"
        assert gene.uniprot_id == "Q9GZN7"
        assert gene.protein_name == "Protein rogdi homolog"
        assert gene.cds_length_bp in {861, 864}
        assert gene.aa_length == 287
        assert gene.is_secreted is False


class TestMechanismEvidence:
    """Validate source-linked mechanism evidence is explicit and conservative."""

    def test_rogdi_mechanism_is_source_linked_loss_of_function(self) -> None:
        mechanism = lookup_mechanism("ORPHA:1946", "ROGDI")
        score, notes = score_gene_addition_compatibility(mechanism)

        assert mechanism.mechanism_category == "loss_of_function"
        assert mechanism.gene_addition_compatibility == "conditional"
        assert "22482807" in mechanism.evidence_url
        assert score == 1.5
        assert any("Disease mechanism" in note for note in notes)
        assert any("Mechanism source" in note for note in notes)

    def test_unknown_mechanism_does_not_assume_lof_from_inheritance(self) -> None:
        mechanism = lookup_mechanism("ORPHA:999999", "FAKE1")
        score, notes = score_gene_addition_compatibility(mechanism)

        assert mechanism.mechanism_category == "unknown"
        assert mechanism.gene_addition_compatibility == "uncertain"
        assert mechanism.evidence_status == "missing"
        assert score == 1.0
        assert any("Do not infer mechanism from inheritance alone" in note for note in notes)


class TestDatabaseAndScoring:
    """Exercise the current SQLite-backed precedent scoring path."""

    @pytest.fixture
    def conn(self, tmp_path: Path) -> sqlite3.Connection:
        return setup(tmp_path / "nanogt.db")

    def test_setup_initializes_and_seeds_catalog(self, conn: sqlite3.Connection) -> None:
        vector_count = conn.execute("SELECT COUNT(*) FROM vectors").fetchone()[0]
        program_count = conn.execute("SELECT COUNT(*) FROM gt_programs").fetchone()[0]

        assert vector_count == len(VECTORS)
        assert program_count == len(GT_PROGRAMS)
        assert vector_count >= 5
        assert program_count >= 10

    def test_rogdi_packaging_fits_aav(self) -> None:
        gene = fetch_gene("ROGDI")
        score, notes = score_packaging(gene, program_cds=861, vector_cargo=4700)

        assert score == 2.0
        assert any("861bp" in note for note in notes)

    def test_rogdi_ranks_cns_aav9_precedents_high(self, conn: sqlite3.Connection) -> None:
        disease = fetch_disease("ORPHA:1946")
        assert disease is not None
        gene = fetch_gene("ROGDI")

        scores = rank_programs(disease, gene, conn)
        ranked = [score for score in scores if score.confidence != "fail"]

        assert ranked
        assert ranked[0].vector == "AAV9"
        assert ranked[0].confidence == "high"
        assert ranked[0].composite_score >= 7.5
        assert {"OAV101-IT", "Zolgensma"} & {score.program_name for score in ranked[:3]}

    def test_dmd_surfaces_microdystrophin_strategy(
        self,
        conn: sqlite3.Connection,
    ) -> None:
        disease = fetch_disease("ORPHA:98896")
        assert disease is not None
        gene = fetch_gene("DMD")

        scores = rank_programs(disease, gene, conn)
        scored = [score for score in scores if score.confidence != "fail"]
        srp9001 = next(score for score in scores if score.program_name == "SRP-9001")

        assert scored
        assert scored[0].program_name == "SRP-9001"
        assert srp9001.confidence == "high"
        assert srp9001.packaging_fit > 0
        assert srp9001.protein_class_match > 0
        assert any("micro/mini-transgene strategy" in note for note in srp9001.notes)
        assert any(
            score.confidence == "fail" and "11055bp" in " ".join(score.notes)
            for score in scores
        )
        assert any("Native CDS exceeds standard single-AAV capacity" in flag for flag in srp9001.review_flags)
        assert any("Engineered mini/micro-transgene strategy" in flag for flag in srp9001.review_flags)

    def test_achromatopsia_flags_gene_specific_subtype_scoring(
        self,
        conn: sqlite3.Connection,
    ) -> None:
        disease = fetch_disease("ORPHA:49382")
        assert disease is not None
        assert {"CNGB3", "CNGA3", "GNAT2", "PDE6C", "PDE6H", "ATF6"} <= set(disease.gene_symbols)

        gene = fetch_gene("CNGB3")
        scores = rank_programs(disease, gene, conn)
        top = next(score for score in scores if score.confidence != "fail")

        assert any("Multiple causal genes listed" in flag for flag in top.review_flags)


class TestReportsAndCLI:
    """Smoke test user-facing report generation and CLI commands."""

    def test_markdown_report_uses_current_match_result(self, tmp_path: Path) -> None:
        conn = setup(tmp_path / "nanogt.db")
        disease = fetch_disease("ORPHA:1946")
        assert disease is not None
        gene = fetch_gene("ROGDI")
        scores = rank_programs(disease, gene, conn)
        result = MatchResult(disease=disease, gene=gene, scores=scores, top_n=3)

        rendered = generate_report(result)
        assert "NanoGT Match Report" in rendered
        assert "Kohlschutter-Tonz" in rendered
        assert "ROGDI" in rendered
        assert "861 bp" in rendered or "864 bp" in rendered
        assert "## Interpretation" in rendered
        assert "Study-Level Limitations" in rendered
        assert "Catalog-relative ranking" in rendered
        assert "Endpoint" in rendered
        assert "Top 3 GT Precedent Matches" in rendered

    def test_report_warns_when_scoring_one_gene_in_multigene_disease(self, tmp_path: Path) -> None:
        conn = setup(tmp_path / "nanogt.db")
        disease = fetch_disease("ORPHA:49382")
        assert disease is not None
        gene = fetch_gene("CNGB3")
        scores = rank_programs(disease, gene, conn)
        result = MatchResult(disease=disease, gene=gene, scores=scores, top_n=3)

        rendered = generate_report(result)

        assert "Gene selection note" in rendered
        assert "this report scores CNGB3 only" in rendered
        assert "Manual Review Flags" in rendered

        output_path = save_report(result, tmp_path / "reports")
        assert output_path.exists()
        assert output_path.name.endswith("_cngb3.md")
        assert output_path.read_text() == rendered

    def test_report_records_primary_tissue_assumption(self, tmp_path: Path) -> None:
        conn = setup(tmp_path / "nanogt.db")
        disease = fetch_disease("ORPHA:324")
        assert disease is not None
        narrowed = replace(disease, affected_tissues=["heart"])
        gene = fetch_gene("GLA")
        scores = rank_programs(narrowed, gene, conn)
        result = MatchResult(
            disease=narrowed,
            gene=gene,
            scores=scores,
            top_n=3,
            primary_tissue="heart",
            source_tissues=disease.affected_tissues,
        )

        rendered = generate_report(result)

        assert "Primary tissue assumption" in rendered
        assert "heart selected from original tissue list" in rendered

    def test_cli_init_and_match_generate_report(self, tmp_path: Path) -> None:
        runner = CliRunner()
        db_path = tmp_path / "cli.db"
        output_dir = tmp_path / "output"

        init_result = runner.invoke(
            app,
            ["init", "--db-path", str(db_path)],
            env={"NANOGT_DB": str(db_path)},
        )
        assert init_result.exit_code == 0, init_result.output
        assert "Database ready" in init_result.output

        match_result = runner.invoke(
            app,
            ["match", "ORPHA:1946", "--top", "3", "-o", str(output_dir)],
            env={"NANOGT_DB": str(db_path)},
        )
        assert match_result.exit_code == 0, match_result.output
        assert "Kohlschutter-Tonz" in match_result.output

        reports = list(output_dir.glob("match_ORPHA1946_*.md"))
        assert len(reports) == 1
        report_text = reports[0].read_text()
        assert "NanoGT Match Report" in report_text
        assert "ROGDI" in report_text

    def test_cli_match_all_genes_generates_subtype_reports(self, tmp_path: Path) -> None:
        runner = CliRunner()
        db_path = tmp_path / "cli.db"
        output_dir = tmp_path / "subtypes"

        init_result = runner.invoke(
            app,
            ["init", "--db-path", str(db_path)],
            env={"NANOGT_DB": str(db_path)},
        )
        assert init_result.exit_code == 0, init_result.output

        match_result = runner.invoke(
            app,
            ["match", "ORPHA:49382", "--all-genes", "--top", "1", "-o", str(output_dir)],
            env={"NANOGT_DB": str(db_path)},
        )

        assert match_result.exit_code == 0, match_result.output
        assert "Subtype reports saved" in match_result.output
        assert (output_dir / "match_ORPHA49382_achromatopsia_cngb3.md").exists()
        assert (output_dir / "match_ORPHA49382_achromatopsia_cnga3.md").exists()

    def test_cli_match_primary_tissue_override_is_reported(self, tmp_path: Path) -> None:
        runner = CliRunner()
        db_path = tmp_path / "cli.db"
        output_dir = tmp_path / "primary"

        init_result = runner.invoke(
            app,
            ["init", "--db-path", str(db_path)],
            env={"NANOGT_DB": str(db_path)},
        )
        assert init_result.exit_code == 0, init_result.output

        match_result = runner.invoke(
            app,
            ["match", "ORPHA:324", "--primary-tissue", "heart", "-o", str(output_dir), "--top", "1"],
            env={"NANOGT_DB": str(db_path)},
        )

        assert match_result.exit_code == 0, match_result.output
        reports = list(output_dir.glob("match_ORPHA324_*_heart.md"))
        assert len(reports) == 1
        assert "Primary tissue assumption" in reports[0].read_text()
