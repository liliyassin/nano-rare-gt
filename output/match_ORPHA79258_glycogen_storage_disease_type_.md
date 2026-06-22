# NanoGT Match Report: Glycogen storage disease type Ia

**Disease:** Glycogen storage disease type Ia (ORPHA:79258)  
**Primary gene:** G6PC1  
**Gene CDS:** 1071 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** liver, kidney  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: Vector does not naturally cover all annotated disease tissues: kidney; Only partial tissue match; verify target-cell transduction and delivery route manually; Cell-autonomous protein across multiple tissues; high transduction coverage may be required.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** Glucose-6-phosphatase catalytic subunit deficiency  
**Gene-addition compatibility:** compatible  
**Preferred modality class:** liver kidney gene addition  
**Evidence level/status:** direct / source_linked_needs_review  
**Evidence summary:** G6PC deficiency is a metabolic enzyme loss where liver-directed expression is a plausible gene-addition strategy  
**Evidence source:** [OMIM G6PC gene entry](https://omim.org/entry/613742)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and integrating ex vivo HSC vector precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint readiness: liver/metabolic targets may have biochemical biomarkers, but biomarker correction must be linked to clinical benefit.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | SRP-9001 | AAV9 | 7.8/10 | 🟢 High | approved |
| 2 | ST-920 | AAV2/6 | 7.8/10 | 🟢 High | phase1/2 |
| 3 | RGX-121 | AAV9 | 7.7/10 | 🟢 High | phase3 |
| 4 | Hemgenix | AAV5 | 7.6/10 | 🟢 High | approved |
| 5 | Roctavian | AAV5 | 7.6/10 | 🟢 High | approved |

---

## Match #1: SRP-9001

**Precedent disease:** Duchenne muscular dystrophy  
**Vector:** AAV9  
**Tissue target:** muscle  
**Composite score:** 7.8 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.20 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.81** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1071bp / cargo 4700bp (23% utilized)
- Vector tropism overlaps liver, but precedent target is muscle
- Both membrane proteins
- LOF inheritance — compatible for gene replacement
- Pathway match: myopathy
- Disease mechanism: loss of function — Glucose-6-phosphatase catalytic subunit deficiency
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: G6PC deficiency is a metabolic enzyme loss where liver-directed expression is a plausible gene-addition strategy
- Mechanism source: OMIM G6PC gene entry (https://omim.org/entry/613742)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate-to-narrow window — early childhood onset; newborn screening integration would significantly improve outcomes
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — G6PC1 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: kidney
- Only partial tissue match; verify target-cell transduction and delivery route manually
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Therapeutic window is not wide; natural-history timing and irreversible damage should be reviewed
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #2: ST-920

**Precedent disease:** Fabry disease  
**Vector:** AAV2/6  
**Tissue target:** liver  
**Composite score:** 7.8 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.50 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.20 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.81** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1071bp / cargo 4700bp (23% utilized)
- Vector tropism plus precedent target match: liver
- Protein class mismatch
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Glucose-6-phosphatase catalytic subunit deficiency
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: G6PC deficiency is a metabolic enzyme loss where liver-directed expression is a plausible gene-addition strategy
- Mechanism source: OMIM G6PC gene entry (https://omim.org/entry/613742)
- Approval status: phase1/2
- Vector immunogenicity (AAV2/6): moderate (~17%) — significant proportion may require pre-screening or exclusion
- Moderate-to-narrow window — early childhood onset; newborn screening integration would significantly improve outcomes
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — G6PC1 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: kidney
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Therapeutic window is not wide; natural-history timing and irreversible damage should be reviewed
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #3: RGX-121

**Precedent disease:** Mucopolysaccharidosis type II  
**Vector:** AAV9  
**Tissue target:** CNS/liver  
**Composite score:** 7.7 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.80 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.20 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.71** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1071bp / cargo 4700bp (23% utilized)
- Vector tropism plus precedent target match: liver
- Protein class mismatch
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Glucose-6-phosphatase catalytic subunit deficiency
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: G6PC deficiency is a metabolic enzyme loss where liver-directed expression is a plausible gene-addition strategy
- Mechanism source: OMIM G6PC gene entry (https://omim.org/entry/613742)
- Approval status: phase3
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate-to-narrow window — early childhood onset; newborn screening integration would significantly improve outcomes
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — G6PC1 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: kidney
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Therapeutic window is not wide; natural-history timing and irreversible damage should be reviewed
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: Hemgenix

**Precedent disease:** Hemophilia B  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 7.6 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.20 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.57** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1071bp / cargo 4700bp (23% utilized)
- Vector tropism plus precedent target match: liver
- Protein class mismatch
- LOF inheritance — compatible for gene replacement
- Different pathway (glycogen_storage vs coagulation)
- Disease mechanism: loss of function — Glucose-6-phosphatase catalytic subunit deficiency
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: G6PC deficiency is a metabolic enzyme loss where liver-directed expression is a plausible gene-addition strategy
- Mechanism source: OMIM G6PC gene entry (https://omim.org/entry/613742)
- Approval status: approved
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Moderate-to-narrow window — early childhood onset; newborn screening integration would significantly improve outcomes
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — G6PC1 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: kidney
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Therapeutic window is not wide; natural-history timing and irreversible damage should be reviewed
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #5: Roctavian

**Precedent disease:** Hemophilia A  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 7.6 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.20 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.80 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.57** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1071bp / cargo 4700bp (23% utilized)
- Vector tropism plus precedent target match: liver
- Protein class mismatch
- LOF inheritance — compatible for gene replacement
- Different pathway (glycogen_storage vs coagulation)
- Disease mechanism: loss of function — Glucose-6-phosphatase catalytic subunit deficiency
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: G6PC deficiency is a metabolic enzyme loss where liver-directed expression is a plausible gene-addition strategy
- Mechanism source: OMIM G6PC gene entry (https://omim.org/entry/613742)
- Approval status: approved
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Moderate-to-narrow window — early childhood onset; newborn screening integration would significantly improve outcomes
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-high privilege — tolerogenic microenvironment (Kupffer cells, IL-10, PD-L1)
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — G6PC1 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: kidney
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Therapeutic window is not wide; natural-history timing and irreversible damage should be reviewed
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone
