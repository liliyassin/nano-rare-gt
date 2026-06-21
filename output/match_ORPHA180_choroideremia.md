# NanoGT Match Report: Choroideremia

**Disease:** Choroideremia (ORPHA:180)  
**Primary gene:** CHM  
**Gene CDS:** 1962 bp  
**Inheritance:** X-linked recessive  
**Target tissues scored:** retina  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone; Vector does not naturally cover all annotated disease tissues: retina; No direct tissue overlap; treat this as weak precedent unless route or modality is changed.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** REP1 deficiency affecting retinal cells  
**Gene-addition compatibility:** compatible  
**Preferred modality class:** retinal gene addition  
**Evidence level/status:** direct / source_linked_needs_review  
**Evidence summary:** CHM loss of function is a retinal gene-addition target if viable retina remains  
**Evidence source:** [OMIM CHM gene entry](https://omim.org/entry/300390)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Few catalog vectors cover the annotated disease tissue(s): AAV2.
- Endpoint readiness: retinal diseases often have measurable endpoints such as OCT, ERG, visual acuity, visual fields, or mobility testing, but genotype-specific progression still needs confirmation.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Luxturna | AAV2 | 8.0/10 | 🟢 High | approved |
| 2 | Strimvelis | LV | 7.4/10 | 🟡 Medium | approved |
| 3 | CPCB-RPE1 | AAV8 | 7.3/10 | 🟡 Medium | phase2/3 |
| 4 | Skysona | LV | 7.0/10 | 🟡 Medium | approved |
| 5 | BMN 307 | AAV5 | 7.0/10 | 🟡 Medium | phase2 |

---

## Match #1: Luxturna

**Precedent disease:** Leber congenital amaurosis type 2  
**Vector:** AAV2  
**Tissue target:** retina/RPE  
**Composite score:** 8.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 0.50 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.95** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1962bp / cargo 4700bp (42% utilized)
- Vector tropism plus precedent target match: retina
- Both intracellular proteins
- LOF inheritance — compatible for gene replacement
- Pathway match: retinal_visual_cycle
- Disease mechanism: loss of function — REP1 deficiency affecting retinal cells
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: CHM loss of function is a retinal gene-addition target if viable retina remains
- Mechanism source: OMIM CHM gene entry (https://omim.org/entry/300390)
- Approval status: approved
- Vector immunogenicity (AAV2): very high (~55%) — majority of patients may be ineligible; major trial design challenge
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010
- ORGANELLE TARGETING: COMPATIBLE — CHM standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #2: Strimvelis

**Precedent disease:** ADA-SCID  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 7.4 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.38** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1962bp / cargo 8000bp (25% utilized)
- No tissue overlap (disease: ['retina'], vector: ['hematopoietic'])
- Both intracellular proteins
- LOF inheritance — compatible for gene replacement
- Different pathway (retinal_phototransduction vs immune_hematopoietic)
- Disease mechanism: loss of function — REP1 deficiency affecting retinal cells
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: CHM loss of function is a retinal gene-addition target if viable retina remains
- Mechanism source: OMIM CHM gene entry (https://omim.org/entry/300390)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010
- ORGANELLE TARGETING: COMPATIBLE — CHM standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: retina
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed

## Match #3: CPCB-RPE1

**Precedent disease:** Achromatopsia  
**Vector:** AAV8  
**Tissue target:** retina/photoreceptor  
**Composite score:** 7.3 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.70 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.33** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1962bp / cargo 4700bp (42% utilized)
- Precedent target match: retina
- Protein class mismatch
- LOF inheritance — compatible for gene replacement
- Pathway match: retinal_phototransduction
- Disease mechanism: loss of function — REP1 deficiency affecting retinal cells
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: CHM loss of function is a retinal gene-addition target if viable retina remains
- Mechanism source: OMIM CHM gene entry (https://omim.org/entry/300390)
- Approval status: phase2/3
- Vector immunogenicity (AAV8): high (~30%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010
- ORGANELLE TARGETING: COMPATIBLE — CHM standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: retina
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: Skysona

**Precedent disease:** Cerebral adrenoleukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 7.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.05** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1962bp / cargo 8000bp (25% utilized)
- No tissue overlap (disease: ['retina'], vector: ['hematopoietic'])
- Protein class mismatch
- Inheritance match (X-linked recessive <-> XL)
- Different pathway (retinal_phototransduction vs peroxisomal)
- Disease mechanism: loss of function — REP1 deficiency affecting retinal cells
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: CHM loss of function is a retinal gene-addition target if viable retina remains
- Mechanism source: OMIM CHM gene entry (https://omim.org/entry/300390)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010
- ORGANELLE TARGETING: COMPATIBLE — CHM standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: retina
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed

## Match #5: BMN 307

**Precedent disease:** Phenylketonuria  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 7.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.60 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.95** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1962bp / cargo 4700bp (42% utilized)
- No tissue overlap (disease: ['retina'], vector: ['liver', 'lung', 'CNS'])
- Both intracellular proteins
- LOF inheritance — compatible for gene replacement
- Different pathway (retinal_phototransduction vs amino_acid_metabolism)
- Disease mechanism: loss of function — REP1 deficiency affecting retinal cells
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: CHM loss of function is a retinal gene-addition target if viable retina remains
- Mechanism source: OMIM CHM gene entry (https://omim.org/entry/300390)
- Approval status: phase2
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010
- ORGANELLE TARGETING: COMPATIBLE — CHM standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: retina
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone
