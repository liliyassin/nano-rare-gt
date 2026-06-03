# Code Study Note: `src/nanogt/disease.py`

File studied: `/Users/suzie/Projects/nano-rare-gt/src/nanogt/disease.py`

Related files:
- `src/nanogt/cli.py`
- `src/nanogt/gene.py`
- `src/nanogt/scoring.py`
- `src/nanogt/db.py`
- `src/nanogt/report.py`

Study goal:
Understand how NanoGT turns an Orphanet disease ID into a small, usable disease record for gene therapy precedent scoring.

---

## 1. Plain-English identity

`disease.py` is NanoGT's disease lookup file.

If the user gives NanoGT an Orphanet ID such as `ORPHA:1946`, this file tries to answer:

```text
What disease is this?
Which genes are associated with it?
How is it inherited?
What tissues seem affected?
What fallback information do we have if the internet/API fails?
```

It is not the scoring algorithm. It does not rank gene therapy programs.

Instead, it prepares one important input for the scoring algorithm: a structured `DiseaseInfo` object.

Easiest mental model:

```text
disease.py = disease ID in → disease facts out
```

---

## 2. Why this file exists

NanoGT starts from a disease query.

The command-line flow is roughly:

```text
User types: nanogt match ORPHA:1946
        ↓
cli.py calls fetch_disease("ORPHA:1946")
        ↓
disease.py returns a DiseaseInfo object
        ↓
cli.py chooses a gene from disease_info.gene_symbols
        ↓
gene.py fetches protein/gene details
        ↓
scoring.py ranks gene therapy precedent programs
        ↓
report.py writes a Markdown report
```

Without `disease.py`, NanoGT would not know what the disease query means.

For example, for Kohlschutter-Tonz syndrome, the fallback says:

```text
Orphanet ID: ORPHA:1946
Disease name: Kohlschutter-Tonz syndrome
Gene: ROGDI
Inheritance: Autosomal recessive
Affected tissue used by scoring: CNS
```

That information directly affects the score. If `affected_tissues` says `CNS`, then CNS-directed vectors and programs become more relevant.

---

## 3. What this file outputs

The central output is a `DiseaseInfo` dataclass.

A dataclass is a simple Python container with named fields.

Here, one `DiseaseInfo` object stores:

| Field | Meaning | Why NanoGT needs it |
|---|---|---|
| `orphanet_id` | Disease identifier such as `ORPHA:1946` | Keeps the query traceable |
| `name` | Human-readable disease name | Used in terminal output and reports |
| `omim_ids` | OMIM cross-references | Useful disease database links |
| `prevalence` | Rarity category | Descriptive metadata |
| `inheritance` | Inheritance pattern list | Used by inheritance scoring |
| `gene_symbols` | Associated genes | Used to choose which gene to fetch from `gene.py` |
| `hpo_terms` | Phenotype/symptom terms | Used for tissue/pathway inference |
| `affected_tissues` | Simplified tissue labels | Used by tropism, immune privilege, promoter, and route scoring |

Important beginner point:

```text
HPO terms are clinical phenotype words.
Affected tissues are simplified labels derived from those words or manually curated in fallback data.
```

Example:

```text
"Early-onset epilepsy" and "Intellectual disability" → CNS
"Jaundice" and "Hepatic dysfunction" → liver
"Retinal degeneration" → retina
```

---

## 4. How it fits into project data flow

### Main active flow

```text
cli.py
  calls fetch_disease(orpha_id)
        ↓
disease.py
  checks in-memory cache
  tries Orphanet API
  uses fallback if API fails
        ↓
returns DiseaseInfo
        ↓
cli.py
  prints disease summary
  picks first gene symbol unless user overrides with --gene
        ↓
gene.py
  fetches GeneInfo
        ↓
scoring.py
  uses DiseaseInfo + GeneInfo + database catalog
```

### Optional database flow

At the bottom, `cache_disease_to_db(conn, info)` can save a `DiseaseInfo` object into the SQLite `diseases` table.

However, in the currently read CLI flow, `fetch_disease()` is used directly and `cache_disease_to_db()` is not called from `cli.py`.

So practically:

```text
Disease lookup is active.
Disease database caching function exists.
But persistent disease caching is not currently wired into the main CLI path.
```

---

## 5. Line-range walkthrough in code order

### Lines 1-10: File identity comments

The file starts by saying it is an Orphanet disease client.

The comments explain the two-tier approach:

1. Try the live Orphanet API.
2. If that fails, use hardcoded fallback data.

This is important because biomedical APIs can fail, change, or be unavailable during demos. The fallback keeps NanoGT usable offline for the project diseases.

---

### Lines 12-16: Imports

```python
import json
import time
from dataclasses import dataclass, field
from typing import Optional
import requests
```

What each import is for:

| Import | Beginner meaning | Used for |
|---|---|---|
| `json` | Converts between Python data and JSON text | Top-level import appears unused; local `_json` is used later instead |
| `time` | Timing utilities | `time.sleep(0.2)` between API requests |
| `dataclass` | Makes simple data containers | Defines `DiseaseInfo` |
| `field` | Extra dataclass field configuration | Imported but not used in this file |
| `Optional` | Type hint meaning “value or None” | Functions that may return no disease |
| `requests` | HTTP client library | Calls Orphanet API |

Small cleanup note:

```text
json and field are imported at the top but are not needed in the current code.
```

---

### Lines 18-23: API constants, cache, and HTTP session

```python
ORPHANET_BASE = "https://api.orphacode.org/EN/ClinicalEntity"
ORPHADATA_BASE = "https://www.orphadata.com/cgi-bin/ORPHAnomenclature.php"
_CACHE: dict = {}
_SESSION = requests.Session()
_SESSION.headers["accept"] = "application/json"
```

Plain-English meaning:

- `ORPHANET_BASE` is the main API address.
- `ORPHADATA_BASE` is listed as a backup address, but it is not actually used.
- `_CACHE` remembers disease lookups during one program run.
- `_SESSION` reuses the same web connection settings for multiple requests.
- The `accept: application/json` header asks the API to return JSON.

Important cache detail:

```text
This cache is memory-only.
It helps within one run of NanoGT.
It does not persist after the program exits.
```

---

### Lines 26-37: `DiseaseInfo` dataclass

```python
@dataclass
class DiseaseInfo:
    orphanet_id: str
    name: str
    omim_ids: list[str]
    prevalence: Optional[str]
    inheritance: list[str]
    gene_symbols: list[str]
    hpo_terms: list[str]
    affected_tissues: list[str]
```

This class defines the shape of disease information used by the rest of NanoGT.

It is like a labelled form:

```text
DiseaseInfo form
- disease ID
- disease name
- OMIM IDs
- prevalence
- inheritance
- genes
- HPO symptoms
- affected tissues
```

The rest of the project can then write clear code like:

```python
disease.name
disease.gene_symbols
disease.affected_tissues
```

instead of juggling raw API dictionaries.

---

### Lines 39-42: `_orpha_num()` helper

```python
def _orpha_num(orpha_id: str) -> str:
    return orpha_id.replace("ORPHA:", "").strip()
```

This helper normalizes Orphanet IDs.

It accepts either:

```text
ORPHA:1946
```

or:

```text
1946
```

and returns:

```text
1946
```

Why this matters:

The API URL needs only the number, but humans often type the full `ORPHA:` prefix.

Weakness:

It only removes uppercase `ORPHA:`. It does not handle lowercase `orpha:1946` unless the user types the expected format.

---

### Lines 45-67: `_tissues_from_hpo()` helper

This function turns HPO term names into broad tissue labels.

It uses keyword matching.

Example logic:

```text
If an HPO term contains "hepat" or "liver" → add "liver"
If it contains "brain", "seizure", or "intellectual" → add "CNS"
If it contains "retina" or "visual" → add "retina"
```

The tissue labels it can produce are:

```text
liver
CNS
muscle
retina
hematopoietic
heart
kidney
```

Why this matters:

`scoring.py` uses disease tissues to ask:

```text
Does the precedent vector reach the disease's affected tissue?
```

Important weakness:

This is deliberately crude text matching. It is not a formal ontology mapping.

For a beginner biomedical researcher:

```text
The code is not “understanding” HPO biologically.
It is scanning phenotype words for tissue-related substrings.
```

This can work for obvious terms, but it can miss subtle biology or overcall tissue involvement.

---

### Lines 70-79: `fetch_disease()` public function

This is the main function other files call.

```python
def fetch_disease(orpha_id: str) -> Optional[DiseaseInfo]:
```

Flow:

1. Convert `ORPHA:1946` to `1946`.
2. Build a cache key like `disease:1946`.
3. If the disease is already in `_CACHE`, return it immediately.
4. Otherwise call `_fetch_from_orphanet(num)`.
5. Store the result in `_CACHE`.
6. Return the result.

Key idea:

```text
fetch_disease() is the safe front door.
It hides caching and API/fallback details from the rest of the project.
```

Return type:

- It returns a `DiseaseInfo` object if found.
- It can return `None` if the API fails and there is no fallback for that Orphanet number.

---

### Lines 82-136: `_fetch_from_orphanet()` live API logic

This function tries to get disease information from the Orphanet API.

It is inside a `try` block so that any network/API error can fall back safely.

#### Lines 85-91: Request 1, basic disease info

```python
_SESSION.get(f"{ORPHANET_BASE}/orphacode/{orpha_num}", timeout=10)
```

This asks Orphanet for basic information about the disease.

If the response status is not `200`, the code immediately uses fallback data.

`200` means the HTTP request succeeded.

The disease name is pulled from:

```python
data.get("Preferred term", f"ORPHA:{orpha_num}")
```

If no preferred term is available, it uses the ID as the name.

#### Lines 93-103: Request 2, gene associations

The code pauses for 0.2 seconds, then requests:

```text
/orphacode/{number}/Gene
```

It looks inside `Genes` and collects gene symbols from either:

```text
Gene symbol
Symbol
```

This list becomes `DiseaseInfo.gene_symbols`.

Why it matters:

`cli.py` usually picks the first gene symbol and passes it to `gene.py`.

#### Lines 104-113: Request 3, inheritance

The code pauses again, then requests:

```text
/orphacode/{number}/inheritance
```

It collects inheritance labels such as `Autosomal recessive`.

Why it matters:

`scoring.py` gives better inheritance scores when the query disease and precedent program are both compatible with gene replacement.

#### Lines 115-119: OMIM references

The code loops through `data.get("References", [])` and keeps references where:

```python
xref.get("Source") == "OMIM"
```

These become `DiseaseInfo.omim_ids`.

#### Lines 121-132: Build `DiseaseInfo`

The code creates a final `DiseaseInfo` object.

Important detail:

```python
hpo_terms: list[str] = []
affected_tissues=_tissues_from_hpo(hpo_terms)
```

The live Orphanet endpoint used here does not return HPO terms, so live API results may have empty HPO and empty affected tissue fields.

This is a major practical point:

```text
The fallback data may actually be richer for scoring than the live API result,
because the fallback includes manually curated HPO terms and affected tissues.
```

#### Lines 135-136: Error fallback

If anything goes wrong, the code returns:

```python
_fallback_disease(orpha_num)
```

Examples of errors:

- No internet.
- API timeout.
- API JSON format changes.
- Server error.
- Unexpected missing fields.

---

### Lines 139-144: Static fallback section starts

This section announces hardcoded fallback disease data.

The fallback exists so NanoGT still works without internet.

It also gives the project control over key fields such as `affected_tissues`, which strongly influence scoring.

---

### Lines 147-277: `_build_fallbacks()` disease dictionary

`_build_fallbacks()` fills the `_FALLBACK` dictionary.

The dictionary maps Orphanet numbers to `DiseaseInfo` objects.

Example structure:

```python
"1946": DiseaseInfo(
    orphanet_id="ORPHA:1946",
    name="Kohlschutter-Tonz syndrome",
    gene_symbols=["ROGDI"],
    affected_tissues=["CNS"],
)
```

Diseases included include:

| Orphanet number | Disease | Main gene(s) | Main tissue label(s) in fallback |
|---|---|---|---|
| `70` | Spinal Muscular Atrophy | `SMN1`, `SMN2` | CNS, muscle |
| `306` | Hemophilia B | `F9` | liver |
| `324` | Fabry disease | `GLA` | liver, kidney, heart, CNS |
| `79269` | Sanfilippo A | `SGSH` | CNS |
| `1060` | Crigler-Najjar syndrome type I | `UGT1A1` | liver |
| `1946` | Kohlschutter-Tonz syndrome | `ROGDI` | CNS |
| `578` | Mucolipidosis type IV | `MCOLN1` | CNS, retina |
| `61` | Alpha-mannosidosis | `MAN2B1` | CNS, liver |
| `511` | Maple syrup urine disease | `BCKDHA` | liver, CNS |
| `309` | Salla disease | `SLC17A5` | CNS |

The comments label some as positive controls, novel results, or no-trial target diseases.

Why fallback data matters so much:

```text
When the API fails, these hardcoded entries define the disease biology that the scorer sees.
```

If the fallback tissue labels are wrong, scoring will be wrong.

---

### Line 280: `_build_fallbacks()` runs at import time

```python
_build_fallbacks()
```

This line runs as soon as Python imports `disease.py`.

Meaning:

```text
The fallback dictionary is ready before fetch_disease() is called.
```

This is convenient, but it also means importing the module has a small side effect: it populates global state.

---

### Lines 283-284: `_fallback_disease()`

```python
def _fallback_disease(orpha_num: str) -> Optional[DiseaseInfo]:
    return _FALLBACK.get(orpha_num)
```

This is a simple dictionary lookup.

If the Orphanet number is in `_FALLBACK`, it returns the corresponding `DiseaseInfo`.

If not, it returns `None`.

---

### Lines 287-303: `cache_disease_to_db()`

This function saves a disease record into the SQLite database.

It writes into the `diseases` table:

| Database column | Source from `DiseaseInfo` |
|---|---|
| `orphanet_id` | `info.orphanet_id` |
| `name` | `info.name` |
| `omim_id` | first item in `info.omim_ids`, if present |
| `prevalence` | `info.prevalence` |
| `inheritance` | first item in `info.inheritance`, if present |
| `phenotype_terms` | JSON string version of `info.hpo_terms` |

Important details:

- It uses `INSERT OR REPLACE`, so an existing disease row can be overwritten.
- It stores only the first OMIM ID.
- It stores only the first inheritance value.
- It stores HPO terms as a JSON string.
- It does not store `gene_symbols` or `affected_tissues` in this insert.

Weakness:

The fields most important to scoring, especially `affected_tissues`, are not persisted here.

---

## 6. API, fallback, and cache logic in one view

```text
fetch_disease("ORPHA:1946")
        ↓
normalize to "1946"
        ↓
check _CACHE["disease:1946"]
        ↓
if cached: return cached DiseaseInfo
        ↓
if not cached: call Orphanet API
        ↓
if API succeeds: parse API into DiseaseInfo
        ↓
if API fails: use _FALLBACK["1946"]
        ↓
store result in _CACHE
        ↓
return DiseaseInfo or None
```

The fallback is not only a backup. It is also a curated project dataset.

---

## 7. Assumptions and weaknesses

### 7.1 Live API results may lack HPO/tissue information

The code says the Orphanet endpoint does not return HPO terms here.

Consequence:

```text
Live API success can produce empty affected_tissues.
Fallback data can produce better scoring because it has curated tissues.
```

Improvement:

Use an endpoint or data source that reliably provides HPO terms, or always merge live API data with curated local HPO/tissue annotations.

---

### 7.2 Tissue mapping is keyword-based

`_tissues_from_hpo()` uses text snippets such as `hepat`, `seizure`, and `retina`.

This is easy to understand, but scientifically crude.

Weaknesses:

- May miss terms that imply a tissue without naming it directly.
- May overcall tissue relevance from a non-specific word like `weakness`.
- Does not distinguish primary disease tissue from secondary complication.
- Does not use formal HPO-to-anatomy ontology mappings.

Improvement:

Use curated disease-to-tissue mappings with evidence sources, or map HPO terms through Uberon/GO/anatomy ontology relationships.

---

### 7.3 Fallback data is hardcoded

Hardcoded fallback is excellent for reproducible demos, but less ideal for research-grade curation.

Weaknesses:

- No citation field for each disease claim.
- Updating data requires editing Python code.
- No `last_reviewed` date per disease.
- No confidence score per annotation.

Improvement:

Move fallback disease records into a structured file such as:

```text
data/diseases.yaml
```

with fields like:

```text
sources
last_reviewed
curator_notes
tissue_evidence
```

---

### 7.4 Only first gene is usually used downstream

`DiseaseInfo.gene_symbols` can contain multiple genes.

But `cli.py` generally uses the first gene unless the user provides `--gene`.

For genetically heterogeneous diseases, this could be misleading.

Improvement:

If multiple genes are present, either:

1. Ask the user which gene to analyze.
2. Score all genes separately.
3. Require `--gene` for multi-gene diseases.

---

### 7.5 Cache is memory-only

`_CACHE` avoids duplicate API calls during one run.

But it does not survive after the process exits.

Improvement:

Wire `cache_disease_to_db()` into the CLI flow, or create a clear persistent cache layer.

---

### 7.6 Broad exception handling hides errors

The code uses:

```python
except Exception:
    return _fallback_disease(orpha_num)
```

This keeps the program robust, but it hides the reason the API failed.

Improvement:

Log warnings such as:

```text
Orphanet timeout; using fallback for ORPHA:1946
```

Then include the warning in the final report.

---

### 7.7 Some imports/constants are unused

`ORPHADATA_BASE` is defined but not used.
`field` is imported but not used.
Top-level `json` is imported but not used directly.

This is not dangerous, but it is a cleanup opportunity.

---

## 8. Practical improvements

Good next improvements would be:

1. Add persistent disease caching in the database.
2. Store `gene_symbols` and `affected_tissues` in the database if disease caching is used.
3. Add source/citation metadata for every fallback disease.
4. Add a `fallback_used` flag so reports can say whether live or local data was used.
5. Add tests for `_orpha_num()` and `_tissues_from_hpo()`.
6. Make Orphanet ID parsing case-insensitive.
7. Merge live API data with local curated tissue annotations.
8. Handle multi-gene diseases more explicitly.

Possible future return object:

```python
DiseaseInfo(
    orphanet_id="ORPHA:1946",
    name="Kohlschutter-Tonz syndrome",
    gene_symbols=["ROGDI"],
    affected_tissues=["CNS"],
    data_source="fallback",
    source_last_checked="2026-06-03",
)
```

---

## 9. Mini mental model

Say this from memory:

```text
disease.py takes an Orphanet ID and returns a DiseaseInfo object.
It first checks a short-term memory cache, then tries the live Orphanet API,
and falls back to curated local disease records if needed.
The most scoring-relevant fields are gene_symbols, inheritance, hpo_terms,
and affected_tissues. The file is reliable for the included fallback diseases,
but the live API path may lack HPO/tissue detail, and the tissue mapping is crude.
```

Even shorter:

```text
ORPHA ID → DiseaseInfo → gene choice + tissue/inheritance scoring inputs
```

---

## 10. Active recall questions

Use these without looking at the code.

1. What is the main job of `disease.py`?
2. What object does `fetch_disease()` return?
3. What is stored in `DiseaseInfo.gene_symbols`?
4. Why does `affected_tissues` matter for scoring?
5. What does `_orpha_num()` do?
6. What is the purpose of `_CACHE`?
7. Is `_CACHE` persistent after the program exits?
8. What API does the file try first?
9. When does the code use fallback disease data?
10. Why might fallback data be better than live API data for tissue scoring?
11. How does `_tissues_from_hpo()` infer tissues?
12. Why is keyword-based tissue mapping scientifically weak?
13. Which fallback entry contains Kohlschutter-Tonz syndrome?
14. What gene is associated with Kohlschutter-Tonz syndrome in the fallback?
15. What does `cache_disease_to_db()` save?
16. Which important `DiseaseInfo` fields are not saved by `cache_disease_to_db()`?
17. Why can using only the first gene be risky?
18. What would a research-grade fallback disease record need?
19. How would you tell the final report whether fallback data was used?
20. How would you explain this file to a non-coder biomedical researcher?

---

## 11. Final high-level summary

`disease.py` is the disease metadata gateway for NanoGT.

It turns an Orphanet ID into a structured `DiseaseInfo` record that the rest of the pipeline can use. Its design is practical: try the live Orphanet API, but keep curated local fallback data so the tool still works offline and for project target diseases.

The scientific importance of this file is high because disease tissues, inheritance, and gene symbols affect the final gene therapy precedent ranking. Its main limitations are crude tissue inference, hardcoded fallback data, limited citation/audit metadata, memory-only caching, and live API results that may not provide enough phenotype detail for strong scoring.
