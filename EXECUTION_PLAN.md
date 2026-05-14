# Execution Plan — Nano-Rare Gene Therapy Matching Framework

## Overview

This plan decomposes the project into 6 milestones across 12 weeks, with a
concentrated 2-week MVP sprint for Week 1-2. The architecture is modular Python
(CLI → local analysis → reports), with each module independently testable.

---

## Milestones

| Milestone | Week | Deliverable |
|-----------|------|-------------|
| M1 — PoC Pipeline | 1-2 | Single-disease end-to-end match via CLI |
| M1b — ROGDI Deep-Dive | 2-3 | Full 9-dimension analysis + Standardised GT Protocol for ROGDI |
| M2 — Multi-Disease Batch | 3-4 | Batch query Orphanet + OMIM, ranked output |
| M3 — Full Scoring Matrix | 5-6 | All 9 dimensions implemented + weighted aggregation |
| M4 — Regulatory Brief | 7-8 | Auto-generated Standardised Gene Therapy Protocol (ROGDI first) |
| M5 — Validation | 9-10 | Retrospective validation case studies (ROGDI illustrative) |
| M6 — Public Release | 11-12 | Open-source publication, documentation, preprint with ROGDI results |

---

## M1: PoC Pipeline (Week 1-2)

### Week 1: Foundation + Disease Query Module

**Monday: Project Setup + Architecture**
- Create Python project structure with `pyproject.toml`
- Set up `pytest` + `pre-commit` (black, ruff, mypy)
- Define Pydantic models: `Disease`, `Gene`, `Match`, `Score`, `Report`
- Write ADR-001: Architecture Decision Record (SQLite v1, Pydantic models, CLI via Typer)
- **ROGDI data seed:** Hardcode ROGDI facts into test fixtures for validation

**Tuesday: Orphanet + OMIM Integration**
- Implement `disease.py`: query Orphanet API for rare diseases
- Filter: monogenic, high-morbidity, no active GT clinical trials
- Cross-reference OMIM for gene mapping + inheritance
- Cache layer: `requests-cache` for all external APIs
- Unit tests with mocked HTTP responses
- **ROGDI test:** Verify ORPHA:916 plus OMIM 226750 resolves correctly

**Wednesday: UniProt + AlphaFold Linkage**
- Implement `homology.py`: map gene → UniProt entry → AlphaFold structure
- Fetch protein sequence, domains, GO terms
- Store in local SQLite (schema design + `alembic` migration)
- Unit tests for protein data pipeline
- **ROGDI validation:** Verify Q9P2T1 → 348 aa, IMPDH domain, cytosol localization

**Thursday: Vector Sizing + Serotype Check**
- Implement `vector.py`: calculate CDS length, flag AAV packaging limits
- Build serotype-to-tissue mapping from literature (static JSON asset v1)
- Hard gate: genes > 4.7kb = auto-lower match score
- **ROGDI sizing:** Confirm ~1044 bp CDS fits comfortably in all AAV serotypes

**Friday: CLI Integration + v0.1 End-to-End**
- Wire modules into `nanogt match --disease <orphanet_id>`
- Single-disease test case: **ROGDI as primary worked example**
- Output: JSONL + Markdown report (Jinja2 template)
- End-to-end test: from ROGDI disease ID → report in < 2 minutes
- Report must include: gene size, AAV compatibility, cell-type targeting, structural homologs

### Week 2: Scoring Shell + ROGDI Deep-Dive

**Monday-Tuesday: Scoring Framework**
- Implement `scoring.py`: tiered scoring (must-pass → weighted → bonus)
- Default weights v0.1 (equal across dimensions for baseline)
- Manual override system: `--weights-file weights.json`
- Top-N ranking with confidence intervals

**Wednesday-Thursday: ROGDI Deep-Dive Analysis**
- Run all 9 scoring dimensions on ROGDI / KTS
- Identify closest structural homologs (Foldseek run if available)
- Map target cell types: neurons (hippocampus), ameloblasts, renal tubules
- Assess delivery routes: IV vs ICV vs intra-oral injection
- Evaluate therapeutic window: ROGDI is a metabolic enzyme — overexpression risk vs rescue needed
- Immunogenicity: IEDB epitope scan on ROGDI protein sequence
- Codon optimization: CAI for human neurons + ameloblasts
- Generate first-pass "Standardised Gene Therapy Protocol" for ROGDI
- Document: recommended serotype, promoter, RoA, risk mitigations

**Friday: v0.1 Integration Test**
- Run full pipeline on **ROGDI + 4 additional hand-picked diseases**
- Validate ROGDI top match quality against literature
- Fix blocking bugs, document known gaps
- Tag `v0.1-PoC` release
- Supervisor review checkpoint: ROGDI report

---

## M2: Multi-Disease Batch (Week 3-4)

- Parallelize batch queries with `asyncio` or ` concurrent.futures`
- Implement Orphanet full-corpus query (not hand-picked)
- Add `nanogt batch --input diseases.csv --output matches.jsonl`
- Progress bars (`rich`, `tqdm`)
- SQL query layer for post-hoc filtering (`nanogt query --score-min 0.7`)

---

## M3: Full 9-Dimension Scoring (Week 5-6)

- **Immunogenicity:** IEDB API integration, epitope prediction, risk flagging
- **Promoter Matching:** TiProD / EPD / GEO promoter query, enhancer matching
- **Codon Optimization:** CAI scoring relative to tissue (human codon usage)
- **Therapeutic Window:** Overexpression toxicity flags from literature
- **Cross-Correction:** Secreted vs intracellular, rescue radius calculation
- **Weight Tuning:** Run sensitivity analysis, expose `--calibrate` mode

---

## M4: Regulatory Brief Generator (Week 7-8)

- Jinja2 templates for regulatory precedent brief
- Sections: vector precedent, promoter precedent, RoA precedent, CMC analogy
- Auto-populate from matched surrogate data
- Reference FDA CBER guidance docs + EMA CAT qualification procedures
- Output: Word compatible Markdown (Pandoc-ready)

---

## M5: Validation (Week 9-10)

- Retrospective case study: Identify a known successful GT repurposing from literature
- Run the v0.3 framework on the original disease — did it surface the correct surrogate?
- If yes: document + publish as proof-of-concept
- If no: investigate scoring failures, iterate weights, document lessons
- Second case study (if time): a known failure — did the framework correctly flag the risk?

---

## M6: Release (Week 11-12)

- GitHub public repo with MIT license
- Full README with installation, examples, methodology
- Documentation site (MkDocs or GitHub Pages)
- Preprint: bioRxiv or medRxiv submission
- Outreach: patient advocacy orgs, GT biotech BD teams, academic labs

---

## Risk Register

| Risk | Mitigation | Owner | Week to Resolve |
|------|-----------|-------|----------------|
| Orphanet API rate limits / changes | Cache aggressively; build fallback to OMIM direct | Week 1 | |
| AlphaFold structures missing for rare proteins | Domain-level fallback; validate against experimental structures | Week 2 | |
| No retrospective validation case found | Expand to "platform precedent" not just "approved GT" | Week 9 | |
| Regulatory brief rejected by consulting lawyer | Frame as "informational synthesis" not "legal advice"; include disclaimer | Week 7 | |

---

## DECISION: Approve plan with expansions

- **Scope:** Approved as SELECTIVE EXPANSION (platform depth + regulatory brief auto-generation)
- **Architecture:** Approved — modular Python CLI, SQLite v1, FastAPI v2
- **DX:** Approved — TTHW target 3.5 min
- **Next step:** `/ship` when v0.1 PoC is ready (end of Week 2)
