# NanoGT Match Report: Achromatopsia

**Disease:** Achromatopsia (ORPHA:49382)  
**Primary gene:** CNGB3  
**Gene CDS:** 2427 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** retina  
**Gene selection note:** this disease has multiple listed genes (CNGB3, CNGA3, GNAT2, PDE6C, PDE6H, ATF6); this report scores CNGB3 only.  

---

## Interpretation

- No high-confidence vector precedent was found; the best result is medium-confidence and should be treated as manual-review territory.
- Main review flags: Multiple causal genes listed; score is gene-specific and should be repeated for each molecular subtype; Vector does not naturally cover all annotated disease tissues: retina; Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** Cone cyclic nucleotide-gated channel beta-subunit loss  
**Gene-addition compatibility:** compatible  
**Preferred modality class:** retinal gene addition  
**Evidence level/status:** direct / source_linked_needs_review  
**Evidence summary:** Biallelic CNGB3 loss is compatible with photoreceptor-directed gene addition if target cells remain viable  
**Evidence source:** [OMIM CNGB3 gene entry](https://omim.org/entry/605080)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Few catalog vectors cover the annotated disease tissue(s): AAV2.
- Endpoint readiness: retinal diseases often have measurable endpoints such as OCT, ERG, visual acuity, visual fields, or mobility testing, but genotype-specific progression still needs confirmation.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | CPCB-RPE1 | AAV8 | 7.3/10 | 🟡 Medium | phase2/3 |
| 2 | Luxturna | AAV2 | 7.0/10 | 🟡 Medium | approved |
| 3 | Skysona | LV | 6.5/10 | 🟡 Medium | approved |
| 4 | Libmeldy | LV | 6.2/10 | 🟡 Medium | approved |
| 5 | Strimvelis | LV | 6.2/10 | 🟡 Medium | approved |

---

## Match #1: CPCB-RPE1

**Precedent disease:** Achromatopsia  
**Vector:** AAV8  
**Tissue target:** retina/photoreceptor  
**Composite score:** 7.3 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.70 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **7.35** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 2427bp / cargo 4700bp (52% utilized)
- Precedent target match: retina
- Both membrane proteins
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: retinal_phototransduction
- Disease mechanism: loss of function — Cone cyclic nucleotide-gated channel beta-subunit loss
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: Biallelic CNGB3 loss is compatible with photoreceptor-directed gene addition if target cells remain viable
- Mechanism source: OMIM CNGB3 gene entry (https://omim.org/entry/605080)
- Approval status: phase2/3
- Vector immunogenicity (AAV8): high (~30%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010

### Manual Review Flags

- Multiple causal genes listed; score is gene-specific and should be repeated for each molecular subtype
- Vector does not naturally cover all annotated disease tissues: retina
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #2: Luxturna

**Precedent disease:** Leber congenital amaurosis type 2  
**Vector:** AAV2  
**Tissue target:** retina/RPE  
**Composite score:** 7.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 0.50 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **7.00** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 2427bp / cargo 4700bp (52% utilized)
- Vector tropism plus precedent target match: retina
- Protein class mismatch
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: retinal_visual_cycle
- Disease mechanism: loss of function — Cone cyclic nucleotide-gated channel beta-subunit loss
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: Biallelic CNGB3 loss is compatible with photoreceptor-directed gene addition if target cells remain viable
- Mechanism source: OMIM CNGB3 gene entry (https://omim.org/entry/605080)
- Approval status: approved
- Vector immunogenicity (AAV2): very high (~55%) — majority of patients may be ineligible; major trial design challenge
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010

### Manual Review Flags

- Multiple causal genes listed; score is gene-specific and should be repeated for each molecular subtype
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #3: Skysona

**Precedent disease:** Cerebral adrenoleukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.5 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **6.50** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 2427bp / cargo 8000bp (30% utilized)
- No tissue overlap (disease: ['retina'], vector: ['hematopoietic'])
- Both membrane proteins
- LOF inheritance — compatible for gene replacement
- Different pathway (retinal_phototransduction vs peroxisomal)
- Disease mechanism: loss of function — Cone cyclic nucleotide-gated channel beta-subunit loss
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: Biallelic CNGB3 loss is compatible with photoreceptor-directed gene addition if target cells remain viable
- Mechanism source: OMIM CNGB3 gene entry (https://omim.org/entry/605080)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010

### Manual Review Flags

- Multiple causal genes listed; score is gene-specific and should be repeated for each molecular subtype
- Vector does not naturally cover all annotated disease tissues: retina
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility

## Match #4: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.2 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **6.15** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 2427bp / cargo 8000bp (30% utilized)
- No tissue overlap (disease: ['retina'], vector: ['hematopoietic'])
- Protein class mismatch
- Inheritance match (Autosomal recessive <-> AR)
- Different pathway (retinal_phototransduction vs leukodystrophy)
- Disease mechanism: loss of function — Cone cyclic nucleotide-gated channel beta-subunit loss
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: Biallelic CNGB3 loss is compatible with photoreceptor-directed gene addition if target cells remain viable
- Mechanism source: OMIM CNGB3 gene entry (https://omim.org/entry/605080)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010

### Manual Review Flags

- Multiple causal genes listed; score is gene-specific and should be repeated for each molecular subtype
- Vector does not naturally cover all annotated disease tissues: retina
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility

## Match #5: Strimvelis

**Precedent disease:** ADA-SCID  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 6.2 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **6.15** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 2427bp / cargo 8000bp (30% utilized)
- No tissue overlap (disease: ['retina'], vector: ['hematopoietic'])
- Protein class mismatch
- Inheritance match (Autosomal recessive <-> AR)
- Different pathway (retinal_phototransduction vs immune_hematopoietic)
- Disease mechanism: loss of function — Cone cyclic nucleotide-gated channel beta-subunit loss
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: Biallelic CNGB3 loss is compatible with photoreceptor-directed gene addition if target cells remain viable
- Mechanism source: OMIM CNGB3 gene entry (https://omim.org/entry/605080)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010

### Manual Review Flags

- Multiple causal genes listed; score is gene-specific and should be repeated for each molecular subtype
- Vector does not naturally cover all annotated disease tissues: retina
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
