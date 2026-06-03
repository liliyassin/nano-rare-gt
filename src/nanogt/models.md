# Code Study Note: `src/nanogt/models.py`

File studied: `/Users/suzie/Projects/nano-rare-gt/src/nanogt/models.py`

Related files:
- `src/nanogt/disease.py`
- `src/nanogt/gene.py`
- `src/nanogt/scoring.py`
- `src/nanogt/report.py`
- `src/nanogt/db.py`

Study goal:
Understand the Pydantic data models in `models.py`, what each model represents, and how these intended “data shapes” compare with the dataclasses currently used by the active NanoGT pipeline.

---

## 1. Plain-English identity

`models.py` defines formal data shapes for NanoGT.

Think of each class in this file as a structured form with labelled boxes.

For example:

```text
Disease form:
- orphanet_id
- name
- OMIM ID
- prevalence
- inheritance
- phenotype terms
```

or:

```text
Vector form:
- serotype
- cargo limit
- tissue tropism
- CNS/liver/retina/muscle flags
- clinical precedent count
```

These forms are written using Pydantic.

Pydantic is a Python library that can check and organize data according to type hints.

Easiest mental model:

```text
models.py = NanoGT's typed data-contract definitions
```

---

## 2. Important current-project caveat

In the source files read for this study, the active CLI/scoring/report path mainly uses dataclasses from other files:

```text
disease.py  → DiseaseInfo dataclass
gene.py     → GeneInfo dataclass
scoring.py  → ScoreBreakdown dataclass
report.py   → MatchResult dataclass
```

A search of the Python source did not find active imports of `models.py`.

So this file appears to be an intended or future schema layer rather than the main active runtime model layer.

That does not make it useless. It is still valuable because it documents the data shapes NanoGT wants.

But a beginner should not assume every class here is currently used by the command:

```bash
nanogt match ORPHA:1946
```

The active flow is currently closer to:

```text
cli.py → disease.py dataclass → gene.py dataclass → scoring.py dataclass → report.py
```

while `models.py` is a more formal Pydantic version of those concepts.

---

## 3. Why this file exists

Projects like NanoGT pass structured information between many layers:

```text
disease lookup
gene/protein lookup
vector catalog
gene therapy program scoring
report generation
```

Without clear data shapes, it is easy to make mistakes such as:

- Misspelling a field name.
- Passing a string where a number is expected.
- Forgetting that a field can be missing.
- Mixing up disease-level data and gene-level data.
- Creating reports with inconsistent objects.

`models.py` exists to define what a valid object should look like.

For a non-coder biomedical researcher:

```text
This file is like a set of standard case-report forms for the software.
Each form says which fields are expected and what type of value belongs in each field.
```

---

## 4. How it fits into project data flow

### Intended conceptual flow

If fully integrated, the file could support this flow:

```text
Orphanet/API/database data
        ↓
Disease Pydantic model
        ↓
Gene and Protein Pydantic models
        ↓
Vector model from catalog/database
        ↓
ScoreBreakdown model
        ↓
Match model
        ↓
Report model
```

### Current practical flow

The current active pipeline uses similar concepts but not these exact classes:

```text
cli.py
  uses DiseaseInfo from disease.py
  uses GeneInfo from gene.py
  uses ScoreBreakdown from scoring.py
  uses MatchResult from report.py
```

So `models.py` currently functions more like:

```text
schema/design reference = yes
central runtime dependency = not currently obvious
```

---

## 5. API, fallback, and cache logic

Unlike `disease.py` and `gene.py`, this file does not call APIs.

It has:

```text
No Orphanet call
No UniProt call
No fallback dictionary
No HTTP session
No cache
No database connection
```

Its job is definition, not fetching.

In one line:

```text
models.py describes data; it does not retrieve data.
```

---

## 6. Line-range walkthrough in code order

### Lines 1-7: File identity comments

The file says it contains Pydantic models for the NanoGT matching framework.

The comments explain the key idea:

```text
Each class is a template/form with labelled fields.
Pydantic checks data types automatically.
```

This is different from plain dictionaries, where a typo might go unnoticed until much later.

---

### Line 8: Future annotations import

```python
from __future__ import annotations
```

Plain-English meaning:

This lets Python handle type hints more flexibly, especially when one class refers to another class defined later or when using modern type syntax.

It is common in typed Python projects.

---

### Line 10: Pydantic imports

```python
from pydantic import BaseModel, Field
```

What each part means:

| Import | Beginner meaning | Used for |
|---|---|---|
| `BaseModel` | The Pydantic base class | Every model class inherits from it |
| `Field` | Field configuration helper | Defaults, descriptions, and metadata |

When a class inherits from `BaseModel`, Pydantic can:

- Store fields as attributes.
- Validate types.
- Provide defaults.
- Convert some compatible values.
- Export the object as a dictionary/JSON.

Example concept:

```python
Disease(orphanet_id="ORPHA:1946", name="Kohlschutter-Tonz syndrome")
```

Pydantic checks that required fields are present.

---

## 7. Lines 13-24: `Disease` model

```python
class Disease(BaseModel):
```

This model represents one rare disease record.

Fields:

| Field | Type | Meaning |
|---|---|---|
| `orphanet_id` | `str` | Orphanet disease code, e.g. `ORPHA:1946` |
| `name` | `str` | Disease name |
| `omim_id` | `str | None` | Optional OMIM disease ID |
| `prevalence` | `str | None` | Optional prevalence category |
| `morbidity_flag` | `bool` | Whether disease is high morbidity; defaults to `False` |
| `inheritance` | `str | None` | Simplified inheritance such as AR, AD, XL |
| `active_gt_trials` | `int` | Number of active gene therapy trials; defaults to `0` |
| `phenotype_terms` | `list[str]` | HPO/phenotype terms; default empty list |

Important Pydantic syntax:

```python
Field(...)
```

The `...` means the field is required.

So `orphanet_id` and `name` must be provided.

Important default syntax:

```python
phenotype_terms: list[str] = Field(default_factory=list)
```

This means every `Disease` gets its own empty list by default.

Beginner warning:

```text
Using default_factory=list is safer than using [] directly.
It avoids accidentally sharing one list between many objects.
```

Comparison with `disease.py`:

- `disease.py` uses `DiseaseInfo`, a dataclass.
- `models.py` defines `Disease`, a Pydantic model.
- They overlap but are not identical.

For example:

```text
DiseaseInfo has gene_symbols and affected_tissues.
Disease model does not.
Disease model has morbidity_flag and active_gt_trials.
DiseaseInfo does not.
```

This mismatch matters if someone tries to replace one with the other.

---

## 8. Lines 27-39: `Gene` model

```python
class Gene(BaseModel):
```

This model represents gene-level properties.

Fields:

| Field | Type | Meaning |
|---|---|---|
| `symbol` | `str` | HGNC gene symbol, e.g. `ROGDI` |
| `aliases` | `list[str]` | Alternative symbols |
| `omim_id` | `str | None` | Optional OMIM gene ID |
| `uniprot_id` | `str | None` | UniProt protein accession |
| `chromosome` | `str | None` | Cytogenetic location |
| `exon_count` | `int | None` | Number of exons |
| `cds_length_bp` | `int | None` | Coding sequence length in base pairs |
| `aa_length` | `int | None` | Protein length in amino acids |
| `molecular_weight_da` | `float | None` | Protein molecular weight in daltons |

This model is about the gene as a genomic object.

Comparison with `gene.py`:

`gene.py` uses `GeneInfo`, which combines gene and protein details in one dataclass.

`models.py` splits that concept into:

```text
Gene = gene-level metadata
Protein = protein-level annotations
```

That split is cleaner for larger software.

Important scoring field:

```text
cds_length_bp
```

This is critical for vector packaging.

If the coding sequence is too large, an AAV vector may not be able to carry it.

---

## 9. Lines 42-57: `Protein` model

```python
class Protein(BaseModel):
```

This model represents protein-level annotations.

Fields:

| Field | Type | Meaning |
|---|---|---|
| `uniprot_id` | `str` | UniProt accession; required |
| `name` | `str | None` | Protein name |
| `sequence` | `str | None` | Amino acid sequence |
| `domains` | `list[str]` | Functional regions/domains |
| `go_terms` | `list[str]` | Gene Ontology annotations |
| `keywords` | `list[str]` | UniProt keywords |
| `subcellular_location` | `list[str]` | Where the protein is located in the cell |
| `is_secreted` | `bool` | Whether it is secreted/extracellular |
| `afdb_id` | `str | None` | AlphaFold DB identifier |
| `afdb_url` | `str | None` | AlphaFold structure URL |

This is the model most closely connected to protein biology.

Why it matters for gene therapy:

- A secreted protein can sometimes rescue cells that were not directly transduced.
- A lysosomal enzyme may allow cross-correction.
- A membrane/intracellular protein usually requires delivery to each target cell.
- Domains and structure could support future similarity matching.

Important future direction:

`Protein` could become the right place to store AlphaFold/structure data for structural homology scoring.

---

## 10. Lines 60-74: `Vector` model

```python
class Vector(BaseModel):
```

This model represents a delivery vehicle, especially AAV serotypes.

Fields:

| Field | Type | Meaning |
|---|---|---|
| `serotype` | `str` | Vector name, e.g. `AAV9` |
| `cargo_limit_bp` | `int` | Packaging limit, default `4700` bp |
| `tissue_tropism` | `list[str]` | Tissues the vector tends to reach |
| `cns_tropic` | `bool` | Whether it can reach CNS/brain-spinal cord context |
| `retinal_tropic` | `bool` | Whether it targets retina |
| `hepatic_tropic` | `bool` | Whether it targets liver |
| `muscle_tropic` | `bool` | Whether it targets muscle |
| `clinical_precedents` | `int` | Approximate number of clinical programs |
| `freely_available` | `bool` | Whether IP/licensing is assumed unencumbered |

This model overlaps strongly with entries in `catalog.py` and rows in the `vectors` database table.

Important distinction:

```text
catalog.py stores vector data as dictionaries with 0/1 flags.
models.py defines vector data as a Pydantic model with bool flags.
```

That is a design difference.

Pydantic can often coerce `0`/`1` into `False`/`True`, but a clear conversion layer would be better.

---

## 11. Lines 77-103: `ScoreBreakdown` model

```python
class ScoreBreakdown(BaseModel):
```

This model stores per-dimension match scores.

Fields include 12 score dimensions:

| Field | Meaning | Current note |
|---|---|---|
| `structural_homology` | 3D structural similarity | Future/not active in current scoring dataclass |
| `sequence_identity` | Sequence similarity | Future/not active |
| `domain_similarity` | Shared protein domains | Future/not active |
| `size_compatibility` | Gene size vs vector cargo | Related to active `packaging_fit` |
| `tissue_tropism` | Vector tissue match | Related to active tropism scoring |
| `roa_precedent` | Route-of-administration precedent | Similar concept to active `roa_feasibility` |
| `promoter_match` | Promoter suitability | Similar concept to active promoter scoring |
| `localization_match` | Subcellular/protein localization match | Related to active protein class scoring |
| `immunogenicity` | Immune risk | Active scoring uses immunogenicity |
| `therapeutic_window` | Timing/natural-history fit | Active scoring uses therapeutic window |
| `codon_optimization` | Whether coding sequence is optimized | Future/not active |
| `platform_depth` | Clinical platform experience | Future/not active |

Important current-code mismatch:

`scoring.py` defines its own dataclass also called `ScoreBreakdown`, but with different field names:

```text
scoring.py ScoreBreakdown has:
program_name, program_disease, vector, tissue_target, approval_status,
composite_score, confidence, packaging_fit, tropism_match,
protein_class_match, inheritance_match, pathway_similarity,
approval_weight, immunogenicity, therapeutic_window,
cross_correction, immune_privilege, promoter_availability,
roa_feasibility, notes
```

So there are two different `ScoreBreakdown` concepts:

```text
models.py ScoreBreakdown = ideal/schema score dimensions
scoring.py ScoreBreakdown = active runtime scoring result
```

This is not fatal, but it can confuse beginners.

---

### Lines 95-102: `must_pass_gates` property

```python
@property
def must_pass_gates(self) -> dict[str, bool]:
    return {
        "size_compatibility": self.size_compatibility >= 0.5,
    }
```

A property is a method you access like an attribute.

Example idea:

```python
score.must_pass_gates
```

This returns a dictionary saying whether hard gates pass.

Here, the only hard gate is size compatibility:

```text
size_compatibility must be at least 0.5
```

Important comparison with active `scoring.py`:

`scoring.py` uses a different packaging hard gate:

```text
If gene_cds > vector_cargo, packaging_fit = 0 and the program fails.
```

So the concept is similar, but the exact implementation differs.

---

## 12. Lines 105-123: `Match` model

```python
class Match(BaseModel):
```

This model represents one disease-to-precedent match result.

It bundles together:

| Field | Meaning |
|---|---|
| `disease` | The query `Disease` object |
| `gene` | The query `Gene` object |
| `vector` | The precedent program's `Vector` object |
| `surrogate_program` | Name of the precedent program/platform |
| `scores` | A `ScoreBreakdown` object |
| `composite_score` | Final overall score |
| `confidence` | Low/medium/high confidence label |
| `notes` | Plain-English explanation notes |
| `protocol_sections` | Optional generated protocol text sections |

Plain-English meaning:

```text
A Match is one ranked comparison between the query disease/gene and one possible GT precedent.
```

Example concept:

```text
Kohlschutter-Tonz / ROGDI compared to Zolgensma / AAV9
```

The active project currently creates similar outputs using the `ScoreBreakdown` dataclass in `scoring.py` and `MatchResult` dataclass in `report.py`, not this exact Pydantic `Match` class.

---

## 13. Lines 126-135: `Report` model

```python
class Report(BaseModel):
```

This is the top-level output object for one matching run.

Fields:

| Field | Meaning |
|---|---|
| `query_disease` | The disease being analyzed |
| `matches` | List of all match results |
| `top_match` | Best match, or None |
| `generated_at` | Timestamp string |
| `query_time_s` | Runtime duration |
| `warnings` | Warnings, such as API fallback or missing data |

Plain-English meaning:

```text
Report = the full package of results for one disease query
```

This is a good design because it separates the data from how it is printed.

The current `report.py` creates Markdown text directly from a `MatchResult` dataclass. A future version could instead generate a `Report` Pydantic object first, then export it to Markdown, JSON, or HTML.

---

## 14. Assumptions and weaknesses

### 14.1 The file is not obviously wired into the current pipeline

The biggest practical issue is that the active pipeline uses dataclasses elsewhere.

This means `models.py` may be:

- An early design layer.
- A future intended schema layer.
- A partially superseded file.
- A documentation-like reference.

Improvement:

Decide one of these paths:

1. Fully integrate `models.py` and use Pydantic models throughout.
2. Keep dataclasses and remove/rename unused Pydantic models.
3. Treat `models.py` as a schema reference and document that clearly.

---

### 14.2 Model names overlap with active dataclass names

There is a `ScoreBreakdown` in `models.py` and another `ScoreBreakdown` in `scoring.py`.

They are not the same.

This can cause confusion.

Improvement:

Rename one, for example:

```text
models.py: ScoreSchema
scoring.py: ProgramScoreResult
```

or standardize on one shared model.

---

### 14.3 `Disease` model lacks active scoring fields

The active `DiseaseInfo` dataclass has:

```text
gene_symbols
affected_tissues
hpo_terms as list
inheritance as list
```

The `Disease` Pydantic model has:

```text
phenotype_terms
inheritance as one optional string
no gene_symbols
no affected_tissues
```

If someone tried to use `Disease` directly in `scoring.py`, the scoring code would need changes.

Improvement:

Add fields or create a separate query model:

```text
QueryDisease
- orphanet_id
- name
- gene_symbols
- inheritance list
- hpo_terms
- affected_tissues
```

---

### 14.4 `Gene` and `Protein` are separated, but active code combines them

This is not wrong.

Actually, separating gene and protein can be cleaner.

But if active code uses `GeneInfo`, integration needs a conversion step:

```text
GeneInfo dataclass → Gene model + Protein model
```

Improvement:

Write converter functions:

```python
def gene_info_to_models(info: GeneInfo) -> tuple[Gene, Protein]:
    ...
```

---

### 14.5 Pydantic validates types but not scientific meaning

Pydantic can check that `cds_length_bp` is an integer.

But it does not automatically know that:

- CDS length should be positive.
- `confidence` should only be `low`, `medium`, or `high`.
- AAV cargo limit should be realistic.
- `inheritance` should use a controlled vocabulary.
- Scores should stay between 0 and 1.

Improvement:

Add constraints and validators.

Example concept:

```python
composite_score: float = Field(0.0, ge=0.0, le=10.0)
confidence: Literal["low", "medium", "high"]
```

---

### 14.6 Score scale is not fully explicit

`ScoreBreakdown` says scores are 0.0-1.0 in the docstring, but active `scoring.py` uses mixed raw maxima:

```text
some dimensions max 2.0
some max 1.0
final normalized to 10
```

This is another integration mismatch.

Improvement:

Standardize all model score fields to either:

```text
0-1 normalized per dimension
```

or:

```text
raw scoring scale with explicit max values
```

Then document it consistently.

---

### 14.7 No model for GT program catalog entries

`catalog.py` has gene therapy program dictionaries, but `models.py` does not define a clear `GTProgram` model.

That would be useful.

Possible future model:

```python
class GTProgram(BaseModel):
    name: str
    disease: str
    gene_symbol: str
    vector: str
    tissue_target: str
    cds_bp: int
    approval_status: str
    approval_year: int | None
    mechanism: str
    protein_class: str
    inheritance: str
    pathway: str
    notes: str | None = None
```

This would help validate catalog entries before seeding the database.

---

## 15. Practical improvements

Good next improvements would be:

1. Decide whether Pydantic models are the official project data layer.
2. If yes, refactor `disease.py`, `gene.py`, `scoring.py`, and `report.py` to use these models.
3. If no, rename this file to make its role clear or remove unused models.
4. Add a `GTProgram` model for `catalog.py` entries.
5. Add validators for score ranges, positive lengths, and controlled vocabulary fields.
6. Align `models.py.ScoreBreakdown` with `scoring.py.ScoreBreakdown`.
7. Add fields needed by active scoring, especially `affected_tissues` and `gene_symbols`.
8. Add warning/source fields to support API fallback transparency.
9. Add tests that instantiate each model with realistic example data.
10. Add conversion functions between dataclasses and Pydantic models if both styles remain.

---

## 16. Useful comparison: dataclass vs Pydantic model

The project currently uses both concepts.

| Feature | Dataclass | Pydantic BaseModel |
|---|---|---|
| Main purpose | Simple Python data container | Validated structured data model |
| Used in active files | `disease.py`, `gene.py`, `scoring.py`, `report.py` | `models.py` |
| Type validation | Minimal at runtime | Stronger runtime validation |
| Easy JSON export | Manual or helper needed | Built in |
| Good for beginners | Very simple | Slightly more complex but safer |
| Good for API/database boundaries | Acceptable | Often better |

Plain-English analogy:

```text
Dataclass = a simple labelled worksheet.
Pydantic model = a labelled worksheet that checks whether the answers are in the expected format.
```

---

## 17. Mini mental model

Say this from memory:

```text
models.py defines Pydantic templates for the major objects NanoGT cares about:
Disease, Gene, Protein, Vector, ScoreBreakdown, Match, and Report.
It does not fetch data, call APIs, use fallback dictionaries, or cache anything.
It is a schema/design layer. In the current codebase, the active CLI pipeline mostly uses dataclasses in disease.py, gene.py, scoring.py, and report.py instead, so models.py needs either integration or clearer documentation.
```

Even shorter:

```text
models.py = formal data shapes, not active fetching/scoring logic
```

---

## 18. Active recall questions

Use these without looking at the code.

1. What is the main job of `models.py`?
2. What library provides `BaseModel` and `Field`?
3. What does `Field(...)` mean?
4. Why is `default_factory=list` used for list fields?
5. What fields are required in the `Disease` model?
6. What important fields does `DiseaseInfo` have that `Disease` lacks?
7. What is the difference between `Gene` and `Protein` in this file?
8. Why does `cds_length_bp` matter for gene therapy?
9. Why does `is_secreted` matter?
10. What does the `Vector` model describe?
11. How does the `Vector` model relate to `catalog.py`?
12. What does `ScoreBreakdown` store?
13. What does `must_pass_gates` check?
14. How is `models.py.ScoreBreakdown` different from `scoring.py.ScoreBreakdown`?
15. What does the `Match` model represent?
16. What does the `Report` model represent?
17. Does `models.py` call Orphanet or UniProt APIs?
18. Does `models.py` contain fallback or cache logic?
19. Why might unused models be confusing in a project?
20. What would you change to make this file align better with the active pipeline?

---

## 19. Final high-level summary

`models.py` defines the formal Pydantic data shapes for NanoGT: disease, gene, protein, vector, score breakdown, match result, and report.

Its strength is that it makes the intended structure of the project visible and could support better validation, JSON export, and safer data flow.

Its main weakness is integration mismatch: the currently active pipeline appears to use dataclasses in `disease.py`, `gene.py`, `scoring.py`, and `report.py` rather than these Pydantic models. To make the project cleaner, either integrate these models fully or document/rename them as schema references.
