# NanoGT Match Report: Salla disease

**Disease:** Salla disease (ORPHA:309)  
**Primary gene:** SLC17A5  
**Gene CDS:** 1485 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** CNS  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: LYSOSOMAL MEMBRANE PROTEIN (SLC17A5): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.; Vector does not naturally cover all annotated disease tissues: cns; Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** Sialin lysosomal membrane transporter deficiency — cell-autonomous membrane protein NOT a secretable enzyme  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** direct cns aav per cell delivery  
**Evidence level/status:** direct / source_linked_needs_review  
**Evidence summary:** SLC17A5 encodes sialin a lysosomal MEMBRANE TRANSPORTER for sialic acid efflux. Like MCOLN1 in ML-IV it is anchored in the lysosomal membrane and cannot be secreted or taken up via M6P receptor by neighbouring cells. HSC/LV cross-correction programs (Libmeldy) are not applicable as direct therapeutic precedents. Per-cell CNS delivery is required.  
**Evidence source:** [OMIM SLC17A5 gene entry](https://omim.org/entry/604322)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint risk: CNS/neurodevelopmental outcomes may require natural-history data, age-stratified endpoints, and long follow-up because short-term clinical change can be hard to interpret.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Skysona | LV | 8.1/10 | 🟢 High | approved |
| 2 | Libmeldy | LV | 8.1/10 | 🟢 High | approved |
| 3 | ABO-101 | AAV9 | 7.3/10 | 🟡 Medium | phase1/2 |
| 4 | RGX-121 | AAV9 | 7.3/10 | 🟡 Medium | phase3 |
| 5 | AVR-RD-01 | LV | 7.1/10 | 🟡 Medium | phase1/2 |

---

## Match #1: Skysona

**Precedent disease:** Cerebral adrenoleukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 8.1 / 10  

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
| Cross-correction | 0.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.14** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1485bp / cargo 8000bp (19% utilized)
- Precedent target match: cns
- Both membrane proteins
- LOF inheritance — compatible for gene replacement
- Pathway match: peroxisomal
- Disease mechanism: loss of function — Sialin lysosomal membrane transporter deficiency — cell-autonomous membrane protein NOT a secretable enzyme
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: SLC17A5 encodes sialin a lysosomal MEMBRANE TRANSPORTER for sialic acid efflux. Like MCOLN1 in ML-IV it is anchored in the lysosomal membrane and cannot be secreted or taken up via M6P receptor by neighbouring cells. HSC/LV cross-correction programs (Libmeldy) are not applicable as direct therapeutic precedents. Per-cell CNS delivery is required.
- Mechanism source: OMIM SLC17A5 gene entry (https://omim.org/entry/604322)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Lysosomal MEMBRANE protein (channel/transporter) — no cross-correction possible. The protein is anchored in the lysosomal membrane and cannot be released as soluble cargo. Every target cell must individually receive the vector. HSC-based lentiviral programs (Libmeldy) depend on secreted enzyme cross-correction and are not applicable as direct strategies for this protein class.
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — SLC17A5 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (SLC17A5): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Vector does not naturally cover all annotated disease tissues: cns
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #2: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 8.1 / 10  

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
| Cross-correction | 0.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.05** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1485bp / cargo 8000bp (19% utilized)
- Precedent target match: cns
- Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated cross-correction mechanism of the matched precedent is not applicable. Direct per-cell vector delivery to every target neuron is required.
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: leukodystrophy
- Disease mechanism: loss of function — Sialin lysosomal membrane transporter deficiency — cell-autonomous membrane protein NOT a secretable enzyme
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: SLC17A5 encodes sialin a lysosomal MEMBRANE TRANSPORTER for sialic acid efflux. Like MCOLN1 in ML-IV it is anchored in the lysosomal membrane and cannot be secreted or taken up via M6P receptor by neighbouring cells. HSC/LV cross-correction programs (Libmeldy) are not applicable as direct therapeutic precedents. Per-cell CNS delivery is required.
- Mechanism source: OMIM SLC17A5 gene entry (https://omim.org/entry/604322)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Lysosomal MEMBRANE protein (channel/transporter) — no cross-correction possible. The protein is anchored in the lysosomal membrane and cannot be released as soluble cargo. Every target cell must individually receive the vector. HSC-based lentiviral programs (Libmeldy) depend on secreted enzyme cross-correction and are not applicable as direct strategies for this protein class.
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — SLC17A5 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (SLC17A5): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Vector does not naturally cover all annotated disease tissues: cns
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #3: ABO-101

**Precedent disease:** Mucopolysaccharidosis type IIIB  
**Vector:** AAV9  
**Tissue target:** CNS  
**Composite score:** 7.3 / 10  

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
| Cross-correction | 0.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.33** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1485bp / cargo 4700bp (32% utilized)
- Vector tropism plus precedent target match: cns
- Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated cross-correction mechanism of the matched precedent is not applicable. Direct per-cell vector delivery to every target neuron is required.
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Sialin lysosomal membrane transporter deficiency — cell-autonomous membrane protein NOT a secretable enzyme
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: SLC17A5 encodes sialin a lysosomal MEMBRANE TRANSPORTER for sialic acid efflux. Like MCOLN1 in ML-IV it is anchored in the lysosomal membrane and cannot be secreted or taken up via M6P receptor by neighbouring cells. HSC/LV cross-correction programs (Libmeldy) are not applicable as direct therapeutic precedents. Per-cell CNS delivery is required.
- Mechanism source: OMIM SLC17A5 gene entry (https://omim.org/entry/604322)
- Approval status: phase1/2
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Lysosomal MEMBRANE protein (channel/transporter) — no cross-correction possible. The protein is anchored in the lysosomal membrane and cannot be released as soluble cargo. Every target cell must individually receive the vector. HSC-based lentiviral programs (Libmeldy) depend on secreted enzyme cross-correction and are not applicable as direct strategies for this protein class.
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — SLC17A5 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (SLC17A5): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: RGX-121

**Precedent disease:** Mucopolysaccharidosis type II  
**Vector:** AAV9  
**Tissue target:** CNS/liver  
**Composite score:** 7.3 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.80 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.33** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1485bp / cargo 4700bp (32% utilized)
- Vector tropism plus precedent target match: cns
- Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated cross-correction mechanism of the matched precedent is not applicable. Direct per-cell vector delivery to every target neuron is required.
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Sialin lysosomal membrane transporter deficiency — cell-autonomous membrane protein NOT a secretable enzyme
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: SLC17A5 encodes sialin a lysosomal MEMBRANE TRANSPORTER for sialic acid efflux. Like MCOLN1 in ML-IV it is anchored in the lysosomal membrane and cannot be secreted or taken up via M6P receptor by neighbouring cells. HSC/LV cross-correction programs (Libmeldy) are not applicable as direct therapeutic precedents. Per-cell CNS delivery is required.
- Mechanism source: OMIM SLC17A5 gene entry (https://omim.org/entry/604322)
- Approval status: phase3
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Lysosomal MEMBRANE protein (channel/transporter) — no cross-correction possible. The protein is anchored in the lysosomal membrane and cannot be released as soluble cargo. Every target cell must individually receive the vector. HSC-based lentiviral programs (Libmeldy) depend on secreted enzyme cross-correction and are not applicable as direct strategies for this protein class.
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — SLC17A5 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (SLC17A5): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #5: AVR-RD-01

**Precedent disease:** Fabry disease  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 7.1 / 10  

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
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.10** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1485bp / cargo 8000bp (19% utilized)
- No tissue overlap (disease: ['CNS'], vector: ['hematopoietic'])
- Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated cross-correction mechanism of the matched precedent is not applicable. Direct per-cell vector delivery to every target neuron is required.
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Sialin lysosomal membrane transporter deficiency — cell-autonomous membrane protein NOT a secretable enzyme
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: SLC17A5 encodes sialin a lysosomal MEMBRANE TRANSPORTER for sialic acid efflux. Like MCOLN1 in ML-IV it is anchored in the lysosomal membrane and cannot be secreted or taken up via M6P receptor by neighbouring cells. HSC/LV cross-correction programs (Libmeldy) are not applicable as direct therapeutic precedents. Per-cell CNS delivery is required.
- Mechanism source: OMIM SLC17A5 gene entry (https://omim.org/entry/604322)
- Approval status: phase1/2
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Lysosomal MEMBRANE protein (channel/transporter) — no cross-correction possible. The protein is anchored in the lysosomal membrane and cannot be released as soluble cargo. Every target cell must individually receive the vector. HSC-based lentiviral programs (Libmeldy) depend on secreted enzyme cross-correction and are not applicable as direct strategies for this protein class.
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — SLC17A5 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (SLC17A5): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- Vector does not naturally cover all annotated disease tissues: cns
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
