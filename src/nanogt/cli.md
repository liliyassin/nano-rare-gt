# Code Study Note: `src/nanogt/cli.py`

File studied: `/Users/suzie/Projects/nano-rare-gt/src/nanogt/cli.py`

Related files:
- `src/nanogt/db.py`
- `src/nanogt/disease.py`
- `src/nanogt/gene.py`
- `src/nanogt/scoring.py`
- `src/nanogt/report.py`

Study goal:
Understand how `cli.py` acts as the user-facing command-line entry point for NanoGT, how it moves a disease ID through database setup, disease lookup, gene lookup, scoring, terminal display, and Markdown report creation, and where its practical assumptions and weaknesses are.

---

## 1. Plain-English identity

`cli.py` is the front door of NanoGT.

It is the file that turns Python functions into terminal commands. When someone types commands such as:

```bash
nanogt init
nanogt match ORPHA:324
nanogt batch ORPHA:70 ORPHA:306 ORPHA:1946
```

this file decides what should happen.

It does not contain the main biomedical scoring algorithm itself. Instead, it coordinates other parts of the project:

- `db.py` sets up the SQLite database.
- `disease.py` fetches disease information from Orphanet or fallback data.
- `gene.py` fetches gene/protein information from UniProt or fallback data.
- `scoring.py` ranks gene therapy precedent programs.
- `report.py` writes the final Markdown report.

The easiest mental model:

```text
cli.py = the receptionist / traffic controller for NanoGT
```

It receives the user's command, calls the right helper files in the right order, and shows or saves the result.

---

## 2. Why this file exists

NanoGT needs a way for a user to run the project without opening Python and manually calling functions.

`cli.py` exists so the project can be used from the terminal as a small application.

For example, a biomedical researcher should be able to type:

```bash
nanogt match ORPHA:1946 --gene ROGDI --top 5
```

and get:

1. A database check/setup.
2. A disease lookup.
3. A gene/protein lookup.
4. A ranked list of gene therapy precedents.
5. A saved Markdown report.

So `cli.py` is not mainly about scientific reasoning. It is about workflow orchestration.

---

## 3. How this file fits into the project data flow

For one disease match, the data flow is:

```text
User terminal command
    ↓
cli.py receives disease ID and options
    ↓
db.py opens/creates/seeds SQLite database
    ↓
disease.py fetches DiseaseInfo from Orphanet or fallback data
    ↓
gene.py fetches GeneInfo from UniProt or fallback data
    ↓
scoring.py reads GT programs/vectors from SQLite and ranks them
    ↓
cli.py prints a Rich terminal table
    ↓
report.py writes a Markdown report into output/
```

For batch mode, the same process is repeated for several disease IDs, then `cli.py` also writes a combined `SUMMARY.md`.

Important: `cli.py` is the place where the pieces are connected. If one of the helper modules changes its input or output format, `cli.py` may need to change too.

---

## 4. Line-range walkthrough in code order

### Lines 1-10: File description and available commands

The opening docstring and comments explain that this file is the command-line interface.

The file advertises three user commands:

| Command | Meaning |
|---|---|
| `nanogt init` | Create/setup the database and load catalog data |
| `nanogt match ORPHA:xxx` | Score one disease against gene therapy precedents |
| `nanogt batch ORPHA:xxx ORPHA:yyy` | Score multiple diseases and create a summary |

Beginner translation:

```text
This file says: "If the user types this command, run that Python function."
```

---

### Lines 12-19: Standard and display imports

```python
from __future__ import annotations
import pathlib
from typing import Optional
```

These support Python typing and file paths.

- `pathlib` is used for paths such as `output/` or a custom database path.
- `Optional` means a value can be either a real value or `None`.

```python
import typer
from rich.console import Console
from rich.table import Table
from rich import print as rprint
```

These are user-interface libraries.

- `Typer` turns Python functions into terminal commands.
- `Rich` makes terminal output nicer, with colours, status spinners, and tables.
- `Table` makes the ranked results readable.
- `rprint` is imported but not used in this file; that is a small cleanup opportunity.

---

### Lines 21-29: NanoGT internal imports

```python
from .db import setup, get_db_path
from .disease import fetch_disease
from .gene import fetch_gene, GeneInfo
from .scoring import rank_programs
from .report import MatchResult, generate_report, save_report
```

These imports are the pipeline pieces.

| Import | Role in this file |
|---|---|
| `setup` | Opens/creates/seeds the database |
| `get_db_path` | Reports where the default database lives |
| `fetch_disease` | Gets disease metadata from Orphanet/fallbacks |
| `fetch_gene` | Gets gene/protein metadata from UniProt/fallbacks |
| `GeneInfo` | Used to create an empty gene record if no gene is found |
| `rank_programs` | Runs the scoring algorithm |
| `MatchResult` | Bundles disease, gene, and scores for reporting |
| `save_report` | Writes a Markdown report |
| `generate_report` | Imported but not used directly here |

Beginner point: the `.` before module names means “import from the same Python package.”

---

### Lines 31-36: Create the Typer app and Rich console

```python
app = typer.Typer(...)
console = Console()
```

`app` is the object that stores the command definitions.

`console` is the object used to print styled text and tables.

Important settings:

- `name="nanogt"` means the command-line app is called `nanogt`.
- `help="Gene therapy precedent matching for rare diseases."` is the help message.
- `add_completion=False` disables automatic shell completion setup.

Mental model:

```text
app = command registry
console = terminal printer
```

---

### Lines 39-42: `_require_db()` helper

```python
def _require_db():
    return setup()
```

This small helper makes sure the database is ready before running commands that need data.

It calls `setup()` from `db.py`, which:

1. Opens a SQLite connection.
2. Creates database tables if needed.
3. Seeds vectors and GT programs if the relevant tables are empty.

Why it matters:

`match` and `batch` need the catalog data in SQLite before scoring can happen.

Weakness:

`_require_db()` always calls `setup()` with no custom path. If a user wants `match` or `batch` to use a custom database path, this function currently does not expose that option.

---

### Lines 45-59: Command 1, `nanogt init`

The decorator:

```python
@app.command()
```

means “register the next function as a terminal command.”

The function:

```python
def init(db_path: Optional[pathlib.Path] = typer.Option(None, help="Path to SQLite DB")):
```

creates the `nanogt init` command.

Its optional input is:

| Option | Meaning |
|---|---|
| `--db-path` | Let the user choose where the SQLite database should be created |

Inside the function:

1. `conn = setup(db_path)` creates/opens/seeds the database.
2. SQL queries count rows in `gt_programs` and `vectors`.
3. The counts are printed to the terminal.

Database interaction:

```python
SELECT COUNT(*) FROM gt_programs
SELECT COUNT(*) FROM vectors
```

These are simple checks to say how much catalog data is loaded.

Important weakness:

The message prints:

```python
get_db_path()
```

This reports the default or environment-variable database path, not necessarily the custom `db_path` passed to `setup(db_path)`. If a user runs `nanogt init --db-path custom.db`, the printed path may be misleading.

---

### Lines 62-79: Command 2, `nanogt match`

This defines the main single-disease command.

Inputs:

| Argument/option | Example | Meaning |
|---|---|---|
| `disease` | `ORPHA:324` | Required Orphanet disease ID |
| `--top` | `--top 3` | Number of top matches to show; default is 5 |
| `-o` / `output` | `-o results/` | Directory where the Markdown report should be saved |
| `--gene` | `--gene GLA` | Override the gene symbol if automatic disease lookup is incomplete or wrong |

Biomedical meaning:

The disease ID tells NanoGT which rare disease to analyse. The optional gene override is important because disease databases can be incomplete or may list multiple genes.

---

### Lines 80-92: Start `match` and fetch disease information

```python
conn = _require_db()
```

First, the database is made ready.

Then:

```python
disease_info = fetch_disease(disease)
```

fetches disease information. It returns either:

- a `DiseaseInfo` object, or
- `None` if the disease cannot be found.

The `console.status(...)` wrapper shows a loading spinner while the lookup runs.

If no disease is found:

```python
raise typer.Exit(1)
```

This stops the command with error code 1, meaning the command failed.

External API interaction:

`cli.py` does not call Orphanet directly. It delegates that to `disease.py`.

---

### Lines 94-100: Print the disease summary

The code prints:

- disease name and Orphanet ID,
- associated genes,
- affected tissues,
- inheritance pattern.

This gives the user a quick sanity check before seeing scores.

Example conceptually:

```text
Fabry disease (ORPHA:324)
  Genes: GLA
  Tissues: liver, kidney, heart, CNS
  Inheritance: X-linked dominant
```

Why this matters:

If the disease summary looks wrong, the scoring results may also be wrong.

---

### Lines 102-127: Choose and fetch gene information

The code chooses a gene symbol using this priority:

```text
1. Use --gene if the user provided it.
2. Otherwise use the first gene listed in disease_info.gene_symbols.
3. If there is no gene, use a generic unknown gene record.
```

This variable is central:

```python
target_gene_sym
```

It is the gene that will be used for packaging size, protein class, secreted/lysosomal status, and other scoring signals.

If no gene is found, the code creates a blank `GeneInfo` object:

```python
GeneInfo(symbol="unknown", cds_length_bp=None, is_secreted=False, ...)
```

That allows scoring to continue instead of crashing.

If a gene is found, the code calls:

```python
gene_info = fetch_gene(target_gene_sym)
```

External API interaction:

Again, `cli.py` delegates. `gene.py` handles UniProt and fallback data.

Assumption:

If multiple disease genes exist, taking the first one may be too simplistic for genetically heterogeneous diseases.

---

### Lines 129-132: Run the scoring algorithm

```python
scores = rank_programs(disease_info, gene_info, conn)
```

This is the key scientific handoff.

Inputs sent to `scoring.py`:

- disease information,
- gene/protein information,
- database connection.

Output returned:

- a ranked list of `ScoreBreakdown` objects.

Each score contains program name, vector, tissue target, composite score, confidence level, individual dimension scores, and explanatory notes.

Important: `cli.py` does not decide which program is best. `scoring.py` does that.

---

### Lines 134-157: Display top results in a Rich table

The code creates a terminal table with columns:

| Column | Meaning |
|---|---|
| Rank | 1, 2, 3, etc. |
| Program | Gene therapy precedent name |
| Vector | AAV/LV vector used by the precedent |
| Score | Composite score out of 10 |
| Confidence | high/medium/low with emoji |
| Status | approval or trial status |

This line filters out hard failures:

```python
shown = [s for s in scores if s.confidence != "fail"][:top]
```

Meaning:

- Do not show programs where packaging is impossible.
- Keep only the top N requested by the user.

The `emoji` dictionary maps confidence labels to visual symbols:

```python
{"high": "🟢", "medium": "🟡", "low": "🔴", "fail": "⛔"}
```

Beginner point:

```python
for i, s in enumerate(shown, 1):
```

means “loop over the shown scores and number them starting at 1.”

---

### Lines 159-168: Save a Markdown report

The scores are bundled into:

```python
result = MatchResult(disease=disease_info, gene=gene_info, scores=scores, top_n=top)
```

Then the report is saved.

If the user gave `-o some_folder`, it saves there.

If not, it saves to:

```text
./output/
```

This is a file-writing interaction. The actual Markdown generation happens in `report.py`, not here.

Practical implication:

Running `nanogt match` changes the filesystem because it writes a report file.

---

### Lines 171-220: Command 3, `nanogt batch`

`batch` runs the matching workflow for multiple diseases.

Inputs:

| Argument/option | Meaning |
|---|---|
| `diseases` | One or more Orphanet IDs |
| `-o output` | Output directory; default `output/` |
| `--top` | Number of top matches per disease; default 3 |

Flow inside the loop:

1. Print which disease is being processed.
2. Fetch disease information.
3. Skip if disease is not found.
4. Choose the first gene if available.
5. Fetch gene information, or create an unknown `GeneInfo`.
6. Rank programs.
7. Create a `MatchResult`.
8. Save an individual disease report.
9. Add the result to a `results` list.

Important difference from `match`:

`batch` does not support `--gene` overrides for each disease. It always uses the first gene from the disease record when a gene exists.

---

### Lines 223-262: `_write_summary()` helper

This function creates a combined batch summary report.

Inputs:

| Input | Meaning |
|---|---|
| `results` | All successful `MatchResult` objects from the batch run |
| `output_dir` | Where `SUMMARY.md` should be written |
| `top` | How many matches to list per disease |

It builds a list of Markdown lines:

```python
lines = [
    "# NanoGT Batch Summary",
    ...
]
```

Then it adds:

1. An overview table with one top match per disease.
2. A section for each disease listing top matches.

This line finds the first non-failing top match:

```python
top_match = next((s for s in r.scores if s.confidence != "fail"), None)
```

Then it writes:

```python
(output_dir / "SUMMARY.md").write_text("\n".join(lines))
```

File interaction:

This creates or overwrites `SUMMARY.md` in the output directory.

---

### Lines 265-266: Direct execution entry point

```python
if __name__ == "__main__":
    app()
```

This means:

```text
If someone runs cli.py directly as a script, start the Typer app.
```

In installed command-line usage, the project may call `app` through package entry points instead. This block is still useful for direct execution during development.

---

## 5. Important variables and objects

| Name | What it is | Why it matters |
|---|---|---|
| `app` | Typer app | Registers terminal commands |
| `console` | Rich console | Prints styled terminal output |
| `db_path` | Optional database path | Lets init use a non-default SQLite file |
| `disease` | Orphanet ID string | Main user query |
| `top` | Number of matches to show | Controls result length |
| `output` | Output directory | Controls where reports are saved |
| `gene_symbol` | Optional gene override | Fixes/overrides automatic disease gene selection |
| `conn` | SQLite connection | Lets scoring read vector/program data |
| `disease_info` | `DiseaseInfo` object | Disease metadata used in scoring |
| `target_gene_sym` | Chosen gene symbol | Determines which gene gets fetched/scored |
| `gene_info` | `GeneInfo` object | Protein/gene metadata used in scoring |
| `scores` | List of `ScoreBreakdown` | Ranked GT precedents |
| `shown` | Filtered top scores | What appears in terminal table |
| `result` | `MatchResult` | Bundle passed to report writer |
| `results` | List of batch results | Used to write `SUMMARY.md` |
| `lines` | Markdown line list | Used when building batch summary |

---

## 6. Database, API, and file interactions

### Database

`cli.py` calls `setup()` through `_require_db()` or directly in `init()`.

That reaches `db.py`, which creates and seeds SQLite tables.

The CLI itself performs only simple count queries in `init()`.

### APIs

`cli.py` does not directly call Orphanet or UniProt.

Instead:

```text
cli.py → disease.py → Orphanet/fallback
cli.py → gene.py → UniProt/fallback
```

### Filesystem

`cli.py` writes output indirectly through `save_report()` and directly through `_write_summary()`.

Expected output files include:

```text
output/match_*.md
output/SUMMARY.md
```

---

## 7. Assumptions, weaknesses, and improvement ideas

### 7.1 First disease gene is assumed to be the main gene

In both `match` and `batch`, if no override is given, the first gene is selected.

Weakness:

Some rare diseases are genetically heterogeneous. The first listed gene may not be the patient's actual gene.

Improvement:

Require or strongly encourage `--gene` when multiple genes are present, or show a menu/list.

---

### 7.2 Batch mode has no per-disease gene override

`match` supports `--gene`, but `batch` does not.

Weakness:

For a batch of diseases with multiple possible genes, the analysis may silently use the first listed gene.

Improvement:

Allow a CSV input with columns such as:

```text
orphanet_id,gene_symbol
ORPHA:1946,ROGDI
ORPHA:324,GLA
```

---

### 7.3 Custom database path support is incomplete

`init` accepts a `db_path`, but `match` and `batch` use `_require_db()` with no path.

Weakness:

A user may initialise one database but later match against another/default database.

Improvement:

Add a shared `--db-path` option to `match` and `batch`, or rely consistently on the `NANOGT_DB` environment variable.

---

### 7.4 Printed database path may be misleading

`init(db_path=...)` calls `setup(db_path)`, but prints `get_db_path()`.

Weakness:

If a custom path was passed, the success message may not show the actual path used.

Improvement:

Have `setup()` or `get_conn()` return/store the actual resolved path, then print that.

---

### 7.5 Some imported names are unused

`rprint` and `generate_report` are imported but not used.

Weakness:

Unused imports add noise for beginners and can suggest missing logic.

Improvement:

Remove unused imports unless they are about to be used.

---

### 7.6 Error handling is basic

If disease lookup fails, the command exits. But if report writing fails or the output directory is not writable, the error will likely be a raw Python exception.

Improvement:

Catch common filesystem/API/database errors and print beginner-friendly messages.

---

### 7.7 Reports are saved automatically

`match` always saves a report, even if the user only wanted terminal output.

Weakness:

This creates files as a side effect.

Improvement:

Add options such as:

```bash
--no-save
--save
```

or make saving explicit.

---

## 8. Things to memorise

1. `cli.py` is the user-facing command layer.
2. `Typer` turns functions into terminal commands.
3. `Rich` makes terminal output readable.
4. `init` sets up and seeds the database.
5. `match` runs one disease through the full pipeline.
6. `batch` repeats matching for multiple diseases.
7. `cli.py` delegates scientific work to `disease.py`, `gene.py`, `scoring.py`, and `report.py`.
8. The key handoff to the algorithm is `rank_programs(disease_info, gene_info, conn)`.
9. The key report object is `MatchResult`.
10. The file is mostly orchestration, not biomedical scoring.

---

## 9. Mini mental model

Say this from memory:

```text
cli.py is NanoGT's command-line front door. It defines init, match, and batch commands. It makes sure the database exists, fetches disease and gene information, sends those objects to the scoring engine, prints a ranked table, and saves Markdown reports. It coordinates the workflow but does not contain the main scoring algorithm itself.
```

Even shorter:

```text
User command → cli.py → database + disease + gene → scoring → table + report
```

---

## 10. Active recall questions

Use these without looking at the code.

1. What is the job of `cli.py`?
2. What are the three commands defined in this file?
3. What does `@app.command()` do?
4. What is `Typer` used for?
5. What is `Rich` used for?
6. What does `_require_db()` do?
7. Which function sets up and seeds the database?
8. What user input is required for `nanogt match`?
9. What does the `--top` option control?
10. What does the `--gene` option control?
11. What happens if no disease is found?
12. How does the code choose a gene if `--gene` is not given?
13. Why can choosing the first gene be scientifically risky?
14. Which function runs the scoring algorithm?
15. What kind of object does `MatchResult` bundle together?
16. How are hard-fail scores filtered out of the terminal table?
17. Where does `match` save reports by default?
18. What extra file does `batch` create?
19. Which imports appear unused in this file?
20. How would you explain `cli.py` to a non-coder biomedical researcher?
