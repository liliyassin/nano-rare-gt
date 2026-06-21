# NanoGT Match Report: Dravet syndrome

**Disease:** Dravet syndrome (ORPHA:1306)  
**Primary gene:** SCN1A  
**Gene CDS:** 6027 bp  
**Inheritance:** Autosomal dominant  
**Target tissues scored:** CNS  

---

## Interpretation

- No high-confidence vector precedent was found; the best result is medium-confidence and should be treated as manual-review territory.
- Main review flags: MULTI-SUBUNIT ENZYME (SCN1A): the disease gene encodes one subunit of a multi-polypeptide enzyme complex. Scoring addresses this subunit only. Confirm whether restoring this single subunit reconstitutes full enzymatic activity, or whether co-delivery of other complex subunits is required.; Vector does not naturally cover all annotated disease tissues: cns; Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy.

### Disease Mechanism Evidence

**Molecular mechanism:** haploinsufficiency  
**Mechanistic detail:** Haploinsufficiency of Nav1.1 sodium channel (SCN1A) preferentially reduces firing in fast-spiking GABAergic inhibitory interneurons causing disinhibition and refractory seizures  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** lv or aav inhibitory interneuron targeted scn1a  
**Evidence level/status:** direct / source_checked  
**Evidence summary:** Claes L et al. (2003 Hum Mutat PMID 12754708) established de novo SCN1A haploinsufficiency as the primary mechanism; Colasante G et al. (2020 Mol Ther PMID 31607539) demonstrated that cell-type-specific SCN1A upregulation restores interneuron excitability; gene addition is conditional because ectopic expression in excitatory neurons would worsen seizures  
**Evidence source:** [Claes L et al. 2003 Hum Mutat PMID 12754708; Colasante G et al. 2020 Mol Ther PMID 31607539](https://pubmed.ncbi.nlm.nih.gov/12754708/)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint risk: CNS/neurodevelopmental outcomes may require natural-history data, age-stratified endpoints, and long follow-up because short-term clinical change can be hard to interpret.

---

## Top 4 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Skysona | LV | 7.1/10 | 🟡 Medium | approved |
| 2 | Libmeldy | LV | 6.6/10 | 🟡 Medium | approved |
| 3 | Strimvelis | LV | 6.0/10 | 🟡 Medium | approved |
| 4 | AVR-RD-01 | LV | 5.8/10 | 🟡 Medium | phase1/2 |

---

## Match #1: Skysona

**Precedent disease:** Cerebral adrenoleukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 7.1 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.10** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 6027bp / cargo 8000bp (75% utilized)
- Precedent target match: cns
- Both membrane proteins
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Unknown pathway — neutral score
- Disease mechanism: haploinsufficiency — Haploinsufficiency of Nav1.1 sodium channel (SCN1A) preferentially reduces firing in fast-spiking GABAergic inhibitory interneurons causing disinhibition and refractory seizures
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Claes L et al. (2003 Hum Mutat PMID 12754708) established de novo SCN1A haploinsufficiency as the primary mechanism; Colasante G et al. (2020 Mol Ther PMID 31607539) demonstrated that cell-type-specific SCN1A upregulation restores interneuron excitability; gene addition is conditional because ectopic expression in excitatory neurons would worsen seizures
- Mechanism source: Claes L et al. 2003 Hum Mutat PMID 12754708; Colasante G et al. 2020 Mol Ther PMID 31607539 (https://pubmed.ncbi.nlm.nih.gov/12754708/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — SCN1A standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- MULTI-SUBUNIT ENZYME (SCN1A): the disease gene encodes one subunit of a multi-polypeptide enzyme complex. Scoring addresses this subunit only. Confirm whether restoring this single subunit reconstitutes full enzymatic activity, or whether co-delivery of other complex subunits is required.
- Vector does not naturally cover all annotated disease tissues: cns
- Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition

## Match #2: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.6 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.62** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 6027bp / cargo 8000bp (75% utilized)
- Precedent target match: cns
- Protein class mismatch
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Unknown pathway — neutral score
- Disease mechanism: haploinsufficiency — Haploinsufficiency of Nav1.1 sodium channel (SCN1A) preferentially reduces firing in fast-spiking GABAergic inhibitory interneurons causing disinhibition and refractory seizures
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Claes L et al. (2003 Hum Mutat PMID 12754708) established de novo SCN1A haploinsufficiency as the primary mechanism; Colasante G et al. (2020 Mol Ther PMID 31607539) demonstrated that cell-type-specific SCN1A upregulation restores interneuron excitability; gene addition is conditional because ectopic expression in excitatory neurons would worsen seizures
- Mechanism source: Claes L et al. 2003 Hum Mutat PMID 12754708; Colasante G et al. 2020 Mol Ther PMID 31607539 (https://pubmed.ncbi.nlm.nih.gov/12754708/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — SCN1A standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- MULTI-SUBUNIT ENZYME (SCN1A): the disease gene encodes one subunit of a multi-polypeptide enzyme complex. Scoring addresses this subunit only. Confirm whether restoring this single subunit reconstitutes full enzymatic activity, or whether co-delivery of other complex subunits is required.
- Vector does not naturally cover all annotated disease tissues: cns
- Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition

## Match #3: Strimvelis

**Precedent disease:** ADA-SCID  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 6.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.05** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 6027bp / cargo 8000bp (75% utilized)
- No tissue overlap (disease: ['CNS'], vector: ['hematopoietic'])
- Protein class mismatch
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Unknown pathway — neutral score
- Disease mechanism: haploinsufficiency — Haploinsufficiency of Nav1.1 sodium channel (SCN1A) preferentially reduces firing in fast-spiking GABAergic inhibitory interneurons causing disinhibition and refractory seizures
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Claes L et al. (2003 Hum Mutat PMID 12754708) established de novo SCN1A haploinsufficiency as the primary mechanism; Colasante G et al. (2020 Mol Ther PMID 31607539) demonstrated that cell-type-specific SCN1A upregulation restores interneuron excitability; gene addition is conditional because ectopic expression in excitatory neurons would worsen seizures
- Mechanism source: Claes L et al. 2003 Hum Mutat PMID 12754708; Colasante G et al. 2020 Mol Ther PMID 31607539 (https://pubmed.ncbi.nlm.nih.gov/12754708/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — SCN1A standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- MULTI-SUBUNIT ENZYME (SCN1A): the disease gene encodes one subunit of a multi-polypeptide enzyme complex. Scoring addresses this subunit only. Confirm whether restoring this single subunit reconstitutes full enzymatic activity, or whether co-delivery of other complex subunits is required.
- Vector does not naturally cover all annotated disease tissues: cns
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition

## Match #4: AVR-RD-01

**Precedent disease:** Fabry disease  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 5.8 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **5.81** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 6027bp / cargo 8000bp (75% utilized)
- No tissue overlap (disease: ['CNS'], vector: ['hematopoietic'])
- Protein class mismatch
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Unknown pathway — neutral score
- Disease mechanism: haploinsufficiency — Haploinsufficiency of Nav1.1 sodium channel (SCN1A) preferentially reduces firing in fast-spiking GABAergic inhibitory interneurons causing disinhibition and refractory seizures
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Claes L et al. (2003 Hum Mutat PMID 12754708) established de novo SCN1A haploinsufficiency as the primary mechanism; Colasante G et al. (2020 Mol Ther PMID 31607539) demonstrated that cell-type-specific SCN1A upregulation restores interneuron excitability; gene addition is conditional because ectopic expression in excitatory neurons would worsen seizures
- Mechanism source: Claes L et al. 2003 Hum Mutat PMID 12754708; Colasante G et al. 2020 Mol Ther PMID 31607539 (https://pubmed.ncbi.nlm.nih.gov/12754708/)
- Approval status: phase1/2
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — SCN1A standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- MULTI-SUBUNIT ENZYME (SCN1A): the disease gene encodes one subunit of a multi-polypeptide enzyme complex. Scoring addresses this subunit only. Confirm whether restoring this single subunit reconstitutes full enzymatic activity, or whether co-delivery of other complex subunits is required.
- Vector does not naturally cover all annotated disease tissues: cns
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition

---

## Excluded Programs (Packaging Failure)

| Program | Vector | Gene CDS Issue |
|---------|--------|----------------|
| ABO-101 | AAV9 | Gene CDS (6027bp) exceeds vector cargo (4700bp) — hard fail |
| AT132 | AAV8 | Gene CDS (6027bp) exceeds vector cargo (4700bp) — hard fail |
| BMN 307 | AAV5 | Gene CDS (6027bp) exceeds vector cargo (4700bp) — hard fail |
| CPCB-RPE1 | AAV8 | Gene CDS (6027bp) exceeds vector cargo (4700bp) — hard fail |
| DTX201 | AAV8 | Gene CDS (6027bp) exceeds vector cargo (4700bp) — hard fail |
