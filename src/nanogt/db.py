# db.py — Nano-rare GT Framework
"""SQLite database manager."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

SCHEMA_PATH = Path(__file__).with_name("schema.sql")


class DB:
    """Lightweight SQLite wrapper with dict-row factory."""

    def __init__(self, db_path: str | Path) -> None:
        self.db_path = Path(db_path)
        self._ensure_schema()

    def _connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _ensure_schema(self) -> None:
        if not SCHEMA_PATH.exists():
            raise FileNotFoundError(f"Schema file not found: {SCHEMA_PATH}")
        with self._connection() as conn:
            conn.executescript(SCHEMA_PATH.read_text())

    # --- Diseases ---

    def insert_disease(self, **kwargs: Any) -> int:
        cols = list(kwargs.keys())
        placeholders = ", ".join(f":{c}" for c in cols)
        sql = f"INSERT INTO diseases ({', '.join(cols)}) VALUES ({placeholders})"
        with self._connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, kwargs)
            conn.commit()
            return cur.lastrowid or 0

    def get_disease_by_orphanet(self, orphanet_id: str) -> dict[str, Any] | None:
        with self._connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM diseases WHERE orphanet_id = ?", (orphanet_id,)
            )
            row = cur.fetchone()
            return dict(row) if row else None

    # --- Genes ---

    def insert_gene(self, **kwargs: Any) -> int:
        cols = list(kwargs.keys())
        placeholders = ", ".join(f":{c}" for c in cols)
        sql = f"INSERT INTO genes ({', '.join(cols)}) VALUES ({placeholders})"
        with self._connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, kwargs)
            conn.commit()
            return cur.lastrowid or 0

    def get_gene_by_symbol(self, symbol: str) -> dict[str, Any] | None:
        with self._connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM genes WHERE symbol = ?", (symbol,))
            row = cur.fetchone()
            return dict(row) if row else None

    # --- Vectors (static seed) ---

    def seed_vectors(self) -> None:
        """Insert default AAV serotype data."""
        defaults = [
            {
                "serotype": "AAV9",
                "cargo_limit_bp": 4700,
                "tissue_tropism": json.dumps(
                    ["CNS", "heart", "liver", "muscle", "retina"]
                ),
                "cns_tropic": 1,
                "retinal_tropic": 1,
                "hepatic_tropic": 1,
                "muscle_tropic": 1,
                "clinical_precedents": 25,
                "freely_available": 1,
            },
            {
                "serotype": "AAV8",
                "cargo_limit_bp": 4700,
                "tissue_tropism": json.dumps(["CNS", "liver", "retina", "muscle"]),
                "cns_tropic": 1,
                "retinal_tropic": 1,
                "hepatic_tropic": 1,
                "muscle_tropic": 1,
                "clinical_precedents": 18,
                "freely_available": 1,
            },
            {
                "serotype": "AAVrh.10",
                "cargo_limit_bp": 4700,
                "tissue_tropism": json.dumps(["CNS", "systemic"]),
                "cns_tropic": 1,
                "retinal_tropic": 0,
                "hepatic_tropic": 0,
                "muscle_tropic": 0,
                "clinical_precedents": 8,
                "freely_available": 1,
            },
            {
                "serotype": "AAV-DJ",
                "cargo_limit_bp": 4700,
                "tissue_tropism": json.dumps(["broad", "liver", "CNS"]),
                "cns_tropic": 1,
                "retinal_tropic": 0,
                "hepatic_tropic": 1,
                "muscle_tropic": 0,
                "clinical_precedents": 5,
                "freely_available": 1,
            },
        ]
        with self._connection() as conn:
            cur = conn.cursor()
            for v in defaults:
                cur.execute(
                    "INSERT OR IGNORE INTO vectors (serotype, cargo_limit_bp, tissue_tropism, "
                    "cns_tropic, retinal_tropic, hepatic_tropic, muscle_tropic, "
                    "clinical_precedents, freely_available) VALUES ("
                    ":serotype, :cargo_limit_bp, :tissue_tropism, :cns_tropic, "
                    ":retinal_tropic, :hepatic_tropic, :muscle_tropic, "
                    ":clinical_precedents, :freely_available)",
                    v,
                )
            conn.commit()
