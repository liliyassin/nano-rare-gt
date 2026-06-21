# NanoGT Match Report: Pompe disease

**Disease:** Pompe disease (ORPHA:365)  
**Primary gene:** GAA  
**Gene CDS:** 2856 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** muscle, heart  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints; Vector does not naturally cover all annotated disease tissues: heart, muscle; No direct tissue overlap; treat this as weak precedent unless route or modality is changed.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** Acid alpha-glucosidase lysosomal enzyme deficiency  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** gene addition or secreted enzyme rescue  
**Evidence level/status:** direct / source_linked_needs_review  
**Evidence summary:** GAA deficiency supports replacement logic but skeletal and cardiac delivery needs broad tissue correction  
**Evidence source:** [OMIM GAA gene entry](https://omim.org/entry/606800)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint risk: muscle/cardiac diseases may need functional, respiratory, imaging, or cardiac endpoints that progress slowly and vary by age/stage.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Libmeldy | LV | 8.4/10 | 🟢 High | approved |
| 2 | ABO-101 | AAV9 | 8.0/10 | 🟢 High | phase1/2 |
| 3 | AVR-RD-01 | LV | 8.0/10 | 🟢 High | phase1/2 |
| 4 | RGX-121 | AAV9 | 8.0/10 | 🟢 High | phase3 |
| 5 | ST-920 | AAV2/6 | 7.9/10 | 🟢 High | phase1/2 |

---

## Match #1: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 8.4 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 2.00 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.60 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.38** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 2856bp / cargo 8000bp (36% utilized)
- No tissue overlap (disease: ['muscle', 'heart'], vector: ['hematopoietic'])
- Both lysosomal enzymes — cross-correction via M6P receptor pathway likely
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: leukodystrophy
- Disease mechanism: loss of function — Acid alpha-glucosidase lysosomal enzyme deficiency
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: GAA deficiency supports replacement logic but skeletal and cardiac delivery needs broad tissue correction
- Mechanism source: OMIM GAA gene entry (https://omim.org/entry/606800)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Wide therapeutic window — adult or chronic onset; GT can be administered at multiple timepoints; irreversible damage has not yet occurred at typical diagnosis age
- Secreted lysosomal enzyme — maximum cross-correction via M6P receptor pathway; high therapeutic efficiency; substantially lower required transduction rate
- Immune privilege: moderate immune surveillance — standard immunosuppression protocols typically sufficient
- Promoter availability: MHCK7, CK8, Desmin — validated in Elevidys (DMD) and SMA programs
- Route of administration: IV systemic or intramuscular injection — well established; used in SMA, DMD, Glybera
- ORGANELLE TARGETING: COMPATIBLE — GAA standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: heart, muscle
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #2: ABO-101

**Precedent disease:** Mucopolysaccharidosis type IIIB  
**Vector:** AAV9  
**Tissue target:** CNS  
**Composite score:** 8.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 2.00 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.60 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.00** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 2856bp / cargo 4700bp (61% utilized)
- Vector tropism overlap: heart, muscle
- Both lysosomal enzymes — cross-correction via M6P receptor pathway likely
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Acid alpha-glucosidase lysosomal enzyme deficiency
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: GAA deficiency supports replacement logic but skeletal and cardiac delivery needs broad tissue correction
- Mechanism source: OMIM GAA gene entry (https://omim.org/entry/606800)
- Approval status: phase1/2
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Wide therapeutic window — adult or chronic onset; GT can be administered at multiple timepoints; irreversible damage has not yet occurred at typical diagnosis age
- Secreted lysosomal enzyme — maximum cross-correction via M6P receptor pathway; high therapeutic efficiency; substantially lower required transduction rate
- Immune privilege: moderate immune surveillance — standard immunosuppression protocols typically sufficient
- Promoter availability: MHCK7, CK8, Desmin — validated in Elevidys (DMD) and SMA programs
- Route of administration: IV systemic or intramuscular injection — well established; used in SMA, DMD, Glybera
- ORGANELLE TARGETING: COMPATIBLE — GAA standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #3: AVR-RD-01

**Precedent disease:** Fabry disease  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 8.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 2.00 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.60 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.00** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 2856bp / cargo 8000bp (36% utilized)
- No tissue overlap (disease: ['muscle', 'heart'], vector: ['hematopoietic'])
- Both lysosomal enzymes — cross-correction via M6P receptor pathway likely
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Acid alpha-glucosidase lysosomal enzyme deficiency
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: GAA deficiency supports replacement logic but skeletal and cardiac delivery needs broad tissue correction
- Mechanism source: OMIM GAA gene entry (https://omim.org/entry/606800)
- Approval status: phase1/2
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Wide therapeutic window — adult or chronic onset; GT can be administered at multiple timepoints; irreversible damage has not yet occurred at typical diagnosis age
- Secreted lysosomal enzyme — maximum cross-correction via M6P receptor pathway; high therapeutic efficiency; substantially lower required transduction rate
- Immune privilege: moderate immune surveillance — standard immunosuppression protocols typically sufficient
- Promoter availability: MHCK7, CK8, Desmin — validated in Elevidys (DMD) and SMA programs
- Route of administration: IV systemic or intramuscular injection — well established; used in SMA, DMD, Glybera
- ORGANELLE TARGETING: COMPATIBLE — GAA standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: heart, muscle
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #4: RGX-121

**Precedent disease:** Mucopolysaccharidosis type II  
**Vector:** AAV9  
**Tissue target:** CNS/liver  
**Composite score:** 8.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.80 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 2.00 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.60 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.00** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 2856bp / cargo 4700bp (61% utilized)
- Vector tropism overlap: heart, muscle
- Both lysosomal enzymes — cross-correction via M6P receptor pathway likely
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Acid alpha-glucosidase lysosomal enzyme deficiency
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: GAA deficiency supports replacement logic but skeletal and cardiac delivery needs broad tissue correction
- Mechanism source: OMIM GAA gene entry (https://omim.org/entry/606800)
- Approval status: phase3
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Wide therapeutic window — adult or chronic onset; GT can be administered at multiple timepoints; irreversible damage has not yet occurred at typical diagnosis age
- Secreted lysosomal enzyme — maximum cross-correction via M6P receptor pathway; high therapeutic efficiency; substantially lower required transduction rate
- Immune privilege: moderate immune surveillance — standard immunosuppression protocols typically sufficient
- Promoter availability: MHCK7, CK8, Desmin — validated in Elevidys (DMD) and SMA programs
- Route of administration: IV systemic or intramuscular injection — well established; used in SMA, DMD, Glybera
- ORGANELLE TARGETING: COMPATIBLE — GAA standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #5: ST-920

**Precedent disease:** Fabry disease  
**Vector:** AAV2/6  
**Tissue target:** liver  
**Composite score:** 7.9 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.50 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 2.00 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.60 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.86** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 2856bp / cargo 4700bp (61% utilized)
- Vector tropism overlaps muscle, but precedent target is liver
- Both lysosomal enzymes — cross-correction via M6P receptor pathway likely
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Acid alpha-glucosidase lysosomal enzyme deficiency
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: GAA deficiency supports replacement logic but skeletal and cardiac delivery needs broad tissue correction
- Mechanism source: OMIM GAA gene entry (https://omim.org/entry/606800)
- Approval status: phase1/2
- Vector immunogenicity (AAV2/6): moderate (~17%) — significant proportion may require pre-screening or exclusion
- Wide therapeutic window — adult or chronic onset; GT can be administered at multiple timepoints; irreversible damage has not yet occurred at typical diagnosis age
- Secreted lysosomal enzyme — maximum cross-correction via M6P receptor pathway; high therapeutic efficiency; substantially lower required transduction rate
- Immune privilege: moderate immune surveillance — standard immunosuppression protocols typically sufficient
- Promoter availability: MHCK7, CK8, Desmin — validated in Elevidys (DMD) and SMA programs
- Route of administration: IV systemic or intramuscular injection — well established; used in SMA, DMD, Glybera
- ORGANELLE TARGETING: COMPATIBLE — GAA standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: heart
- Only partial tissue match; verify target-cell transduction and delivery route manually
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone
