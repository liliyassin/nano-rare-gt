# Manual Disease Deep Dive Template

## Disease / Project

**Disease name:**  
`[fill in disease name]`

**Date started:**  
`[fill in date]`

**Main question:**  
`What am I trying to understand about this disease?`

Example:

```text
How does this disease arise biologically, what genes/proteins are involved, and how would I manually verify the AI-generated findings?
```

---

# 1. Quick Overview

## Plain-English Disease Summary

**What is the disease?**

```text
[Write 3–5 sentences explaining the disease in simple language.]
```

**Who does it affect?**

```text
[Age of onset, population, inheritance, prevalence if known.]
```

**Main clinical features / symptoms**

- `[symptom 1]`
- `[symptom 2]`
- `[symptom 3]`

**Why is this disease biologically interesting?**

```text
[Explain why this disease matters: rare disease, genetic cause, protein dysfunction, pathway relevance, possible therapy, etc.]
```

---

# 2. Source Map

Use this table to track where each type of information comes from.

| Information Needed | Main Source | Link Used | Notes |
|---|---|---|---|
| Disease overview | Orphanet | `[link]` | `[notes]` |
| Human genetics | OMIM | `[link]` | `[notes]` |
| Disease terminology | MedGen / MONDO | `[link]` | `[notes]` |
| Gene information | NCBI Gene / Ensembl / HGNC | `[link]` | `[notes]` |
| Protein information | UniProt | `[link]` | `[notes]` |
| Protein domains | InterPro / Pfam | `[link]` | `[notes]` |
| Protein structure | AlphaFold / PDB | `[link]` | `[notes]` |
| Variants | ClinVar / gnomAD | `[link]` | `[notes]` |
| Pathways | Reactome / KEGG | `[link]` | `[notes]` |
| Literature | PubMed / Europe PMC / Google Scholar | `[link]` | `[notes]` |

---

# 3. Disease Database Deep Dive

## 3.1 Orphanet

**Search query**

```text
[disease name] site:orpha.net
```

**Link used**

```text
[Paste Orphanet link here]
```

**Orpha ID**

```text
[fill in]
```

**Disease synonyms**

- `[synonym 1]`
- `[synonym 2]`
- `[synonym 3]`

**Disease classification**

```text
[Where does Orphanet classify this disease? Neurological? Metabolic? Developmental? etc.]
```

**Prevalence**

```text
[fill in]
```

**Inheritance pattern**

```text
[autosomal dominant / autosomal recessive / X-linked / mitochondrial / unknown]
```

**Associated genes listed by Orphanet**

| Gene | Evidence / Notes |
|---|---|
| `[gene]` | `[notes]` |
| `[gene]` | `[notes]` |

**My understanding**

```text
[In your own words, explain what Orphanet is telling you.]
```

---

## 3.2 OMIM

**Search query**

```text
[disease name] OMIM
```

**Link used**

```text
[Paste OMIM link here]
```

**OMIM disease ID**

```text
[fill in]
```

**OMIM phenotype title**

```text
[fill in]
```

**Known gene(s)**

| Gene | OMIM Gene ID | Notes |
|---|---|---|
| `[gene]` | `[ID]` | `[notes]` |

**Inheritance**

```text
[fill in]
```

**Key OMIM points**

- `[point 1]`
- `[point 2]`
- `[point 3]`

**What OMIM adds that Orphanet did not**

```text
[Write what extra genetic/clinical detail OMIM provides.]
```

---

# 4. Gene Deep Dive

Repeat this section for each important gene.

---

## Gene 1

**Gene symbol**

```text
[fill in]
```

**Full gene name**

```text
[fill in]
```

**Main links**

| Database | Link |
|---|---|
| NCBI Gene | `[link]` |
| Ensembl | `[link]` |
| HGNC | `[link]` |
| GeneCards | `[link]` |

---

## 4.1 Gene Identity

**Chromosome location**

```text
[fill in]
```

**Aliases / alternative names**

- `[alias 1]`
- `[alias 2]`
- `[alias 3]`

**What does this gene do?**

```text
[Plain-English summary.]
```

**Where is it expressed?**

```text
[Tissues/cells/organs if known.]
```

**Why is this gene relevant to the disease?**

```text
[Explain the causal relationship if known.]
```

---

## 4.2 Gene-to-Disease Evidence

| Evidence Type | What I Found | Source Link |
|---|---|---|
| Disease association | `[fill in]` | `[link]` |
| Inheritance | `[fill in]` | `[link]` |
| Known pathogenic variants | `[fill in]` | `[link]` |
| Functional evidence | `[fill in]` | `[link]` |
| Animal/cell model evidence | `[fill in]` | `[link]` |

**Confidence level**

```text
High / Medium / Low
```

**Why?**

```text
[Explain why you trust or do not trust the gene-disease link.]
```

---

# 5. Variant / Mutation Deep Dive

Use this section if the disease involves known variants.

## Main variant sources

| Database | Link Used | Notes |
|---|---|---|
| ClinVar | `[link]` | `[notes]` |
| gnomAD | `[link]` | `[notes]` |
| dbSNP | `[link]` | `[notes]` |
| LOVD | `[link]` | `[notes]` |

---

## Variant Table

| Variant | Gene | Variant Type | Clinical Significance | Frequency | Source |
|---|---|---|---|---|---|
| `[variant]` | `[gene]` | `[missense / nonsense / frameshift / splice / deletion]` | `[pathogenic / likely pathogenic / VUS / benign]` | `[frequency]` | `[link]` |

---

## Variant Interpretation

**Most important variant(s)**

```text
[fill in]
```

**What does the mutation change?**

```text
[Example: amino acid substitution, premature stop codon, altered splicing, loss of function.]
```

**Why might this cause disease?**

```text
[Explain the biological mechanism.]
```

**Is this variant common in healthy populations?**

```text
[Use gnomAD if available.]
```

**My confidence**

```text
High / Medium / Low
```

**Reason**

```text
[fill in]
```

---

# 6. Protein Deep Dive

## Protein Identity

**Gene**

```text
[fill in]
```

**Protein name**

```text
[fill in]
```

**UniProt link**

```text
[Paste UniProt link here]
```

**UniProt accession ID**

```text
[fill in]
```

---

## Protein Function

**What does this protein normally do?**

```text
[Plain-English explanation.]
```

**Where is the protein located in the cell?**

```text
[cell membrane / nucleus / mitochondria / cytoplasm / extracellular / other]
```

**What biological process is it involved in?**

```text
[fill in]
```

**What happens if this protein fails?**

```text
[Explain disease mechanism.]
```

---

## Protein Domains

| Domain | Position | Source | Why It Matters |
|---|---|---|---|
| `[domain]` | `[amino acid range]` | `[InterPro/Pfam/UniProt link]` | `[notes]` |

**Important domain links**

| Database | Link |
|---|---|
| InterPro | `[link]` |
| Pfam | `[link]` |

**My understanding of the protein**

```text
[Explain this protein as if teaching it to someone else.]
```

---

# 7. Protein Structure Deep Dive

## Structure Sources

| Source | Link | Notes |
|---|---|---|
| AlphaFold | `[link]` | `[notes]` |
| PDB | `[link]` | `[notes]` |

---

## AlphaFold / PDB Information

**Structure available?**

```text
Yes / No
```

**Structure type**

```text
Predicted / Experimental / Both
```

**Important structural regions**

```text
[Folded domains, disordered regions, binding pockets, transmembrane regions, active sites.]
```

**Are disease variants located in important regions?**

```text
[Explain if known.]
```

---

## Structural Interpretation

**Could the mutation disrupt protein folding?**

```text
Yes / No / Unsure
```

**Could the mutation affect a binding site or functional domain?**

```text
Yes / No / Unsure
```

**Could the mutation affect protein stability?**

```text
Yes / No / Unsure
```

**Explanation**

```text
[Write your reasoning.]
```

---

# 8. Pathway / Network Deep Dive

## Pathway Sources

| Database | Link | Notes |
|---|---|---|
| Reactome | `[link]` | `[notes]` |
| KEGG | `[link]` | `[notes]` |
| STRING | `[link]` | `[notes]` |

---

## Pathways Involved

| Pathway | Source | Why It Matters |
|---|---|---|
| `[pathway]` | `[link]` | `[notes]` |

---

## Interaction Partners

| Interacting Protein / Gene | Source | Possible Relevance |
|---|---|---|
| `[protein/gene]` | `[STRING/UniProt/etc.]` | `[notes]` |

---

## Systems-Level Interpretation

**What larger biological system is affected?**

```text
[Example: ion transport, mitochondrial function, DNA repair, protein degradation, immune signalling.]
```

**What downstream effects might happen?**

```text
[fill in]
```

**My understanding**

```text
[Explain how the gene/protein fits into the bigger biological picture.]
```

---

# 9. Literature Validation

## PubMed Search Queries

Use several versions.

```text
[disease name] [gene name]
```

```text
[disease name] [gene name] mutation
```

```text
[gene name] protein function disease
```

```text
[disease name] genotype phenotype
```

```text
[disease name] therapy review
```

---

## Key Papers

| Paper Title | Year | Link | What It Shows | Evidence Strength |
|---|---|---|---|---|
| `[title]` | `[year]` | `[link]` | `[summary]` | `High / Medium / Low` |

---

## Evidence Summary

**Strongest evidence found**

```text
[fill in]
```

**Any conflicting evidence?**

```text
[fill in]
```

**Most useful review paper**

```text
[link + notes]
```

**Most useful experimental paper**

```text
[link + notes]
```

---

# 10. Therapeutic / Translational Relevance

## Existing Treatments

| Treatment | Mechanism | Source | Notes |
|---|---|---|---|
| `[treatment]` | `[how it works]` | `[link]` | `[notes]` |

---

## Experimental / Emerging Therapies

| Therapy Type | Example | Source | Notes |
|---|---|---|---|
| Gene therapy | `[fill in]` | `[link]` | `[notes]` |
| Small molecule | `[fill in]` | `[link]` | `[notes]` |
| Protein replacement | `[fill in]` | `[link]` | `[notes]` |
| RNA therapy | `[fill in]` | `[link]` | `[notes]` |

---

## Therapeutic Interpretation

**What is the main therapeutic challenge?**

```text
[fill in]
```

**What kind of therapy would make biological sense?**

```text
[gene replacement / enzyme replacement / small molecule / RNA therapy / symptomatic treatment / unknown]
```

**Why?**

```text
[Explain the reasoning.]
```

---

# 11. Computational Workflow Equivalent

This is the section where you connect the manual work to what the AI/code is doing.

---

## 11.1 Disease Search

**Manual version**

```text
Search Orphanet / OMIM / MedGen for disease name.
```

**Code-like version**

```python
disease_name = "[fill in disease name]"

# Goal:
# 1. Search disease database
# 2. Retrieve disease identifiers
# 3. Extract linked genes
# 4. Store source links
```

**Expected output**

```text
Disease ID:
Synonyms:
Associated genes:
Source links:
```

---

## 11.2 Gene Lookup

**Manual version**

```text
Search NCBI Gene / Ensembl / HGNC for gene symbol.
```

**Code-like version**

```python
gene_symbol = "[fill in gene]"

# Goal:
# 1. Resolve official gene symbol
# 2. Collect aliases
# 3. Get chromosome location
# 4. Link gene to disease evidence
```

**Expected output**

```text
Gene symbol:
Full name:
Aliases:
Location:
Disease evidence:
```

---

## 11.3 UniProt Protein Lookup

**Manual version**

```text
Search UniProt for the gene/protein.
```

**Example code**

```python
import requests

gene = "[GENE_SYMBOL]"

url = "https://rest.uniprot.org/uniprotkb/search"
params = {
    "query": f"gene_exact:{gene} AND organism_id:9606",
    "format": "json"
}

response = requests.get(url, params=params)
data = response.json()

print(data.keys())
```

**What I should extract**

```text
Protein name:
UniProt accession:
Function:
Subcellular location:
Domains:
Sequence:
```

---

## 11.4 PubMed Literature Search

**Manual version**

```text
Search PubMed using disease + gene + mutation terms.
```

**Example code**

```python
from Bio import Entrez

Entrez.email = "your_email@example.com"

query = "[DISEASE_NAME] [GENE_SYMBOL] mutation"

handle = Entrez.esearch(
    db="pubmed",
    term=query,
    retmax=10
)

record = Entrez.read(handle)

print(record["IdList"])
```

**What I should extract**

```text
Top papers:
Review papers:
Experimental evidence:
Clinical evidence:
```

---

# 12. AI Output Validation Checklist

Use this whenever AI gives you an answer.

## Disease Claims

- [ ] Did AI provide a disease ID?
- [ ] Did I verify it in Orphanet or OMIM?
- [ ] Did AI list synonyms?
- [ ] Did I check whether synonyms are real?

## Gene Claims

- [ ] Did AI identify associated genes?
- [ ] Did I verify each gene in NCBI / OMIM / Orphanet?
- [ ] Did AI confuse aliases with official symbols?
- [ ] Did I check HGNC for official names?

## Variant Claims

- [ ] Did AI name specific variants?
- [ ] Did I verify variants in ClinVar?
- [ ] Did I check whether variants are pathogenic or uncertain?
- [ ] Did I check population frequency in gnomAD?

## Protein Claims

- [ ] Did AI identify the correct protein?
- [ ] Did I verify it in UniProt?
- [ ] Did I check domains?
- [ ] Did I check cellular location?

## Structure Claims

- [ ] Did AI mention AlphaFold or PDB?
- [ ] Did I verify structure availability?
- [ ] Did I check whether mutation positions actually map to important regions?

## Literature Claims

- [ ] Did AI cite papers?
- [ ] Did I open the papers or abstracts?
- [ ] Did I check dates?
- [ ] Did I check whether evidence is review, clinical, or experimental?

---

# 13. Final Disease Summary

## Disease

```text
[fill in]
```

## Main gene(s)

```text
[fill in]
```

## Main protein(s)

```text
[fill in]
```

## Main biological mechanism

```text
[Explain how the disease happens biologically.]
```

## Main variants / mutations

```text
[fill in]
```

## Main affected pathway

```text
[fill in]
```

## Strongest evidence

```text
[fill in]
```

## Weakest / uncertain evidence

```text
[fill in]
```

## Therapeutic relevance

```text
[fill in]
```

---

# 14. My Understanding In Plain English

Write this last.

```text
This disease is caused by...

The main gene involved is...

That gene produces...

The protein normally does...

When the gene/protein is disrupted...

This leads to disease because...

The strongest evidence comes from...

The main uncertainty is...
```

---

# 15. Things I Still Don’t Understand

Use this as your learning list.

| Question | Why It Matters | Who/What Can Help |
|---|---|---|
| `[question]` | `[notes]` | `[AI / paper / database / supervisor]` |
| `[question]` | `[notes]` | `[AI / paper / database / supervisor]` |

---

# 16. Glossary Terms To Add

Add these to `docs/GLOSSARY.md`.

| Term | My Definition | Source |
|---|---|---|
| `[term]` | `[plain-English definition]` | `[link]` |
| `[term]` | `[plain-English definition]` | `[link]` |

---

# 17. Final Confidence Score

## How well do I understand this disease?

```text
1 / 5 = I barely understand it
2 / 5 = I understand the basic disease
3 / 5 = I understand disease → gene → protein
4 / 5 = I can explain mechanism and evidence
5 / 5 = I can independently validate AI output
```

**Score**

```text
[fill in]
```

**Why?**

```text
[fill in]
```

**Next action**

```text
[What is the next thing I should verify or learn?]
```