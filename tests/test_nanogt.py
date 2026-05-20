"""Basic tests for nano-rare GT framework core modules."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from nanogt.cli import _load_rogdi_data
from nanogt.db import DB
from nanogt.models import Disease, Gene, Match, Report, ScoreBreakdown, Vector
from nanogt.report import ReportRenderer

DATA_DIR = Path(__file__).parent.parent / "data"


class TestModels:
    """Validate Pydantic models round-trip correctly."""

    def test_disease_model(self) -> None:
        d = Disease(
            orphanet_id="ORPHA:1946",
            name="Kohlschutter-Tonz syndrome",
            omim_id="226750",
            inheritance="AR",
        )
        assert d.orphanet_id == "ORPHA:1946"
        assert d.inheritance == "AR"

    def test_score_breakdown_must_pass(self) -> None:
        sb = ScoreBreakdown(size_compatibility=0.6)
        assert sb.must_pass_gates["size_compatibility"] is True
        sb2 = ScoreBreakdown(size_compatibility=0.3)
        assert sb2.must_pass_gates["size_compatibility"] is False


class TestROGDIFixture:
    """Validate the ROGDI test fixture matches known biological facts."""

    def test_rogdi_fixture_exists(self) -> None:
        fixture_path = DATA_DIR / "rogdi_test_fixture.json"
        assert fixture_path.exists()

    def test_rogdi_fixture_values(self) -> None:
        fixture_path = DATA_DIR / "rogdi_test_fixture.json"
        data = json.loads(fixture_path.read_text())
        assert data["gene"] == "ROGDI"
        assert data["orphanet_id"] == "ORPHA:1946"
        assert data["omim_id"] == "226750"
        assert data["omim_gene_id"] == "614574"
        assert data["uniprot_id"] == "Q9GZN7"
        assert data["afdb_id"] == "Q9GZN7"
        assert data["aa_length"] == 287
        assert data["cds_length_bp"] in {861, 864}
        assert data["protein_name"] == "Protein rogdi homolog"
        assert data["molecular_weight_da"] == 32254
        assert data["aav_compatible"] is True
        assert data["is_secreted"] is False
        assert data["inheritance"] == "autosomal recessive"
        assert data["active_gt_trials"] == 0
        serialized = json.dumps(data).lower()
        assert "q9p2t1" not in serialized
        assert "gmpr2" not in serialized
        assert "gmp reductase" not in serialized
        assert "impdh" not in serialized

    def test_rogdi_cli_loader_uses_correct_identity(self) -> None:
        disease, gene, protein, vector, scores = _load_rogdi_data()
        assert disease.orphanet_id == "ORPHA:1946"
        assert gene.omim_id == "614574"
        assert gene.uniprot_id == "Q9GZN7"
        assert gene.aa_length == 287
        assert gene.cds_length_bp in {861, 864}
        assert protein.uniprot_id == "Q9GZN7"
        assert protein.afdb_id == "Q9GZN7"
        assert protein.name == "Protein rogdi homolog"
        combined = " ".join(gene.aliases + protein.domains + protein.go_terms + protein.keywords).lower()
        assert "gmpr2" not in combined
        assert "gmp reductase" not in combined
        assert "impdh" not in combined
        assert scores.size_compatibility >= 0.5
        assert vector.cargo_limit_bp == 4700


class TestDB:
    """SQLite schema and basic CRUD."""

    @pytest.fixture
    def db(self, tmp_path: Path) -> DB:
        p = tmp_path / "test.db"
        return DB(p)

    def test_schema_initialization(self, db: DB) -> None:
        # seed_vectors populates the vectors table
        db.seed_vectors()

    def test_insert_and_get_disease(self, db: DB) -> None:
        db.insert_disease(
            orphanet_id="ORPHA:1946",
            name="Kohlschutter-Tonz syndrome",
            omim_id="226750",
            inheritance="AR",
        )
        row = db.get_disease_by_orphanet("ORPHA:1946")
        assert row is not None
        assert row["name"] == "Kohlschutter-Tonz syndrome"
        assert row["omim_id"] == "226750"

    def test_insert_and_get_gene(self, db: DB) -> None:
        db.insert_gene(
            symbol="ROGDI",
            aliases=json.dumps(["KIAA0267"]),
            uniprot_id="Q9GZN7",
            cds_length_bp=861,
            aa_length=287,
        )
        row = db.get_gene_by_symbol("ROGDI")
        assert row is not None
        assert row["uniprot_id"] == "Q9GZN7"
        assert row["aa_length"] == 287

    def test_rogdi_fits_aav(self) -> None:
        """ROGDI CDS (~861 bp amino-acid coding region) is under the AAV packaging limit."""
        assert 861 <= 4700

    def test_vector_seed(self, db: DB) -> None:
        db.seed_vectors()


class TestReportRenderer:
    """Markdown report rendering."""

    def test_batch_report_formats_scores_and_table_spacing(self, tmp_path: Path) -> None:
        disease = Disease(
            orphanet_id="ORPHA:1946",
            name="Kohlschutter-Tonz syndrome",
            omim_id="226750",
            inheritance="AR",
            prevalence="<1 / 1,000,000",
            active_gt_trials=0,
            phenotype_terms=["amelogenesis imperfecta", "epilepsy"],
        )
        gene = Gene(
            symbol="ROGDI",
            uniprot_id="Q9GZN7",
            chromosome="16p12.1",
            cds_length_bp=861,
            aa_length=287,
        )
        vector = Vector(serotype="AAV9")
        scores = ScoreBreakdown(
            structural_homology=0.7,
            sequence_identity=0.8,
            domain_similarity=0.5,
            size_compatibility=1.0,
            tissue_tropism=0.4,
            roa_precedent=0.1 + 0.2,
            promoter_match=0.8,
            localization_match=0.8,
            immunogenicity=0.6000000000000001,
            therapeutic_window=0.7,
            codon_optimization=0.9,
            platform_depth=1.0,
        )
        match = Match(
            disease=disease,
            gene=gene,
            vector=vector,
            surrogate_program="Zolgensma (onasemnogene abeparvovec)",
            scores=scores,
            composite_score=0.845,
            confidence="high",
        )
        report = Report(
            query_disease=disease,
            matches=[match],
            top_match=match,
            generated_at="2026-05-17 17:46:45",
            query_time_s=0.14,
        )

        output_path = ReportRenderer().render_batch_report(
            report,
            tmp_path / "report.md",
        )
        rendered = output_path.read_text()

        assert "0.30000000000000004" not in rendered
        assert "0.6000000000000001" not in rendered
        assert "| Route-of-administration precedent | 0.30 |" in rendered
        assert "| Immunogenicity | 0.60 |" in rendered
        assert "\n\n| 1 |" not in rendered
        assert "\n\n- epilepsy" not in rendered
        assert "Q9GZN7" in rendered
        assert "ORPHA:1946" in rendered
        assert "Q9P2T1" not in rendered
        assert "1044 bp" not in rendered
        assert "348" not in rendered

    def test_protocol_uses_corrected_rogdi_science(self, tmp_path: Path) -> None:
        disease, gene, protein, vector, scores = _load_rogdi_data()
        output_path = ReportRenderer().render_protocol(
            disease,
            gene,
            protein,
            vector,
            scores,
            tmp_path / "protocol.md",
        )
        rendered = output_path.read_text()
        assert "Q9GZN7" in rendered
        assert "ORPHA:1946" in rendered
        assert "287 aa" in rendered
        assert "861 bp" in rendered or "864 bp" in rendered
        assert "Rabconnectin-3" in rendered
        assert "V-ATPase" in rendered
        assert "Q9P2T1" not in rendered
        assert "GMPR2" not in rendered
        assert "GMP reductase" not in rendered
        assert "IMPDH" not in rendered
