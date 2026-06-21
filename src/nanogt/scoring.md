# Code Study Note: `src/nanogt/scoring.py`

File studied: `/Users/suzie/Projects/nano-rare-gt/src/nanogt/scoring.py`

Related files:
- `src/nanogt/catalog.py`
- `src/nanogt/db.py`
- `src/nanogt/report.py`
- `src/nanogt/disease.py`
- `src/nanogt/gene.py`
- `src/nanogt/schema.sql`
- `tests/test_nanogt.py`

Study goal:
Understand what `scoring.py` is, why it exists, how it scores gene therapy precedents, what each line-range does in code order, what every scoring dimension means biologically, and what assumptions/weaknesses/improvements matter for a non-coder biomedical researcher reading beside the Python file.

---

## 1. Plain-English identity

`scoring.py` is the main scoring engine of NanoGT.

It takes one query disease and one query gene, then compares them against every gene therapy program in the NanoGT catalog/database.

For each existing gene therapy program, it asks:

```text
How useful is this program as a precedent for the query disease/gene?
```

It answers that question using 12 scoring dimensions.

The easiest mental model:

```text
scoring.py = NanoGT's comparison and ranking algorithm
```

Or even more simply:

```text
query disease/gene + known GT programs → scored and ranked precedent matches
```

---

## 2. Why this file exists

NanoGT needs a way to move from biomedical facts to a ranked recommendation.

The project has facts such as:
- Disease name.
- Orphanet ID.
- Inheritance.
- Affected tissues.
- HPO terms.
- Gene coding sequence length.
- Protein location.
- Existing GT programs.
- Vector cargo capacities.
- Vector tissue tropism.
- Approval status.

But those facts are not useful until the software compares them.

`scoring.py` exists to perform that comparison systematically.

It turns many separate facts into:

```text
ScoreBreakdown(program_name='Zolgensma', composite_score=..., confidence='...', notes=[...])
```

That `ScoreBreakdown` is then passed to `report.py`, which makes the human-readable Markdown report.

---

## 3. How this file fits into the project data flow

High-level data flow:

```text
catalog.py
  defines vectors and gene therapy programs
        ↓
db.py
  seeds those records into SQLite tables
        ↓
disease.py + gene.py
  create DiseaseInfo and GeneInfo for the query disease/gene
        ↓
scoring.py
  compares the query disease/gene against every GT program
        ↓
rank_programs()
  returns a ranked list of ScoreBreakdown objects
        ↓
report.py
  formats the ranked list into Markdown
```

More concrete flow:

```text
DiseaseInfo + GeneInfo + SQLite connection
              ↓
          rank_programs()
              ↓
  reads gt_programs and vectors tables
              ↓
    calls score_program() once per GT program
              ↓
  each score_program() calls all 12 dimension functions
              ↓
        returns ScoreBreakdown objects
              ↓
     sorted highest composite score first
```

Important point:

```text
scoring.py does not create the catalog data. It consumes the catalog data.
```

---

## 4. The 12 scoring dimensions at a glance

`scoring.py` scores each program using these dimensions:

| # | Dimension | Max score | What it asks |
|---:|---|---:|---|
| 1 | Packaging fit | 2.0 | Does the query gene fit inside the vector? |
| 2 | Tissue tropism | 2.0 | Does the vector/program reach the disease tissue? |
| 3 | Protein class | 2.0 | Is the query protein similar to the precedent protein type? |
| 4 | Inheritance compatibility | 1.0 | Is the inheritance pattern compatible with gene replacement? |
| 5 | Pathway similarity | 2.0 | Is the biological disease pathway similar? |
| 6 | Approval weight | 1.0 | How mature/regulatorily proven is the precedent? |
| 7 | Immunogenicity | 2.0 | Are pre-existing antibodies against the vector likely? |
| 8 | Therapeutic window | 2.0 | Can treatment happen before irreversible damage? |
| 9 | Cross-correction | 1.0 | Can corrected cells rescue uncorrected neighbours? |
| 10 | Immune privilege | 1.0 | Is the target tissue somewhat protected from immune attack? |
| 11 | Promoter availability | 1.0 | Are good tissue-specific promoters available? |
| 12 | Route of administration feasibility | 1.0 | Is there a practical delivery route to the target tissue? |

Total raw maximum:

```text
2 + 2 + 2 + 2 + 1 + 2 + 1 + 2 + 2 + 1 + 1 + 1 + 1 = 20
```

The raw score is normalised to 10:

```text
composite = raw_sum / 20 × 10
```

---

## 5. Top-level structure of the file

The file is organised in a clear order:

```text
Lines 1-20      Docstring: explains the 13-dimensional scoring engine
Lines 22-43     Plain-English comments and max score totals
Lines 45-52     Imports
Line 54         _RAW_MAX constant
Lines 57-106    ScoreBreakdown dataclass
Lines 112-137   Dimension 1: score_packaging()
Lines 143-181   Dimension 2: score_tropism()
Lines 188-216   Dimension 3: score_protein_class()
Lines 222-248   Dimension 5: score_inheritance()
Lines 254-313   Dimension 6: pathway groups, _infer_pathway(), score_pathway()
Mechanism module Dimension 4: source-linked mechanism/modality compatibility
Lines 319-332   Dimension 7: approval scores and score_approval()
Lines 348-380   Dimension 8: seroprevalence table and score_immunogenicity()
Lines 394-445   Dimension 9: score_therapeutic_window()
Lines 463-491   Dimension 10: score_cross_correction()
Lines 510-536   Dimension 11: immune privilege table and score_immune_privilege()
Lines 552-578   Dimension 12: promoter table and score_promoter_availability()
Lines 595-621   Dimension 13: route table and score_roa_feasibility()
Lines 627-755   score_program(): combines all 13 scores for one program
Lines 761-783   rank_programs(): scores and ranks all programs in the database
```

The two most important functions to understand are:

```python
score_program()
rank_programs()
```

The 13 dimension functions are the building blocks used by `score_program()`.

---

## 6. Line-range walkthrough in code order

## Lines 1-20: File docstring

The docstring says this is a:

```text
13-dimension scoring engine
```

It states the basic purpose:

```text
For a given disease/gene/tissue tuple, score each GT program in the catalog as a potential precedent/surrogate.
```

Important wording:

- `precedent` means an existing program that gives useful clinical or technical evidence.
- `surrogate` means a proxy example, not necessarily the exact same disease.

For example, a CNS AAV9 program for SMA may be a precedent for another neurological monogenic disease, even if the disease biology is different.

---

## Lines 22-43: Plain-English file identity and raw score maxima

These comments call the file:

```text
THE ALGORITHM
```

They also list the maximum raw score for each dimension.

This matters because not all dimensions have equal weight.

Dimensions worth 2.0 have double the weight of dimensions worth 1.0.

High-weight dimensions:
- Packaging fit.
- Tissue tropism.
- Protein class.
- Pathway similarity.
- Immunogenicity.
- Therapeutic window.

Lower-weight dimensions:
- Inheritance match.
- Approval weight.
- Cross-correction.
- Immune privilege.
- Promoter availability.
- Route of administration.

This weighting is a scientific modelling choice.

---

## Lines 45-52: Imports

```python
from __future__ import annotations
import json
from dataclasses import dataclass, field
from typing import Optional
import sqlite3

from .disease import DiseaseInfo
from .gene import GeneInfo
```

| Import | Plain-English meaning | Used? |
|---|---|---|
| `annotations` future import | Makes type hints easier/more flexible | Yes, safe typing support |
| `json` | Reads JSON text into Python objects | Yes, used for vector tissue tropism |
| `dataclass` | Creates simple labelled data containers | Yes, used for `ScoreBreakdown` |
| `field` | Helps create default list fields safely | Yes, used for `notes` |
| `Optional` | Type hint for “value or None” | Imported but not used here |
| `sqlite3` | Python SQLite database library | Yes, used in `rank_programs()` type hint |
| `DiseaseInfo` | Query disease data structure | Yes |
| `GeneInfo` | Query gene/protein data structure | Yes |

Small cleanup note:

`Optional` could be removed because this file does not use it.

---

## Line 54: `_RAW_MAX`

```python
_RAW_MAX = 20.0
```

This is the maximum possible raw score across all 13 dimensions.

It is used here:

```python
composite = round((raw_sum / _RAW_MAX) * 10.0, 2)
```

The leading underscore means this is intended as an internal constant.

Beginner mental model:

```text
_RAW_MAX is the denominator used to convert raw scores into a 0-10 score.
```

---

## 7. `ScoreBreakdown` dataclass: lines 57-106

`ScoreBreakdown` is the result object for one program comparison.

One `ScoreBreakdown` answers:

```text
How did one GT program score against the query disease/gene?
```

If the database contains 18 GT programs, then `rank_programs()` will produce 18 `ScoreBreakdown` objects.

### Main metadata fields: lines 60-67

| Field | Meaning |
|---|---|
| `program_name` | Name of the precedent program, e.g. Zolgensma |
| `program_disease` | Disease the precedent program was designed for |
| `vector` | Vector used by the precedent program, e.g. AAV9 |
| `tissue_target` | Tissue/cell type targeted by the precedent |
| `approval_status` | Approved, phase2, phase1/2, etc. |
| `composite_score` | Final score out of 10 |
| `confidence` | `high`, `medium`, `low`, or `fail` |

### Original six dimensions: lines 68-74

| Field | Range | Meaning |
|---|---:|---|
| `packaging_fit` | 0-2 | Gene size versus vector cargo limit |
| `tropism_match` | 0-2 | Disease tissues versus vector/program target |
| `protein_class_match` | 0-2 | Similar protein class/type |
| `inheritance_match` | 0-1 | Inheritance compatibility |
| `pathway_similarity` | 0-2 | Biological pathway similarity |
| `approval_weight` | 0-1 | Regulatory/clinical maturity |

### Additional six dimensions: lines 76-104

| Field | Range | Meaning |
|---|---:|---|
| `immunogenicity` | 0-2 | Pre-existing antibody problem for vector |
| `therapeutic_window` | 0-2 | Timing feasibility before irreversible disease |
| `cross_correction` | 0-1 | Whether corrected cells can help neighbours |
| `immune_privilege` | 0-1 | Whether target tissue has reduced immune exposure |
| `promoter_availability` | 0-1 | Availability of validated promoters |
| `roa_feasibility` | 0-1 | Practicality of delivery route |

### Notes field: line 106

```python
notes: list[str] = field(default_factory=list)
```

This stores plain-English explanations for the scores.

Important beginner concept:

The code uses `field(default_factory=list)` instead of `notes: list[str] = []`.

Why?

Because mutable defaults like lists can accidentally be shared between objects. `default_factory=list` creates a fresh empty list for each `ScoreBreakdown`.

---

# 8. Dimension 1: Packaging fit, lines 109-137

Function:

```python
score_packaging(disease_gene, program_cds, vector_cargo)
```

Max score: 2.0

Question it asks:

```text
Can the query gene physically fit inside the precedent program's vector?
```

This is the first dimension because it is a hard gate.

If the gene is too big, the program fails immediately.

---

## 8.1 Inputs

| Input | Meaning |
|---|---|
| `disease_gene` | The query gene's `GeneInfo` object |
| `program_cds` | CDS size of the precedent program's gene |
| `vector_cargo` | Maximum cargo size of the vector |

Line 119:

```python
gene_cds = disease_gene.cds_length_bp or program_cds
```

Plain English:

```text
Use the query gene CDS length if known. If it is missing, use the precedent program's CDS size as a fallback proxy.
```

This prevents scoring from crashing when the query gene size is missing.

But it is also a scientific assumption. Using the precedent CDS as a proxy may be inaccurate.

---

## 8.2 Hard fail logic: lines 121-123

```python
if gene_cds > vector_cargo:
    return 0.0, ["Gene CDS ... exceeds vector cargo ... — hard fail"]
```

If the query gene is larger than the vector cargo limit, the score is 0.0 and the whole program is marked as `fail` later in `score_program()`.

Biomedical meaning:

AAV vectors have limited packaging capacity. If the therapeutic cassette is too large, standard single-vector AAV delivery is not feasible.

Important caveat:

The code compares CDS length only. Real vector design must also include:
- Promoter.
- PolyA signal.
- Regulatory elements.
- Inverted terminal repeats for AAV.
- Other construct elements.

So the real packaging margin is tighter than the CDS-only estimate.

---

## 8.3 Ratio scoring: lines 125-137

If the gene fits, the code calculates:

```python
ratio = gene_cds / vector_cargo
```

Then it scores:

| Cargo utilisation | Score | Meaning |
|---:|---:|---|
| `<= 30%` | 2.0 | Excellent room left |
| `<= 60%` | 1.5 | Good fit |
| `<= 85%` | 1.0 | Tight but workable |
| `> 85%` | 0.5 | Very tight; high packaging/design risk |
| `> 100%` | hard fail | Does not fit |

The note reports the exact ratio, such as:

```text
Gene CDS 3000bp / cargo 4700bp (64% utilized)
```

---

# 9. Dimension 2: Tissue tropism, lines 140-181

Function:

```python
score_tropism(disease_tissues, vector_tropism, program_tissue_target=None)
```

Max score: 2.0

Question it asks:

```text
Does the vector and/or precedent program target tissues relevant to the query disease?
```

Tissue targeting is central because gene therapy only works if the therapeutic gene reaches the cells that need it.

---

## 9.1 Inputs

| Input | Meaning |
|---|---|
| `disease_tissues` | Tissues affected by the query disease, e.g. CNS, muscle, retina |
| `vector_tropism` | Tissues the vector naturally tends to reach |
| `program_tissue_target` | Tissue target of the precedent program |

Line 149:

```python
if not disease_tissues:
    return 1.0, ["No tissue data — neutral score"]
```

If the disease tissue list is missing, the code gives a neutral score of 1.0 out of 2.0.

This avoids over-penalising missing data, but it also hides uncertainty.

---

## 9.2 Set matching: lines 152-154

```python
disease_set = set(t.lower() for t in disease_tissues)
vector_set = set(t.lower() for t in vector_tropism)
overlap = disease_set & vector_set
```

Plain English:

```text
Lowercase all tissue labels, remove duplicates, then find tissues present in both lists.
```

The `&` operator means intersection.

Example:

```text
disease tissues = {CNS, muscle}
vector tropism  = {CNS, liver, heart}
overlap         = {CNS}
```

---

## 9.3 Precedent target matching: lines 156-164

The function also checks whether the precedent program's target tissue text mentions the disease tissue.

Special handling for `CNS`:

```python
if tissue == "cns":
    return any(word in target for word in ("cns", "brain", "spinal", "motor neuron", "neuron"))
```

This means a target like `CNS/motor neuron` can match a disease tissue labelled `CNS`.

This is helpful because biomedical tissue labels are often not identical strings.

---

## 9.4 Scoring logic: lines 167-181

| Condition | Score | Meaning |
|---|---:|---|
| Direct target match and vector overlap | 2.0 | Best case: vector and precedent both support target tissue |
| Direct target match only | 1.5 | Precedent aimed at the right tissue |
| Two or more vector overlaps | 1.5 | Vector covers multiple disease tissues |
| One vector overlap | 1.0 | Partial tissue match |
| No overlap | 0.3 | Poor tissue fit |
| Missing disease tissue data | 1.0 | Neutral |

Example interpretation:

AAV9 for SMA may score highly for a CNS disease because:
- AAV9 tropism includes CNS.
- Zolgensma/OAV101 target motor neurons/CNS.

---

# 10. Dimension 3: Protein class, lines 185-216

Function:

```python
score_protein_class(gene_info, program_class)
```

Max score: 2.0

Question it asks:

```text
Is the query gene's protein similar in biological class to the precedent program's protein?
```

Protein class matters because the delivery strategy depends on where the protein works.

---

## 10.1 Biomedical idea

Different protein types behave differently after gene delivery:

| Protein class | Why it matters |
|---|---|
| Secreted | One corrected cell may secrete protein that helps other cells/systemic tissues |
| Lysosomal | Enzymes may cross-correct via uptake pathways such as mannose-6-phosphate receptor |
| Membrane | Protein often must be expressed in the correct cell membrane |
| Intracellular | Each relevant cell usually needs its own corrected gene expression |

Secreted and lysosomal proteins are often easier for gene therapy because not every single cell must be transduced.

---

## 10.2 How the code infers the query protein class: lines 197-203

The function uses `GeneInfo` fields:

```python
kws = [k.lower() for k in gene_info.keywords]
locs = [l.lower() for l in gene_info.subcellular_location]
```

Then it checks:

```python
is_secreted_gene
is_lysosomal_gene
is_membrane_gene
```

These are inferred from UniProt-like keywords and subcellular location strings.

Example:
- If location contains `secreted`, the gene is treated as secreted.
- If location contains `lysosome` or keywords include `lysosome`, it is treated as lysosomal.
- If location contains `membrane`, it is treated as membrane-associated.

---

## 10.3 Scoring logic: lines 206-216

| Condition | Score | Meaning |
|---|---:|---|
| Program is lysosomal and query gene is lysosomal | 2.0 | Strong match; cross-correction likely |
| Program is secreted and query gene is secreted | 2.0 | Strong systemic/secreted precedent |
| Program is intracellular and query appears intracellular | 1.5 | Good intracellular match |
| Program is membrane and query is membrane | 1.5 | Good membrane match |
| Query is secreted or lysosomal but not exact match | 1.0 | Partial extracellular/lysosomal relevance |
| Otherwise | 0.5 | Protein class mismatch |

Important limitation:

The program's protein class comes from catalog data, while the query gene's class is inferred from `GeneInfo`. If either source is oversimplified, the score may be wrong.

---

# 11. Dimension 4: Inheritance compatibility, lines 219-248

Function:

```python
score_inheritance(disease_inheritance, program_inheritance)
```

Max score: 1.0

Question it asks:

```text
Is the query disease's inheritance pattern compatible with gene replacement precedents?
```

---

## 11.1 Biomedical idea

Many AAV gene therapies are gene replacement or gene addition strategies.

These usually fit best when the disease is caused by loss of function.

Common loss-of-function-friendly patterns:
- Autosomal recessive (AR).
- X-linked recessive/loss-of-function contexts (XL).

Dominant diseases can be harder because simply adding a healthy copy may not fix a toxic or dominant-negative mutant protein.

Dominant disease may require:
- Allele-specific silencing.
- Gene editing.
- Knockdown plus replacement.
- Other more complex strategies.

---

## 11.2 Missing inheritance: lines 230-231

```python
if not disease_inheritance:
    return 0.5, ["Unknown inheritance"]
```

Missing inheritance gets a neutral-ish score of 0.5 out of 1.0.

This avoids over-penalising unknown data.

---

## 11.3 Exact and partial logic: lines 233-248

The code lowercases inheritance strings, then checks:

| Condition | Score | Meaning |
|---|---:|---|
| Query is autosomal recessive and program is AR | 1.0 | Exact AR match |
| Query is X-linked and program is XL | 1.0 | Exact XL match |
| Query is recessive/X-linked and program is AR/XL | 0.7 | General loss-of-function compatibility |
| Otherwise | 0.3 | Dominant/mitochondrial/other mismatch or more complex biology |
| Unknown query inheritance | 0.5 | Neutral |

Important coding detail:

The code checks for exact string membership:

```python
"autosomal recessive" in di_lower
```

This means data formatting matters. If the inheritance string is phrased differently, matching could be weaker than expected.

---

# 12. Dimension 5: Pathway similarity, lines 251-313

Main pieces:

```python
_PATHWAY_GROUPS
_infer_pathway()
score_pathway()
```

Max score: 2.0

Question it asks:

```text
Is the query disease/gene biology similar to the precedent program's disease pathway?
```

---

## 12.1 `_PATHWAY_GROUPS`: lines 254-266

`_PATHWAY_GROUPS` defines which pathways are considered related.

Examples:

| Inferred pathway | Related group |
|---|---|
| `lysosomal_storage` | `lysosomal_storage` |
| `coagulation` | `coagulation` |
| `motor_neuron` | `motor_neuron`, `myopathy` |
| `myopathy` | `myopathy`, `motor_neuron` |
| `retinal_visual_cycle` | `retinal_visual_cycle`, `retinal_phototransduction` |
| `amino_acid_metabolism` | `amino_acid_metabolism`, `urea_cycle` |
| `urea_cycle` | `urea_cycle`, `amino_acid_metabolism` |
| `mitochondrial_complex` | `mitochondrial_complex`, `retinal_visual_cycle` |

This is a manually curated similarity map.

It lets the algorithm say:

```text
These two pathways are not identical, but they are related enough to get partial credit.
```

---

## 12.2 `_infer_pathway()`: lines 269-291

Function:

```python
_infer_pathway(disease, gene)
```

This helper tries to infer the query disease pathway from:
- Gene keywords.
- Gene GO terms.
- Gene subcellular location.
- Disease HPO terms.
- Disease affected tissues.

It checks for word patterns.

Examples:

| If it sees... | It infers... |
|---|---|
| `lysosom` in location or HPO | `lysosomal_storage` |
| `coagulat` in keywords or HPO | `coagulation` |
| `retina` in tissues or HPO | `retinal_visual_cycle` |
| `motor neuron` or `spinal cord` in HPO | `motor_neuron` |
| `muscul` or `myopat` in HPO | `myopathy` |
| `amino acid` or `phenylalan` in keywords | `amino_acid_metabolism` |
| `urea` or `nitrogen` in keywords | `urea_cycle` |
| `mitochondri` in keywords | `mitochondrial_complex` |
| None of the above | `unknown` |

Beginner note:

This is not machine learning. It is rule-based keyword matching.

---

## 12.3 `score_pathway()`: lines 294-313

Function:

```python
score_pathway(disease, gene, program_pathway)
```

It first infers the query pathway:

```python
inferred = _infer_pathway(disease, gene)
```

Then compares it to the program's pathway from the catalog.

Scoring:

| Condition | Score | Meaning |
|---|---:|---|
| Program pathway is in the inferred pathway group | 2.0 | Strong pathway match |
| Inferred and program pathways are related by group mapping | 1.5 | Related pathway |
| Inferred pathway is known but different | 0.5 | Different biology |
| Inferred pathway is unknown | 1.0 | Neutral |

Scientific limitation:

Pathway inference is simplified. It may miss important biology if the HPO/GO/keyword terms do not contain the expected words.

---

# 13. Dimension 6: Approval weight, lines 316-332

Main pieces:

```python
_APPROVAL_SCORES
score_approval()
```

Max score: 1.0

Question it asks:

```text
How clinically mature is the precedent program?
```

---

## 13.1 `_APPROVAL_SCORES`: lines 319-327

The file assigns scores by regulatory/trial status:

| Status | Score |
|---|---:|
| `approved` | 1.0 |
| `withdrawn` | 0.7 |
| `phase3` | 0.8 |
| `phase2/3` | 0.7 |
| `phase2` | 0.6 |
| `phase1/2` | 0.5 |
| `phase1` | 0.4 |
| Unknown status | 0.3 |

Interesting point:

`withdrawn` gets 0.7, not 0.0.

Why might that make sense?

A withdrawn product may still provide useful precedent about vector, tissue, manufacturing, dosing, or regulatory history, even if it failed commercially or was removed from the market.

But a withdrawn product should also carry caveats.

---

## 13.2 `score_approval()`: lines 330-332

```python
s = _APPROVAL_SCORES.get(status.lower(), 0.3)
return s, [f"Approval status: {status}"]
```

It lowercases the status, looks up the score, and returns a note.

Limitation:

The function does not explain why a program was withdrawn, paused, or unsuccessful.

A future version should distinguish:
- Withdrawn for commercial reasons.
- Withdrawn for safety reasons.
- Failed efficacy.
- Trial hold.
- Active recruitment.
- Approved in one region but not another.

---

# 14. Dimension 7: Immunogenicity, lines 335-380

Main pieces:

```python
_SEROPREVALENCE
score_immunogenicity()
```

Max score: 2.0

Question it asks:

```text
How much of a problem are pre-existing neutralising antibodies against this vector?
```

---

## 14.1 Biomedical idea

Many people have already been exposed to natural AAVs.

If a patient has neutralising antibodies against a vector, they may be excluded from treatment or at higher risk of poor vector delivery.

Lower seroprevalence is better.

In this model:

```text
Low antibody prevalence → higher score
High antibody prevalence → lower score
```

---

## 14.2 `_SEROPREVALENCE`: lines 348-357

Approximate population seroprevalence values:

| Vector | Approx seroprevalence | Model interpretation |
|---|---:|---|
| `AAV1` | 20% | Moderate/high |
| `AAV2` | 55% | Very high |
| `AAV5` | 9% | Low/favourable |
| `AAV8` | 30% | High |
| `AAV9` | 22% | High/moderate |
| `AAVrh10` | 10% | Low-moderate |
| `AAV2/6` | 17% | Moderate |
| `LV` | 2% | Low |

The comments cite broad source families:
- Boutin et al. 2010.
- Calcedo et al. 2011.
- Mingozzi & High 2013.

But the code does not store formal citation objects.

---

## 14.3 Scoring logic: lines 365-380

| Seroprevalence | Score | Meaning |
|---:|---:|---|
| `< 10%` | 2.0 | Low; most patients eligible |
| `< 20%` | 1.5 | Moderate; screening/exclusion needed |
| `< 40%` | 1.0 | High; substantial exclusions expected |
| `>= 40%` | 0.5 | Very high; major trial design challenge |
| Unknown vector | Uses 25% default | Score usually 1.0 |

Line 365:

```python
sero = _SEROPREVALENCE.get(vector_serotype, 0.25)
```

If the vector is not in the table, the code assumes 25% seroprevalence.

Limitation:

Real seroprevalence depends on geography, age, assay, titre threshold, and patient population.

---

# 15. Dimension 8: Therapeutic window, lines 383-445

Function:

```python
score_therapeutic_window(disease)
```

Max score: 2.0

Question it asks:

```text
Is there enough time to deliver gene therapy before irreversible damage occurs?
```

---

## 15.1 Biomedical idea

Gene therapy is most useful if target cells are still alive and recoverable.

A disease with adult onset or slow progression often has a wider treatment window.

A congenital, neonatal, or rapidly fatal disease may need treatment immediately after birth or even before birth.

That makes clinical development much harder.

---

## 15.2 How the code detects timing clues: lines 396-419

The function combines disease HPO terms and disease name:

```python
combined = (" ".join(disease.hpo_terms) + " " + disease.name).lower()
```

Then it searches for keyword groups:

| Variable | Example trigger words |
|---|---|
| `neonatal` | neonatal onset, congenital, in utero, fetal, antenatal, hydrops |
| `rapidly_fatal` | death in infancy, lethal, fatal in infancy |
| `progressive` | neurodegenerative, progressive, brain atrophy, white matter |
| `early_childhood` | early-onset, infantile, childhood onset, pediatric |
| `adult_onset` | adult onset, late onset, adolescent onset |
| `chronic` | chronic, slowly progressive, episodic, relapsing |
| `irreversible` | intellectual disability, neurodegenerative, cirrhosis, fibrosis, brain atrophy |

This is rule-based text matching.

---

## 15.3 Scoring logic: lines 421-445

| Disease timing pattern | Score | Meaning |
|---|---:|---|
| Adult onset OR chronic without irreversible damage | 2.0 | Wide therapeutic window |
| Progressive but not neonatal | 1.5 | Moderate window; early intervention recommended |
| Early childhood, not neonatal, not rapidly fatal | 1.2 | Moderate-to-narrow window |
| Neonatal but not rapidly fatal | 0.8 | Narrow; treatment needed within weeks |
| Otherwise | 0.5 | Very narrow; congenital/rapidly fatal/in utero or immediate neonatal treatment may be needed |

Important project detail:

This score depends only on the query disease, not on the precedent program.

So for one query disease, every GT program receives the same therapeutic-window score.

---

# 16. Dimension 9: Cross-correction, lines 448-491

Function:

```python
score_cross_correction(gene)
```

Max score: 1.0

Question it asks:

```text
Can corrected/transduced cells help neighbouring uncorrected cells?
```

---

## 16.1 Biomedical idea

Cross-correction is very important in gene therapy.

If only some cells receive the vector, they may produce a protein that helps other cells too.

This is especially relevant for:
- Secreted proteins.
- Lysosomal enzymes.

It is less helpful for:
- Intracellular proteins.
- Membrane-bound proteins.

Why it matters:

```text
High cross-correction → fewer cells need to be transduced → potentially lower dose and safer therapy
```

---

## 16.2 How the code detects cross-correction: lines 465-470

The function checks:

```python
is_secreted
is_lysosomal
```

based on gene subcellular location and keywords.

---

## 16.3 Scoring logic: lines 471-491

| Protein property | Score | Meaning |
|---|---:|---|
| Secreted and lysosomal | 1.0 | Maximum cross-correction via M6P-like pathway |
| Secreted | 1.0 | Systemic/extracellular benefit possible |
| Lysosomal but not clearly secreted | 0.8 | Moderate cross-correction possible |
| Intracellular or membrane-bound | 0.2 | Little/no cross-correction; each target cell needs delivery |

Important distinction:

This dimension scores the query gene's protein, not the precedent program's protein.

So it is the same across all programs for one query disease/gene.

---

# 17. Dimension 10: Immune privilege, lines 494-536

Main pieces:

```python
_IMMUNE_PRIVILEGE_SCORES
score_immune_privilege()
```

Max score: 1.0

Question it asks:

```text
Are the disease target tissues relatively protected from immune attack?
```

---

## 17.1 Biomedical idea

Some tissues are partially separated from systemic immune surveillance.

Examples:
- Retina: blood-retinal barrier and local immunosuppressive environment.
- CNS: blood-brain barrier.
- Liver: tolerogenic immune environment.

In gene therapy, immune privilege can help because transduced cells may be less likely to be destroyed by immune responses.

---

## 17.2 `_IMMUNE_PRIVILEGE_SCORES`: lines 510-518

| Tissue | Score | Model meaning |
|---|---:|---|
| `retina` | 1.0 | Highest immune privilege |
| `cns` | 0.9 | High privilege |
| `liver` | 0.8 | Moderate-high/tolerogenic |
| `muscle` | 0.6 | Moderate surveillance |
| `heart` | 0.6 | Moderate |
| `kidney` | 0.5 | Moderate-low |
| `hematopoietic` | 0.3 | Low privilege |
| Unknown tissue | 0.5 | Standard/neutral assumption |

---

## 17.3 `score_immune_privilege()`: lines 521-536

If no tissue data exists:

```python
return 0.5, ["No tissue data — neutral immune privilege score applied"]
```

If multiple tissues exist, the function picks the best-scoring tissue.

Example:

```text
disease tissues = [CNS, kidney]
CNS score = 0.9
kidney score = 0.5
returned score = 0.9
```

Important assumption:

The code uses the best tissue, not the average or worst tissue.

That can make a multi-system disease look more feasible than it really is.

---

# 18. Dimension 11: Promoter availability, lines 539-578

Main pieces:

```python
_PROMOTER_DATA
score_promoter_availability()
```

Max score: 1.0

Question it asks:

```text
Are there validated promoters that can drive expression in the target tissue?
```

---

## 18.1 Biomedical idea

A promoter controls when, where, and how strongly a therapeutic gene is expressed.

Promoters matter for:
- Efficacy: expression in the right cells.
- Safety: avoiding off-target expression.
- Regulatory confidence: prior clinical validation helps.

Some tissues have many validated promoters. Others have few.

---

## 18.2 `_PROMOTER_DATA`: lines 552-560

| Tissue | Score | Examples/meaning |
|---|---:|---|
| `liver` | 1.0 | ApoE/hAAT, TBG, transthyretin, albumin; strong clinical precedent |
| `retina` | 1.0 | VMD2, RPGR, GRK1, CRX, IRBP; strong retinal precedent |
| `cns` | 0.8 | Synapsin-1, CaMKII, GFAP; useful but cell-specificity varies |
| `muscle` | 0.8 | MHCK7, CK8, Desmin; used in muscle programs |
| `hematopoietic` | 0.7 | EFS, PGK, SFFV; ex vivo lentiviral precedent |
| `heart` | 0.6 | Some cardiac promoters, less clinical use |
| `kidney` | 0.4 | Few clinical-grade kidney-specific promoters |
| Unknown tissue | 0.5 | Limited validated promoters assumed |

---

## 18.3 `score_promoter_availability()`: lines 563-578

Like immune privilege, this function:
- Returns 0.5 if tissue data is missing.
- Loops through disease tissues.
- Chooses the best-scoring tissue.

Important assumption:

A multi-tissue disease may need expression in several tissues, but this function gives credit for the easiest/best tissue.

A future version might score:
- Primary tissue only.
- Average across tissues.
- Worst required tissue.
- Weighted tissues based on disease severity.

---

# 19. Dimension 12: Route of administration feasibility, lines 581-621

Main pieces:

```python
_ROA_DATA
score_roa_feasibility()
```

Max score: 1.0

Question it asks:

```text
Is there an accessible and clinically established way to deliver the vector to the target tissue?
```

RoA means route of administration.

---

## 19.1 Biomedical idea

Vector tropism alone is not enough.

You also need a practical delivery route.

Examples:
- Liver: intravenous systemic delivery is established.
- Retina: subretinal/intravitreal injection is specialised but established.
- CNS: intrathecal/ICV delivery is invasive but clinically used.
- Hematopoietic: ex vivo HSC approach is complex but precise.
- Kidney: less established in clinical gene therapy.

---

## 19.2 `_ROA_DATA`: lines 595-603

| Tissue | Score | Meaning |
|---|---:|---|
| `liver` | 1.0 | IV systemic delivery is established |
| `muscle` | 0.9 | IV or intramuscular delivery established |
| `hematopoietic` | 0.9 | Ex vivo HSC delivery complex but proven |
| `retina` | 0.8 | Subretinal/intravitreal injection established |
| `cns` | 0.7 | Intrathecal/ICV possible but invasive |
| `heart` | 0.6 | Cardiac delivery technically demanding |
| `kidney` | 0.4 | No well-established kidney-specific clinical route |
| Unknown tissue | 0.5 | Route not well established/neutral |

---

## 19.3 `score_roa_feasibility()`: lines 606-621

This function behaves like the promoter and immune privilege functions:
- If no tissue data, return 0.5.
- If multiple tissues, choose the best-scoring one.
- Return one score and one explanatory note.

Again, the “best tissue wins” assumption may overestimate feasibility for multi-organ disease.

---

# 20. `score_program()`: lines 624-755

Function:

```python
score_program(disease, gene, program, vector)
```

This is the main scoring function for one GT program.

It combines all 12 scoring dimensions into one `ScoreBreakdown`.

Plain-English question:

```text
Given this query disease/gene, how good a precedent is this one specific GT program?
```

---

## 20.1 Inputs

| Input | Meaning |
|---|---|
| `disease` | Query `DiseaseInfo` |
| `gene` | Query `GeneInfo` |
| `program` | One GT program row from the database/catalog |
| `vector` | The vector row matching that program's vector |

Example conceptual call:

```python
score_program(
    disease=KohlschutterTonzInfo,
    gene=ROGDIInfo,
    program=ZolgensmaRow,
    vector=AAV9Row,
)
```

---

## 20.2 Lines 634-638: Start notes and score packaging

```python
notes: list[str] = []
pkg, pkg_notes = score_packaging(gene, program["cds_bp"], vector["cargo_limit_bp"])
notes.extend(pkg_notes)
```

The function starts with an empty notes list.

Then it scores packaging first.

Why packaging first?

Because if the gene cannot fit in the vector, the rest of the scores do not matter.

---

## 20.3 Lines 640-663: Packaging hard fail return

If packaging score is 0.0, the function immediately returns a `ScoreBreakdown` with:
- `composite_score=0.0`
- `confidence="fail"`
- all dimension scores set to 0.0
- notes explaining the packaging failure

This is a hard stop.

The program is not compared further.

Scientific meaning:

```text
A vector precedent is not feasible if the query gene cannot physically fit.
```

Important caveat:

This is only true for the current model of single-vector gene replacement. It does not consider special engineering approaches such as dual AAV or mini-gene strategies.

---

## 20.4 Lines 665-676: Step 2, tropism

The code loads vector tropism:

```python
v_tropism = (
    json.loads(vector["tissue_tropism"])
    if isinstance(vector.get("tissue_tropism"), str)
    else vector.get("tissue_tropism", [])
)
```

Why?

In the database, tissue tropism may be stored as JSON text, such as:

```text
["CNS", "liver", "muscle"]
```

`json.loads()` converts that text back into a Python list.

Then:

```python
trp, trp_notes = score_tropism(...)
notes.extend(trp_notes)
```

---

## 20.5 Lines 678-692: Steps 3-6

The next four scores are calculated:

```python
prc = score_protein_class(...)
inh = score_inheritance(...)
pth = score_pathway(...)
apv = score_approval(...)
```

Each function returns:

```python
(score, notes)
```

Then the notes are appended to the shared `notes` list.

This means one final `ScoreBreakdown` contains all score explanations in one place.

---

## 20.6 Lines 694-724: Steps 7-12

The additional six dimensions are calculated:

```python
imm = score_immunogenicity(program["vector"])
tw = score_therapeutic_window(disease)
cc = score_cross_correction(gene)
ip = score_immune_privilege(disease.affected_tissues)
pa = score_promoter_availability(disease.affected_tissues)
roa = score_roa_feasibility(disease.affected_tissues)
```

Important distinction:

Some scores depend on the precedent program/vector:
- Packaging fit.
- Tissue tropism.
- Protein class partly.
- Inheritance partly.
- Pathway partly.
- Approval weight.
- Immunogenicity.

Some scores depend mainly or entirely on the query disease/gene:
- Therapeutic window.
- Cross-correction.
- Immune privilege.
- Promoter availability.
- Route of administration.

So some values will be identical across all programs for a given disease/gene.

---

## 20.7 Lines 726-732: Final composite score and confidence

Raw sum:

```python
raw_sum = pkg + trp + prc + pth + inh + apv + imm + tw + cc + ip + pa + roa
```

Normalised composite:

```python
composite = round((raw_sum / _RAW_MAX) * 10.0, 2)
```

Confidence:

```python
confidence = "high" if composite >= 7.5 else "medium" if composite >= 5.0 else "low"
```

Confidence thresholds:

| Composite score | Confidence |
|---:|---|
| `>= 7.5` | `high` |
| `>= 5.0` and `< 7.5` | `medium` |
| `< 5.0` | `low` |
| Packaging hard fail | `fail` |

Beginner note:

The compact confidence line is a chained conditional expression. It is equivalent to:

```python
if composite >= 7.5:
    confidence = "high"
elif composite >= 5.0:
    confidence = "medium"
else:
    confidence = "low"
```

---

## 20.8 Lines 734-755: Return `ScoreBreakdown`

The function returns a complete `ScoreBreakdown` containing:
- Program metadata.
- Final composite score.
- Confidence label.
- All 12 individual dimension scores.
- The combined rationale notes.

This object is what `report.py` later reads to make its tables.

---

# 21. `rank_programs()`: lines 758-783

Function:

```python
rank_programs(disease, gene, conn)
```

Plain-English question:

```text
Score every GT program in the database, then rank them from best to worst.
```

---

## 21.1 Inputs

| Input | Meaning |
|---|---|
| `disease` | Query disease info |
| `gene` | Query gene info |
| `conn` | SQLite database connection |

This function does not receive the catalog directly. It reads from the database.

---

## 21.2 Lines 768-773: Read database rows

```python
programs = [dict(r) for r in conn.execute("SELECT * FROM gt_programs").fetchall()]
```

This reads every GT program from the `gt_programs` table and turns each row into a dictionary.

Then:

```python
vectors_by_sero = {
    r["serotype"]: dict(r)
    for r in conn.execute("SELECT * FROM vectors").fetchall()
}
```

This reads all vector rows and creates a dictionary keyed by serotype.

Example shape:

```python
{
    "AAV9": {"serotype": "AAV9", "cargo_limit_bp": 4700, ...},
    "AAV5": {"serotype": "AAV5", "cargo_limit_bp": 4700, ...},
}
```

This makes it easy to find the vector row for each program.

---

## 21.3 Lines 775-780: Score every program

```python
scores: list[ScoreBreakdown] = []
for prog in programs:
    vec = vectors_by_sero.get(prog["vector"])
    if vec is None:
        vec = {"cargo_limit_bp": 4700, "tissue_tropism": "[]"}
    scores.append(score_program(disease, gene, prog, vec))
```

For every GT program:
1. Look up the vector by name.
2. If missing, use a default vector with cargo limit 4700 and no tissue tropism.
3. Call `score_program()`.
4. Add the returned `ScoreBreakdown` to the `scores` list.

Important limitation:

If a vector is missing from the database, the code silently uses a generic AAV-like cargo limit of 4700 bp and no tropism.

That prevents crashes, but it can hide database/catalog errors.

A research-grade version should probably warn or fail loudly.

---

## 21.4 Lines 782-783: Sort and return

```python
scores.sort(key=lambda s: (-s.composite_score, s.program_name))
return scores
```

Sorting logic:

1. Sort by negative composite score.
   - Negative means highest score first.
2. If two programs have the same score, sort alphabetically by program name.

Example:

```text
8.2 Zolgensma
7.4 Luxturna
7.4 Roctavian
```

If Luxturna and Roctavian have equal scores, alphabetical order breaks the tie.

This ranked list is what `report.py` expects.

---

# 22. How all scoring pieces fit together

For one program, the flow is:

```text
score_program()
    ↓
score_packaging()
    ↓ if fail, stop and return fail
score_tropism()
score_protein_class()
score_inheritance()
score_pathway()
score_approval()
score_immunogenicity()
score_therapeutic_window()
score_cross_correction()
score_immune_privilege()
score_promoter_availability()
score_roa_feasibility()
    ↓
raw_sum = all dimensions added
    ↓
composite = raw_sum / 18 × 10
    ↓
confidence = high / medium / low
    ↓
return ScoreBreakdown
```

For all programs:

```text
rank_programs()
    ↓
read all programs from SQLite
    ↓
read all vectors from SQLite
    ↓
call score_program() once per program
    ↓
sort ScoreBreakdown objects by composite score
    ↓
return ranked list
```

---

# 23. Which dimensions are program-specific versus disease/gene-specific?

This is important for interpreting results.

| Dimension | Changes by program? | Why |
|---|---|---|
| Packaging fit | Yes | Different vectors have different cargo limits; program CDS fallback can differ |
| Tissue tropism | Yes | Different vectors/program targets hit different tissues |
| Protein class | Yes partly | Program protein class differs; query gene is fixed |
| Inheritance | Yes partly | Program inheritance differs; query disease is fixed |
| Pathway | Yes partly | Program pathway differs; query inferred pathway is fixed |
| Approval weight | Yes | Each program has its own status |
| Immunogenicity | Yes | Each program uses a vector serotype |
| Therapeutic window | No | It is a property of the query disease |
| Cross-correction | No | It is a property of the query gene/protein |
| Immune privilege | No | It uses the query disease tissues |
| Promoter availability | No | It uses the query disease tissues |
| Route feasibility | No | It uses the query disease tissues |

This means a program can rise or fall in ranking mainly because of:
- Vector fit.
- Target tissue fit.
- Program biology.
- Regulatory precedent.
- Immunogenicity.

But some feasibility factors are shared across all programs for the same query.

---

# 24. Scientific assumptions built into the scoring model

## 24.1 The model assumes gene replacement is the central modality

Inheritance scoring favours recessive and X-linked loss-of-function patterns.

This is sensible for many monogenic rare diseases, but not all.

Less well-covered cases:
- Dominant-negative disease.
- Toxic gain-of-function disease.
- Repeat expansion disorders.
- Mitochondrial DNA diseases.
- Diseases requiring gene editing rather than gene addition.

Improvement:
Add a therapeutic modality dimension:
- Gene replacement.
- Gene silencing.
- Editing.
- Exon skipping.
- RNA therapy.

---

## 24.2 Packaging uses CDS length, not full cassette size

The code compares coding sequence length to vector cargo capacity.

But a real vector cassette includes more than CDS.

Improvement:
Estimate full cassette size:

```text
promoter + CDS + polyA + regulatory elements + vector-specific elements
```

---

## 24.3 Missing gene CDS uses precedent CDS as fallback

Line 119 uses program CDS if the query gene CDS is missing.

This keeps the system running, but it can distort packaging scores.

Improvement:
If query CDS is missing, report an explicit uncertainty warning or fetch from a reliable gene database.

---

## 24.4 Tissue labels are simplified

The model uses labels like `CNS`, `liver`, `retina`, and `muscle`.

Real delivery depends on:
- Cell subtype.
- Route.
- Dose.
- Patient age.
- Species differences.
- Capsid engineering.
- Promoter.
- Blood-brain or blood-retinal barriers.

Improvement:
Use controlled ontology terms and route-specific evidence.

---

## 24.5 Pathway inference is rule-based keyword matching

The pathway system is understandable, but crude.

It may miss diseases whose HPO/GO terms do not contain expected keywords.

Improvement:
Use curated pathway annotations from sources such as Reactome, GO, Orphanet, OMIM, or manual disease-gene curation.

---

## 24.6 Immunogenicity uses approximate population averages

Seroprevalence varies by:
- Geography.
- Age.
- Assay method.
- Antibody titre cutoff.
- Disease cohort.
- Prior exposure.

Improvement:
Store ranges, citations, and population context instead of one number.

---

## 24.7 Best tissue wins for several dimensions

Immune privilege, promoter availability, and RoA feasibility choose the highest-scoring tissue if multiple tissues are affected.

This may overestimate feasibility.

Example:

```text
Disease affects CNS and kidney.
CNS scores well, kidney scores poorly.
The function returns the CNS score.
```

If kidney pathology is clinically important, this may be too optimistic.

Improvement:
Use primary/secondary tissue weights or worst-critical-tissue scoring.

---

## 24.8 Approval status is simplified

A program's clinical maturity is reduced to one label.

But real interpretation depends on:
- Why it was withdrawn.
- Safety outcomes.
- Efficacy outcomes.
- Dose-limiting toxicities.
- Manufacturing feasibility.
- Region of approval.
- Trial population.

Improvement:
Add richer regulatory and evidence fields.

---

# 25. Coding/design weaknesses

## 25.1 Hardcoded scoring thresholds

Many thresholds are written directly in functions.

Examples:
- Packaging ratio cutoffs: 30%, 60%, 85%.
- Confidence thresholds: 7.5 and 5.0.
- Immunogenicity cutoffs: 10%, 20%, 40%.

Improvement:
Move thresholds into a configuration object or documented scoring methods file.

---

## 25.2 No formal validation of program/vector dictionaries

`score_program()` assumes keys exist:

```python
program["cds_bp"]
program["protein_class"]
vector["cargo_limit_bp"]
```

If a key is missing, the code can crash.

Improvement:
Validate database rows or use typed models/dataclasses/Pydantic.

---

## 25.3 Silent fallback for missing vector rows

In `rank_programs()`, if a vector is missing, the code uses:

```python
{"cargo_limit_bp": 4700, "tissue_tropism": "[]"}
```

This can hide data problems.

Improvement:
Raise a warning or error when a program references an unknown vector.

---

## 25.4 Notes are plain strings, not structured evidence

The notes are readable, but they are not machine-auditable.

Improvement:
Use structured notes:

```python
{
    "dimension": "immunogenicity",
    "score": 1.0,
    "rationale": "AAV9 seroprevalence ~22%",
    "source": "Calcedo et al. 2011"
}
```

---

## 25.5 The score is a weighted sum without calibration

The model adds scores and normalises to 10.

This is transparent and easy to explain, but it may not be empirically calibrated.

Improvement:
Validate against known successful/unsuccessful programs or expert scoring panels.

---

## 25.6 `Optional` import is unused

This is minor, but the import can be removed.

Improvement:
Run linting tools such as Ruff to catch unused imports.

---

## 25.7 No explicit model version

If thresholds change, old reports may be hard to interpret.

Improvement:
Add:

```python
SCORING_MODEL_VERSION = "12D-v1-2026-06-03"
```

Then include it in reports.

---

# 26. Improvements that would make `scoring.py` more research-grade

Recommended improvements:

1. Add scoring model metadata:
   - Version.
   - Date.
   - Author/curator.
   - Rationale for each threshold.

2. Add citations for each evidence table:
   - Seroprevalence.
   - Immune privilege.
   - Promoter availability.
   - Route feasibility.
   - Vector cargo limits.

3. Add structured evidence objects instead of plain notes.

4. Validate input data:
   - Program fields.
   - Vector fields.
   - Allowed pathway names.
   - Allowed approval statuses.

5. Improve tissue modelling:
   - Primary versus secondary tissues.
   - Cell-type specificity.
   - Route-specific tropism.
   - Disease severity by tissue.

6. Improve packaging modelling:
   - Full cassette size.
   - AAV ITR constraints.
   - Promoter size.
   - Dual-vector option.
   - Lentiviral/non-viral alternatives.

7. Improve pathway inference:
   - Curated pathway annotations.
   - Reactome/GO/OMIM/Orphanet mapping.
   - Manual overrides.

8. Improve clinical precedent scoring:
   - Safety outcomes.
   - Efficacy magnitude.
   - Trial size.
   - Regulatory region.
   - Withdrawal reason.

9. Add uncertainty scoring:
   - Penalise missing data.
   - Show confidence intervals or evidence grades.
   - Distinguish unknown from neutral.

10. Add tests:
   - Each scoring function expected outputs.
   - Packaging fail behavior.
   - Sorting behavior.
   - Missing vector behavior.
   - Pathway inference behavior.

---

# 27. Things to memorise

Core memory anchors:

1. `scoring.py` is NanoGT's algorithmic core.
2. It compares one query disease/gene against every GT program.
3. One program comparison returns one `ScoreBreakdown`.
4. `rank_programs()` returns a ranked list of `ScoreBreakdown` objects.
5. There are 12 scoring dimensions.
6. Raw maximum score is 18.
7. Composite score is normalised to 10.
8. Packaging is a hard gate: if the gene does not fit, the program fails.
9. Confidence is high at `>= 7.5`, medium at `>= 5.0`, low below 5.0.
10. Report notes come from the scoring functions.
11. Several dimensions use simplified keyword/table lookups.
12. The model is transparent but not fully evidence-audited or clinically calibrated.

Short explanation to practise from memory:

`scoring.py` is the NanoGT scoring engine. It takes a query disease and gene, reads all gene therapy programs and vectors from the database, scores each program across 12 biomedical/translation dimensions, normalises the raw score out of 18 to a composite score out of 10, assigns a confidence label, and returns ranked `ScoreBreakdown` objects for `report.py` to display.

---

# 28. Final mini mental model

```text
One query disease/gene
        ↓
All catalogued GT programs from SQLite
        ↓
For each program:
    packaging
    tropism
    protein class
    inheritance
    pathway
    approval
    immunogenicity
    therapeutic window
    cross-correction
    immune privilege
    promoter availability
    route feasibility
        ↓
Raw score out of 18
        ↓
Composite score out of 10
        ↓
High / medium / low / fail confidence
        ↓
Rank all programs best to worst
```

Simplest version:

```text
scoring.py is a transparent rule-based rubric for ranking GT precedents.
```

---

# 29. Active recall questions

Use these without looking at the code.

1. What is the main purpose of `scoring.py`?
2. What object does one program comparison return?
3. What does `ScoreBreakdown` store?
4. What is `_RAW_MAX`, and why is it 20.0?
5. How is the composite score calculated?
6. What confidence label is assigned to a score of 8.0?
7. What confidence label is assigned to a score of 6.0?
8. What confidence label is assigned to a score of 4.0?
9. What causes `confidence="fail"`?
10. Why is packaging scored first?
11. What does packaging fit measure?
12. What does tissue tropism measure?
13. Why does `score_tropism()` specially handle CNS wording?
14. What does protein class scoring measure?
15. Why are secreted and lysosomal proteins important?
16. What does mechanism/modality compatibility measure?
17. What does inheritance scoring measure?
18. Why are AR and XL diseases often compatible with gene replacement?
19. What does pathway scoring compare?
20. How does `_infer_pathway()` infer a pathway?
21. What does approval weight represent?
22. Why might a withdrawn program still get some credit?
23. What does immunogenicity scoring use as input?
24. Why does lower seroprevalence get a higher score?
25. What does therapeutic window measure?
26. Why do neonatal/rapidly fatal diseases score lower for therapeutic window?
27. What is cross-correction?
28. Which proteins usually have high cross-correction potential?
29. What is immune privilege?
30. Which tissues score highly for immune privilege?
31. Why does promoter availability matter?
32. Why does route of administration matter?
33. Which functions choose the best-scoring tissue when multiple tissues are listed?
34. What does `score_program()` do?
35. What does `rank_programs()` do?
36. How does `rank_programs()` sort tied scores?
37. What happens if a vector is missing from the database?
38. Which scoring assumptions could overestimate feasibility?
39. Which dimensions are based mainly on the query disease/gene rather than the program?
40. What citations or evidence metadata are missing from the current model?
41. How would you make `scoring.py` more research-grade?

---

# 30. Mini self-test

Close the code and try to say this out loud:

> `scoring.py` is NanoGT's rule-based scoring engine. It compares a query disease and gene with each gene therapy program in the database. For each program, it first checks whether the gene fits into the vector, then scores tissue tropism, protein class, mechanism/modality compatibility, inheritance, pathway, approval status, immunogenicity, therapeutic window, cross-correction, immune privilege, promoter availability, and route feasibility. It adds those raw scores to a maximum of 20, normalises the result to 10, assigns high/medium/low confidence, and returns a `ScoreBreakdown`. `rank_programs()` repeats this for all programs and sorts them from best to worst.

If you can say that from memory, you understand the backbone of this file.
