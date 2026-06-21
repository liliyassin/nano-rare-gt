# NanoGT Match Report: GATA2 deficiency

**Disease:** GATA2 deficiency (ORPHA:247770)  
**Primary gene:** GATA2  
**Gene CDS:** 1443 bp  
**Inheritance:** Autosomal dominant  
**Target tissues scored:** hematopoietic  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility; Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology; Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable.

### Disease Mechanism Evidence

**Molecular mechanism:** haploinsufficiency  
**Mechanistic detail:** Autosomal dominant haploinsufficiency of GATA2 transcription factor depletes haematopoietic stem cells and lymphatic endothelial progenitors causing combined immunodeficiency bone marrow failure and lymphedema  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** ex vivo hsc gata2 gene addition  
**Evidence level/status:** direct / source_checked  
**Evidence summary:** Spinner MA et al. (2014 Blood PMID 24227816) characterised the full clinical spectrum of GATA2 haploinsufficiency; gene addition is conditional via ex vivo HSC transduction because systemic in vivo delivery risks ectopic GATA2 expression in non-haematopoietic tissues where dosage must be precisely regulated  
**Evidence source:** [Spinner MA et al. 2014 Blood PMID 24227816](https://pubmed.ncbi.nlm.nih.gov/24227816/)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Few catalog vectors cover the annotated disease tissue(s): LV.
- Endpoint readiness unclear from available annotations; identify biomarkers, natural-history measures, and patient-relevant outcomes before trial prioritisation.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Strimvelis | LV | 7.6/10 | 🟢 High | approved |
| 2 | Libmeldy | LV | 6.4/10 | 🟡 Medium | approved |
| 3 | Skysona | LV | 6.4/10 | 🟡 Medium | approved |
| 4 | AVR-RD-01 | LV | 6.1/10 | 🟡 Medium | phase1/2 |
| 5 | BMN 307 | AAV5 | 5.6/10 | 🟡 Medium | phase2 |

---

## Match #1: Strimvelis

**Precedent disease:** ADA-SCID  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 7.6 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.30 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.70 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.57** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1443bp / cargo 8000bp (18% utilized)
- Vector tropism plus precedent target match: hematopoietic
- Both intracellular proteins
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Pathway match: immune_hematopoietic
- Disease mechanism: haploinsufficiency — Autosomal dominant haploinsufficiency of GATA2 transcription factor depletes haematopoietic stem cells and lymphatic endothelial progenitors causing combined immunodeficiency bone marrow failure and lymphedema
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Spinner MA et al. (2014 Blood PMID 24227816) characterised the full clinical spectrum of GATA2 haploinsufficiency; gene addition is conditional via ex vivo HSC transduction because systemic in vivo delivery risks ectopic GATA2 expression in non-haematopoietic tissues where dosage must be precisely regulated
- Mechanism source: Spinner MA et al. 2014 Blood PMID 24227816 (https://pubmed.ncbi.nlm.nih.gov/24227816/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: low privilege — immune cells reside here; robust conditioning and monitoring required
- Promoter availability: EFS, PGK, SFFV — validated in lentiviral ex vivo programs (ADA-SCID, beta-thalassaemia)
- Route of administration: Ex vivo HSC delivery — technically complex but highly precise; gold standard for blood disorders
- ORGANELLE TARGETING: COMPATIBLE — GATA2 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition

## Match #2: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.4 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.30 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.70 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.38** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1443bp / cargo 8000bp (18% utilized)
- Vector tropism plus precedent target match: hematopoietic
- Protein class mismatch
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Different pathway (immune_hematopoietic vs leukodystrophy)
- Disease mechanism: haploinsufficiency — Autosomal dominant haploinsufficiency of GATA2 transcription factor depletes haematopoietic stem cells and lymphatic endothelial progenitors causing combined immunodeficiency bone marrow failure and lymphedema
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Spinner MA et al. (2014 Blood PMID 24227816) characterised the full clinical spectrum of GATA2 haploinsufficiency; gene addition is conditional via ex vivo HSC transduction because systemic in vivo delivery risks ectopic GATA2 expression in non-haematopoietic tissues where dosage must be precisely regulated
- Mechanism source: Spinner MA et al. 2014 Blood PMID 24227816 (https://pubmed.ncbi.nlm.nih.gov/24227816/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: low privilege — immune cells reside here; robust conditioning and monitoring required
- Promoter availability: EFS, PGK, SFFV — validated in lentiviral ex vivo programs (ADA-SCID, beta-thalassaemia)
- Route of administration: Ex vivo HSC delivery — technically complex but highly precise; gold standard for blood disorders
- ORGANELLE TARGETING: COMPATIBLE — GATA2 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition

## Match #3: Skysona

**Precedent disease:** Cerebral adrenoleukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.4 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.30 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.70 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.38** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1443bp / cargo 8000bp (18% utilized)
- Vector tropism plus precedent target match: hematopoietic
- Protein class mismatch
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Different pathway (immune_hematopoietic vs peroxisomal)
- Disease mechanism: haploinsufficiency — Autosomal dominant haploinsufficiency of GATA2 transcription factor depletes haematopoietic stem cells and lymphatic endothelial progenitors causing combined immunodeficiency bone marrow failure and lymphedema
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Spinner MA et al. (2014 Blood PMID 24227816) characterised the full clinical spectrum of GATA2 haploinsufficiency; gene addition is conditional via ex vivo HSC transduction because systemic in vivo delivery risks ectopic GATA2 expression in non-haematopoietic tissues where dosage must be precisely regulated
- Mechanism source: Spinner MA et al. 2014 Blood PMID 24227816 (https://pubmed.ncbi.nlm.nih.gov/24227816/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: low privilege — immune cells reside here; robust conditioning and monitoring required
- Promoter availability: EFS, PGK, SFFV — validated in lentiviral ex vivo programs (ADA-SCID, beta-thalassaemia)
- Route of administration: Ex vivo HSC delivery — technically complex but highly precise; gold standard for blood disorders
- ORGANELLE TARGETING: COMPATIBLE — GATA2 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition

## Match #4: AVR-RD-01

**Precedent disease:** Fabry disease  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 6.1 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.50 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.30 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.70 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.14** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1443bp / cargo 8000bp (18% utilized)
- Vector tropism plus precedent target match: hematopoietic
- Protein class mismatch
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Different pathway (immune_hematopoietic vs lysosomal_storage)
- Disease mechanism: haploinsufficiency — Autosomal dominant haploinsufficiency of GATA2 transcription factor depletes haematopoietic stem cells and lymphatic endothelial progenitors causing combined immunodeficiency bone marrow failure and lymphedema
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Spinner MA et al. (2014 Blood PMID 24227816) characterised the full clinical spectrum of GATA2 haploinsufficiency; gene addition is conditional via ex vivo HSC transduction because systemic in vivo delivery risks ectopic GATA2 expression in non-haematopoietic tissues where dosage must be precisely regulated
- Mechanism source: Spinner MA et al. 2014 Blood PMID 24227816 (https://pubmed.ncbi.nlm.nih.gov/24227816/)
- Approval status: phase1/2
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: low privilege — immune cells reside here; robust conditioning and monitoring required
- Promoter availability: EFS, PGK, SFFV — validated in lentiviral ex vivo programs (ADA-SCID, beta-thalassaemia)
- Route of administration: Ex vivo HSC delivery — technically complex but highly precise; gold standard for blood disorders
- ORGANELLE TARGETING: COMPATIBLE — GATA2 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition

## Match #5: BMN 307

**Precedent disease:** Phenylketonuria  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 5.6 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.60 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.30 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.70 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **5.62** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1443bp / cargo 4700bp (31% utilized)
- No tissue overlap (disease: ['hematopoietic'], vector: ['liver', 'lung', 'CNS'])
- Both intracellular proteins
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Different pathway (immune_hematopoietic vs amino_acid_metabolism)
- Disease mechanism: haploinsufficiency — Autosomal dominant haploinsufficiency of GATA2 transcription factor depletes haematopoietic stem cells and lymphatic endothelial progenitors causing combined immunodeficiency bone marrow failure and lymphedema
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Spinner MA et al. (2014 Blood PMID 24227816) characterised the full clinical spectrum of GATA2 haploinsufficiency; gene addition is conditional via ex vivo HSC transduction because systemic in vivo delivery risks ectopic GATA2 expression in non-haematopoietic tissues where dosage must be precisely regulated
- Mechanism source: Spinner MA et al. 2014 Blood PMID 24227816 (https://pubmed.ncbi.nlm.nih.gov/24227816/)
- Approval status: phase2
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: low privilege — immune cells reside here; robust conditioning and monitoring required
- Promoter availability: EFS, PGK, SFFV — validated in lentiviral ex vivo programs (ADA-SCID, beta-thalassaemia)
- Route of administration: Ex vivo HSC delivery — technically complex but highly precise; gold standard for blood disorders
- ORGANELLE TARGETING: COMPATIBLE — GATA2 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: hematopoietic
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone
