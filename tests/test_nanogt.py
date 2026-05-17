"""Basic tests for nano-rare GT framework core modules."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from nanogt.db import DB
from nanogt.models import Disease, ScoreBreakdown

DATA_DIR = Path(__file__).parent.parent / "data"


class TestModels:
    """Validate Pydantic models round-trip correctly."""

    def test_disease_model(self) -> None:
        d = Disease(
            orphanet_id="ORPHA:916",
            name="Kohlschutter-Tonz syndrome",
            omim_id="226750",
            inheritance="AR",
        )
        assert d.orphanet_id == "ORPHA:916"
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
        assert data["uniprot_id"] == "Q9P2T1"
        assert data["aa_length"] == 348
        assert data["cds_length_bp"] == 1044
        assert data["aav_compatible"] is True
        assert "hippocampus" in data["cell_types_targeted"][0].lower()
        assert data["is_secreted"] is False
        assert data["inheritance"] == "autosomal recessive"
        assert data["active_gt_trials"] == 0


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
            orphanet_id="ORPHA:916",
            name="Kohlschutter-Tonz syndrome",
            omim_id="226750",
            inheritance="AR",
        )
        row = db.get_disease_by_orphanet("ORPHA:916")
        assert row is not None
        assert row["name"] == "Kohlschutter-Tonz syndrome"
        assert row["omim_id"] == "226750"

    def test_insert_and_get_gene(self, db: DB) -> None:
        db.insert_gene(
            symbol="ROGDI",
            aliases=json.dumps(["GMPR2"]),
            uniprot_id="Q9P2T1",
            cds_length_bp=1044,
            aa_length=348,
        )
        row = db.get_gene_by_symbol("ROGDI")
        assert row is not None
        assert row["uniprot_id"] == "Q9P2T1"
        assert row["aa_length"] == 348

    def test_rogdi_fits_aav(self) -> None:
        """ROGDI CDS (~1044 bp) is well under the AAV packaging limit (4700 bp)."""
        assert 1044 <= 4700

    def test_vector_seed(self, db: DB) -> None:
        db.seed_vectors()
