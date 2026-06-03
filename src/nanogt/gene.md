# Code Study Note: `src/nanogt/gene.py`

File studied: `/Users/suzie/Projects/nano-rare-gt/src/nanogt/gene.py`

Related files:
- `src/nanogt/disease.py`
- `src/nanogt/cli.py`
- `src/nanogt/scoring.py`
- `src/nanogt/report.py`
- `src/nanogt/catalog.py`

Study goal:
Understand how NanoGT turns a gene symbol into protein/gene properties used for gene therapy feasibility and precedent scoring.

---

## 1. Plain-English identity

`gene.py` is NanoGT's gene and protein lookup file.

If the project has a gene symbol such as `ROGDI`, `SMN1`, or `GLA`, this file tries to answer:

```text
What protein does this gene encode?
How long is the coding sequence?
Is the protein secreted?
Where in the cell does the protein live?
Does it have keywords/domains that suggest a biological class?
```

It mostly gets this information from UniProt, a major public protein database.

If UniProt is unavailable or does not return a result, it uses hardcoded fallback data for genes already relevant to the project.

Easiest mental model:

```text
gene.py = gene symbol in → GeneInfo out
```

---

## 2. Why this file exists

NanoGT scores whether a disease/gene looks feasible for gene therapy and whether it resembles previous gene therapy programs.

To do that, it needs gene/protein facts.

For example:

| Question | Field from `GeneInfo` | Why it matters |
|---|---|---|
| Is the gene small enough for AAV? | `cds_length_bp` | Used by packaging score |
| Is the protein secreted? | `is_secreted` | Used by protein class and cross-correction scoring |
| Is it lysosomal, membrane, intracellular, etc.? | `subcellular_location`, `keywords` | Used by protein class and pathway logic |
| What protein is it? | `protein_name`, `uniprot_id` | Used for interpretation/reporting |
| Does it have domains? | `domains` | Not deeply used yet, but useful for future similarity scoring |

For Kohlschutter-Tonz syndrome, `disease.py` gives the gene `ROGDI`.
Then `gene.py` gives NanoGT a `GeneInfo` object for ROGDI.
Then `scoring.py` uses ROGDI size/localisation/keywords to score precedent programs.

---

## 3. How it fits into project data flow

Main path:

```text
cli.py receives disease query
        ↓
disease.py returns DiseaseInfo
        ↓
cli.py chooses gene symbol
        ↓
gene.py fetch_gene(gene_symbol)
        ↓
returns GeneInfo
        ↓
scoring.py uses GeneInfo for:
  - packaging fit
  - protein class match
  - pathway inference
  - cross-correction potential
        ↓
report.py displays scoring notes
```

Important connection:

```text
disease.py identifies the gene.
gene.py explains the gene/protein.
scoring.py uses that explanation to rank GT precedents.
```

---

## 4. What this file outputs

The central output is a `GeneInfo` dataclass.

A dataclass is a simple object with named fields.

`GeneInfo` stores:

| Field | Meaning | Why NanoGT needs it |
|---|---|---|
| `symbol` | Gene symbol, e.g. `ROGDI` | The main gene name |
| `uniprot_id` | UniProt accession, e.g. `Q9GZN7` | Traceable protein database ID |
| `protein_name` | Full protein name | Human-readable meaning |
| `cds_length_bp` | Approximate coding sequence length in base pairs | Determines whether the gene fits in vector cargo |
| `aa_length` | Protein length in amino acids | Used to estimate CDS from UniProt sequence |
| `is_secreted` | Whether protein is secreted/extracellular | Important for cross-correction and systemic delivery logic |
| `subcellular_location` | Where protein lives in/around cell | Helps classify lysosomal/membrane/intracellular proteins |
| `go_terms` | Gene Ontology IDs or related terms | Helps describe biological function/pathway |
| `keywords` | UniProt keywords or curated tags | Used by scoring for protein/pathway clues |
| `domains` | Protein domain names | Useful for future domain/structure similarity scoring |

Beginner note:

```text
A gene is DNA.
A protein is the molecule made from that gene.
UniProt is mostly a protein database, so gene.py is really fetching protein annotations for a gene symbol.
```

---

## 5. Line-range walkthrough in code order

### Lines 1-9: File identity comments

The file says it is a UniProt gene/protein client.

The comments state the same general pattern as `disease.py`:

1. Try the live API.
2. Fall back to static data.

This keeps NanoGT usable even when the internet is unavailable.

---

### Lines 11-14: Imports

```python
import time
from dataclasses import dataclass
from typing import Optional
import requests
```

What each import is for:

| Import | Meaning | Used for |
|---|---|---|
| `time` | Timing utilities | Imported but not used in current code |
| `dataclass` | Simple labelled data container | Defines `GeneInfo` |
| `Optional` | Type hint meaning “value or None” | Optional UniProt/protein/CDS fields |
| `requests` | HTTP library | Calls UniProt REST API |

Cleanup note:

```text
`time` is currently unused.
```

---

### Lines 16-19: API base URL, session, cache

```python
UNIPROT_BASE = "https://rest.uniprot.org/uniprotkb"
_SESSION = requests.Session()
_SESSION.headers["Accept"] = "application/json"
_CACHE: dict = {}
```

Plain-English meaning:

- `UNIPROT_BASE` is the API endpoint for UniProtKB.
- `_SESSION` reuses HTTP settings/connections.
- The `Accept` header asks for JSON.
- `_CACHE` remembers gene lookups during one run.

Important cache detail:

```text
The cache is in memory only.
It avoids duplicate API calls during one run, but does not persist between CLI runs.
```

---

### Lines 22-35: `GeneInfo` dataclass

```python
@dataclass
class GeneInfo:
    symbol: str
    uniprot_id: Optional[str]
    protein_name: Optional[str]
    cds_length_bp: Optional[int]
    aa_length: Optional[int]
    is_secreted: bool
    subcellular_location: list[str]
    go_terms: list[str]
    keywords: list[str]
    domains: list[str]
```

This is the standard gene/protein record that `fetch_gene()` returns.

Think of it as a research summary card:

```text
GeneInfo card for ROGDI
- symbol: ROGDI
- UniProt ID: Q9GZN7
- protein name: Protein rogdi homolog
- CDS length: 861 bp
- protein length: 287 amino acids
- secreted: no
- location: nuclear envelope, presynapse, synaptic vesicle
- keywords/domains: synapse/Rabconnectin/V-ATPase related
```

Why this matters for scoring:

- Small CDS improves packaging feasibility.
- Secreted/lysosomal proteins may have cross-correction advantages.
- Subcellular location helps compare protein class to precedent programs.

---

### Lines 37-59: `_search_uniprot()` live API search

This helper searches UniProt for a human gene symbol.

```python
def _search_uniprot(gene_symbol: str, organism: str = "human") -> Optional[dict]:
```

The `organism` argument defaults to `human`, but the code actually hardcodes human using:

```python
organism_id:9606
```

So the argument is not used to build a different species query.

#### Lines 40-41: Query construction

```python
query = f"gene_exact:{gene_symbol} AND organism_id:9606 AND reviewed:true"
```

Meaning:

- `gene_exact:{gene_symbol}`: exact gene symbol match.
- `organism_id:9606`: human.
- `reviewed:true`: reviewed Swiss-Prot entries only.

This is a sensible choice because reviewed UniProt entries are higher confidence.

#### Lines 43-53: API request

The code calls:

```text
https://rest.uniprot.org/uniprotkb/search
```

with parameters including:

| Parameter | Meaning |
|---|---|
| `query` | The search terms |
| `fields` | Which information to return |
| `size=1` | Return only the top result |
| `format=json` | Return JSON |
| `timeout=15` | Stop waiting after 15 seconds |

Fields requested include:

```text
accession
gene_names
protein_name
sequence
subcellular location
GO terms
keywords
domains
organism name
```

#### Lines 54-59: Return first result or None

If the response succeeds, the code returns the first result.

If there are no results or an exception happens, it returns `None`.

Important weakness:

```text
Only the top result is used.
This is usually fine for reviewed human gene symbols, but synonyms or unusual symbols could still cause misses.
```

---

### Lines 62-74: `fetch_gene()` public function

This is the main function other files call.

Flow:

1. If the gene symbol is already in `_CACHE`, return the cached `GeneInfo`.
2. Search UniProt.
3. If UniProt returns data, parse it with `_parse_uniprot()`.
4. If UniProt fails or gives no result, use `_fallback_gene()`.
5. Cache the `GeneInfo`.
6. Return it.

Key idea:

```text
fetch_gene() is the safe front door.
Other files do not need to know whether data came from UniProt or fallback.
```

Unlike `fetch_disease()`, this function always returns a `GeneInfo` object.

If the gene is unknown, fallback creates a mostly empty `GeneInfo` with the requested symbol.

---

### Lines 77-134: `_parse_uniprot()` converts raw UniProt JSON into `GeneInfo`

This function is the translator between UniProt's nested JSON and NanoGT's simple `GeneInfo` dataclass.

#### Lines 79-82: Accession and sequence length

```python
acc = data.get("primaryAccession", "")
seq = data.get("sequence", {})
aa_len = seq.get("length", 0)
cds_bp = aa_len * 3 if aa_len else None
```

`aa_len` is amino acid length.

`cds_bp` is estimated as:

```text
amino acid length × 3 base pairs per codon
```

Beginner biology reminder:

```text
One amino acid is encoded by a codon of 3 DNA bases.
```

Important scientific simplification:

This estimate ignores stop codon, UTRs, isoforms, tags, promoters, regulatory elements, and vector expression cassette design.

For packaging feasibility, it is a useful rough estimate, not a full construct size.

#### Lines 84-92: Subcellular location

The code searches through UniProt `comments` and finds entries where:

```python
comment.get("commentType") == "SUBCELLULAR LOCATION"
```

Then it extracts location values.

These might be labels like:

```text
Lysosome
Secreted
Cytoplasm
ER membrane
Nucleus
```

Why it matters:

`scoring.py` later uses these labels to infer:

- secreted vs intracellular
- lysosomal vs non-lysosomal
- membrane vs non-membrane

#### Lines 94-95: `is_secreted`

```python
is_secreted = any("secret" in loc.lower() or "extracell" in loc.lower() for loc in sub_locs)
```

This marks a protein as secreted if its location text contains `secret` or `extracell`.

Weakness:

It depends on exact wording in location annotations.

#### Lines 97-102: GO terms

The code extracts GO cross-reference IDs from UniProt and keeps the first 10.

GO means Gene Ontology.

GO terms describe biological processes, molecular functions, and cellular components.

The limit of 10 avoids giving later text-matching/scoring logic too much noisy information.

Weakness:

Keeping only the first 10 could discard useful terms.

#### Lines 104-106: Keywords

The code collects UniProt keyword names.

Examples might include:

```text
Lysosome
Glycoprotein
Secreted
Coagulation
```

These are helpful for simple biological classification.

#### Lines 108-114: Protein name

The code digs through nested JSON:

```text
proteinDescription → recommendedName → fullName → value
```

This returns the recommended full protein name.

#### Lines 116-121: Domains

The code loops through `features` and keeps descriptions where:

```python
feat.get("type") == "Domain"
```

Domains are functional regions within proteins.

This is not heavily used yet in the current scoring engine, but it is valuable for future domain similarity scoring.

#### Lines 123-134: Return `GeneInfo`

Finally, all parsed pieces become one `GeneInfo` object.

This simple object is much easier for `scoring.py` to use than raw UniProt JSON.

---

### Lines 137-142: Static fallback section starts

The comments say fallback data is hardcoded for all genes in the project.

This fallback protects the project from:

- UniProt downtime.
- Network problems.
- Missing API results.
- Reproducibility problems during demonstrations.

---

### Lines 143-238: `_fallback_gene()` static gene records

`_fallback_gene(symbol)` contains a dictionary called `FALLBACKS`.

Each key is a gene symbol.
Each value is a `GeneInfo` object.

Genes included include:

| Gene | Protein/function context in this project | Notable scoring relevance |
|---|---|---|
| `SMN1` | Survival motor neuron protein | Small gene, CNS/motor neuron precedent |
| `F9` | Coagulation factor IX | Secreted clotting factor, liver/systemic precedent |
| `GLA` | Alpha-galactosidase A | Lysosomal/secreted, Fabry/cross-correction relevance |
| `SGSH` | Lysosomal enzyme | Sanfilippo/lysosomal CNS relevance |
| `UGT1A1` | Liver ER enzyme | Liver disease but not secreted/lysosomal |
| `ROGDI` | Synapse-related protein | Small CNS intracellular/synaptic protein, unusual pathway |
| `RPE65` | Retinal visual cycle protein | Retina precedent |
| `F8` | Coagulation factor VIII | Large secreted gene, tight AAV packaging |
| `PAH` | Phenylalanine metabolism enzyme | Liver metabolic disease precedent |
| `OTC` | Urea cycle mitochondrial enzyme | Liver/mitochondrial metabolism |
| `NAGLU` | Lysosomal enzyme | MPS IIIB precedent |
| `MTM1` | Myotubularin | Muscle/myopathy precedent |
| `DMD_micro` | Synthetic micro-dystrophin | Designed shortened gene to fit AAV |
| `MCOLN1` | Lysosome membrane channel | Mucolipidosis type IV |
| `MAN2B1` | Lysosomal alpha-mannosidase | Large lysosomal enzyme |
| `BCKDHA` | Mitochondrial metabolic enzyme | Maple syrup urine disease |
| `SLC17A5` | Lysosomal transporter | Salla disease |

Important fallback behavior:

```python
return FALLBACKS.get(
    symbol,
    GeneInfo(symbol, None, None, None, None, False, [], [], [], []),
)
```

If the gene symbol is not known, the function returns an empty-but-valid `GeneInfo`.

This avoids crashing. `scoring.py` can still run, but with weak/neutral information.

---

## 6. API, fallback, and cache logic in one view

```text
fetch_gene("ROGDI")
        ↓
check _CACHE["ROGDI"]
        ↓
if cached: return cached GeneInfo
        ↓
search UniProt for reviewed human ROGDI
        ↓
if result found:
    parse UniProt JSON into GeneInfo
else:
    use fallback GeneInfo for ROGDI
        ↓
store GeneInfo in _CACHE
        ↓
return GeneInfo
```

Important difference from `disease.py`:

```text
disease.py can return None.
gene.py always returns a GeneInfo object, even if mostly empty.
```

---

## 7. How `GeneInfo` affects scoring

`scoring.py` uses `GeneInfo` in several ways.

### 7.1 Packaging fit

```text
GeneInfo.cds_length_bp compared with vector cargo_limit_bp
```

Small genes score better because they leave more room inside AAV.

If the gene is too large for the vector, the program is a hard fail.

### 7.2 Protein class match

`scoring.py` looks at:

```text
GeneInfo.is_secreted
GeneInfo.subcellular_location
GeneInfo.keywords
```

It asks whether the query gene's protein is similar to the precedent program's protein class.

For example:

- Secreted clotting factor vs secreted clotting factor = strong match.
- Lysosomal enzyme vs lysosomal enzyme = strong match.
- Intracellular synaptic protein vs secreted liver protein = weaker match.

### 7.3 Pathway inference

`scoring.py` uses gene keywords, GO terms, subcellular location, and disease HPO terms to infer broad pathways such as:

```text
lysosomal_storage
coagulation
retinal_visual_cycle
motor_neuron
myopathy
amino_acid_metabolism
urea_cycle
mitochondrial_complex
unknown
```

### 7.4 Cross-correction potential

If the protein is secreted or lysosomal, one corrected cell may help neighboring cells.

This is called cross-correction.

`GeneInfo.is_secreted`, `subcellular_location`, and `keywords` help score this.

---

## 8. Assumptions and weaknesses

### 8.1 CDS length is estimated from amino acid length

The live UniProt parser estimates:

```text
cds_length_bp = amino acid length × 3
```

This is useful but incomplete.

It does not include:

- Stop codon.
- UTRs.
- Promoter.
- PolyA signal.
- Introns if used in a mini-gene.
- Tags or regulatory elements.
- Isoform differences.
- Codon optimization effects.

Improvement:

Store a separate field for therapeutic cassette size:

```text
coding_sequence_bp
expression_cassette_bp
promoter_bp
polyA_bp
vector_payload_bp
```

---

### 8.2 UniProt top result may not always be the intended gene

The query asks for one reviewed human result.

Usually this is good.

But edge cases can happen:

- Gene aliases.
- Withdrawn symbols.
- Synthetic constructs like `DMD_micro`.
- Genes with complex isoforms.

Improvement:

Validate returned gene names against the requested symbol and known aliases.

---

### 8.3 Protein secretion/location is inferred from text

`is_secreted` is based on whether location strings contain `secret` or `extracell`.

This is simple and transparent, but not perfect.

Improvement:

Use explicit UniProt feature/comment evidence, GO cellular component terms, and manually reviewed overrides.

---

### 8.4 Fallback data has no formal source fields

The fallback comments say data came from UniProt and literature, but individual fields do not have citations.

For research-grade use, each fallback record should include:

```text
source_database
source_url
accessed_date
field-level evidence
confidence
```

---

### 8.5 Fallback dictionary is rebuilt every call

`FALLBACKS` is defined inside `_fallback_gene()`.

That means the dictionary is reconstructed whenever fallback lookup is called.

For this small project, that is fine.

For a larger project, it would be cleaner to build it once at module level, as `disease.py` does.

---

### 8.6 Cache is memory-only

`_CACHE` helps within one run, but there is no persistent gene cache.

Improvement:

Save gene/protein lookups to SQLite or a local JSON cache with a version/date.

---

### 8.7 Dataclass does not validate values

`GeneInfo` is a dataclass, not a Pydantic model.

It does not enforce that CDS length is positive, that keywords are strings, or that the symbol is uppercase.

Improvement:

Use Pydantic validation or add tests.

---

### 8.8 Unknown genes quietly become empty records

This behavior keeps the program running:

```text
Unknown gene → GeneInfo(symbol, None, None, None, None, False, [], [], [], [])
```

But it can also hide missing data.

Improvement:

Return a warning such as:

```text
No UniProt/fallback data found for XYZ; scoring used neutral defaults.
```

Then show this warning in the report.

---

## 9. Practical improvements

Good next improvements would be:

1. Add source and date metadata to every fallback gene.
2. Add persistent gene cache to SQLite or local files.
3. Add warnings when fallback or empty gene data is used.
4. Validate UniProt result gene symbol and aliases.
5. Support synthetic constructs more explicitly, such as `DMD_micro`.
6. Store cassette size separately from CDS size.
7. Use a shared Pydantic model or validation layer for `GeneInfo`.
8. Add unit tests for `_parse_uniprot()` using saved example UniProt JSON.
9. Move fallback gene data to `data/genes.yaml` or `data/genes.json`.
10. Add field-level confidence and citations.

Possible future fallback record shape:

```text
symbol: ROGDI
uniprot_id: Q9GZN7
protein_name: Protein rogdi homolog
cds_length_bp: 861
aa_length: 287
subcellular_location:
  - Nuclear envelope
  - Presynapse
  - Synaptic vesicle
sources:
  - database: UniProt
    url: ...
    accessed: 2026-06-03
confidence: medium
```

---

## 10. Mini mental model

Say this from memory:

```text
gene.py takes a gene symbol and returns a GeneInfo object.
It checks a one-run cache, searches reviewed human UniProt entries,
parses protein length, name, location, GO terms, keywords, and domains,
and falls back to curated local gene records if needed.
The most scoring-important fields are cds_length_bp, is_secreted,
subcellular_location, keywords, and domains. The file is useful and robust,
but CDS size and protein class are simplified and fallback data needs citations.
```

Even shorter:

```text
Gene symbol → UniProt/fallback → GeneInfo → packaging/protein/pathway scoring
```

---

## 11. Active recall questions

Use these without looking at the code.

1. What is the main job of `gene.py`?
2. What public function does `cli.py` call to get gene information?
3. What object does `fetch_gene()` return?
4. Which public database does this file query?
5. What does `organism_id:9606` mean?
6. Why does the query use `reviewed:true`?
7. What is stored in `GeneInfo.cds_length_bp`?
8. How does the live parser estimate CDS length from amino acid length?
9. Why is CDS length important for AAV gene therapy?
10. What does `is_secreted` mean?
11. How does the code infer whether a protein is secreted?
12. Why do subcellular locations matter for scoring?
13. What are GO terms?
14. What are UniProt keywords used for here?
15. What are protein domains?
16. What happens if UniProt returns no result?
17. What happens if the gene is not in the fallback dictionary?
18. Why is an empty `GeneInfo` both useful and risky?
19. What fallback gene is used for Kohlschutter-Tonz syndrome?
20. What would make this file more research-grade?

---

## 12. Final high-level summary

`gene.py` is the gene/protein metadata gateway for NanoGT.

It turns a gene symbol into a structured `GeneInfo` object by trying UniProt first and falling back to curated local records. The output feeds directly into packaging, protein class, pathway, and cross-correction scoring.

Its strengths are simplicity, transparency, and offline robustness. Its main weaknesses are simplified CDS-size estimation, text-based protein classification, memory-only caching, no persistent warning system, and fallback records without field-level citations.
