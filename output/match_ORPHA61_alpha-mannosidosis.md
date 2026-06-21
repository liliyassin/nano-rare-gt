# NanoGT Match Report: Alpha-mannosidosis

**Disease:** Alpha-mannosidosis (ORPHA:61)  
**Primary gene:** MAN2B1  
**Gene CDS:** 3033 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** CNS, liver  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints; Vector does not naturally cover all annotated disease tissues: cns, liver; Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** Lysosomal alpha-mannosidase enzyme deficiency  
**Gene-addition compatibility:** compatible  
**Preferred modality class:** gene addition or cross correction  
**Evidence level/status:** direct / source_linked_needs_review  
**Evidence summary:** Lysosomal enzyme deficiency supports gene addition and possible cross-correction logic  
**Evidence source:** [OMIM MAN2B1 gene entry](https://omim.org/entry/609458)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint readiness: liver/metabolic targets may have biochemical biomarkers, but biomarker correction must be linked to clinical benefit.
- Endpoint risk: CNS/neurodevelopmental outcomes may require natural-history data, age-stratified endpoints, and long follow-up because short-term clinical change can be hard to interpret.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Libmeldy | LV | 8.7/10 | 🟢 High | approved |
| 2 | ST-920 | AAV2/6 | 8.1/10 | 🟢 High | phase1/2 |
| 3 | ABO-101 | AAV9 | 8.0/10 | 🟢 High | phase1/2 |
| 4 | RGX-121 | AAV9 | 8.0/10 | 🟢 High | phase3 |
| 5 | Hemgenix | AAV5 | 7.8/10 | 🟢 High | approved |

---

## Match #1: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 8.7 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **8.70** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 3033bp / cargo 8000bp (38% utilized)
- Precedent target match: cns
- Both lysosomal proteins — cross-correction likely
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: leukodystrophy
- Disease mechanism: loss of function — Lysosomal alpha-mannosidase enzyme deficiency
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: Lysosomal enzyme deficiency supports gene addition and possible cross-correction logic
- Mechanism source: OMIM MAN2B1 gene entry (https://omim.org/entry/609458)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Secreted lysosomal enzyme — maximum cross-correction via M6P receptor pathway; high therapeutic efficiency; substantially lower required transduction rate
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: cns, liver
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility

## Match #2: ST-920

**Precedent disease:** Fabry disease  
**Vector:** AAV2/6  
**Tissue target:** liver  
**Composite score:** 8.1 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.50 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **8.05** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 3033bp / cargo 4700bp (65% utilized)
- Vector tropism plus precedent target match: liver
- Both lysosomal proteins — cross-correction likely
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Lysosomal alpha-mannosidase enzyme deficiency
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: Lysosomal enzyme deficiency supports gene addition and possible cross-correction logic
- Mechanism source: OMIM MAN2B1 gene entry (https://omim.org/entry/609458)
- Approval status: phase1/2
- Vector immunogenicity (AAV2/6): moderate (~17%) — significant proportion may require pre-screening or exclusion
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Secreted lysosomal enzyme — maximum cross-correction via M6P receptor pathway; high therapeutic efficiency; substantially lower required transduction rate
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: cns
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #3: ABO-101

**Precedent disease:** Mucopolysaccharidosis type IIIB  
**Vector:** AAV9  
**Tissue target:** CNS  
**Composite score:** 8.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **7.95** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 3033bp / cargo 4700bp (65% utilized)
- Vector tropism plus precedent target match: cns
- Both lysosomal proteins — cross-correction likely
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Lysosomal alpha-mannosidase enzyme deficiency
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: Lysosomal enzyme deficiency supports gene addition and possible cross-correction logic
- Mechanism source: OMIM MAN2B1 gene entry (https://omim.org/entry/609458)
- Approval status: phase1/2
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Secreted lysosomal enzyme — maximum cross-correction via M6P receptor pathway; high therapeutic efficiency; substantially lower required transduction rate
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: RGX-121

**Precedent disease:** Mucopolysaccharidosis type II  
**Vector:** AAV9  
**Tissue target:** CNS/liver  
**Composite score:** 8.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.80 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **7.95** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 3033bp / cargo 4700bp (65% utilized)
- Vector tropism plus precedent target match: cns, liver
- Both lysosomal proteins — cross-correction likely
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Lysosomal alpha-mannosidase enzyme deficiency
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: Lysosomal enzyme deficiency supports gene addition and possible cross-correction logic
- Mechanism source: OMIM MAN2B1 gene entry (https://omim.org/entry/609458)
- Approval status: phase3
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Secreted lysosomal enzyme — maximum cross-correction via M6P receptor pathway; high therapeutic efficiency; substantially lower required transduction rate
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #5: Hemgenix

**Precedent disease:** Hemophilia B  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 7.8 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **7.80** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 3033bp / cargo 4700bp (65% utilized)
- Vector tropism plus precedent target match: liver
- Both secreted proteins — systemic delivery viable
- LOF inheritance — compatible for gene replacement
- Different pathway (lysosomal_storage vs coagulation)
- Disease mechanism: loss of function — Lysosomal alpha-mannosidase enzyme deficiency
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: Lysosomal enzyme deficiency supports gene addition and possible cross-correction logic
- Mechanism source: OMIM MAN2B1 gene entry (https://omim.org/entry/609458)
- Approval status: approved
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Secreted lysosomal enzyme — maximum cross-correction via M6P receptor pathway; high therapeutic efficiency; substantially lower required transduction rate
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone
