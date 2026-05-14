# This Week (Week 1) — Nano-Rare GT Framework

## Monday: Project Setup + Architecture

- [ ] `cd ~/nano-rare-gt && mkdir src/nanogt tests data docs`
- [ ] Create `pyproject.toml` with dependencies: `typer`, `requests`, `pydantic`, `jinja2`, `pytest`, `requests-cache`, `pandas`
- [ ] Initialize git repo (done), set up `pre-commit` with `black`, `ruff`, `mypy`
- [ ] Write `docs/ADR-001-architecture.md` — SQLite v1, Pydantic v2 models, Typer CLI
- [ ] Define core Pydantic models in `src/nanogt/models.py`:
  - `Disease` (orphanet_id, name, prevalence, morbidity_flag)
  - `Gene` (symbol, omim_id, uniprot_id, cds_length, aa_length)
  - `Protein` (uniprot_id, afdb_id, sequence, domains[])
  - `Vector` (serotype, cargo_limit, tissue_tropism[])
  - `Match` (disease, gene, vector, surrogate_program, scores{})
  - `ScoreBreakdown` (structural, size, tissue, roa, promoter, localization, immuno, toxicity, cai)
- [ ] Define SQLite schema in `src/nanogt/schema.sql`

## Tuesday: Disease Discovery Module

- [ ] Implement `src/nanogt/disease.py`:
  - `query_orphanet(rarity_threshold="nano-rare")` → list[Disease]
  - `filter_no_active_trials(diseases)` → cross-ref ClinicalTrials.gov
  - `filter_high_morbidity(diseases)` → boost if Orphanet disability weight > threshold
  - `link_to_omim(disease)` → resolve OMIM gene entry
- [ ] Add `requests-cache` to all HTTP clients (7-day TTL default)
- [ ] Unit tests in `tests/test_disease.py` with mocked Orphanet/OMIM responses
- [ ] Save sample output to `data/sample_diseases.jsonl`

## Wednesday: Protein + Structure Linkage

- [ ] Implement `src/nanogt/homology.py`:
  - `fetch_uniprot(uniprot_id)` → sequence, domains, GO terms
  - `fetch_alphafold(uniprot_id)` → PDB file URL or structural summary
  - `calculate_domain_similarity(protein_a, protein_b)` → cosine on domain vectors
  - `sequence_identity(a, b)` → global + local alignment scores
- [ ] Store in SQLite via `src/nanogt/db.py` (Connection manager, insert/update/query)
- [ ] Unit tests in `tests/test_homology.py`

## Thursday: Vector Sizing + Serotype Check

- [ ] Implement `src/nanogt/vector.py`:
  - `is_aav_compatible(cds_length_bp)` → bool (gate: <= 4700)
  - `aav_serotypes` → static dictionary: name → tissue list, cargo limit, clinical precedent count
  - `match_serotype_to_tissue(serotype, target_tissues)` → compatibility score
  - `precedent_count(serotype, promoter)` → platform depth metric
- [ ] Build `data/serotype_map.json` from literature
- [ ] Unit tests in `tests/test_vector.py`

## Friday: CLI Integration + v0.1 End-to-End

- [ ] Implement `src/nanogt/cli.py` (Typer):
  - `nanogt match --disease ORPHA:324 --output report.md`
  - `nanogt init` → create ~/.nanogt/ directory + SQLite DB
  - `nanogt status` → check DB health, API connectivity
- [ ] Implement `src/nanogt/report.py`:
  - Markdown output (Jinja2 template)
  - JSONL for downstream analysis
- [ ] Run single end-to-end test: `nanogt match --disease ORPHA:324`
  - Must complete in < 2 min
  - Must produce `report.md` with plausible surrogate match
- [ ] Fix all blockers, tag `v0.1-PoC`
- [ ] Run `pytest` — all tests green
- [ ] Run `mypy src/` — clean
- [ ] Review: `/review` then `/ship`
