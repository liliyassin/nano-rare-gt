# Code Study Note: `src/nanogt/db.py`

File studied: `/Users/suzie/Projects/nano-rare-gt/src/nanogt/db.py`

Related files:
- `src/nanogt/catalog.py`
- `src/nanogt/schema.sql`
- `src/nanogt/cli.py`
- `src/nanogt/scoring.py`

Study goal:
Understand how `db.py` creates the SQLite database, loads the curated vector and gene therapy program catalog into tables, and provides a ready database connection for the rest of NanoGT.

---

## 1. Plain-English identity

`db.py` is NanoGT's database setup and seeding layer.

It is responsible for making sure there is a usable SQLite database before scoring happens.

It does three main jobs:

1. Decide where the database file should live.
2. Open a SQLite connection with useful settings.
3. Create tables and load starter data from `catalog.py`.

The easiest mental model:

```text
db.py = the database builder and catalog loader
```

Or:

```text
catalog.py data → db.py → SQLite tables → scoring.py reads rows
```

---

## 2. Why this file exists

NanoGT needs structured data that can be queried repeatedly.

The project has curated data in `catalog.py`:

- `VECTORS`: delivery vehicle properties.
- `GT_PROGRAMS`: gene therapy precedent programs.

But the scoring engine works from database rows. `db.py` bridges that gap by inserting the curated Python lists into SQLite tables.

Without `db.py`, the project would not have a consistent way to:

- create the database file,
- create required tables,
- turn Python catalog dictionaries into SQL rows,
- enable foreign key checks,
- reuse the same database between commands.

---

## 3. How this file fits into the project data flow

The database flow is:

```text
catalog.py defines VECTORS and GT_PROGRAMS
    ↓
db.py imports those lists
    ↓
db.py opens/creates SQLite database
    ↓
db.py runs schema.sql to create core tables
    ↓
db.py creates gt_programs table
    ↓
db.py seeds vectors and gt_programs if empty
    ↓
cli.py and scoring.py use the ready connection
```

For a normal `nanogt match` command:

```text
cli.py calls setup()
    ↓
setup() calls get_conn()
    ↓
setup() calls init_db()
    ↓
setup() calls seed_db()
    ↓
setup() returns conn
    ↓
scoring.py uses conn to read vectors/programs
```

---

## 4. Line-range walkthrough in code order

### Line 1: File docstring

```python
"""Database layer for nanogt — SQLite with WAL mode."""
```

This says the file controls database access.

SQLite is a lightweight database stored in a file. WAL mode means “write-ahead logging,” a SQLite feature that usually improves reliability and allows better concurrent reading/writing.

---

### Lines 2-5: Standard library imports

```python
import json
import os
import pathlib
import sqlite3
```

| Import | Why it is used |
|---|---|
| `json` | Converts Python lists like tissue tropism into JSON strings for SQLite |
| `os` | Reads environment variables such as `NANOGT_DB` |
| `pathlib` | Handles file paths cleanly |
| `sqlite3` | Built-in Python library for SQLite databases |

Beginner point:

SQLite does not have a native Python list type, so lists often get stored as JSON text.

---

### Line 7: Import curated catalog data

```python
from .catalog import VECTORS, GT_PROGRAMS
```

This imports the static curated data.

- `VECTORS` becomes rows in the `vectors` table.
- `GT_PROGRAMS` becomes rows in the `gt_programs` table.

This line is the key connection between biomedical curation and database storage.

---

### Lines 9-10: Important path constants

```python
DEFAULT_DB = pathlib.Path.home() / ".nanogt" / "nanogt.db"
SCHEMA_SQL = pathlib.Path(__file__).parent / "schema.sql"
```

`DEFAULT_DB` is the default database file path.

On this machine, because the user home is `/Users/suzie`, the default path would be conceptually:

```text
/Users/suzie/.nanogt/nanogt.db
```

`SCHEMA_SQL` points to:

```text
/Users/suzie/Projects/nano-rare-gt/src/nanogt/schema.sql
```

That SQL file creates several core tables such as diseases, genes, proteins, vectors, and matches.

Important distinction:

- `schema.sql` creates the `vectors` table.
- `db.py` itself creates the `gt_programs` table.

That split is functional, but slightly inconsistent.

---

### Lines 13-14: `get_db_path()`

```python
def get_db_path() -> pathlib.Path:
    return pathlib.Path(os.environ.get("NANOGT_DB", DEFAULT_DB))
```

This function decides which database file path to use.

Priority:

```text
1. If environment variable NANOGT_DB exists, use it.
2. Otherwise use DEFAULT_DB.
```

Example:

```bash
NANOGT_DB=/tmp/test_nanogt.db nanogt match ORPHA:324
```

would make `get_db_path()` point to `/tmp/test_nanogt.db`.

Assumption:

The environment variable value is a valid path.

---

### Lines 17-24: `get_conn(db_path=None)`

This function opens a database connection.

Step by step:

```python
path = db_path or get_db_path()
```

If a custom path is passed, use it. Otherwise use `get_db_path()`.

```python
path.parent.mkdir(parents=True, exist_ok=True)
```

Create the parent folder if it does not exist. For the default database, this creates:

```text
~/.nanogt/
```

```python
conn = sqlite3.connect(path)
```

Open the SQLite database file. If it does not exist, SQLite creates it.

```python
conn.row_factory = sqlite3.Row
```

This makes query results easier to use. Instead of only tuple-like access, rows can be accessed by column name.

```python
conn.execute("PRAGMA journal_mode=WAL")
conn.execute("PRAGMA foreign_keys=ON")
```

These configure SQLite:

| PRAGMA | Meaning |
|---|---|
| `journal_mode=WAL` | Use write-ahead logging for safer/better database writes |
| `foreign_keys=ON` | Enforce relationships between tables when foreign keys exist |

Then the connection is returned.

Database interaction:

This function creates/opens a real `.db` file on disk.

---

### Lines 27-49: `init_db(conn)`

This function creates database tables.

First:

```python
conn.executescript(SCHEMA_SQL.read_text())
```

This reads `schema.sql` and runs all SQL statements inside it.

Those statements create tables such as:

- `diseases`
- `genes`
- `proteins`
- `disease_genes`
- `vectors`
- `matches`
- `diseases_fts`

Then this file adds another table:

```python
CREATE TABLE IF NOT EXISTS gt_programs (...)
```

The `gt_programs` table stores the clinical precedent programs from `catalog.py`.

Columns:

| Column | Meaning |
|---|---|
| `id` | Internal numeric ID |
| `name` | Program/product name; unique |
| `disease` | Precedent disease |
| `gene_symbol` | Gene used in precedent |
| `vector` | Vector name such as AAV9 or LV |
| `tissue_target` | Tissue/cell target |
| `cds_bp` | Coding sequence size in base pairs |
| `approval_status` | Approved, phase1/2, phase2, withdrawn, etc. |
| `approval_year` | Approval year, if known |
| `mechanism` | Therapy mechanism, currently gene replacement/addition style |
| `protein_class` | Intracellular, secreted, lysosomal, membrane, etc. |
| `inheritance` | AR, XL, mitochondrial, etc. |
| `pathway` | Biological pathway label |
| `notes` | Optional extra notes |

Finally:

```python
conn.commit()
```

saves the table creation changes.

Important design note:

The table is created with `IF NOT EXISTS`, so running setup repeatedly should not recreate or delete existing tables.

---

### Lines 51-71: Seed the `vectors` table

`seed_db(conn)` starts by checking whether `vectors` is empty:

```python
if conn.execute("SELECT COUNT(*) FROM vectors").fetchone()[0] == 0:
```

If the table has zero rows, it loops through `VECTORS` and inserts each vector.

The SQL insert columns are:

```text
serotype
cargo_limit_bp
tissue_tropism
cns_tropic
retinal_tropic
hepatic_tropic
muscle_tropic
clinical_precedents
freely_available
```

Important data conversion:

```python
json.dumps(v.get("tissue_tropism", []))
```

`tissue_tropism` starts as a Python list, for example:

```python
["CNS", "muscle", "liver", "heart"]
```

SQLite stores it as JSON text, for example:

```text
["CNS", "muscle", "liver", "heart"]
```

The `.get(..., default)` pattern protects against missing optional keys:

| Code | Meaning |
|---|---|
| `v.get("cns_tropic", 0)` | Use 0 if missing |
| `v.get("clinical_precedents", 0)` | Use 0 if missing |
| `v.get("freely_available", 1)` | Assume available if missing |

Then `conn.commit()` saves inserted vector rows.

Assumption:

The `vectors` table already exists because `schema.sql` created it.

---

### Lines 73-88: Seed the `gt_programs` table

Next, `seed_db(conn)` checks whether `gt_programs` is empty:

```python
if conn.execute("SELECT COUNT(*) FROM gt_programs").fetchone()[0] == 0:
```

If empty, it loops through `GT_PROGRAMS` and inserts each program.

The required fields use direct dictionary indexing:

```python
p["name"]
p["disease"]
p["gene_symbol"]
```

This means those keys must exist, or Python will raise an error.

Optional fields use `.get()`:

```python
p.get("approval_year")
p.get("notes")
```

This allows approval year or notes to be missing/`None`.

`INSERT OR IGNORE` means if a duplicate unique value appears, SQLite skips it instead of crashing.

Finally, `conn.commit()` saves inserted program rows.

Important limitation:

This seeding only happens when the whole table is empty. If the table already has rows, new or changed catalog entries will not be loaded automatically.

---

### Lines 91-96: `setup(db_path=None)`

```python
def setup(db_path=None) -> sqlite3.Connection:
    conn = get_conn(db_path)
    init_db(conn)
    seed_db(conn)
    return conn
```

This is the convenience function used by the CLI.

It packages the full setup process into one call:

```text
connect → create tables → seed starter data → return connection
```

This is why `cli.py` can simply call:

```python
setup()
```

instead of manually doing every database step.

---

## 5. Important variables and objects

| Name | What it is | Why it matters |
|---|---|---|
| `DEFAULT_DB` | Default SQLite file path | Controls where the app stores persistent data |
| `SCHEMA_SQL` | Path to schema file | Defines core database tables |
| `VECTORS` | List imported from `catalog.py` | Seed data for delivery vector table |
| `GT_PROGRAMS` | List imported from `catalog.py` | Seed data for precedent program table |
| `conn` | SQLite connection | Used to execute SQL |
| `path` | Actual database path | File that SQLite opens/creates |
| `json.dumps(...)` | Python-to-JSON converter | Allows lists to be stored as text |

---

## 6. Database interactions in plain English

`db.py` creates and populates two especially important tables for scoring:

### `vectors`

Created by `schema.sql`, seeded by `db.py`.

Stores vector properties:

```text
AAV9 → cargo limit, tissue tropism, CNS/liver/muscle flags, clinical precedents
```

### `gt_programs`

Created by `db.py`, seeded by `db.py`.

Stores clinical precedent programs:

```text
Zolgensma → SMA, SMN1, AAV9, CNS/motor neuron, approved, etc.
```

The scoring engine later combines these.

A simplified scoring query conceptually needs:

```text
For each GT program:
    get its vector
    get vector cargo/tropism
    compare to query disease/gene
```

---

## 7. Assumptions, weaknesses, and improvement ideas

### 7.1 Seeding only happens if tables are empty

This is the most important gotcha.

If `vectors` already has rows, `VECTORS` will not be reloaded.
If `gt_programs` already has rows, `GT_PROGRAMS` will not be reloaded.

Weakness:

Editing `catalog.py` may not change the existing database.

Improvement:

Add an explicit reseed command, for example:

```bash
nanogt reseed-catalog
```

or:

```bash
nanogt init --force-reseed
```

---

### 7.2 `gt_programs` table is not in `schema.sql`

Most tables are created in `schema.sql`, but `gt_programs` is created in Python.

Weakness:

The schema is split across two files, which can confuse maintenance.

Improvement:

Move `gt_programs` table creation into `schema.sql`, or clearly document why it is separate.

---

### 7.3 No database migrations

The code uses `CREATE TABLE IF NOT EXISTS`, but there is no formal migration system.

Weakness:

If columns change later, existing databases may not update correctly.

Improvement:

Add migration tooling or a simple `schema_version` table.

---

### 7.4 Limited validation before insert

The code assumes each catalog dictionary has the right keys and types.

Weakness:

A typo such as `gene_symbl` instead of `gene_symbol` would fail at runtime.

Improvement:

Validate catalog entries before insertion with dataclasses, Pydantic, or explicit tests.

---

### 7.5 Vector/program relationship is stored as text

`gt_programs.vector` stores a text value like `AAV9`.

Weakness:

The database does not enforce that every program vector exists in the `vectors` table.

Improvement:

Use a foreign key from `gt_programs.vector` to `vectors.serotype`, or validate this in tests.

---

### 7.6 `INSERT OR IGNORE` can hide problems

`INSERT OR IGNORE` prevents duplicate crashes.

Strength:

Repeated setup is less likely to fail.

Weakness:

If duplicate names or conflicting data appear, the issue can be silently ignored.

Improvement:

Log skipped rows, or use explicit upsert logic with checks.

---

### 7.7 Database connection is returned but not closed here

`setup()` returns a connection and leaves it to the caller to manage.

Weakness:

Long-running or repeated code should close connections when finished.

Improvement:

Use context managers or clear CLI-level connection closing.

---

### 7.8 Default missing value assumptions may be too optimistic

Example:

```python
v.get("freely_available", 1)
```

If availability is missing, the code assumes the vector is freely available.

Weakness:

For translational gene therapy, intellectual property and licensing assumptions should be cautious.

Improvement:

Require every vector to explicitly state availability, source, and confidence.

---

## 8. Things to memorise

1. `db.py` connects Python catalog data to SQLite.
2. `DEFAULT_DB` points to `~/.nanogt/nanogt.db` unless `NANOGT_DB` overrides it.
3. `get_conn()` opens SQLite, creates the parent folder, enables WAL, and enables foreign keys.
4. `init_db()` runs `schema.sql` and creates `gt_programs`.
5. `seed_db()` inserts vectors and GT programs only if their tables are empty.
6. `json.dumps()` stores Python lists as JSON text in SQLite.
7. `setup()` is the one-call database setup function used by the CLI.
8. Editing `catalog.py` does not automatically update an already seeded database.
9. The database design is simple and useful for a prototype, but needs migrations/validation for research-grade use.

---

## 9. Mini mental model

Say this from memory:

```text
db.py opens the NanoGT SQLite database, creates tables, and loads the curated vector and gene therapy program catalog into those tables. cli.py calls setup(), and scoring.py later reads the seeded rows. The main gotcha is that catalog data is only seeded when the tables are empty, so editing catalog.py does not automatically update an existing database.
```

Even shorter:

```text
catalog.py → db.py seeds SQLite → scoring.py reads SQLite
```

---

## 10. Active recall questions

Use these without looking at the code.

1. What is the job of `db.py`?
2. What is SQLite?
3. What is `DEFAULT_DB`?
4. What environment variable can override the default database path?
5. What does `SCHEMA_SQL` point to?
6. Which catalog variables does `db.py` import?
7. What does `get_db_path()` return?
8. What does `get_conn()` do?
9. Why does the code create `path.parent`?
10. What does `conn.row_factory = sqlite3.Row` help with?
11. What does `PRAGMA journal_mode=WAL` mean at a high level?
12. What does `PRAGMA foreign_keys=ON` do?
13. What does `init_db()` create?
14. Which table is created in Python instead of `schema.sql`?
15. What does `seed_db()` insert into `vectors`?
16. Why is `json.dumps()` used for `tissue_tropism`?
17. What does `seed_db()` insert into `gt_programs`?
18. Why might editing `catalog.py` not update results?
19. What is risky about `INSERT OR IGNORE`?
20. How would you make this database layer more research-grade?
