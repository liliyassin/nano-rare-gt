# NanoGT Match Report: Hemophilia A

**Disease:** Hemophilia A (ORPHA:98878)  
**Primary gene:** F8  
**Gene CDS:** 4374 bp  
**Inheritance:** X-linked recessive  
**Target tissues scored:** liver  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility; AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone; Vector does not naturally cover all annotated disease tissues: liver.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** Factor VIII deficiency from pathogenic F8 variants; liver-directed F8 expression is an approved gene-addition precedent (Roctavian)  
**Gene-addition compatibility:** compatible  
**Preferred modality class:** gene addition or factor expression  
**Evidence level/status:** direct / needs_user_fact_check  
**Evidence summary:** BioMarin Roctavian (valoctocogene roxaparvovec) approved for Hemophilia A; AAV5 liver-directed F8 expression precedent  
**Evidence source:** [OMIM Hemophilia A 306700](https://omim.org/entry/306700)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and integrating ex vivo HSC vector precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint readiness: liver/metabolic targets may have biochemical biomarkers, but biomarker correction must be linked to clinical benefit.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Hemgenix | AAV5 | 8.5/10 | 🟢 High | approved |
| 2 | Roctavian | AAV5 | 8.5/10 | 🟢 High | approved |
| 3 | SPK-8011 | AAVrh10 | 8.1/10 | 🟢 High | phase3 |
| 4 | DTX201 | AAV8 | 7.8/10 | 🟢 High | phase2 |
| 5 | Libmeldy | LV | 7.3/10 | 🟡 Medium | approved |

---

## Match #1: Hemgenix

**Precedent disease:** Hemophilia B  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 8.5 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 0.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.48** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 4374bp / cargo 4700bp (93% utilized)
- Vector tropism plus precedent target match: liver
- Both secreted proteins — systemic delivery viable
- Inheritance match (X-linked recessive <-> XL)
- Pathway match: coagulation
- Disease mechanism: loss of function — Factor VIII deficiency from pathogenic F8 variants; liver-directed F8 expression is an approved gene-addition precedent (Roctavian)
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: BioMarin Roctavian (valoctocogene roxaparvovec) approved for Hemophilia A; AAV5 liver-directed F8 expression precedent
- Mechanism source: OMIM Hemophilia A 306700 (https://omim.org/entry/306700)
- Approval status: approved
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — F8 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #2: Roctavian

**Precedent disease:** Hemophilia A  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 8.5 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 0.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.48** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 4374bp / cargo 4700bp (93% utilized)
- Vector tropism plus precedent target match: liver
- Both secreted proteins — systemic delivery viable
- Inheritance match (X-linked recessive <-> XL)
- Pathway match: coagulation
- Disease mechanism: loss of function — Factor VIII deficiency from pathogenic F8 variants; liver-directed F8 expression is an approved gene-addition precedent (Roctavian)
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: BioMarin Roctavian (valoctocogene roxaparvovec) approved for Hemophilia A; AAV5 liver-directed F8 expression precedent
- Mechanism source: OMIM Hemophilia A 306700 (https://omim.org/entry/306700)
- Approval status: approved
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — F8 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #3: SPK-8011

**Precedent disease:** Hemophilia A  
**Vector:** AAVrh10  
**Tissue target:** liver  
**Composite score:** 8.1 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 0.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.80 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.50 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.14** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 4374bp / cargo 4700bp (93% utilized)
- Vector tropism plus precedent target match: liver
- Both secreted proteins — systemic delivery viable
- Inheritance match (X-linked recessive <-> XL)
- Pathway match: coagulation
- Disease mechanism: loss of function — Factor VIII deficiency from pathogenic F8 variants; liver-directed F8 expression is an approved gene-addition precedent (Roctavian)
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: BioMarin Roctavian (valoctocogene roxaparvovec) approved for Hemophilia A; AAV5 liver-directed F8 expression precedent
- Mechanism source: OMIM Hemophilia A 306700 (https://omim.org/entry/306700)
- Approval status: phase3
- Vector immunogenicity (AAVrh10): moderate (~10%) — significant proportion may require pre-screening or exclusion
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — F8 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: DTX201

**Precedent disease:** Hemophilia A  
**Vector:** AAV8  
**Tissue target:** liver  
**Composite score:** 7.8 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 0.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.60 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.81** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 4374bp / cargo 4700bp (93% utilized)
- Vector tropism plus precedent target match: liver
- Both secreted proteins — systemic delivery viable
- Inheritance match (X-linked recessive <-> XL)
- Pathway match: coagulation
- Disease mechanism: loss of function — Factor VIII deficiency from pathogenic F8 variants; liver-directed F8 expression is an approved gene-addition precedent (Roctavian)
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: BioMarin Roctavian (valoctocogene roxaparvovec) approved for Hemophilia A; AAV5 liver-directed F8 expression precedent
- Mechanism source: OMIM Hemophilia A 306700 (https://omim.org/entry/306700)
- Approval status: phase2
- Vector immunogenicity (AAV8): high (~30%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — F8 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #5: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 7.3 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.29** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 4374bp / cargo 8000bp (55% utilized)
- No tissue overlap (disease: ['liver'], vector: ['hematopoietic'])
- Both secreted proteins — systemic delivery viable
- LOF inheritance — compatible for gene replacement
- Different pathway (coagulation vs leukodystrophy)
- Disease mechanism: loss of function — Factor VIII deficiency from pathogenic F8 variants; liver-directed F8 expression is an approved gene-addition precedent (Roctavian)
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: BioMarin Roctavian (valoctocogene roxaparvovec) approved for Hemophilia A; AAV5 liver-directed F8 expression precedent
- Mechanism source: OMIM Hemophilia A 306700 (https://omim.org/entry/306700)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — F8 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: liver
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
