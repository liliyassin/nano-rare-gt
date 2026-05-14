-- Nano-rare GT Framework — SQLite schema v0.1
-- PGLite-compatible, no Postgres-specific features.

-- Diseases table (Orphanet canonical, cross-walked to OMIM)
CREATE TABLE IF NOT EXISTS diseases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    orphanet_id TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    omim_id TEXT,
    prevalence TEXT,
    morbidity_flag INTEGER NOT NULL DEFAULT 0,
    inheritance TEXT,
    active_gt_trials INTEGER NOT NULL DEFAULT 0,
    phenotype_terms TEXT,  -- JSON array
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Genes table
CREATE TABLE IF NOT EXISTS genes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    aliases TEXT,  -- JSON array
    omim_id TEXT,
    uniprot_id TEXT UNIQUE,
    chromosome TEXT,
    exon_count INTEGER,
    cds_length_bp INTEGER,
    aa_length INTEGER,
    molecular_weight_da REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Proteins table
CREATE TABLE IF NOT EXISTS proteins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uniprot_id TEXT NOT NULL UNIQUE,
    name TEXT,
    sequence TEXT,
    domains TEXT,  -- JSON array
    go_terms TEXT,  -- JSON array
    keywords TEXT,  -- JSON array
    subcellular_location TEXT,  -- JSON array
    is_secreted INTEGER NOT NULL DEFAULT 0,
    afdb_id TEXT,
    afdb_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Link diseases to genes (many-to-many)
CREATE TABLE IF NOT EXISTS disease_genes (
    disease_id INTEGER NOT NULL REFERENCES diseases(id) ON DELETE CASCADE,
    gene_id INTEGER NOT NULL REFERENCES genes(id) ON DELETE CASCADE,
    relationship_type TEXT DEFAULT "causal",  -- causal, modifier, etc.
    PRIMARY KEY (disease_id, gene_id)
);

-- Vectors table (static for v0.1)
CREATE TABLE IF NOT EXISTS vectors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    serotype TEXT NOT NULL UNIQUE,
    cargo_limit_bp INTEGER NOT NULL DEFAULT 4700,
    tissue_tropism TEXT,  -- JSON array
    cns_tropic INTEGER NOT NULL DEFAULT 0,
    retinal_tropic INTEGER NOT NULL DEFAULT 0,
    hepatic_tropic INTEGER NOT NULL DEFAULT 0,
    muscle_tropic INTEGER NOT NULL DEFAULT 0,
    clinical_precedents INTEGER NOT NULL DEFAULT 0,
    freely_available INTEGER NOT NULL DEFAULT 1
);

-- Matches table (generated results)
CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    disease_id INTEGER NOT NULL REFERENCES diseases(id) ON DELETE CASCADE,
    gene_id INTEGER NOT NULL REFERENCES genes(id) ON DELETE CASCADE,
    vector_id INTEGER NOT NULL REFERENCES vectors(id) ON DELETE CASCADE,
    surrogate_program TEXT NOT NULL,
    composite_score REAL NOT NULL DEFAULT 0.0,
    confidence TEXT NOT NULL DEFAULT "low",
    scores_json TEXT NOT NULL,  -- ScoreBreakdown as JSON
    notes TEXT,  -- JSON array
    protocol_sections_json TEXT,  -- dict[string, string] as JSON
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Full-text search on diseases (for quick keyword lookup)
CREATE VIRTUAL TABLE IF NOT EXISTS diseases_fts USING fts5(
    name, phenotype_terms,
    content='diseases',
    content_rowid='id'
);

-- Indices for common queries
CREATE INDEX IF NOT EXISTS idx_genes_uniprot ON genes(uniprot_id);
CREATE INDEX IF NOT EXISTS idx_genes_symbol ON genes(symbol);
CREATE INDEX IF NOT EXISTS idx_matches_score ON matches(composite_score);
CREATE INDEX IF NOT EXISTS idx_diseases_omim ON diseases(omim_id);
