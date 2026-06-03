# Code Study Note: `src/nanogt/catalog.py`

## 1. Plain-English identity

`catalog.py` is the static curated knowledge base for NanoGT.

It does not fetch information from the internet. 
It does not run an algorithm. 
It does not score anything by itself.

Instead, it contains hand-entered biomedical/clinical reference data that the rest of the project uses later.

It defines two main lists:

1. `VECTORS`
   - A list of gene therapy delivery vehicles.
   - Examples: `AAV1`, `AAV2`, `AAV5`, `AAV8`, `AAV9`, `AAVrh10`, `AAV2/6`, `LV`.
   - Each vector has properties such as cargo capacity, tissue tropism, whether it targets CNS/liver/muscle/retina, number of clinical precedents and whether it is freely available.

2. `GT_PROGRAMS`
   - A list of real gene therapy programs used as precedent examples.
   - Examples: Zolgensma, Hemgenix, Roctavian, Luxturna, Glybera, RGX-121, ST-920, etc.
   - Each program records disease, gene, vector, target tissue, coding sequence size, approval status, protein class, inheritance and pathway.

The easiest mental model:

```text
catalog.py = NanoGT's small hand-curated reference library
```

Or even more simply:

```text
VECTORS = delivery vehicles
GT_PROGRAMS = real-world gene therapy examples
```

---

## 2. Why this file exists

NanoGT is trying to answer a question like:

> Given a rare disease and gene, what existing gene therapy programs are the best precedents?

To answer that, the project needs a reference set of known gene therapy examples.

`catalog.py` provides that reference set.

Without `catalog.py`, NanoGT would have no internal catalogue of:
- Which vectors exist.
- What tissues those vectors reach.
- What clinical gene therapy examples already exist.
- Which diseases/genes/vectors have precedent.
- Which precedent programs are approved, in trials, or withdrawn.
- What biological pathway each program belongs to.

So this file exists because the scoring algorithm needs something to compare the query disease against.

In project terms:

```text
A query disease/gene is compared against the GT_PROGRAMS in catalog.py.
```

Example:

If the user asks about Kohlschutter-Tonz syndrome / ROGDI, NanoGT needs to compare ROGDI against programs like:
- Zolgensma / SMN1 / AAV9 / CNS
- Luxturna / RPE65 / AAV2 / retina
- RGX-121 / IDS / AAV9 / CNS/liver
- ST-920 / GLA / AAV2/6 / liver

That comparison is only possible because `catalog.py` has encoded those precedent examples.

---

## 3. What this file contains

### 3.1 Top-level structure

The file has two main objects:

```python
VECTORS = [
    {...},
    {...},
]

GT_PROGRAMS = [
    {...},
    {...},
]
```

Each item inside the list is a Python dictionary.

A dictionary is a set of labelled facts.

Example simplified vector dictionary:

```python
{
    "serotype": "AAV9",
    "cargo_limit_bp": 4700,
    "tissue_tropism": ["CNS", "muscle", "liver", "heart"],
    "cns_tropic": 1,
    "retinal_tropic": 0,
    "hepatic_tropic": 1,
    "muscle_tropic": 1,
    "clinical_precedents": 18,
    "freely_available": 1,
}
```

Example simplified GT program dictionary:

```python
{
    "name": "Zolgensma",
    "disease": "Spinal Muscular Atrophy",
    "gene_symbol": "SMN1",
    "vector": "AAV9",
    "tissue_target": "CNS/motor neuron",
    "cds_bp": 891,
    "approval_status": "approved",
    "approval_year": 2019,
    "mechanism": "gene_replacement",
    "protein_class": "intracellular",
    "inheritance": "AR",
    "pathway": "motor_neuron",
    "notes": None,
}
```

---

## 4. What `VECTORS` means

`VECTORS` stores delivery vehicle information.

A gene therapy vector is the vehicle used to deliver genetic material into cells.

In this project, each vector has the following fields:

| Field | Meaning | Why it matters |
|---|---|---|
| `serotype` | Name of the vector, e.g. `AAV9` | Used to link GT programs to vector properties |
| `cargo_limit_bp` | Approximate DNA cargo capacity in base pairs | Used in packaging feasibility scoring |
| `tissue_tropism` | Tissues the vector naturally tends to reach | Used in tissue/tropism scoring |
| `cns_tropic` | Whether the vector can target CNS | Useful for neurological disease reasoning |
| `retinal_tropic` | Whether the vector targets retina | Useful for eye/retinal disorders |
| `hepatic_tropic` | Whether the vector targets liver | Useful for metabolic/secreted protein disorders |
| `muscle_tropic` | Whether the vector targets muscle | Useful for myopathy/muscle disorders |
| `clinical_precedents` | Approximate count of clinical experience | Used as a rough confidence/prior signal |
| `freely_available` | Whether the vector is patent/licence restricted | Practical translational consideration |

### Vectors currently included

| Vector | Main idea in this project |
|---|---|
| `AAV1` | Early AAV type; mainly muscle and CNS |
| `AAV2` | Highly studied; retina, liver, CNS; used in Luxturna |
| `AAV5` | Liver and CNS; used in Hemgenix/Roctavian; patent-restricted here |
| `AAV8` | Liver-tropic workhorse; also muscle |
| `AAV9` | Broad tropism; CNS/muscle/liver/heart; used in Zolgensma |
| `AAVrh10` | CNS/liver, rhesus-derived, lower pre-existing immunity in some contexts |
| `AAV2/6` | Hybrid; liver and muscle |
| `LV` | Lentiviral vector; larger cargo; integrates; commonly ex vivo |

### Key point to memorise

`VECTORS` tells NanoGT what each delivery vehicle is capable of.

If this data is wrong or oversimplified, the scoring system can recommend bad vector precedents.

---

## 5. What `GT_PROGRAMS` means

`GT_PROGRAMS` stores real gene therapy precedent programs.

Each program is an example of a disease/gene/vector combination that has been approved, tested, or clinically developed.

Each GT program has fields like:

| Field | Meaning | Why it matters |
|---|---|---|
| `name` | Program or product name | Human-readable precedent name |
| `disease` | Disease treated by the precedent | Shows clinical context |
| `gene_symbol` | Gene delivered/replaced | Used for biological comparison |
| `vector` | Vector used by the program | Links to `VECTORS` |
| `tissue_target` | Tissue/cell type targeted | Used in tropism scoring |
| `cds_bp` | Coding sequence size in base pairs | Used for packaging comparison |
| `approval_status` | Approved, phase2, phase3, withdrawn, etc. | Used as evidence maturity weight |
| `approval_year` | Year of approval, or `None` if not approved | Tracks maturity/timeline |
| `mechanism` | Currently always `gene_replacement` | Defines therapeutic strategy |
| `protein_class` | Intracellular, secreted, membrane, lysosomal etc. | Used in protein-class scoring |
| `inheritance` | AR, XL, mitochondrial | Used in inheritance compatibility scoring |
| `pathway` | Biological pathway group | Used in pathway similarity scoring |
| `notes` | Optional extra notes | Could hold extra caveats but currently mostly `None` |

### Programs currently included

| Program | Disease | Gene | Vector | Main learning value |
|---|---|---|---|---|
| Zolgensma | Spinal muscular atrophy | SMN1 | AAV9 | CNS/motor neuron AAV9 precedent |
| Hemgenix | Hemophilia B | FIX/F9 | AAV5 | Liver-secreted clotting factor precedent |
| Roctavian | Hemophilia A | F8 | AAV5 | Large AAV cargo precedent |
| Luxturna | Leber congenital amaurosis type 2 | RPE65 | AAV2 | Retinal AAV precedent |
| Glybera | Lipoprotein lipase deficiency | LPL | AAV1 | Early Western gene therapy approval/withdrawal |
| AT132 | X-linked myotubular myopathy | MTM1 | AAV8 | Muscle/myopathy precedent |
| SRP-9001 | Duchenne muscular dystrophy | DMD_micro | AAV9 | Micro-dystrophin/muscle precedent |
| BMN 307 | Phenylketonuria | PAH | AAV5 | Liver metabolic enzyme precedent |
| GS010 | Leber hereditary optic neuropathy | ND4 | AAV2 | Retinal/mitochondrial precedent |
| OAV101-IT | Spinal muscular atrophy | SMN1 | AAV9 | Intrathecal CNS AAV9 precedent |
| RGX-121 | MPS II | IDS | AAV9 | CNS/liver lysosomal precedent |
| ABO-101 | MPS IIIB | NAGLU | AAV9 | CNS lysosomal precedent |
| AVR-RD-01 | Fabry disease | GLA | LV | Ex vivo lentiviral lysosomal precedent |
| ST-920 | Fabry disease | GLA | AAV2/6 | Liver-targeted Fabry precedent |
| DTX301 | OTC deficiency | OTC | AAV8 | Urea cycle liver enzyme precedent |
| CPCB-RPE1 | Achromatopsia | CNGB3 | AAV8 | Retinal photoreceptor precedent |
| SPK-8011 | Hemophilia A | F8 | AAVrh10 | Liver/coagulation precedent |
| DTX201 | Hemophilia A | F8 | AAV8 | Liver/coagulation precedent |

### Key point to memorise

`GT_PROGRAMS` is the set of examples NanoGT compares against.

The software is not inventing precedents from nothing. It is ranking these specific examples.

---

## 6. Inputs and outputs of this file

### Inputs

`catalog.py` has no runtime inputs.

It does not ask the user anything.
It does not call APIs.
It does not read files.
It does not query the database.

The input was human research done before coding:
- Someone selected vectors.
- Someone selected GT programs.
- Someone entered their properties manually.

### Outputs

It outputs two Python variables:

```python
VECTORS
GT_PROGRAMS
```

These are imported by `db.py`.

So the output is not a printed report. The output is data made available to the rest of the program.

---

## 7. How this file connects to the project

The important connection is:

```text
catalog.py → db.py → SQLite database → scoring.py → report.py/CLI output
```

More detailed flow:

```text
1. catalog.py defines VECTORS and GT_PROGRAMS

2. db.py imports them:
   from .catalog import VECTORS, GT_PROGRAMS

3. db.py creates database tables.

4. db.py seeds the vectors table with VECTORS.

5. db.py seeds the gt_programs table with GT_PROGRAMS.

6. scoring.py reads program/vector rows from the database.

7. scoring.py compares each program to the query disease/gene.

8. report.py turns the ranking into a human-readable report.
```

### Very important gotcha

Changing `catalog.py` does not necessarily update an existing database.

Why?

Because in `db.py`, seeding only happens if the database table is empty.

The logic is roughly:

```python
if vectors table count is 0:
    insert VECTORS

if gt_programs table count is 0:
    insert GT_PROGRAMS
```

So if you already ran `nanogt init`, then edited `catalog.py`, the old database may still contain the old version.

### Practical implication

If you edit `catalog.py`, you may need to:
- Delete/recreate the database, or
- Add a reseed command, or
- Add a migration/update mechanism.

This is a major reproducibility point.

---

## 8. How `catalog.py` applies to the biomedical project

NanoGT is a rare disease gene therapy matching framework.

For a disease like Kohlschutter-Tonz syndrome / ROGDI, the software needs to reason about questions like:

- Is the gene small enough for AAV?
- Which tissues are affected?
- Which vectors can reach those tissues?
- Are there existing approved or clinical programs in similar tissues/pathways?
- Is the protein intracellular, secreted, lysosomal, or membrane-bound?
- Is the disease recessive and therefore suitable for gene replacement?
- Are there precedents in CNS, retina, liver, lysosomal storage, muscle, etc.?

`catalog.py` is where many of the comparison examples come from.

For ROGDI/Kohlschutter-Tonz, CNS precedents such as AAV9/Zolgensma and OAV101-IT are important because the disease has neurological/CNS relevance.

So the catalog shapes the answer to:

> Which gene therapy precedents look most relevant to my disease?

---

## 9. Things to memorise

Memorise these ideas, not the exact syntax.

### Core memory anchors

1. `catalog.py` is data, not algorithm.
2. `VECTORS` describes delivery vehicles.
3. `GT_PROGRAMS` describes clinical gene therapy precedents.
4. `db.py` imports this data and puts it into SQLite.
5. `scoring.py` later scores against these programs.
6. The quality of NanoGT depends heavily on the quality of this catalog.
7. If the catalog is outdated, biased, or oversimplified, the final ranking can be misleading.
8. Changing the catalog does not automatically update a database that was already seeded.
9. The catalog currently lacks source/citation fields for every claim.
10. A research-grade version should make every clinical/scientific claim auditable.

### Short explanation to practise from memory

`catalog.py` is NanoGT's hand-curated precedent library. It contains vector data and gene therapy program data. The database layer imports it and seeds SQLite tables. The scoring layer then compares a new rare disease/gene against these precedents. Its strength is that it gives the algorithm real biomedical examples, but its weakness is that the data is hardcoded, simplified, and not yet fully citation-auditable.

---

## 10. Scientific assumptions and weaknesses

### 10.1 Hardcoded data

The data is manually written into the Python file.

Strength:
- Simple.
- Easy to read.
- Good for a proof-of-concept.

Weakness:
- Hard to keep updated.
- Hard to audit.
- Easy to accidentally encode stale facts.
- Scientific claims are mixed with code.

Improvement:
Move the data into a separate structured file such as:
- `data/vectors.yaml`
- `data/gt_programs.yaml`
- `data/gt_programs.csv`
- or a proper database migration/seed file.

How to do it:
1. Create a `data/catalog/` folder.
2. Move vector entries into `vectors.yaml` or `vectors.json`.
3. Move GT program entries into `gt_programs.yaml` or `gt_programs.json`.
4. Write a loader function in Python that reads those files.
5. Add tests that confirm all fields are present and valid.

Possible future structure:

```text
data/catalog/
  vectors.yaml
  gt_programs.yaml
  sources.bib
```

---

### 10.2 Missing citations/source fields

Many comments mention important facts, but the file does not include formal source fields.

Example:
- AAV9 crosses the blood-brain barrier.
- Luxturna uses AAV2.
- Hemgenix uses AAV5.
- AAV5 is patent-restricted.
- Clinical precedent counts are assigned.

These claims need evidence if this project is used academically.

Weakness:
A supervisor/examiner could ask:

> Where did this fact come from?

Right now the code comments explain the reasoning, but they do not provide enough traceable evidence.

Improvement:
Add source metadata to every vector and program.

How to do it:
Add fields such as:

```python
"sources": [
    {
        "type": "FDA label",
        "title": "Zolgensma prescribing information",
        "url": "...",
        "accessed": "2026-06-03",
        "supports": ["approval_status", "vector", "indication"]
    }
]
```

Or for papers:

```python
"citations": [
    "Mendell et al. 2017",
    "FDA Zolgensma label 2019"
]
```

Best future direction:
Each field should be traceable to a source.

For example:

```text
Program: Zolgensma
Claim: vector = AAV9
Source: FDA label or pivotal clinical paper
```

---

### 10.3 Clinical approval status can become outdated

`approval_status` is manually entered.

Examples:
- `approved`
- `phase3`
- `phase2`
- `phase1/2`
- `withdrawn`

Weakness:
Clinical trial status changes over time.
A program that is phase 2 today may be discontinued, approved, paused, or changed later.

Improvement:
Add source and date fields:

```python
"approval_status": "phase3",
"status_last_checked": "2026-06-03",
"status_source": "ClinicalTrials.gov / company pipeline / FDA / EMA"
```

How to do it:
1. Add `status_last_checked` to every GT program.
2. Add `status_source_url`.
3. Add a test that checks every program has a status date.
4. Create a periodic manual review checklist.

---

### 10.4 Tissue tropism is simplified

The file encodes tissue tropism as simple labels like:

```python
["CNS", "muscle", "liver", "heart"]
```

Strength:
- Easy for scoring.
- Easy to understand.

Weakness:
Real tropism is more complicated.
It depends on:
- Species.
- Dose.
- Route of administration.
- Promoter.
- Capsid engineering.
- Patient age.
- Pre-existing antibodies.
- Whether delivery is systemic, intrathecal, subretinal, intramuscular, or ex vivo.

Improvement:
Separate vector tropism from route-specific delivery evidence.

Possible future fields:

```python
"tissue_tropism": ["CNS", "liver"],
"route_specific_evidence": [
    {
        "route": "intrathecal",
        "target": "CNS",
        "evidence_level": "clinical",
        "source": "..."
    },
    {
        "route": "intravenous",
        "target": "liver",
        "evidence_level": "clinical",
        "source": "..."
    }
]
```

---

### 10.5 Clinical precedent counts are rough

`clinical_precedents` is an integer.

Example:

```python
"clinical_precedents": 18
```

Weakness:
It is not clear exactly how that number was counted.

Questions:
- Does it count approved products only?
- Does it count all clinical trials?
- Does it count unique diseases?
- Does it count active and discontinued programs?
- Does it count preclinical programs?
- What is the source?

Improvement:
Replace one rough number with more explicit fields:

```python
"clinical_experience": {
    "approved_products": 1,
    "active_trials": 8,
    "completed_trials": 10,
    "discontinued_programs": 2,
    "source": "ClinicalTrials.gov query date ..."
}
```

---

### 10.6 Patent/licence availability is oversimplified

`freely_available` is currently `0` or `1`.

Weakness:
Vector IP status is complex.

It may depend on:
- Jurisdiction.
- Patent expiry.
- Manufacturing method.
- Capsid variant.
- Academic vs commercial use.
- Material transfer agreements.

Improvement:
Use a more careful field:

```python
"availability": {
    "status": "restricted",
    "reason": "capsid IP / licence required",
    "jurisdiction": "US/EU",
    "source": "...",
    "confidence": "medium"
}
```

---

### 10.7 `mechanism` is always gene replacement

Every GT program currently has:

```python
"mechanism": "gene_replacement"
```

Weakness:
Real gene therapy includes multiple mechanisms:
- Gene replacement.
- Gene addition.
- Gene editing.
- Exon skipping.
- RNA modulation.
- Knockdown/silencing.
- Base/prime editing.
- Cell therapy.

For this project, focusing on gene replacement may be appropriate, especially for recessive loss-of-function diseases. But it should be stated clearly as a scope limitation.

Improvement:
Either:
1. Keep only gene replacement programs and explicitly document that scope; or
2. Add support for other mechanisms.

Possible future fields:

```python
"mechanism": "gene_replacement",
"modality": "AAV gene addition",
"delivery_context": "in vivo",
"genome_integration": False
```

---

### 10.8 Protein class is simplified

`protein_class` uses categories like:
- `intracellular`
- `secreted`
- `membrane`
- `secreted_lysosomal`

Strength:
Useful for scoring because secreted/lysosomal proteins can sometimes cross-correct.

Weakness:
Some proteins do not fit neatly into one category.
Also, subcellular location and therapeutic mechanism can be context-dependent.

Improvement:
Use multiple labels and source them from UniProt/GO terms.

Example:

```python
"protein_class": ["lysosomal", "secreted"],
"protein_class_source": "UniProt subcellular location / GO annotation"
```

---

### 10.9 Pathway labels must stay aligned with `scoring.py`

Each GT program has a `pathway` such as:
- `coagulation`
- `motor_neuron`
- `myopathy`
- `lysosomal_storage`
- `amino_acid_metabolism`
- `urea_cycle`
- `retinal_visual_cycle`
- `retinal_phototransduction`
- `mitochondrial_complex`

These must match the pathway groups in `scoring.py`.

Weakness:
If someone adds a new pathway to `catalog.py` but forgets to add it to `scoring.py`, pathway scoring may break or become meaningless.

Improvement:
Add a validation test:

```python
def test_all_catalog_pathways_are_known():
    catalog_pathways = {p["pathway"] for p in GT_PROGRAMS}
    scoring_pathways = set(_PATHWAY_GROUPS)
    assert catalog_pathways <= scoring_pathways
```

This kind of test protects the project from silent errors.

---

### 10.10 Static data is mixed with explanatory comments

The file has lots of helpful comments, which is good for learning.

Weakness:
As the dataset grows, long comments inside a Python file can become hard to maintain.

Improvement:
Separate:
- Machine-readable data.
- Human-readable explanation.
- Source bibliography.

Possible structure:

```text
src/nanogt/catalog.py       # loader + validation only
data/catalog/programs.yaml  # actual data
docs/catalog-methods.md     # explanation of curation method
docs/catalog-sources.md     # citations/source notes
```

---

## 11. Coding/design weaknesses

### 11.1 No formal schema validation inside `catalog.py`

Currently, the dictionaries are assumed to be correct.

If someone misspells a key, e.g.:

```python
"approoval_status": "approved"
```

then the database seeding or scoring could fail later.

Improvement:
Use Pydantic models or dataclasses to validate entries.

Possible approach:

```python
from pydantic import BaseModel

class VectorCatalogEntry(BaseModel):
    serotype: str
    cargo_limit_bp: int
    tissue_tropism: list[str]
    cns_tropic: int
    retinal_tropic: int
    hepatic_tropic: int
    muscle_tropic: int
    clinical_precedents: int
    freely_available: int

class GTProgramCatalogEntry(BaseModel):
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
    notes: str | None
```

Then validate every entry before seeding.

---

### 11.2 Boolean values are encoded as `0`/`1`

Example:

```python
"cns_tropic": 1
"freely_available": 0
```

This works with SQLite, but as Python data, `True`/`False` may be clearer.

Improvement:
Use booleans in Python:

```python
"cns_tropic": True
"freely_available": False
```

Then convert to integers only when inserting into SQLite if needed.

---

### 11.3 Data update pathway is not obvious

A beginner might think:

> I changed catalog.py, so the results changed.

But this may not happen if the database already exists.

Improvement:
Add a CLI command such as:

```bash
nanogt reseed-catalog
```

or:

```bash
nanogt init --force-reseed
```

Possible implementation idea:
1. Add a CLI option in `cli.py`.
2. In `db.py`, add a function that clears and reloads `vectors` and `gt_programs`.
3. Add a test proving that edited/new catalog data can reseed correctly.

---

### 11.4 No data versioning

The catalog does not have a version number.

Weakness:
If results change later, it may be hard to know which catalog version generated an old report.

Improvement:
Add:

```python
CATALOG_VERSION = "2026-06-03"
```

Then store that version in reports and/or the database.

Even better:

```python
CATALOG_METADATA = {
    "version": "2026-06-03",
    "curator": "Suzie / NanoGT",
    "last_reviewed": "2026-06-03",
    "scope": "AAV/LV gene replacement precedents for monogenic rare disease"
}
```

---

## 12. Future directions and how to actually do them

### Direction 1: Add citation/source fields

Why:
Make the catalog defensible for dissertation/research use.

How:
1. Add a `sources` field to every vector and GT program.
2. Decide what a source object looks like.
3. Update database schema to store source information, or store sources in JSON.
4. Update report generation to show citations.
5. Add tests requiring every entry to have at least one source.

Example field:

```python
"sources": [
    {
        "label": "FDA label",
        "url": "https://...",
        "accessed": "2026-06-03",
        "supports": ["approval_status", "vector", "disease"]
    }
]
```

Test idea:

```python
def test_every_program_has_sources():
    for program in GT_PROGRAMS:
        assert program.get("sources"), program["name"]
```

---

### Direction 2: Add catalog validation tests

Why:
Catch mistakes before they affect scientific results.

How:
Add tests to `tests/test_nanogt.py` or a new file like `tests/test_catalog.py`.

Useful checks:

```python
def test_program_vectors_exist():
    vector_names = {v["serotype"] for v in VECTORS}
    for program in GT_PROGRAMS:
        assert program["vector"] in vector_names
```

```python
def test_program_names_are_unique():
    names = [p["name"] for p in GT_PROGRAMS]
    assert len(names) == len(set(names))
```

```python
def test_all_programs_have_positive_cds():
    for program in GT_PROGRAMS:
        assert program["cds_bp"] > 0
```

```python
def test_approval_status_values_are_known():
    allowed = {"approved", "withdrawn", "phase1/2", "phase2", "phase2/3", "phase3"}
    for program in GT_PROGRAMS:
        assert program["approval_status"] in allowed
```

---

### Direction 3: Move data out of Python and into YAML/JSON

Why:
It separates data from code and makes curation easier.

How:
1. Create `data/catalog/programs.yaml`.
2. Copy each program entry into YAML format.
3. Create `data/catalog/vectors.yaml`.
4. Replace hardcoded lists in `catalog.py` with a loader function.
5. Validate loaded data.

Future `catalog.py` could become:

```python
from pathlib import Path
import yaml

DATA_DIR = Path(__file__).parents[2] / "data" / "catalog"

VECTORS = load_yaml(DATA_DIR / "vectors.yaml")
GT_PROGRAMS = load_yaml(DATA_DIR / "gt_programs.yaml")
```

This makes it clearer that the file's job is to load catalog data, not to be the catalog itself.

---

### Direction 4: Add evidence confidence levels

Why:
Not all facts are equally certain.

How:
Add fields like:

```python
"evidence_confidence": "high"
```

or per claim:

```python
"claims": [
    {
        "field": "tissue_target",
        "value": "CNS/motor neuron",
        "confidence": "high",
        "source": "FDA label / pivotal trial"
    }
]
```

Possible confidence levels:
- `high`: regulator label, peer-reviewed clinical paper, official trial registry.
- `medium`: company pipeline, review article, secondary source.
- `low`: inferred or uncertain.

---

### Direction 5: Add route of administration

Why:
Vector tropism alone is not enough. Delivery route changes everything.

Possible field:

```python
"route_of_administration": "intrathecal"
```

Examples:
- `intravenous`
- `intrathecal`
- `subretinal`
- `intramuscular`
- `ex vivo hematopoietic stem cell`

How:
1. Add `route_of_administration` to GT programs.
2. Update `db.py` schema to include the new column.
3. Update report output to display it.
4. Update scoring.py if route feasibility should become more precise.

---

### Direction 6: Make updates reproducible

Why:
Reports should state which catalog version was used.

How:
1. Add `CATALOG_VERSION` to `catalog.py`.
2. Store it in the database during setup.
3. Include it in generated reports.
4. When the catalog changes, update the version/date.

Example:

```python
CATALOG_VERSION = "2026-06-03"
```

Report could say:

```text
Catalog version: 2026-06-03
```

This makes old outputs easier to interpret.

---

## 13. Active recall questions

Use these without looking at the code.

1. What is `catalog.py`?
2. What are the two main variables in the file?
3. What is the difference between `VECTORS` and `GT_PROGRAMS`?
4. Why does NanoGT need a catalog of precedent programs?
5. Which file imports `VECTORS` and `GT_PROGRAMS`?
6. How does catalog data get into the SQLite database?
7. Why might editing `catalog.py` not change existing results?
8. What does `cargo_limit_bp` mean?
9. Why does `cds_bp` matter?
10. Why does `tissue_tropism` matter?
11. Why does `approval_status` matter?
12. Why does `protein_class` matter?
13. Why does `inheritance` matter?
14. Why does `pathway` matter?
15. What are the main scientific limitations of this file?
16. What are the main coding/design limitations of this file?
17. How would you make this file more research-grade?
18. How would you add citations to the catalog?
19. How would you test that all programs reference valid vectors?
20. How would you explain this file to a non-coder?

---

## 14. Mini self-test

Close the code and try to say this out loud:

> `catalog.py` stores the curated vector and gene therapy precedent data for NanoGT. `VECTORS` describes delivery vehicle properties, and `GT_PROGRAMS` describes real clinical programs. `db.py` imports these lists and seeds them into SQLite. `scoring.py` later uses the seeded data to compare a new disease/gene against existing precedents. The file is central because the scoring output is only as reliable as the catalog data. Its main limitations are that the data is hardcoded, simplified, not fully citation-auditable, and not automatically reseeded after edits.

If you can say that from memory, you understand the backbone of this file.

---

## 15. Flashcards to make

These have also been written to an Anki-importable text file on the Desktop.

Recommended Anki import settings:
- File type: tab-separated values / `.txt` or `.tsv`
- Field 1: Front
- Field 2: Back
- Field 3: Tags
- Do not import the first line as a header, because the file has no header.

Suggested tags:
- `nanogt`
- `catalog_py`
- `architecture`
- `limitations`
- `future_directions`

---

## 16. Final high-level summary

`catalog.py` is one of the most important files in NanoGT because it defines the biomedical precedent universe that the algorithm can reason over.

It is easy to underestimate this file because it looks like “just data”. But for this project, the data is the scientific foundation.

If the catalog is strong, sourced, validated, and well-designed, the rest of the NanoGT pipeline becomes more credible.

If the catalog is weak, outdated, biased, or unsourced, then even a beautifully written scoring algorithm will produce fragile results.

So when studying this file, focus on both:

1. Coding understanding:
   - Lists, dictionaries, imports, database seeding.

2. Scientific understanding:
   - Vector choice, tissue tropism, clinical precedent, approval maturity, protein class, inheritance, biological pathway, evidence quality.

This file is where biomedical curation becomes computational input.
