# NanoGT Match Report: Mucolipidosis type IV

**Disease:** Mucolipidosis type IV (ORPHA:578)  
**Primary gene:** MCOLN1  
**Gene CDS:** 1740 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** CNS, retina  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints; Vector does not naturally cover all annotated disease tissues: cns, retina; Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** TRPML1 lysosomal membrane channel deficiency  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** cell autonomous gene addition  
**Evidence level/status:** direct / source_linked_needs_review  
**Evidence summary:** MCOLN1 loss supports gene addition but membrane-channel biology is cell-autonomous and not a strong cross-correction case  
**Evidence source:** [OMIM MCOLN1 gene entry](https://omim.org/entry/605248)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint readiness: retinal diseases often have measurable endpoints such as OCT, ERG, visual acuity, visual fields, or mobility testing, but genotype-specific progression still needs confirmation.
- Endpoint risk: CNS/neurodevelopmental outcomes may require natural-history data, age-stratified endpoints, and long follow-up because short-term clinical change can be hard to interpret.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Libmeldy | LV | 9.1/10 | 🟢 High | approved |
| 2 | Skysona | LV | 8.7/10 | 🟢 High | approved |
| 3 | ABO-101 | AAV9 | 8.3/10 | 🟢 High | phase1/2 |
| 4 | RGX-121 | AAV9 | 8.3/10 | 🟢 High | phase3 |
| 5 | AVR-RD-01 | LV | 8.1/10 | 🟢 High | phase1/2 |

---

## Match #1: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 9.1 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.80 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **9.05** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 1740bp / cargo 8000bp (22% utilized)
- Precedent target match: cns
- Both lysosomal proteins — cross-correction likely
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: leukodystrophy
- Disease mechanism: loss of function — TRPML1 lysosomal membrane channel deficiency
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: MCOLN1 loss supports gene addition but membrane-channel biology is cell-autonomous and not a strong cross-correction case
- Mechanism source: OMIM MCOLN1 gene entry (https://omim.org/entry/605248)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Lysosomal enzyme (non-secreted) — moderate cross-correction via M6P pathway; neighbouring cells can benefit but uptake efficiency is lower than fully secreted
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: cns, retina
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #2: Skysona

**Precedent disease:** Cerebral adrenoleukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 8.7 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.80 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **8.65** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 1740bp / cargo 8000bp (22% utilized)
- Precedent target match: cns
- Both membrane proteins
- LOF inheritance — compatible for gene replacement
- Pathway match: peroxisomal
- Disease mechanism: loss of function — TRPML1 lysosomal membrane channel deficiency
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: MCOLN1 loss supports gene addition but membrane-channel biology is cell-autonomous and not a strong cross-correction case
- Mechanism source: OMIM MCOLN1 gene entry (https://omim.org/entry/605248)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Lysosomal enzyme (non-secreted) — moderate cross-correction via M6P pathway; neighbouring cells can benefit but uptake efficiency is lower than fully secreted
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: cns, retina
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #3: ABO-101

**Precedent disease:** Mucopolysaccharidosis type IIIB  
**Vector:** AAV9  
**Tissue target:** CNS  
**Composite score:** 8.3 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.80 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **8.30** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 1740bp / cargo 4700bp (37% utilized)
- Vector tropism plus precedent target match: cns
- Both lysosomal proteins — cross-correction likely
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — TRPML1 lysosomal membrane channel deficiency
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: MCOLN1 loss supports gene addition but membrane-channel biology is cell-autonomous and not a strong cross-correction case
- Mechanism source: OMIM MCOLN1 gene entry (https://omim.org/entry/605248)
- Approval status: phase1/2
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Lysosomal enzyme (non-secreted) — moderate cross-correction via M6P pathway; neighbouring cells can benefit but uptake efficiency is lower than fully secreted
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: retina
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: RGX-121

**Precedent disease:** Mucopolysaccharidosis type II  
**Vector:** AAV9  
**Tissue target:** CNS/liver  
**Composite score:** 8.3 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.80 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.80 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **8.30** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 1740bp / cargo 4700bp (37% utilized)
- Vector tropism plus precedent target match: cns
- Both lysosomal proteins — cross-correction likely
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — TRPML1 lysosomal membrane channel deficiency
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: MCOLN1 loss supports gene addition but membrane-channel biology is cell-autonomous and not a strong cross-correction case
- Mechanism source: OMIM MCOLN1 gene entry (https://omim.org/entry/605248)
- Approval status: phase3
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Lysosomal enzyme (non-secreted) — moderate cross-correction via M6P pathway; neighbouring cells can benefit but uptake efficiency is lower than fully secreted
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: retina
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #5: AVR-RD-01

**Precedent disease:** Fabry disease  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 8.1 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.80 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **8.05** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 1740bp / cargo 8000bp (22% utilized)
- No tissue overlap (disease: ['CNS', 'retina'], vector: ['hematopoietic'])
- Both lysosomal proteins — cross-correction likely
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — TRPML1 lysosomal membrane channel deficiency
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: MCOLN1 loss supports gene addition but membrane-channel biology is cell-autonomous and not a strong cross-correction case
- Mechanism source: OMIM MCOLN1 gene entry (https://omim.org/entry/605248)
- Approval status: phase1/2
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Lysosomal enzyme (non-secreted) — moderate cross-correction via M6P pathway; neighbouring cells can benefit but uptake efficiency is lower than fully secreted
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: cns, retina
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
