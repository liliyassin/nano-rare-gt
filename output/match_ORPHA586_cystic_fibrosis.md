# NanoGT Match Report: Cystic fibrosis

**Disease:** Cystic fibrosis (ORPHA:586)  
**Primary gene:** CFTR  
**Gene CDS:** 4443 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** lung, pancreas, liver  

---

## Interpretation

- No high-confidence vector precedent was found; the best result is medium-confidence and should be treated as manual-review territory.
- Main review flags: Multi-system disease; define a primary therapeutic target tissue before selecting route/vector; Vector does not naturally cover all annotated disease tissues: liver, lung, pancreas; No direct tissue overlap; treat this as weak precedent unless route or modality is changed.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** CFTR chloride channel dysfunction; gene addition must achieve sufficient cell-surface expression in airway epithelium  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** airway gene addition  
**Evidence level/status:** direct / needs_user_fact_check  
**Evidence summary:** CFTR LOF supports gene addition logic; lung delivery and transient episomal expression in cycling airway epithelium are the main challenges  
**Evidence source:** [OMIM CFTR 219700](https://omim.org/entry/219700)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and integrating ex vivo HSC vector precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint readiness: liver/metabolic targets may have biochemical biomarkers, but biomarker correction must be linked to clinical benefit.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Skysona | LV | 6.7/10 | 🟡 Medium | approved |
| 2 | Hemgenix | AAV5 | 6.5/10 | 🟡 Medium | approved |
| 3 | Roctavian | AAV5 | 6.5/10 | 🟡 Medium | approved |
| 4 | BMN 307 | AAV5 | 6.5/10 | 🟡 Medium | phase2 |
| 5 | Libmeldy | LV | 6.3/10 | 🟡 Medium | approved |

---

## Match #1: Skysona

**Precedent disease:** Cerebral adrenoleukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.7 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.67** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 4443bp / cargo 8000bp (56% utilized)
- No tissue overlap (disease: ['lung', 'pancreas', 'liver'], vector: ['hematopoietic'])
- Both membrane proteins
- LOF inheritance — compatible for gene replacement
- Unknown pathway — neutral score
- Disease mechanism: loss of function — CFTR chloride channel dysfunction; gene addition must achieve sufficient cell-surface expression in airway epithelium
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CFTR LOF supports gene addition logic; lung delivery and transient episomal expression in cycling airway epithelium are the main challenges
- Mechanism source: OMIM CFTR 219700 (https://omim.org/entry/219700)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — CFTR standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Multi-system disease; define a primary therapeutic target tissue before selecting route/vector
- Vector does not naturally cover all annotated disease tissues: liver, lung, pancreas
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #2: Hemgenix

**Precedent disease:** Hemophilia B  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 6.5 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 0.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.52** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 4443bp / cargo 4700bp (95% utilized)
- Vector tropism plus precedent target match: liver
- Protein class mismatch
- LOF inheritance — compatible for gene replacement
- Unknown pathway — neutral score
- Disease mechanism: loss of function — CFTR chloride channel dysfunction; gene addition must achieve sufficient cell-surface expression in airway epithelium
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CFTR LOF supports gene addition logic; lung delivery and transient episomal expression in cycling airway epithelium are the main challenges
- Mechanism source: OMIM CFTR 219700 (https://omim.org/entry/219700)
- Approval status: approved
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — CFTR standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Multi-system disease; define a primary therapeutic target tissue before selecting route/vector
- Vector does not naturally cover all annotated disease tissues: pancreas
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #3: Roctavian

**Precedent disease:** Hemophilia A  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 6.5 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 0.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.52** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 4443bp / cargo 4700bp (95% utilized)
- Vector tropism plus precedent target match: liver
- Protein class mismatch
- LOF inheritance — compatible for gene replacement
- Unknown pathway — neutral score
- Disease mechanism: loss of function — CFTR chloride channel dysfunction; gene addition must achieve sufficient cell-surface expression in airway epithelium
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CFTR LOF supports gene addition logic; lung delivery and transient episomal expression in cycling airway epithelium are the main challenges
- Mechanism source: OMIM CFTR 219700 (https://omim.org/entry/219700)
- Approval status: approved
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — CFTR standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Multi-system disease; define a primary therapeutic target tissue before selecting route/vector
- Vector does not naturally cover all annotated disease tissues: pancreas
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: BMN 307

**Precedent disease:** Phenylketonuria  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 6.5 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 0.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.60 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.48** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 4443bp / cargo 4700bp (95% utilized)
- Vector tropism plus precedent target match: liver
- Protein class mismatch
- Inheritance match (Autosomal recessive <-> AR)
- Unknown pathway — neutral score
- Disease mechanism: loss of function — CFTR chloride channel dysfunction; gene addition must achieve sufficient cell-surface expression in airway epithelium
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CFTR LOF supports gene addition logic; lung delivery and transient episomal expression in cycling airway epithelium are the main challenges
- Mechanism source: OMIM CFTR 219700 (https://omim.org/entry/219700)
- Approval status: phase2
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — CFTR standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Multi-system disease; define a primary therapeutic target tissue before selecting route/vector
- Vector does not naturally cover all annotated disease tissues: pancreas
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #5: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.3 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.33** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 4443bp / cargo 8000bp (56% utilized)
- No tissue overlap (disease: ['lung', 'pancreas', 'liver'], vector: ['hematopoietic'])
- Protein class mismatch
- Inheritance match (Autosomal recessive <-> AR)
- Unknown pathway — neutral score
- Disease mechanism: loss of function — CFTR chloride channel dysfunction; gene addition must achieve sufficient cell-surface expression in airway epithelium
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CFTR LOF supports gene addition logic; lung delivery and transient episomal expression in cycling airway epithelium are the main challenges
- Mechanism source: OMIM CFTR 219700 (https://omim.org/entry/219700)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — CFTR standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Multi-system disease; define a primary therapeutic target tissue before selecting route/vector
- Vector does not naturally cover all annotated disease tissues: liver, lung, pancreas
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
