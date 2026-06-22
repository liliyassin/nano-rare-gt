# NanoGT Match Report: Kohlschutter-Tonz syndrome

**Disease:** Kohlschutter-Tonz syndrome (ORPHA:1946)  
**Primary gene:** ROGDI  
**Gene CDS:** 861 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** CNS  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: UNRESOLVED DISEASE BIOLOGY (ROGDI): the molecular function of the gene product is not fully characterised in the literature. Scoring assumes a standard LOF mechanism compatible with gene addition, but this assumption has not been experimentally validated. Do not use this score as evidence of gene therapy tractability without independent confirmation of gene function, target cell type, and expected therapeutic benefit.; Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable; AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** ROGDI loss of function — gene addition is plausible by genetics but molecular function is not fully resolved and disease biology has not been established  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** cns gene addition pending mechanism validation  
**Evidence level/status:** direct / source_checked  
**Evidence summary:** Published KTS variants in ROGDI are consistent with loss of function (Schossig 2012) and gene addition is mechanistically plausible. However the molecular function of ROGDI protein is not fully resolved: proposed roles include V-ATPase regulation via the RAVE/Rabconnectin-3 complex and synaptic vesicle biology but no disease-specific in vivo model or gene addition rescue experiment has been published as of 2025. Scoring assumptions (LOF gene addition is sufficient) are unvalidated. Do not interpret the composite score as evidence of clinical tractability without independent confirmation of gene function and therapeutic rationale.  
**Evidence source:** [Schossig et al. 2012 Mutations in ROGDI Cause Kohlschutter-Tonz Syndrome](https://pubmed.ncbi.nlm.nih.gov/22482807/)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and integrating ex vivo HSC vector precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint risk: CNS/neurodevelopmental outcomes may require natural-history data, age-stratified endpoints, and long follow-up because short-term clinical change can be hard to interpret.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | OAV101-IT | AAV9 | 7.7/10 | 🟢 High | approved |
| 2 | Zolgensma | AAV9 | 7.7/10 | 🟢 High | approved |
| 3 | BMN 307 | AAV5 | 7.5/10 | 🟡 Medium | phase2 |
| 4 | Libmeldy | LV | 7.4/10 | 🟡 Medium | approved |
| 5 | Strimvelis | LV | 7.3/10 | 🟡 Medium | approved |

---

## Match #1: OAV101-IT

**Precedent disease:** Spinal Muscular Atrophy  
**Vector:** AAV9  
**Tissue target:** CNS/spinal cord  
**Composite score:** 7.7 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.67** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 861bp / cargo 4700bp (18% utilized)
- Vector tropism plus precedent target match: cns
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Unknown pathway — neutral score
- Disease mechanism: loss of function — ROGDI loss of function — gene addition is plausible by genetics but molecular function is not fully resolved and disease biology has not been established
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Published KTS variants in ROGDI are consistent with loss of function (Schossig 2012) and gene addition is mechanistically plausible. However the molecular function of ROGDI protein is not fully resolved: proposed roles include V-ATPase regulation via the RAVE/Rabconnectin-3 complex and synaptic vesicle biology but no disease-specific in vivo model or gene addition rescue experiment has been published as of 2025. Scoring assumptions (LOF gene addition is sufficient) are unvalidated. Do not interpret the composite score as evidence of clinical tractability without independent confirmation of gene function and therapeutic rationale.
- Mechanism source: Schossig et al. 2012 Mutations in ROGDI Cause Kohlschutter-Tonz Syndrome (https://pubmed.ncbi.nlm.nih.gov/22482807/)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — ROGDI standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- UNRESOLVED DISEASE BIOLOGY (ROGDI): the molecular function of the gene product is not fully characterised in the literature. Scoring assumes a standard LOF mechanism compatible with gene addition, but this assumption has not been experimentally validated. Do not use this score as evidence of gene therapy tractability without independent confirmation of gene function, target cell type, and expected therapeutic benefit.
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #2: Zolgensma

**Precedent disease:** Spinal Muscular Atrophy  
**Vector:** AAV9  
**Tissue target:** CNS/motor neuron  
**Composite score:** 7.7 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.67** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 861bp / cargo 4700bp (18% utilized)
- Vector tropism plus precedent target match: cns
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Unknown pathway — neutral score
- Disease mechanism: loss of function — ROGDI loss of function — gene addition is plausible by genetics but molecular function is not fully resolved and disease biology has not been established
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Published KTS variants in ROGDI are consistent with loss of function (Schossig 2012) and gene addition is mechanistically plausible. However the molecular function of ROGDI protein is not fully resolved: proposed roles include V-ATPase regulation via the RAVE/Rabconnectin-3 complex and synaptic vesicle biology but no disease-specific in vivo model or gene addition rescue experiment has been published as of 2025. Scoring assumptions (LOF gene addition is sufficient) are unvalidated. Do not interpret the composite score as evidence of clinical tractability without independent confirmation of gene function and therapeutic rationale.
- Mechanism source: Schossig et al. 2012 Mutations in ROGDI Cause Kohlschutter-Tonz Syndrome (https://pubmed.ncbi.nlm.nih.gov/22482807/)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — ROGDI standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- UNRESOLVED DISEASE BIOLOGY (ROGDI): the molecular function of the gene product is not fully characterised in the literature. Scoring assumes a standard LOF mechanism compatible with gene addition, but this assumption has not been experimentally validated. Do not use this score as evidence of gene therapy tractability without independent confirmation of gene function, target cell type, and expected therapeutic benefit.
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #3: BMN 307

**Precedent disease:** Phenylketonuria  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 7.5 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.60 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.48** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 861bp / cargo 4700bp (18% utilized)
- Vector tropism overlaps cns, but precedent target is liver
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Unknown pathway — neutral score
- Disease mechanism: loss of function — ROGDI loss of function — gene addition is plausible by genetics but molecular function is not fully resolved and disease biology has not been established
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Published KTS variants in ROGDI are consistent with loss of function (Schossig 2012) and gene addition is mechanistically plausible. However the molecular function of ROGDI protein is not fully resolved: proposed roles include V-ATPase regulation via the RAVE/Rabconnectin-3 complex and synaptic vesicle biology but no disease-specific in vivo model or gene addition rescue experiment has been published as of 2025. Scoring assumptions (LOF gene addition is sufficient) are unvalidated. Do not interpret the composite score as evidence of clinical tractability without independent confirmation of gene function and therapeutic rationale.
- Mechanism source: Schossig et al. 2012 Mutations in ROGDI Cause Kohlschutter-Tonz Syndrome (https://pubmed.ncbi.nlm.nih.gov/22482807/)
- Approval status: phase2
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — ROGDI standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- UNRESOLVED DISEASE BIOLOGY (ROGDI): the molecular function of the gene product is not fully characterised in the literature. Scoring assumes a standard LOF mechanism compatible with gene addition, but this assumption has not been experimentally validated. Do not use this score as evidence of gene therapy tractability without independent confirmation of gene function, target cell type, and expected therapeutic benefit.
- Only partial tissue match; verify target-cell transduction and delivery route manually
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
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

- Gene CDS 861bp / cargo 8000bp (11% utilized)
- Precedent target match: cns
- Protein class mismatch
- Inheritance match (Autosomal recessive <-> AR)
- Unknown pathway — neutral score
- Disease mechanism: loss of function — ROGDI loss of function — gene addition is plausible by genetics but molecular function is not fully resolved and disease biology has not been established
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Published KTS variants in ROGDI are consistent with loss of function (Schossig 2012) and gene addition is mechanistically plausible. However the molecular function of ROGDI protein is not fully resolved: proposed roles include V-ATPase regulation via the RAVE/Rabconnectin-3 complex and synaptic vesicle biology but no disease-specific in vivo model or gene addition rescue experiment has been published as of 2025. Scoring assumptions (LOF gene addition is sufficient) are unvalidated. Do not interpret the composite score as evidence of clinical tractability without independent confirmation of gene function and therapeutic rationale.
- Mechanism source: Schossig et al. 2012 Mutations in ROGDI Cause Kohlschutter-Tonz Syndrome (https://pubmed.ncbi.nlm.nih.gov/22482807/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — ROGDI standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- UNRESOLVED DISEASE BIOLOGY (ROGDI): the molecular function of the gene product is not fully characterised in the literature. Scoring assumes a standard LOF mechanism compatible with gene addition, but this assumption has not been experimentally validated. Do not use this score as evidence of gene therapy tractability without independent confirmation of gene function, target cell type, and expected therapeutic benefit.
- Vector does not naturally cover all annotated disease tissues: cns
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #5: Strimvelis

**Precedent disease:** ADA-SCID  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 7.3 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
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
| **TOTAL (normalised)** | **7.33** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 861bp / cargo 8000bp (11% utilized)
- No tissue overlap (disease: ['CNS'], vector: ['hematopoietic'])
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Unknown pathway — neutral score
- Disease mechanism: loss of function — ROGDI loss of function — gene addition is plausible by genetics but molecular function is not fully resolved and disease biology has not been established
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Published KTS variants in ROGDI are consistent with loss of function (Schossig 2012) and gene addition is mechanistically plausible. However the molecular function of ROGDI protein is not fully resolved: proposed roles include V-ATPase regulation via the RAVE/Rabconnectin-3 complex and synaptic vesicle biology but no disease-specific in vivo model or gene addition rescue experiment has been published as of 2025. Scoring assumptions (LOF gene addition is sufficient) are unvalidated. Do not interpret the composite score as evidence of clinical tractability without independent confirmation of gene function and therapeutic rationale.
- Mechanism source: Schossig et al. 2012 Mutations in ROGDI Cause Kohlschutter-Tonz Syndrome (https://pubmed.ncbi.nlm.nih.gov/22482807/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — ROGDI standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- UNRESOLVED DISEASE BIOLOGY (ROGDI): the molecular function of the gene product is not fully characterised in the literature. Scoring assumes a standard LOF mechanism compatible with gene addition, but this assumption has not been experimentally validated. Do not use this score as evidence of gene therapy tractability without independent confirmation of gene function, target cell type, and expected therapeutic benefit.
- Vector does not naturally cover all annotated disease tissues: cns
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
