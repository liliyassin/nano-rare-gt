"""Database layer for nanogt — SQLite with WAL mode."""
import json # converts Python lists like tissue tropism into JSON strings for SQLite 
import os # reads environment variables such as NANOGT_DB
import pathlib # handles file paths cleanly 
import sqlite3 # built-in Python library for SQLite databases

from .catalog import VECTORS, GT_PROGRAMS # rows of the two tables 

DEFAULT_DB = pathlib.Path.home() / ".nanogt" / "nanogt.db"
SCHEMA_SQL = pathlib.Path(__file__).parent / "schema.sql"


def get_db_path() -> pathlib.Path:
    return pathlib.Path(os.environ.get("NANOGT_DB", DEFAULT_DB)) # this is saying that if environment variables NANOGT_DB exists, use it. Otherwise, use DEFAULT_DB


def get_conn(db_path=None) -> sqlite3.Connection:
    path = db_path or get_db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db(conn: sqlite3.Connection) -> None: #init_db(conn) function creates database tables 
    conn.executescript(SCHEMA_SQL.read_text()) # creates tables such as diseases, genes, proteins, disease_genes, vectors, matches, diseases_fts from schema.sql
    conn.execute("""
        CREATE TABLE IF NOT EXISTS gt_programs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            disease TEXT NOT NULL,
            gene_symbol TEXT NOT NULL,
            vector TEXT NOT NULL,
            tissue_target TEXT NOT NULL,
            cds_bp INTEGER NOT NULL,
            approval_status TEXT NOT NULL,
            approval_year INTEGER,
            mechanism TEXT NOT NULL,
            protein_class TEXT NOT NULL,
            inheritance TEXT NOT NULL,
            pathway TEXT NOT NULL,
            notes TEXT
        )
    """)
    conn.commit() # saves the table creation changes 


def seed_db(conn: sqlite3.Connection) -> None:
    # Wipes both tables and re-inserts from catalog.py on every call.
    # This means any change to catalog.py is automatically picked up the next
    # time setup() / nanogt init runs — no need to manually delete the database.
    # (A previous version had a misleading comment saying seeding only happened
    # when the table was empty; that was incorrect — DELETE runs unconditionally.)
    conn.execute("DELETE FROM vectors")
    for v in VECTORS:
        conn.execute("""
            INSERT INTO vectors
            (serotype, cargo_limit_bp, tissue_tropism, cns_tropic, retinal_tropic,
             hepatic_tropic, muscle_tropic, clinical_precedents, freely_available)
            VALUES (?,?,?,?,?,?,?,?,?)
        """, (
            v["serotype"],
            v["cargo_limit_bp"],
            json.dumps(v.get("tissue_tropism", [])),
            v.get("cns_tropic", 0),
            v.get("retinal_tropic", 0),
            v.get("hepatic_tropic", 0),
            v.get("muscle_tropic", 0),
            v.get("clinical_precedents", 0),
            v.get("freely_available", 1),
        ))
    conn.commit()

    conn.execute("DELETE FROM gt_programs")
    for p in GT_PROGRAMS:
        conn.execute("""
            INSERT INTO gt_programs
            (name, disease, gene_symbol, vector, tissue_target, cds_bp,
             approval_status, approval_year, mechanism, protein_class,
             inheritance, pathway, notes)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            p["name"], p["disease"], p["gene_symbol"], p["vector"],
            p["tissue_target"], p["cds_bp"], p["approval_status"],
            p.get("approval_year"), p["mechanism"], p["protein_class"],
            p["inheritance"], p["pathway"], p.get("notes"),
        ))
    conn.commit()


def setup(db_path=None) -> sqlite3.Connection:
    """One-call setup: connect, init schema, seed data from catalog.py."""
    conn = get_conn(db_path)
    init_db(conn)
    seed_db(conn)
    return conn
