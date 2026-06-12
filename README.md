# NanoGT — Nano-Rare Gene Therapy Precedent Matching

NanoGT is a dissertation-stage Python framework for matching monogenic rare diseases to existing gene-therapy precedents. It is designed for early-stage research prioritisation: given an Orphanet disease identifier, it scores the disease against a curated catalogue of approved or clinical-stage gene-therapy programmes and generates ranked Markdown reports.

## Current dissertation status

Current focus: a 30-disease proof-of-concept cohort for the dissertation report.

The current run has:

- 30 diseases in `data/disease_cohort_30.csv`.
- 21 curated surrogate gene-therapy programmes in `src/nanogt/catalog.py`.
- 12 scoring dimensions.
- 29 diseases with at least one compatible single-vector precedent.
- 23 high-confidence compatible matches.
- 6 medium-confidence compatible matches.
- 1 expected packaging hard-gate failure: Duchenne muscular dystrophy / full-length DMD.

Primary outputs:

- `output/SUMMARY.md` — cross-disease result table.
- `output/RESULTS_INTERPRETATION.md` — dissertation-safe interpretation of the 30-disease results.
- `output/match_*.md` — individual disease reports.
- `paper/` — dissertation draft sections.
- `DISSERTATION_TODO.md` — current task list and deadlines.

## What NanoGT does

For each disease-program pair, NanoGT scores:

1. Packaging fit.
2. Tissue tropism.
3. Protein class.
4. Biological pathway similarity.
5. Inheritance compatibility.
6. Regulatory approval/stage precedent.
7. Vector immunogenicity.
8. Therapeutic window.
9. Cross-correction potential.
10. Immune privilege.
11. Promoter availability.
12. Route-of-administration feasibility.

Raw scores are summed to a maximum of 18 and normalised to a 10-point composite score.

## What NanoGT does not claim

NanoGT is not a clinical recommendation engine. A top-ranked precedent does not mean that the same vector, promoter, route, dose, or development plan can be reused directly. Every output requires disease-specific literature review, source verification, vector engineering, toxicology, manufacturing assessment, and supervisor/expert review.

The current dissertation-safe claim is:

> NanoGT is a reproducible proof-of-concept framework for computational gene-therapy precedent mapping. In a 30-disease cohort, it generated interpretable disease-precedent clusters, recovered several expected clinical precedents, and flagged obvious scope failures such as full-length DMD packaging incompatibility.

## Installation for local development

This project uses Python and `uv`.

```bash
cd /Users/suzie/Projects/nano-rare-gt
uv sync --extra dev
uv run nanogt init
```

If using plain pip instead:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
nanogt init
```

## Run one disease

```bash
uv run nanogt match ORPHA:1946 --top 5 -o output
```

This writes an individual Markdown report into `output/`.

## Run the reproducible 30-disease cohort

```bash
uv run python run_results.py
```

Then open:

```bash
open output/SUMMARY.md
open output/RESULTS_INTERPRETATION.md
```

## Run tests

```bash
uv run pytest
```

## Inspect codebase size with pygount

```bash
uv run pygount --format=summary \
  --folders-to-skip=".git,node_modules,venv,.venv,__pycache__,.cache,dist,build,.next,.tox,.eggs,.pytest_cache,PDFs to Read,Trying_to_understand" \
  .
```

Current pygount summary is saved in `docs/CODEBASE_INSPECTION.md`.

## Repository map

```text
src/nanogt/          Python package: CLI, disease lookup, gene lookup, scoring, reports, static catalogue
tests/               pytest tests
data/                30-disease cohort CSV and fixtures
output/              generated match reports and summary interpretation
paper/               dissertation draft sections and figure notes
docs/                architecture notes, codebase inspection, background notes
reports/             generated protocol-style reports
```

## Immediate dissertation priorities

Do not expand the scope before submission. The critical work is now:

1. Fact-check every disease row in `data/disease_cohort_30.csv`.
2. Verify and read the key references that support the final claims.
3. Improve figures and tables for the dissertation.
4. Tighten Methods, Results, and Discussion around the actual 30-disease output.
5. State limitations honestly and explicitly.
6. Send the supervisor a concise update with the current framing and ask what evidence they most want strengthened.

See `DISSERTATION_TODO.md` for the dated work plan.

## Licence

MIT.
