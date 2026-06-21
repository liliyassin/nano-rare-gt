# NanoGT Match Report: Wiskott-Aldrich syndrome

**Disease:** Wiskott-Aldrich syndrome (ORPHA:906)  
**Primary gene:** WAS  
**Gene CDS:** 1506 bp  
**Inheritance:** X-linked recessive  
**Target tissues scored:** hematopoietic  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility; Vector does not naturally cover all annotated disease tissues: hematopoietic; No direct tissue overlap; treat this as weak precedent unless route or modality is changed.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** WASP deficiency in hematopoietic cells  
**Gene-addition compatibility:** compatible  
**Preferred modality class:** ex vivo hsc gene addition  
**Evidence level/status:** direct / source_linked_needs_review  
**Evidence summary:** WAS loss of function is compatible with autologous hematopoietic stem-cell gene addition  
**Evidence source:** [OMIM WAS gene entry](https://omim.org/entry/300392)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Few catalog vectors cover the annotated disease tissue(s): LV.
- Endpoint readiness unclear from available annotations; identify biomarkers, natural-history measures, and patient-relevant outcomes before trial prioritisation.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Strimvelis | LV | 7.9/10 | 🟢 High | approved |
| 2 | Skysona | LV | 6.8/10 | 🟡 Medium | approved |
| 3 | Libmeldy | LV | 6.7/10 | 🟡 Medium | approved |
| 4 | AVR-RD-01 | LV | 6.5/10 | 🟡 Medium | phase1/2 |
| 5 | BMN 307 | AAV5 | 5.8/10 | 🟡 Medium | phase2 |

---

## Match #1: Strimvelis

**Precedent disease:** ADA-SCID  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 7.9 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.30 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.70 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **7.90** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 1506bp / cargo 8000bp (19% utilized)
- Vector tropism plus precedent target match: hematopoietic
- Both intracellular proteins
- LOF inheritance — compatible for gene replacement
- Pathway match: immune_hematopoietic
- Disease mechanism: loss of function — WASP deficiency in hematopoietic cells
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: WAS loss of function is compatible with autologous hematopoietic stem-cell gene addition
- Mechanism source: OMIM WAS gene entry (https://omim.org/entry/300392)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: low privilege — immune cells reside here; robust conditioning and monitoring required
- Promoter availability: EFS, PGK, SFFV — validated in lentiviral ex vivo programs (ADA-SCID, beta-thalassaemia)
- Route of administration: Ex vivo HSC delivery — technically complex but highly precise; gold standard for blood disorders

### Manual Review Flags

- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility

## Match #2: Skysona

**Precedent disease:** Cerebral adrenoleukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.8 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.30 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.70 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **6.80** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 1506bp / cargo 8000bp (19% utilized)
- Vector tropism plus precedent target match: hematopoietic
- Protein class mismatch
- Inheritance match (X-linked recessive <-> XL)
- Different pathway (immune_hematopoietic vs peroxisomal)
- Disease mechanism: loss of function — WASP deficiency in hematopoietic cells
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: WAS loss of function is compatible with autologous hematopoietic stem-cell gene addition
- Mechanism source: OMIM WAS gene entry (https://omim.org/entry/300392)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: low privilege — immune cells reside here; robust conditioning and monitoring required
- Promoter availability: EFS, PGK, SFFV — validated in lentiviral ex vivo programs (ADA-SCID, beta-thalassaemia)
- Route of administration: Ex vivo HSC delivery — technically complex but highly precise; gold standard for blood disorders

### Manual Review Flags

- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility

## Match #3: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.7 / 10  

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
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.30 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.70 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **6.65** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 1506bp / cargo 8000bp (19% utilized)
- Vector tropism plus precedent target match: hematopoietic
- Protein class mismatch
- LOF inheritance — compatible for gene replacement
- Different pathway (immune_hematopoietic vs leukodystrophy)
- Disease mechanism: loss of function — WASP deficiency in hematopoietic cells
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: WAS loss of function is compatible with autologous hematopoietic stem-cell gene addition
- Mechanism source: OMIM WAS gene entry (https://omim.org/entry/300392)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: low privilege — immune cells reside here; robust conditioning and monitoring required
- Promoter availability: EFS, PGK, SFFV — validated in lentiviral ex vivo programs (ADA-SCID, beta-thalassaemia)
- Route of administration: Ex vivo HSC delivery — technically complex but highly precise; gold standard for blood disorders

### Manual Review Flags

- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility

## Match #4: AVR-RD-01

**Precedent disease:** Fabry disease  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 6.5 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.30 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.70 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **6.55** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 1506bp / cargo 8000bp (19% utilized)
- Vector tropism plus precedent target match: hematopoietic
- Protein class mismatch
- Inheritance match (X-linked recessive <-> XL)
- Different pathway (immune_hematopoietic vs lysosomal_storage)
- Disease mechanism: loss of function — WASP deficiency in hematopoietic cells
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: WAS loss of function is compatible with autologous hematopoietic stem-cell gene addition
- Mechanism source: OMIM WAS gene entry (https://omim.org/entry/300392)
- Approval status: phase1/2
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: low privilege — immune cells reside here; robust conditioning and monitoring required
- Promoter availability: EFS, PGK, SFFV — validated in lentiviral ex vivo programs (ADA-SCID, beta-thalassaemia)
- Route of administration: Ex vivo HSC delivery — technically complex but highly precise; gold standard for blood disorders

### Manual Review Flags

- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility

## Match #5: BMN 307

**Precedent disease:** Phenylketonuria  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 5.8 / 10  

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
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.30 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.70 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **5.85** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 1506bp / cargo 4700bp (32% utilized)
- No tissue overlap (disease: ['hematopoietic'], vector: ['liver', 'lung', 'CNS'])
- Both intracellular proteins
- LOF inheritance — compatible for gene replacement
- Different pathway (immune_hematopoietic vs amino_acid_metabolism)
- Disease mechanism: loss of function — WASP deficiency in hematopoietic cells
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: WAS loss of function is compatible with autologous hematopoietic stem-cell gene addition
- Mechanism source: OMIM WAS gene entry (https://omim.org/entry/300392)
- Approval status: phase2
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: low privilege — immune cells reside here; robust conditioning and monitoring required
- Promoter availability: EFS, PGK, SFFV — validated in lentiviral ex vivo programs (ADA-SCID, beta-thalassaemia)
- Route of administration: Ex vivo HSC delivery — technically complex but highly precise; gold standard for blood disorders

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: hematopoietic
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone
