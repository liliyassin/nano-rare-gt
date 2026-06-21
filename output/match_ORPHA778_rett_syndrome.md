# NanoGT Match Report: Rett syndrome

**Disease:** Rett syndrome (ORPHA:778)  
**Primary gene:** MECP2  
**Gene CDS:** 1461 bp  
**Inheritance:** X-linked dominant  
**Target tissues scored:** CNS  

---

## Interpretation

- No high-confidence vector precedent was found; the best result is medium-confidence and should be treated as manual-review territory.
- Main review flags: Vector does not naturally cover all annotated disease tissues: cns; Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable; Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition.

### Disease Mechanism Evidence

**Molecular mechanism:** haploinsufficiency  
**Mechanistic detail:** X-linked haploinsufficiency of MECP2 methyl-CpG binding protein 2; gene addition is dosage-sensitive because MECP2 duplication (three copies) causes a distinct severe neurological disease in males — therapeutic window for expression is narrow  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** aav9 cns gene addition with dosage control  
**Evidence level/status:** direct / source_checked  
**Evidence summary:** Amir RE et al. (1999 Nat Genet PMID 10508514) identified MECP2 as the causal gene; Van Esch H et al. (2005 Am J Hum Genet PMID 16080119) showed MECP2 duplication causes a separate severe disease — any AAV-MECP2 construct must use a regulated or low-expression promoter to stay within the narrow therapeutic dose window  
**Evidence source:** [Amir RE et al. 1999 Nat Genet PMID 10508514; Van Esch H et al. 2005 Am J Hum Genet PMID 16080119](https://pubmed.ncbi.nlm.nih.gov/10508514/)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint risk: CNS/neurodevelopmental outcomes may require natural-history data, age-stratified endpoints, and long follow-up because short-term clinical change can be hard to interpret.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Skysona | LV | 7.4/10 | 🟡 Medium | approved |
| 2 | Libmeldy | LV | 7.3/10 | 🟡 Medium | approved |
| 3 | OAV101-IT | AAV9 | 7.3/10 | 🟡 Medium | approved |
| 4 | Zolgensma | AAV9 | 7.3/10 | 🟡 Medium | approved |
| 5 | Strimvelis | LV | 7.2/10 | 🟡 Medium | approved |

---

## Match #1: Skysona

**Precedent disease:** Cerebral adrenoleukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 7.4 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.43** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1461bp / cargo 8000bp (18% utilized)
- Precedent target match: cns
- Protein class mismatch
- Inheritance match (X-linked dominant <-> XL)
- Unknown pathway — neutral score
- Disease mechanism: haploinsufficiency — X-linked haploinsufficiency of MECP2 methyl-CpG binding protein 2; gene addition is dosage-sensitive because MECP2 duplication (three copies) causes a distinct severe neurological disease in males — therapeutic window for expression is narrow
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Amir RE et al. (1999 Nat Genet PMID 10508514) identified MECP2 as the causal gene; Van Esch H et al. (2005 Am J Hum Genet PMID 16080119) showed MECP2 duplication causes a separate severe disease — any AAV-MECP2 construct must use a regulated or low-expression promoter to stay within the narrow therapeutic dose window
- Mechanism source: Amir RE et al. 1999 Nat Genet PMID 10508514; Van Esch H et al. 2005 Am J Hum Genet PMID 16080119 (https://pubmed.ncbi.nlm.nih.gov/10508514/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — MECP2 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: cns
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition

## Match #2: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 7.3 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.29** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1461bp / cargo 8000bp (18% utilized)
- Precedent target match: cns
- Protein class mismatch
- LOF inheritance — compatible for gene replacement
- Unknown pathway — neutral score
- Disease mechanism: haploinsufficiency — X-linked haploinsufficiency of MECP2 methyl-CpG binding protein 2; gene addition is dosage-sensitive because MECP2 duplication (three copies) causes a distinct severe neurological disease in males — therapeutic window for expression is narrow
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Amir RE et al. (1999 Nat Genet PMID 10508514) identified MECP2 as the causal gene; Van Esch H et al. (2005 Am J Hum Genet PMID 16080119) showed MECP2 duplication causes a separate severe disease — any AAV-MECP2 construct must use a regulated or low-expression promoter to stay within the narrow therapeutic dose window
- Mechanism source: Amir RE et al. 1999 Nat Genet PMID 10508514; Van Esch H et al. 2005 Am J Hum Genet PMID 16080119 (https://pubmed.ncbi.nlm.nih.gov/10508514/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — MECP2 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: cns
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition

## Match #3: OAV101-IT

**Precedent disease:** Spinal Muscular Atrophy  
**Vector:** AAV9  
**Tissue target:** CNS/spinal cord  
**Composite score:** 7.3 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.29** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1461bp / cargo 4700bp (31% utilized)
- Vector tropism plus precedent target match: cns
- Both intracellular proteins
- LOF inheritance — compatible for gene replacement
- Unknown pathway — neutral score
- Disease mechanism: haploinsufficiency — X-linked haploinsufficiency of MECP2 methyl-CpG binding protein 2; gene addition is dosage-sensitive because MECP2 duplication (three copies) causes a distinct severe neurological disease in males — therapeutic window for expression is narrow
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Amir RE et al. (1999 Nat Genet PMID 10508514) identified MECP2 as the causal gene; Van Esch H et al. (2005 Am J Hum Genet PMID 16080119) showed MECP2 duplication causes a separate severe disease — any AAV-MECP2 construct must use a regulated or low-expression promoter to stay within the narrow therapeutic dose window
- Mechanism source: Amir RE et al. 1999 Nat Genet PMID 10508514; Van Esch H et al. 2005 Am J Hum Genet PMID 16080119 (https://pubmed.ncbi.nlm.nih.gov/10508514/)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — MECP2 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: Zolgensma

**Precedent disease:** Spinal Muscular Atrophy  
**Vector:** AAV9  
**Tissue target:** CNS/motor neuron  
**Composite score:** 7.3 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.29** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1461bp / cargo 4700bp (31% utilized)
- Vector tropism plus precedent target match: cns
- Both intracellular proteins
- LOF inheritance — compatible for gene replacement
- Unknown pathway — neutral score
- Disease mechanism: haploinsufficiency — X-linked haploinsufficiency of MECP2 methyl-CpG binding protein 2; gene addition is dosage-sensitive because MECP2 duplication (three copies) causes a distinct severe neurological disease in males — therapeutic window for expression is narrow
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Amir RE et al. (1999 Nat Genet PMID 10508514) identified MECP2 as the causal gene; Van Esch H et al. (2005 Am J Hum Genet PMID 16080119) showed MECP2 duplication causes a separate severe disease — any AAV-MECP2 construct must use a regulated or low-expression promoter to stay within the narrow therapeutic dose window
- Mechanism source: Amir RE et al. 1999 Nat Genet PMID 10508514; Van Esch H et al. 2005 Am J Hum Genet PMID 16080119 (https://pubmed.ncbi.nlm.nih.gov/10508514/)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — MECP2 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #5: Strimvelis

**Precedent disease:** ADA-SCID  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 7.2 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.19** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1461bp / cargo 8000bp (18% utilized)
- No tissue overlap (disease: ['CNS'], vector: ['hematopoietic'])
- Both intracellular proteins
- LOF inheritance — compatible for gene replacement
- Unknown pathway — neutral score
- Disease mechanism: haploinsufficiency — X-linked haploinsufficiency of MECP2 methyl-CpG binding protein 2; gene addition is dosage-sensitive because MECP2 duplication (three copies) causes a distinct severe neurological disease in males — therapeutic window for expression is narrow
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Amir RE et al. (1999 Nat Genet PMID 10508514) identified MECP2 as the causal gene; Van Esch H et al. (2005 Am J Hum Genet PMID 16080119) showed MECP2 duplication causes a separate severe disease — any AAV-MECP2 construct must use a regulated or low-expression promoter to stay within the narrow therapeutic dose window
- Mechanism source: Amir RE et al. 1999 Nat Genet PMID 10508514; Van Esch H et al. 2005 Am J Hum Genet PMID 16080119 (https://pubmed.ncbi.nlm.nih.gov/10508514/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — MECP2 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: cns
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition
