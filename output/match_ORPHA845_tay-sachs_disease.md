# NanoGT Match Report: Tay-Sachs disease

**Disease:** Tay-Sachs disease (ORPHA:845)  
**Primary gene:** HEXA  
**Gene CDS:** 1590 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** CNS  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: LYSOSOMAL MEMBRANE PROTEIN (HEXA): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.; MULTI-SUBUNIT ENZYME (HEXA): the disease gene encodes one subunit of a multi-polypeptide enzyme complex. Scoring addresses this subunit only. Confirm whether restoring this single subunit reconstitutes full enzymatic activity, or whether co-delivery of other complex subunits is required.; Vector does not naturally cover all annotated disease tissues: cns.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** Beta-hexosaminidase alpha subunit deficiency causes GM2 ganglioside accumulation in neurons  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** cns gene addition or cross correction  
**Evidence level/status:** direct / needs_user_fact_check  
**Evidence summary:** HEXA LOF supports gene addition; CNS delivery and heterodimer assembly with HEXB subunit are key considerations  
**Evidence source:** [OMIM HEXA 272800](https://omim.org/entry/272800)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and integrating ex vivo HSC vector precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint risk: CNS/neurodevelopmental outcomes may require natural-history data, age-stratified endpoints, and long follow-up because short-term clinical change can be hard to interpret.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Libmeldy | LV | 8.5/10 | 🟢 High | approved |
| 2 | ABO-101 | AAV9 | 7.8/10 | 🟢 High | phase1/2 |
| 3 | RGX-121 | AAV9 | 7.8/10 | 🟢 High | phase3 |
| 4 | Hemgenix | AAV5 | 7.7/10 | 🟢 High | approved |
| 5 | Roctavian | AAV5 | 7.7/10 | 🟢 High | approved |

---

## Match #1: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 8.5 / 10  

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
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **8.52** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1590bp / cargo 8000bp (20% utilized)
- Precedent target match: cns
- Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated cross-correction mechanism of the matched precedent is not applicable. Direct per-cell vector delivery to every target neuron is required.
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: leukodystrophy
- Disease mechanism: loss of function — Beta-hexosaminidase alpha subunit deficiency causes GM2 ganglioside accumulation in neurons
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: HEXA LOF supports gene addition; CNS delivery and heterodimer assembly with HEXB subunit are key considerations
- Mechanism source: OMIM HEXA 272800 (https://omim.org/entry/272800)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — HEXA standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (HEXA): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- MULTI-SUBUNIT ENZYME (HEXA): the disease gene encodes one subunit of a multi-polypeptide enzyme complex. Scoring addresses this subunit only. Confirm whether restoring this single subunit reconstitutes full enzymatic activity, or whether co-delivery of other complex subunits is required.
- Vector does not naturally cover all annotated disease tissues: cns
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #2: ABO-101

**Precedent disease:** Mucopolysaccharidosis type IIIB  
**Vector:** AAV9  
**Tissue target:** CNS  
**Composite score:** 7.8 / 10  

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
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.81** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1590bp / cargo 4700bp (34% utilized)
- Vector tropism plus precedent target match: cns
- Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated cross-correction mechanism of the matched precedent is not applicable. Direct per-cell vector delivery to every target neuron is required.
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Beta-hexosaminidase alpha subunit deficiency causes GM2 ganglioside accumulation in neurons
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: HEXA LOF supports gene addition; CNS delivery and heterodimer assembly with HEXB subunit are key considerations
- Mechanism source: OMIM HEXA 272800 (https://omim.org/entry/272800)
- Approval status: phase1/2
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — HEXA standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (HEXA): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- MULTI-SUBUNIT ENZYME (HEXA): the disease gene encodes one subunit of a multi-polypeptide enzyme complex. Scoring addresses this subunit only. Confirm whether restoring this single subunit reconstitutes full enzymatic activity, or whether co-delivery of other complex subunits is required.
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #3: RGX-121

**Precedent disease:** Mucopolysaccharidosis type II  
**Vector:** AAV9  
**Tissue target:** CNS/liver  
**Composite score:** 7.8 / 10  

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
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.81** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1590bp / cargo 4700bp (34% utilized)
- Vector tropism plus precedent target match: cns
- Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein (channel/transporter), NOT a soluble enzyme. The HSC-mediated cross-correction mechanism of the matched precedent is not applicable. Direct per-cell vector delivery to every target neuron is required.
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Disease mechanism: loss of function — Beta-hexosaminidase alpha subunit deficiency causes GM2 ganglioside accumulation in neurons
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: HEXA LOF supports gene addition; CNS delivery and heterodimer assembly with HEXB subunit are key considerations
- Mechanism source: OMIM HEXA 272800 (https://omim.org/entry/272800)
- Approval status: phase3
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — HEXA standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (HEXA): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- MULTI-SUBUNIT ENZYME (HEXA): the disease gene encodes one subunit of a multi-polypeptide enzyme complex. Scoring addresses this subunit only. Confirm whether restoring this single subunit reconstitutes full enzymatic activity, or whether co-delivery of other complex subunits is required.
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: Hemgenix

**Precedent disease:** Hemophilia B  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 7.7 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.67** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1590bp / cargo 4700bp (34% utilized)
- Vector tropism overlaps cns, but precedent target is liver
- Both secreted proteins — systemic delivery viable
- LOF inheritance — compatible for gene replacement
- Different pathway (lysosomal_storage vs coagulation)
- Disease mechanism: loss of function — Beta-hexosaminidase alpha subunit deficiency causes GM2 ganglioside accumulation in neurons
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: HEXA LOF supports gene addition; CNS delivery and heterodimer assembly with HEXB subunit are key considerations
- Mechanism source: OMIM HEXA 272800 (https://omim.org/entry/272800)
- Approval status: approved
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — HEXA standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (HEXA): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- MULTI-SUBUNIT ENZYME (HEXA): the disease gene encodes one subunit of a multi-polypeptide enzyme complex. Scoring addresses this subunit only. Confirm whether restoring this single subunit reconstitutes full enzymatic activity, or whether co-delivery of other complex subunits is required.
- Only partial tissue match; verify target-cell transduction and delivery route manually
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #5: Roctavian

**Precedent disease:** Hemophilia A  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 7.7 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 2.00 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 1.00 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.67** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1590bp / cargo 4700bp (34% utilized)
- Vector tropism overlaps cns, but precedent target is liver
- Both secreted proteins — systemic delivery viable
- LOF inheritance — compatible for gene replacement
- Different pathway (lysosomal_storage vs coagulation)
- Disease mechanism: loss of function — Beta-hexosaminidase alpha subunit deficiency causes GM2 ganglioside accumulation in neurons
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: HEXA LOF supports gene addition; CNS delivery and heterodimer assembly with HEXB subunit are key considerations
- Mechanism source: OMIM HEXA 272800 (https://omim.org/entry/272800)
- Approval status: approved
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Secreted protein — systemic cross-correction via bloodstream; all cells can benefit from a minority of transduced cells
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — HEXA standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- LYSOSOMAL MEMBRANE PROTEIN (HEXA): the disease gene encodes a lysosomal membrane channel or transporter, NOT a soluble secretable enzyme. The HSC-lentiviral cross-correction strategy of precedent programs such as Libmeldy (ARSA) and Skysona (ABCD1) relies on enzyme secretion from microglia and M6P receptor-mediated uptake by neurons — a mechanism that is physically impossible for a membrane-anchored protein. Direct in vivo AAV delivery to individual target neurons is required. Precedent scores from HSC/LV programs compare delivery platform only, not therapeutic mechanism.
- MULTI-SUBUNIT ENZYME (HEXA): the disease gene encodes one subunit of a multi-polypeptide enzyme complex. Scoring addresses this subunit only. Confirm whether restoring this single subunit reconstitutes full enzymatic activity, or whether co-delivery of other complex subunits is required.
- Only partial tissue match; verify target-cell transduction and delivery route manually
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone
