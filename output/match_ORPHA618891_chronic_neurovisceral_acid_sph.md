# NanoGT Match Report: Chronic neurovisceral acid sphingomyelinase deficiency

**Disease:** Chronic neurovisceral acid sphingomyelinase deficiency (ORPHA:618891)  
**Primary gene:** SMPD1  
**Gene CDS:** 1890 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** liver, spleen, lung, CNS  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: LYSOSOMAL MEMBRANE PROTEIN (SMPD1): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.; Multi-system disease; define a primary therapeutic target tissue before selecting route/vector; Vector does not naturally cover all annotated disease tissues: cns, liver, lung, spleen.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** Acid sphingomyelinase deficiency causes sphingomyelin accumulation in liver, spleen, lung, and CNS  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** liver or cns gene addition or cross correction  
**Evidence level/status:** direct / needs_user_fact_check  
**Evidence summary:** SMPD1 is a secreted lysosomal enzyme; cross-correction may be feasible for visceral disease but CNS involvement complicates single-compartment delivery  
**Evidence source:** [OMIM SMPD1 607616](https://omim.org/entry/607616)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and integrating ex vivo HSC vector precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint readiness: liver/metabolic targets may have biochemical biomarkers, but biomarker correction must be linked to clinical benefit.
- Endpoint risk: CNS/neurodevelopmental outcomes may require natural-history data, age-stratified endpoints, and long follow-up because short-term clinical change can be hard to interpret.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Libmeldy | LV | 8.8/10 | 🟢 High | approved |
| 2 | Hemgenix | AAV5 | 8.4/10 | 🟢 High | approved |
| 3 | Roctavian | AAV5 | 8.4/10 | 🟢 High | approved |
| 4 | ST-920 | AAV2/6 | 8.1/10 | 🟢 High | phase1/2 |
| 5 | ABO-101 | AAV9 | 8.1/10 | 🟢 High | phase1/2 |

---

## Match #1: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 8.8 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.76** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1890bp / cargo 8000bp (24% utilized)
- Precedent target match: cns
- Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated cross-correction mechanism of the matched precedent is not applicable. Direct per-cell vector delivery to every target neuron is required.
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: leukodystrophy
- Disease mechanism: loss of function — Acid sphingomyelinase deficiency causes sphingomyelin accumulation in liver, spleen, lung, and CNS
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: SMPD1 is a secreted lysosomal enzyme; cross-correction may be feasible for visceral disease but CNS involvement complicates single-compartment delivery
- Mechanism source: OMIM SMPD1 607616 (https://omim.org/entry/607616)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — SMPD1 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (SMPD1): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Multi-system disease; define a primary therapeutic target tissue before selecting route/vector
- Vector does not naturally cover all annotated disease tissues: cns, liver, lung, spleen
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #2: Hemgenix

**Precedent disease:** Hemophilia B  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 8.4 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.38** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1890bp / cargo 4700bp (40% utilized)
- Vector tropism plus precedent target match: liver
- Both secreted proteins — systemic delivery viable
- LOF inheritance — compatible for gene replacement
- Different pathway (lysosomal_storage vs coagulation)
- Disease mechanism: loss of function — Acid sphingomyelinase deficiency causes sphingomyelin accumulation in liver, spleen, lung, and CNS
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: SMPD1 is a secreted lysosomal enzyme; cross-correction may be feasible for visceral disease but CNS involvement complicates single-compartment delivery
- Mechanism source: OMIM SMPD1 607616 (https://omim.org/entry/607616)
- Approval status: approved
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — SMPD1 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (SMPD1): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Multi-system disease; define a primary therapeutic target tissue before selecting route/vector
- Vector does not naturally cover all annotated disease tissues: spleen
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #3: Roctavian

**Precedent disease:** Hemophilia A  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 8.4 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.38** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1890bp / cargo 4700bp (40% utilized)
- Vector tropism plus precedent target match: liver
- Both secreted proteins — systemic delivery viable
- LOF inheritance — compatible for gene replacement
- Different pathway (lysosomal_storage vs coagulation)
- Disease mechanism: loss of function — Acid sphingomyelinase deficiency causes sphingomyelin accumulation in liver, spleen, lung, and CNS
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: SMPD1 is a secreted lysosomal enzyme; cross-correction may be feasible for visceral disease but CNS involvement complicates single-compartment delivery
- Mechanism source: OMIM SMPD1 607616 (https://omim.org/entry/607616)
- Approval status: approved
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — SMPD1 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (SMPD1): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Multi-system disease; define a primary therapeutic target tissue before selecting route/vector
- Vector does not naturally cover all annotated disease tissues: spleen
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: ST-920

**Precedent disease:** Fabry disease  
**Vector:** AAV2/6  
**Tissue target:** liver  
**Composite score:** 8.1 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.50 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.14** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1890bp / cargo 4700bp (40% utilized)
- Vector tropism plus precedent target match: liver
- Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated cross-correction mechanism of the matched precedent is not applicable. Direct per-cell vector delivery to every target neuron is required.
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Acid sphingomyelinase deficiency causes sphingomyelin accumulation in liver, spleen, lung, and CNS
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: SMPD1 is a secreted lysosomal enzyme; cross-correction may be feasible for visceral disease but CNS involvement complicates single-compartment delivery
- Mechanism source: OMIM SMPD1 607616 (https://omim.org/entry/607616)
- Approval status: phase1/2
- Vector immunogenicity (AAV2/6): moderate (~17%) — significant proportion may require pre-screening or exclusion
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — SMPD1 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (SMPD1): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Multi-system disease; define a primary therapeutic target tissue before selecting route/vector
- Vector does not naturally cover all annotated disease tissues: cns, lung, spleen
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #5: ABO-101

**Precedent disease:** Mucopolysaccharidosis type IIIB  
**Vector:** AAV9  
**Tissue target:** CNS  
**Composite score:** 8.1 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.05** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1890bp / cargo 4700bp (40% utilized)
- Vector tropism plus precedent target match: cns
- Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated cross-correction mechanism of the matched precedent is not applicable. Direct per-cell vector delivery to every target neuron is required.
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Acid sphingomyelinase deficiency causes sphingomyelin accumulation in liver, spleen, lung, and CNS
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: SMPD1 is a secreted lysosomal enzyme; cross-correction may be feasible for visceral disease but CNS involvement complicates single-compartment delivery
- Mechanism source: OMIM SMPD1 607616 (https://omim.org/entry/607616)
- Approval status: phase1/2
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: COMPATIBLE — SMPD1 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (SMPD1): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Multi-system disease; define a primary therapeutic target tissue before selecting route/vector
- Vector does not naturally cover all annotated disease tissues: lung, spleen
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone
