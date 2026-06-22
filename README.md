# NanoGT — Nano-Rare Gene Therapy Precedent Matching

NanoGT is a dissertation-stage Python framework for matching monogenic rare diseases to existing gene-therapy precedents. It is designed for early-stage research prioritisation: given an Orphanet disease identifier, it scores the disease against a curated catalogue of approved or clinical-stage gene-therapy programmes and generates ranked Markdown reports.

## Current dissertation status

Current focus: a 46-disease proof-of-concept cohort for the dissertation report.

The current run has:

- 46 diseases in the cohort (stored in `data/disease_cohort_46.csv`).
- Source-linked disease mechanism evidence in `data/disease_mechanisms_46.csv`.
- 21 curated surrogate gene-therapy programmes in `src/nanogt/catalog.py`.
- 14 scoring dimensions (v2 algorithm).
- 45 diseases with at least one ranked precedent; NF1 receives a packaging hard-fail (8,451 bp CDS exceeds all vectors).
- 36 high-confidence matches.
- 8 medium-confidence matches.
- Full-length DMD still triggers packaging failures against ordinary AAV programs, while the engineered micro-dystrophin precedent is scored separately.

Primary outputs:

- `output/SUMMARY.md` — cross-disease result table.
- `output/RESULTS_INTERPRETATION.md` — dissertation-safe interpretation of the cohort results.
- `output/match_*.md` — individual disease reports.
- `paper/` — dissertation draft sections.

## Scripts — what each file does and when to run it

| Script | What it does | When to run |
|---|---|---|
| `run_results.py` | Scores all 46 diseases and writes `output/match_*.md` + `output/SUMMARY.md` | If you change scoring logic or want to regenerate all results from scratch |
| `score_new_diseases.py` | Scores a batch of new diseases and appends them to `SUMMARY.md` | If you add new diseases to `data/disease_cohort_46.csv` |
| `generate_figures.py` | Generates `paper/figure1_scores.pdf`, `figure2_radar.pdf`, `figure3_stacked.pdf` | After any change to scores or disease names |
| `regenerate_match_pdfs.py` | Converts all `output/match_*.md` files to PDFs in `output/pdfs/` | After updating match reports |
| `generate_draft_pdf.py` | Compiles `paper/` markdown sections into a single dissertation draft PDF | When you want a full PDF of the dissertation |
| `extract_pdfs.py` | Extracts text from PDFs in `Reading Literature/` into `.txt` files | If you add new PDFs and want searchable text versions |
| `setup_and_run.sh` | One-command setup + run (installs dependencies, runs `run_results.py`) | First-time setup on a new machine |

All scripts are run from the project root, e.g. `uv run python scripts/generate_figures.py`.

---

## What NanoGT does

For each disease-program pair, NanoGT scores:

1. Packaging fit.
2. Tissue tropism.
3. Protein class.
4. Biological pathway similarity.
5. Molecular mechanism / modality compatibility.
6. Inheritance compatibility.
7. Regulatory approval/stage precedent.
8. Vector immunogenicity.
9. Therapeutic window.
10. Cross-correction potential.
11. Immune privilege.
12. Promoter availability.
13. Route-of-administration feasibility.
14. Organelle targeting feasibility (v2).

Raw scores are summed to a maximum of 21 and normalised to a 10-point composite score. The mechanism/modality layer uses source-linked evidence and returns `unknown`/`uncertain` rather than assuming inheritance alone proves loss of function.

## What NanoGT does not claim

NanoGT is not a clinical recommendation engine. A top-ranked precedent does not mean that the same vector, promoter, route, dose, or development plan can be reused directly. Every output requires disease-specific literature review, source verification, vector engineering, toxicology, manufacturing assessment, and supervisor/expert review.

The current dissertation-safe claim is:

> NanoGT is a reproducible proof-of-concept framework for computational gene-therapy precedent mapping. In a 46-disease cohort spanning LOF, haploinsufficiency, repeat-expansion, and imprinting mechanisms, it generated interpretable disease-precedent clusters, recovered several expected clinical precedents, and correctly flagged scope failures such as DMD native-gene packaging incompatibility and NF1's oversized CDS.

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

(The `nanogt` CLI is installed from `src/nanogt/` and doesn't need to be in `scripts/`.)

This writes an individual Markdown report into `output/`.

## Run the reproducible 46-disease cohort

```bash
uv run python scripts/run_results.py
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

Current pygount summary is saved by re-running the command above.

## Repository map

```text
src/nanogt/          Python package: CLI, disease lookup, gene lookup, scoring, reports, static catalogue
scripts/             pipeline scripts (run from project root)
tests/               pytest tests
data/                46-disease cohort CSV and fixtures
output/              generated match reports and summary interpretation
paper/               dissertation draft sections and figure notes
docs/                architecture notes, scoring fix audit, disease deep-dives, reference PDF
Reading Literature/  source papers (PDFs + extracted text)
```

## Immediate dissertation priorities

Do not expand the scope before submission. The critical work is now:

1. Tighten Methods, Results, and Discussion around the actual 46-disease output.
2. Verify and read the key references that support the final claims.
3. Finalise figures and supplementary tables.
4. State limitations honestly and explicitly.

## Licence

MIT.
