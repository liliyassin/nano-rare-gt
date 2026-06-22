# NanoGT Match Report: Usher syndrome type 1B

**Disease:** Usher syndrome type 1B (ORPHA:886)  
**Primary gene:** MYO7A  
**Gene CDS:** 6648 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** retina, cochlea  

---

## Interpretation

- No high-confidence vector precedent was found; the best result is medium-confidence and should be treated as manual-review territory.
- Main review flags: Vector does not naturally cover all annotated disease tissues: cochlea, retina; No direct tissue overlap; treat this as weak precedent unless route or modality is changed; Cell-autonomous protein across multiple tissues; high transduction coverage may be required.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** MYO7A myosin VIIA deficiency causing combined deafblindness; large CDS (~6.6 kb) exceeds single-AAV capacity  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** dual aav or lv retinal cochlear delivery  
**Evidence level/status:** direct / needs_user_fact_check  
**Evidence summary:** MYO7A LOF supports gene addition logic but oversized CDS requires dual-AAV or lentiviral strategies for retinal and cochlear delivery  
**Evidence source:** [OMIM MYO7A 276900](https://omim.org/entry/276900)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and integrating ex vivo HSC vector precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Few catalog vectors cover the annotated disease tissue(s): AAV2.
- Endpoint readiness: retinal diseases often have measurable endpoints such as OCT, ERG, visual acuity, visual fields, or mobility testing, but genotype-specific progression still needs confirmation.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 4 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Strimvelis | LV | 6.5/10 | 🟡 Medium | approved |
| 2 | Libmeldy | LV | 6.0/10 | 🟡 Medium | approved |
| 3 | Skysona | LV | 5.9/10 | 🟡 Medium | approved |
| 4 | AVR-RD-01 | LV | 5.6/10 | 🟡 Medium | phase1/2 |

---

## Match #1: Strimvelis

**Precedent disease:** ADA-SCID  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 6.5 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.80 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.48** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 6648bp / cargo 8000bp (83% utilized)
- No tissue overlap (disease: ['retina', 'cochlea'], vector: ['hematopoietic'])
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Different pathway (retinal_phototransduction vs immune_hematopoietic)
- Disease mechanism: loss of function — MYO7A myosin VIIA deficiency causing combined deafblindness; large CDS (~6.6 kb) exceeds single-AAV capacity
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: MYO7A LOF supports gene addition logic but oversized CDS requires dual-AAV or lentiviral strategies for retinal and cochlear delivery
- Mechanism source: OMIM MYO7A 276900 (https://omim.org/entry/276900)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Narrow therapeutic window — neonatal onset requires delivery within weeks of birth; trial design must incorporate newborn screening programmes
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010
- ORGANELLE TARGETING: COMPATIBLE — MYO7A standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: cochlea, retina
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #2: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.80 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.00** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 6648bp / cargo 8000bp (83% utilized)
- No tissue overlap (disease: ['retina', 'cochlea'], vector: ['hematopoietic'])
- Protein class mismatch
- Inheritance match (Autosomal recessive <-> AR)
- Different pathway (retinal_phototransduction vs leukodystrophy)
- Disease mechanism: loss of function — MYO7A myosin VIIA deficiency causing combined deafblindness; large CDS (~6.6 kb) exceeds single-AAV capacity
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: MYO7A LOF supports gene addition logic but oversized CDS requires dual-AAV or lentiviral strategies for retinal and cochlear delivery
- Mechanism source: OMIM MYO7A 276900 (https://omim.org/entry/276900)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Narrow therapeutic window — neonatal onset requires delivery within weeks of birth; trial design must incorporate newborn screening programmes
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010
- ORGANELLE TARGETING: COMPATIBLE — MYO7A standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: cochlea, retina
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #3: Skysona

**Precedent disease:** Cerebral adrenoleukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 5.9 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.80 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **5.86** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 6648bp / cargo 8000bp (83% utilized)
- No tissue overlap (disease: ['retina', 'cochlea'], vector: ['hematopoietic'])
- Protein class mismatch
- LOF inheritance — compatible for gene replacement
- Different pathway (retinal_phototransduction vs peroxisomal)
- Disease mechanism: loss of function — MYO7A myosin VIIA deficiency causing combined deafblindness; large CDS (~6.6 kb) exceeds single-AAV capacity
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: MYO7A LOF supports gene addition logic but oversized CDS requires dual-AAV or lentiviral strategies for retinal and cochlear delivery
- Mechanism source: OMIM MYO7A 276900 (https://omim.org/entry/276900)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Narrow therapeutic window — neonatal onset requires delivery within weeks of birth; trial design must incorporate newborn screening programmes
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010
- ORGANELLE TARGETING: COMPATIBLE — MYO7A standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: cochlea, retina
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #4: AVR-RD-01

**Precedent disease:** Fabry disease  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 5.6 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.80 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **5.62** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 6648bp / cargo 8000bp (83% utilized)
- No tissue overlap (disease: ['retina', 'cochlea'], vector: ['hematopoietic'])
- Protein class mismatch
- LOF inheritance — compatible for gene replacement
- Different pathway (retinal_phototransduction vs lysosomal_storage)
- Disease mechanism: loss of function — MYO7A myosin VIIA deficiency causing combined deafblindness; large CDS (~6.6 kb) exceeds single-AAV capacity
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: MYO7A LOF supports gene addition logic but oversized CDS requires dual-AAV or lentiviral strategies for retinal and cochlear delivery
- Mechanism source: OMIM MYO7A 276900 (https://omim.org/entry/276900)
- Approval status: phase1/2
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Narrow therapeutic window — neonatal onset requires delivery within weeks of birth; trial design must incorporate newborn screening programmes
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010
- ORGANELLE TARGETING: COMPATIBLE — MYO7A standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: cochlea, retina
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

---

## Excluded Programs (Packaging Failure)

| Program | Vector | Gene CDS Issue |
|---------|--------|----------------|
| ABO-101 | AAV9 | Gene CDS (6648bp) exceeds vector cargo (4700bp) — hard fail |
| AT132 | AAV8 | Gene CDS (6648bp) exceeds vector cargo (4700bp) — hard fail |
| BMN 307 | AAV5 | Gene CDS (6648bp) exceeds vector cargo (4700bp) — hard fail |
| CPCB-RPE1 | AAV8 | Gene CDS (6648bp) exceeds vector cargo (4700bp) — hard fail |
| DTX201 | AAV8 | Gene CDS (6648bp) exceeds vector cargo (4700bp) — hard fail |
