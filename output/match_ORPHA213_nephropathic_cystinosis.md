# NanoGT Match Report: Nephropathic cystinosis

**Disease:** Nephropathic cystinosis (ORPHA:213)  
**Primary gene:** CTNS  
**Gene CDS:** 1104 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** kidney, multisystem  

---

## Interpretation

- No high-confidence vector precedent was found; the best result is medium-confidence and should be treated as manual-review territory.
- Main review flags: LYSOSOMAL MEMBRANE PROTEIN (CTNS): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.; Vector does not naturally cover all annotated disease tissues: kidney, multisystem; No direct tissue overlap; treat this as weak precedent unless route or modality is changed.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** Cystinosin lysosomal cystine transporter deficiency — membrane protein; per-cell delivery required across kidney and multiple organs  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** kidney or systemic gene addition  
**Evidence level/status:** direct / needs_user_fact_check  
**Evidence summary:** CTNS encodes a lysosomal membrane transporter; cross-correction via M6P uptake is not applicable — per-cell delivery needed in target tissues  
**Evidence source:** [OMIM CTNS 219800](https://omim.org/entry/219800)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and integrating ex vivo HSC vector precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- No catalog program directly targets the annotated disease tissue(s); ranking is extrapolating from indirect precedents.
- No catalog vector naturally covers the annotated disease tissue(s); consider non-catalog vectors or alternative modalities.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Libmeldy | LV | 6.6/10 | 🟡 Medium | approved |
| 2 | AVR-RD-01 | LV | 6.2/10 | 🟡 Medium | phase1/2 |
| 3 | ST-920 | AAV2/6 | 6.0/10 | 🟡 Medium | phase1/2 |
| 4 | Skysona | LV | 6.0/10 | 🟡 Medium | approved |
| 5 | ABO-101 | AAV9 | 5.9/10 | 🟡 Medium | phase1/2 |

---

## Match #1: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.6 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.50 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.50 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.50 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.57** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1104bp / cargo 8000bp (14% utilized)
- No tissue overlap (disease: ['kidney', 'multisystem'], vector: ['hematopoietic'])
- Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated cross-correction mechanism of the matched precedent is not applicable. Direct per-cell vector delivery to every target neuron is required.
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: leukodystrophy
- Disease mechanism: loss of function — Cystinosin lysosomal cystine transporter deficiency — membrane protein; per-cell delivery required across kidney and multiple organs
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CTNS encodes a lysosomal membrane transporter; cross-correction via M6P uptake is not applicable — per-cell delivery needed in target tissues
- Mechanism source: OMIM CTNS 219800 (https://omim.org/entry/219800)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Lysosomal MEMBRANE protein (channel/transporter) — no cross-correction possible. The protein is anchored in the lysosomal membrane and cannot be released as soluble cargo. Every target cell must individually receive the vector. HSC-based lentiviral programs (Libmeldy) depend on secreted enzyme cross-correction and are not applicable as direct strategies for this protein class.
- Immune privilege: moderate-low privilege; renal immune surveillance is significant
- Promoter availability: Limited clinical-grade promoters validated for multisystem
- Route of administration: Delivery route to multisystem not well established in clinical programs
- ORGANELLE TARGETING: COMPATIBLE — CTNS standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (CTNS): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Vector does not naturally cover all annotated disease tissues: kidney, multisystem
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #2: AVR-RD-01

**Precedent disease:** Fabry disease  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 6.2 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.50 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.50 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.50 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.19** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1104bp / cargo 8000bp (14% utilized)
- No tissue overlap (disease: ['kidney', 'multisystem'], vector: ['hematopoietic'])
- Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated cross-correction mechanism of the matched precedent is not applicable. Direct per-cell vector delivery to every target neuron is required.
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Cystinosin lysosomal cystine transporter deficiency — membrane protein; per-cell delivery required across kidney and multiple organs
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CTNS encodes a lysosomal membrane transporter; cross-correction via M6P uptake is not applicable — per-cell delivery needed in target tissues
- Mechanism source: OMIM CTNS 219800 (https://omim.org/entry/219800)
- Approval status: phase1/2
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Lysosomal MEMBRANE protein (channel/transporter) — no cross-correction possible. The protein is anchored in the lysosomal membrane and cannot be released as soluble cargo. Every target cell must individually receive the vector. HSC-based lentiviral programs (Libmeldy) depend on secreted enzyme cross-correction and are not applicable as direct strategies for this protein class.
- Immune privilege: moderate-low privilege; renal immune surveillance is significant
- Promoter availability: Limited clinical-grade promoters validated for multisystem
- Route of administration: Delivery route to multisystem not well established in clinical programs
- ORGANELLE TARGETING: COMPATIBLE — CTNS standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (CTNS): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Vector does not naturally cover all annotated disease tissues: kidney, multisystem
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #3: ST-920

**Precedent disease:** Fabry disease  
**Vector:** AAV2/6  
**Tissue target:** liver  
**Composite score:** 6.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.50 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.50 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.50 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.50 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **5.95** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1104bp / cargo 4700bp (23% utilized)
- No tissue overlap (disease: ['kidney', 'multisystem'], vector: ['liver', 'muscle'])
- Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated cross-correction mechanism of the matched precedent is not applicable. Direct per-cell vector delivery to every target neuron is required.
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Cystinosin lysosomal cystine transporter deficiency — membrane protein; per-cell delivery required across kidney and multiple organs
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CTNS encodes a lysosomal membrane transporter; cross-correction via M6P uptake is not applicable — per-cell delivery needed in target tissues
- Mechanism source: OMIM CTNS 219800 (https://omim.org/entry/219800)
- Approval status: phase1/2
- Vector immunogenicity (AAV2/6): moderate (~17%) — significant proportion may require pre-screening or exclusion
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Lysosomal MEMBRANE protein (channel/transporter) — no cross-correction possible. The protein is anchored in the lysosomal membrane and cannot be released as soluble cargo. Every target cell must individually receive the vector. HSC-based lentiviral programs (Libmeldy) depend on secreted enzyme cross-correction and are not applicable as direct strategies for this protein class.
- Immune privilege: moderate-low privilege; renal immune surveillance is significant
- Promoter availability: Limited clinical-grade promoters validated for multisystem
- Route of administration: Delivery route to multisystem not well established in clinical programs
- ORGANELLE TARGETING: COMPATIBLE — CTNS standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (CTNS): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Vector does not naturally cover all annotated disease tissues: kidney, multisystem
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: Skysona

**Precedent disease:** Cerebral adrenoleukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.50 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.50 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.50 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **5.95** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1104bp / cargo 8000bp (14% utilized)
- No tissue overlap (disease: ['kidney', 'multisystem'], vector: ['hematopoietic'])
- Both membrane proteins
- LOF inheritance — compatible for gene replacement
- Different pathway (lysosomal_storage vs peroxisomal)
- Disease mechanism: loss of function — Cystinosin lysosomal cystine transporter deficiency — membrane protein; per-cell delivery required across kidney and multiple organs
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CTNS encodes a lysosomal membrane transporter; cross-correction via M6P uptake is not applicable — per-cell delivery needed in target tissues
- Mechanism source: OMIM CTNS 219800 (https://omim.org/entry/219800)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Lysosomal MEMBRANE protein (channel/transporter) — no cross-correction possible. The protein is anchored in the lysosomal membrane and cannot be released as soluble cargo. Every target cell must individually receive the vector. HSC-based lentiviral programs (Libmeldy) depend on secreted enzyme cross-correction and are not applicable as direct strategies for this protein class.
- Immune privilege: moderate-low privilege; renal immune surveillance is significant
- Promoter availability: Limited clinical-grade promoters validated for multisystem
- Route of administration: Delivery route to multisystem not well established in clinical programs
- ORGANELLE TARGETING: COMPATIBLE — CTNS standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (CTNS): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Vector does not naturally cover all annotated disease tissues: kidney, multisystem
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #5: ABO-101

**Precedent disease:** Mucopolysaccharidosis type IIIB  
**Vector:** AAV9  
**Tissue target:** CNS  
**Composite score:** 5.9 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.50 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.50 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.50 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **5.86** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1104bp / cargo 4700bp (23% utilized)
- No tissue overlap (disease: ['kidney', 'multisystem'], vector: ['CNS', 'muscle', 'liver', 'heart'])
- Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated cross-correction mechanism of the matched precedent is not applicable. Direct per-cell vector delivery to every target neuron is required.
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Cystinosin lysosomal cystine transporter deficiency — membrane protein; per-cell delivery required across kidney and multiple organs
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CTNS encodes a lysosomal membrane transporter; cross-correction via M6P uptake is not applicable — per-cell delivery needed in target tissues
- Mechanism source: OMIM CTNS 219800 (https://omim.org/entry/219800)
- Approval status: phase1/2
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Lysosomal MEMBRANE protein (channel/transporter) — no cross-correction possible. The protein is anchored in the lysosomal membrane and cannot be released as soluble cargo. Every target cell must individually receive the vector. HSC-based lentiviral programs (Libmeldy) depend on secreted enzyme cross-correction and are not applicable as direct strategies for this protein class.
- Immune privilege: moderate-low privilege; renal immune surveillance is significant
- Promoter availability: Limited clinical-grade promoters validated for multisystem
- Route of administration: Delivery route to multisystem not well established in clinical programs
- ORGANELLE TARGETING: COMPATIBLE — CTNS standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (CTNS): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Vector does not naturally cover all annotated disease tissues: kidney, multisystem
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone
