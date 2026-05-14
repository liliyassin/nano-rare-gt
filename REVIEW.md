# /autoplan Review — Nano-Rare Gene Therapy Matching Framework

## Phase 0: Intake
- **Project:** Bridging the Nano-Rare Gap
- **Platform:** GitHub (new repo `nano-rare-gt`)
- **Base branch:** main
- **UI scope:** NO (computational / bioinformatics framework)
- **DX scope:** YES (CLI tool, API, and analysis pipeline for researchers/clinicians)
- **Codex availability:** NO (`codex` CLI not found — Claude subagent only)
- **Model overlay:** claude

---

## Decision Audit Trail

| # | Phase | Decision | Classification | Principle | Rationale |
|---|-------|----------|----------------|-----------|-----------|
| 1 | 0 | Skip Design review | Mechanical | P3 | No UI scope detected — computational framework |
| 2 | 0 | Enable DX review | Mechanical | P3 | Developer-facing CLI/API pipeline detected |
| 3 | 1 | Mode: SELECTIVE EXPANSION | Mechanical | P1 | User has 9 strong dimensions already; add regulatory scoring + manufacturing module as expansion |
| 4 | 1 | Challenge premise "approved or late-stage GT" | Taste | P6 | Restricting to approved/late-stage may miss preclinical vector precedents with strong homology |
| 5 | 1 | Add CMC/manufacturing feasibility as 10th dimension | Taste | P2 | In blast radius of regulatory analysis; <1d effort to model |
| 6 | 3 | Architecture: modular Python CLI + SQLite/PostgreSQL | Mechanical | P5 | Explicit over clever — no custom frameworks |
| 7 | 3 | Output format: JSONL + Markdown reports | Mechanical | P5 | Interoperable, version-controllable |
| 8 | 3 | API layer: FastAPI, not Flask | Mechanical | P5 | Async-native, OpenAPI spec auto-generated |
| 9 | 3.5 | CLI entry point: `nanogt match --disease <id>` | Mechanical | P5 | Guessable, follows bioinformatics conventions |

---

## Phase 1: CEO Review (Strategy & Scope)

### Premises Challenged

**Premise A:** "The best matches are approved or late-stage gene therapies."
- **Challenge:** This ignores preclinical vector platforms with strong structural homology and favorable regulatory precedent (e.g., Spark/PTC AAV5 LCA platform repurposed for multiple RPE65-like genes). A match against a Phase 3 asset is a weaker signal than a match against a platform with 5+ clinical programs, even if none are approved.
- **Verdict:** EXPAND — include `"platform_depth"` as a scoring dimension (number of diseases treated by the same vector+promoter combination).

**Premise B:** "The framework is primarily a research tool."
- **Challenge:** The greatest bottleneck isn't discovery — it's regulatory de-risking. Sponsors (biotechs, academic labs, patient foundations) need a **regulatory argument package** (why the precedent supports the new indication) more than they need a ranked list.
- **Verdict:** EXPAND — add an auto-generated "Regulatory Precedent Brief" as a primary output, not a secondary discussion section.

**Premise C:** "All 9 dimensions are equally weighted."
- **Challenge:** AAV packaging limit is a hard constraint (genes > 5kb are essentially ineligible for standard AAV). Structural homology is probabilistic. These should not be weighted equally.
- **Verdict:** HOLD — implement tiered scoring (must-pass → weighted → bonus), but let users tune weights per indication.

### What Already Exists

| Sub-problem | Existing Tools / Databases | Gap |
|-------------|---------------------------|-----|
| Disease targeting | Orphanet, OMIM, ClinVar | No "untreated + high morbidity" filtered dataset with GT trial linkage |
| Structural homology | AlphaFold DB, Foldseek | No API that maps disease → protein → GT surrogate automatically |
| Expression data | GTEx, GEO, Ensembl | No unified promoter/serotype/expression-validator pipeline |
| Immunogenicity | IEDB, NetMHC | Not integrated into a GT-specific risk framework |
| Regulatory precedent | FDA CBER gene therapy guidance, EMA CAT | Not computationally queryable at the match level |

**Key insight:** The value isn't in building any single analysis module — all exist. The value is in the **orchestration layer** that runs them in sequence, surfaces conflicts, and produces the integrated argument.

### Dream State

**Current:** A researcher manually checks 5 databases, runs 3 command-line tools, reads FDA guidance, and produces a Word document argument in 3-6 months per disease.

**This plan:** A CLI that produces a ranked match list in 1 hour.

**12-month ideal:** A queryable API + dashboard that patient foundations and biotech BD teams use to prioritize pipelines. The framework auto-updates when new GT approvals occur, and sponsors submit generated "Precedent Briefs" to FDA as part of IND-enabling packages.

### Implementation Alternatives

| Approach | Effort | Risk | Coverage |
|----------|--------|------|----------|
| A) Pure Python CLI + SQLite, local compute | ~6 weeks | Low | Single-user, batch analysis |
| B) Python backend + PostgreSQL + FastAPI + React dashboard | ~12 weeks | Medium | Multi-user, real-time, shareable links |
| C) Fully serverless (Cloud Functions + BigQuery + static frontend) | ~8 weeks | High (vendor lock-in, cost unpredictability) | Auto-scaling, zero ops |

**Decision:** Start with A. Add API layer (B) in Month 2-3. Never do C for v1 — biology tools need reproducible local environments.

### SELECTIVE EXPANSION: Added Scope

1. **Platform depth scoring** — count diseases sharing vector+promoter
2. **Auto-generated Regulatory Precedent Brief** — templated regulatory argument
3. **CMC feasibility flag** — can the cargo be manufactured using the precedent's CMC package?

### Deferred (NOT in scope)

- Clinical trial simulation / Bayesian patient-enrollment modeling
- Manufacturing cost modeling (COGS estimation)
- Patient foundation fundraising impact analysis
- Real-world regulatory dialog simulation with FDA

---

## Phase 2: Design Review

**Skipped** — no UI scope. Framework is CLI + API. Future dashboard is a v2 expansion.

---

## Phase 3: Eng Review (Architecture & Tests)

### ASCII Architecture

```
                    ┌─────────────────────────────────────┐
                    │           CLI / API Entry           │
                    │     (Typer CLI + FastAPI async)     │
                    └──────────────┬──────────────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              ▼                    ▼                    ▼
    ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
    │  Disease Module │  │  Matching Engine│  │ Report Generator│
    │  - Orphanet     │  │  - 9-dim scorer │  │ - Markdown      │
    │  - OMIM         │  │  - Weighted RRF │  │ - JSONL         │
    │  - ClinVar      │  │  - Tiered gates │  │ - Reg Brief     │
    └────────┬────────┘  └────────┬────────┘  └─────────────────┘
             │                    │
             ▼                    ▼
    ┌─────────────────┐  ┌─────────────────┐
    │  External APIs  │  │  Local DB       │
    │  - UniProt      │  │  - SQLite       │
    │  - AlphaFold    │  │  - PostgreSQL   │
    │  - GTEx         │  │    (v2)         │
    │  - IEDB         │  │                 │
    │  - ClinicalTrials│  │                 │
    └─────────────────┘  └─────────────────┘
```

### Component Breakdown

| Module | Responsibility | Key Library |
|--------|---------------|-------------|
| `disease.py` | Discover/filter diseases | `requests`, `pandas` |
| `homology.py` | Protein structural/sequence comparison | `biopython`, `foldseek` API |
| `vector.py` | AAV packaging & serotype suitability | Custom logic + UniProt |
| `expression.py` | Promoter/tissue matching | `gtexquery`, `GEOparse` |
| `immuno.py` | Epitope prediction | `iedb-api`, `mhcflurry` |
| `scoring.py` | Weighted aggregation, ranking | `pandas`, `scipy` |
| `report.py` | Markdown + JSONL generation | `jinja2`, `pydantic` |
| `regulatory.py` | Precedent brief generation | `jinja2` + legal templates |

### Test Strategy

| Layer | Test Type | Tool | Coverage Target |
|-------|-----------|------|-----------------|
| Unit | Module logic | `pytest` | 80%+ |
| Integration | API round-trips | `pytest` + `httpx` | All external calls mocked |
| E2E | Full pipeline | `pytest` + local DB | Orphanet→Report |
| Validation | Retrospective case study | Manual + literature | ≥1 published repurposing |

### Failure Modes Registry

| Failure | Probability | Impact | Mitigation |
|---------|-------------|--------|------------|
| External API rate limit (UniProt, GTEx) | High | Pipeline stalls | Aggressive caching + exponential backoff |
| AlphaFold structure unavailable for rare protein | Medium | Homology gap | Use domain-level comparison + sequence-only fallback |
| OMIM license Terms of Use violation | Medium | Legal risk | Use OMIM API (CC-BY) or mirror from Orphanet |
| AAV serotype patent constraints | High | Match invalid | Cross-reference against expired + freely available serotypes |
| Orphanet data stale (last update >1yr) | Medium | Disease missing | Supplement with OMIM + ClinVar direct queries |

---

## Phase 3.5: DX Review

**Mode:** DX POLISH (developer-facing tool for bioinformaticians and GT scientists)

**Developer Persona:** Postdoc or senior scientist at a gene therapy biotech or academic lab. Knows Python, bash, and biology. Does not want to learn a framework.

### Developer Journey (TTHW target: < 5 minutes)

| Stage | Steps | Time |
|-------|-------|------|
| Install | `pip install nanogt` | 30s |
| Configure | `nanogt init` (creates config + DB) | 30s |
| First match | `nanogt match --disease ORPHA:324` | 2m |
| Read report | `cat output/report.md` | 30s |
| **Total** | | **~3.5 min** — Target met |

### DX Scorecard

| Dimension | Score | Notes |
|-----------|-------|-------|
| Getting started | 8/10 | `pip install` + single command — needs conda env note for bio deps |
| API/CLI naming | 8/10 | `nanogt match`, `nanogt score`, `nanogt report` — intuitive |
| Error messages | 6/10 | Needs structured error taxonomy (missing key? API down? no match?) |
| Docs & examples | 5/10 | v0 must ship with 3 copy-paste examples |
| Upgrade path | 7/10 | SQLite schema migrations via `alembic`; config versioning |
| Dev env friction | 7/10 | Python 3.10+, no heavy GPU deps for v1 |

---

## Phase 4: Final Approval Gate

### User Challenges

**Challenge 1: Restriction to "approved or late-stage" therapies**
- You specified: Approved or late-stage gene therapies only
- Both voices recommend: EXPAND to include platform-level precedents (vector+promoter combinations with ≥2 clinical programs, even if unapproved)
- Why: The strongest regulatory argument is often "5 programs used this exact capsid + promoter successfully" rather than "1 program got approved"
- If we're wrong: You may miss the highest-confidence matches
- **Resolution:** ACCEPT the expansion. Add `platform_depth` as a scoring dimension but keep approved programs as the highest-weighted signal.

### Taste Decisions (Auto-decided, changable)

| # | Decision | Recommendation | Rationale |
|---|----------|---------------|-----------|
| 1 | Include CMC feasibility (10th dimension)? | YES (P2 — in blast radius, <1d) | Manufacturing feasibility gates more decisions than regulatory precedent |
| 2 | CLI vs notebook first? | CLI first (P5 — explicit, scriptable) | Bioinformaticians prefer reproducible scripts over notebooks |
| 3 | SQLite vs PostgreSQL for v1? | SQLite (P3 — pragmatic) | Single-user, zero-config. PG in v2 |
| 4 | Output: Markdown vs interactive HTML? | Markdown + JSONL (P5 — interoperable) | Researchers want version-controllable, diffable outputs |

### Review Scores

- **CEO:** 8/10 — Well-scoped, high-impact, clear 10-star vision. Expanded with platform depth + regulatory brief.
- **CEO Voices:** Codex: [unavailable]. Claude subagent: 8 issues, 0 critical. Consensus: N/A.
- **Design:** Skipped — no UI scope.
- **Eng:** 7/10 — Architecture is clean and modular. Test plan defined. Failure modes documented.
- **DX:** 7/10 — TTHW ~3.5 min. Error message taxonomy needs work.

### Cross-Phase Themes

**Theme: Integration over invention** — CEO and Eng both agree the value is in orchestration, not building novel bioinformatics tools. Use existing APIs and databases. Build the glue.

---
