# NanoGT Match Report: Tuberous sclerosis complex

**Disease:** Tuberous sclerosis complex (ORPHA:805)  
**Primary gene:** TSC1  
**Gene CDS:** 5694 bp  
**Inheritance:** Autosomal dominant  
**Target tissues scored:** CNS, kidney, skin  

---

## Interpretation

- No high-confidence vector precedent was found; the best result is medium-confidence and should be treated as manual-review territory.
- Main review flags: Multi-system disease; define a primary therapeutic target tissue before selecting route/vector; Vector does not naturally cover all annotated disease tissues: cns, kidney, skin; Cell-autonomous protein across multiple tissues; high transduction coverage may be required.

### Disease Mechanism Evidence

**Molecular mechanism:** haploinsufficiency  
**Mechanistic detail:** Germline TSC2 mutation plus somatic second-hit loss of the wild-type allele drives mTORC1 hyperactivation and hamartoma formation in multiple tissues; gene addition addresses the haploinsufficient state but cannot prevent independent somatic second-hit events in susceptible cells throughout the body  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** gene addition tumour suppressor rescue  
**Evidence level/status:** direct / source_checked  
**Evidence summary:** Henske et al. (1995 Genes Chromosomes Cancer PMID 7547639) demonstrated LOH at the TSC2 locus in angiomyolipomas confirming two-hit tumour suppressor mechanism; gene addition is conditional because systemic delivery cannot prevent the many independent somatic second-hit events that initiate individual hamartomas  
**Evidence source:** [Henske et al. 1995 Genes Chromosomes Cancer PMID 7547639](https://pubmed.ncbi.nlm.nih.gov/7547639/)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint risk: CNS/neurodevelopmental outcomes may require natural-history data, age-stratified endpoints, and long follow-up because short-term clinical change can be hard to interpret.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 4 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Libmeldy | LV | 6.1/10 | 🟡 Medium | approved |
| 2 | Skysona | LV | 6.1/10 | 🟡 Medium | approved |
| 3 | Strimvelis | LV | 6.0/10 | 🟡 Medium | approved |
| 4 | AVR-RD-01 | LV | 5.3/10 | 🟡 Medium | phase1/2 |

---

## Match #1: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.1 / 10  

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
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.14** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 5694bp / cargo 8000bp (71% utilized)
- Precedent target match: cns
- Protein class mismatch
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Unknown pathway — neutral score
- Disease mechanism: haploinsufficiency — Germline TSC2 mutation plus somatic second-hit loss of the wild-type allele drives mTORC1 hyperactivation and hamartoma formation in multiple tissues; gene addition addresses the haploinsufficient state but cannot prevent independent somatic second-hit events in susceptible cells throughout the body
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Henske et al. (1995 Genes Chromosomes Cancer PMID 7547639) demonstrated LOH at the TSC2 locus in angiomyolipomas confirming two-hit tumour suppressor mechanism; gene addition is conditional because systemic delivery cannot prevent the many independent somatic second-hit events that initiate individual hamartomas
- Mechanism source: Henske et al. 1995 Genes Chromosomes Cancer PMID 7547639 (https://pubmed.ncbi.nlm.nih.gov/7547639/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — TSC2 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Multi-system disease; define a primary therapeutic target tissue before selecting route/vector
- Vector does not naturally cover all annotated disease tissues: cns, kidney, skin
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition

## Match #2: Skysona

**Precedent disease:** Cerebral adrenoleukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.1 / 10  

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
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.14** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 5694bp / cargo 8000bp (71% utilized)
- Precedent target match: cns
- Protein class mismatch
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Unknown pathway — neutral score
- Disease mechanism: haploinsufficiency — Germline TSC2 mutation plus somatic second-hit loss of the wild-type allele drives mTORC1 hyperactivation and hamartoma formation in multiple tissues; gene addition addresses the haploinsufficient state but cannot prevent independent somatic second-hit events in susceptible cells throughout the body
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Henske et al. (1995 Genes Chromosomes Cancer PMID 7547639) demonstrated LOH at the TSC2 locus in angiomyolipomas confirming two-hit tumour suppressor mechanism; gene addition is conditional because systemic delivery cannot prevent the many independent somatic second-hit events that initiate individual hamartomas
- Mechanism source: Henske et al. 1995 Genes Chromosomes Cancer PMID 7547639 (https://pubmed.ncbi.nlm.nih.gov/7547639/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — TSC2 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Multi-system disease; define a primary therapeutic target tissue before selecting route/vector
- Vector does not naturally cover all annotated disease tissues: cns, kidney, skin
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
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
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.05** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 5694bp / cargo 8000bp (71% utilized)
- No tissue overlap (disease: ['CNS', 'kidney', 'skin'], vector: ['hematopoietic'])
- Both intracellular proteins
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Unknown pathway — neutral score
- Disease mechanism: haploinsufficiency — Germline TSC2 mutation plus somatic second-hit loss of the wild-type allele drives mTORC1 hyperactivation and hamartoma formation in multiple tissues; gene addition addresses the haploinsufficient state but cannot prevent independent somatic second-hit events in susceptible cells throughout the body
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Henske et al. (1995 Genes Chromosomes Cancer PMID 7547639) demonstrated LOH at the TSC2 locus in angiomyolipomas confirming two-hit tumour suppressor mechanism; gene addition is conditional because systemic delivery cannot prevent the many independent somatic second-hit events that initiate individual hamartomas
- Mechanism source: Henske et al. 1995 Genes Chromosomes Cancer PMID 7547639 (https://pubmed.ncbi.nlm.nih.gov/7547639/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — TSC2 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Multi-system disease; define a primary therapeutic target tissue before selecting route/vector
- Vector does not naturally cover all annotated disease tissues: cns, kidney, skin
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition

## Match #4: AVR-RD-01

**Precedent disease:** Fabry disease  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 5.3 / 10  

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
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **5.33** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 5694bp / cargo 8000bp (71% utilized)
- No tissue overlap (disease: ['CNS', 'kidney', 'skin'], vector: ['hematopoietic'])
- Protein class mismatch
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Unknown pathway — neutral score
- Disease mechanism: haploinsufficiency — Germline TSC2 mutation plus somatic second-hit loss of the wild-type allele drives mTORC1 hyperactivation and hamartoma formation in multiple tissues; gene addition addresses the haploinsufficient state but cannot prevent independent somatic second-hit events in susceptible cells throughout the body
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Henske et al. (1995 Genes Chromosomes Cancer PMID 7547639) demonstrated LOH at the TSC2 locus in angiomyolipomas confirming two-hit tumour suppressor mechanism; gene addition is conditional because systemic delivery cannot prevent the many independent somatic second-hit events that initiate individual hamartomas
- Mechanism source: Henske et al. 1995 Genes Chromosomes Cancer PMID 7547639 (https://pubmed.ncbi.nlm.nih.gov/7547639/)
- Approval status: phase1/2
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: COMPATIBLE — TSC2 standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Multi-system disease; define a primary therapeutic target tissue before selecting route/vector
- Vector does not naturally cover all annotated disease tissues: cns, kidney, skin
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Dominant inheritance flagged; assess whether silencing, editing, or allele-specific strategy is needed instead of simple addition

---

## Excluded Programs (Packaging Failure)

| Program | Vector | Gene CDS Issue |
|---------|--------|----------------|
| ABO-101 | AAV9 | Gene CDS (5694bp) exceeds vector cargo (4700bp) — hard fail |
| AT132 | AAV8 | Gene CDS (5694bp) exceeds vector cargo (4700bp) — hard fail |
| BMN 307 | AAV5 | Gene CDS (5694bp) exceeds vector cargo (4700bp) — hard fail |
| CPCB-RPE1 | AAV8 | Gene CDS (5694bp) exceeds vector cargo (4700bp) — hard fail |
| DTX201 | AAV8 | Gene CDS (5694bp) exceeds vector cargo (4700bp) — hard fail |
