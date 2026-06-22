# NanoGT Match Report: Nephropathic cystinosis

**Disease:** Nephropathic cystinosis (ORPHA:213)  
**Primary gene:** CTNS  
**Gene CDS:** 1104 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** kidney, multisystem  

---

## Interpretation

- No high-confidence vector precedent was found; the best result is medium-confidence and should be treated as manual-review territory.
- Main review flags: Vector does not naturally cover all annotated disease tissues: kidney, multisystem; No direct tissue overlap; treat this as weak precedent unless route or modality is changed; Cell-autonomous protein across multiple tissues; high transduction coverage may be required.

> **⚠️ LYSOSOMAL MEMBRANE TRANSPORTER — TOP PRECEDENT CAVEAT:** The top-ranked precedent (Strimvelis, LV, ex vivo HSC) reflects lentiviral/HSC delivery class similarity, not mechanistic transferability. CTNS encodes cystinosin, a lysosomal **membrane transporter** — the same protein class as MCOLN1 (mucolipidosis type IV) and SLC17A5 (Salla disease). It cannot be secreted or taken up by neighbouring cells via the mannose-6-phosphate receptor. The Strimvelis match does not imply that ex vivo HSC gene addition is the appropriate strategy for cystinosis; the actual therapeutic requirement is per-cell delivery to renal tubular epithelium and other affected tissues. This score (6.4/10) should be read as "closest lentiviral/HSC precedent class" rather than "validated renal delivery precedent." Same limitation as ML-IV — see LIMITATIONS_AND_FIXES.md Bug 1.

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
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- No catalog program directly targets the annotated disease tissue(s); ranking is extrapolating from indirect precedents.
- No catalog vector naturally covers the annotated disease tissue(s); consider non-catalog vectors or alternative modalities.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | Strimvelis | LV | 6.4/10 | 🟡 Medium | approved |
| 2 | BMN 307 | AAV5 | 6.2/10 | 🟡 Medium | phase2 |
| 3 | Libmeldy | LV | 6.0/10 | 🟡 Medium | approved |
| 4 | OAV101-IT | AAV9 | 6.0/10 | 🟡 Medium | approved |
| 5 | Zolgensma | AAV9 | 6.0/10 | 🟡 Medium | approved |

---

## Match #1: Strimvelis

**Precedent disease:** ADA-SCID  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 6.4 / 10  

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
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.50 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.50 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.50 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.43** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1092bp / cargo 8000bp (14% utilized)
- No tissue overlap (disease: ['kidney', 'multisystem'], vector: ['hematopoietic'])
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Unknown pathway — neutral score
- Disease mechanism: loss of function — Cystinosin lysosomal cystine transporter deficiency — membrane protein; per-cell delivery required across kidney and multiple organs
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CTNS encodes a lysosomal membrane transporter; cross-correction via M6P uptake is not applicable — per-cell delivery needed in target tissues
- Mechanism source: OMIM CTNS 219800 (https://omim.org/entry/219800)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-low privilege; renal immune surveillance is significant
- Promoter availability: Limited clinical-grade promoters validated for multisystem
- Route of administration: Delivery route to multisystem not well established in clinical programs
- ORGANELLE TARGETING: COMPATIBLE — CTNS standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: kidney, multisystem
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Gene annotation incomplete; packaging, protein class, and localization scores need manual confirmation

## Match #2: BMN 307

**Precedent disease:** Phenylketonuria  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 6.2 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.60 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.50 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.50 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.50 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.24** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1353bp / cargo 4700bp (29% utilized)
- No tissue overlap (disease: ['kidney', 'multisystem'], vector: ['liver', 'lung', 'CNS'])
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Unknown pathway — neutral score
- Disease mechanism: loss of function — Cystinosin lysosomal cystine transporter deficiency — membrane protein; per-cell delivery required across kidney and multiple organs
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CTNS encodes a lysosomal membrane transporter; cross-correction via M6P uptake is not applicable — per-cell delivery needed in target tissues
- Mechanism source: OMIM CTNS 219800 (https://omim.org/entry/219800)
- Approval status: phase2
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-low privilege; renal immune surveillance is significant
- Promoter availability: Limited clinical-grade promoters validated for multisystem
- Route of administration: Delivery route to multisystem not well established in clinical programs
- ORGANELLE TARGETING: COMPATIBLE — CTNS standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: kidney, multisystem
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Gene annotation incomplete; packaging, protein class, and localization scores need manual confirmation
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #3: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 0.30 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 1.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.50 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.50 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.50 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **5.95** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1521bp / cargo 8000bp (19% utilized)
- No tissue overlap (disease: ['kidney', 'multisystem'], vector: ['hematopoietic'])
- Protein class mismatch
- Inheritance match (Autosomal recessive <-> AR)
- Unknown pathway — neutral score
- Disease mechanism: loss of function — Cystinosin lysosomal cystine transporter deficiency — membrane protein; per-cell delivery required across kidney and multiple organs
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CTNS encodes a lysosomal membrane transporter; cross-correction via M6P uptake is not applicable — per-cell delivery needed in target tissues
- Mechanism source: OMIM CTNS 219800 (https://omim.org/entry/219800)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-low privilege; renal immune surveillance is significant
- Promoter availability: Limited clinical-grade promoters validated for multisystem
- Route of administration: Delivery route to multisystem not well established in clinical programs
- ORGANELLE TARGETING: COMPATIBLE — CTNS standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: kidney, multisystem
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Gene annotation incomplete; packaging, protein class, and localization scores need manual confirmation

## Match #4: OAV101-IT

**Precedent disease:** Spinal Muscular Atrophy  
**Vector:** AAV9  
**Tissue target:** CNS/spinal cord  
**Composite score:** 6.0 / 10  

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
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.50 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.50 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.50 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **5.95** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 891bp / cargo 4700bp (19% utilized)
- No tissue overlap (disease: ['kidney', 'multisystem'], vector: ['CNS', 'muscle', 'liver', 'heart'])
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Unknown pathway — neutral score
- Disease mechanism: loss of function — Cystinosin lysosomal cystine transporter deficiency — membrane protein; per-cell delivery required across kidney and multiple organs
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CTNS encodes a lysosomal membrane transporter; cross-correction via M6P uptake is not applicable — per-cell delivery needed in target tissues
- Mechanism source: OMIM CTNS 219800 (https://omim.org/entry/219800)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-low privilege; renal immune surveillance is significant
- Promoter availability: Limited clinical-grade promoters validated for multisystem
- Route of administration: Delivery route to multisystem not well established in clinical programs
- ORGANELLE TARGETING: COMPATIBLE — CTNS standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: kidney, multisystem
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Gene annotation incomplete; packaging, protein class, and localization scores need manual confirmation
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #5: Zolgensma

**Precedent disease:** Spinal Muscular Atrophy  
**Vector:** AAV9  
**Tissue target:** CNS/motor neuron  
**Composite score:** 6.0 / 10  

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
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.50 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.50 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.50 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **5.95** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 891bp / cargo 4700bp (19% utilized)
- No tissue overlap (disease: ['kidney', 'multisystem'], vector: ['CNS', 'muscle', 'liver', 'heart'])
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Unknown pathway — neutral score
- Disease mechanism: loss of function — Cystinosin lysosomal cystine transporter deficiency — membrane protein; per-cell delivery required across kidney and multiple organs
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: CTNS encodes a lysosomal membrane transporter; cross-correction via M6P uptake is not applicable — per-cell delivery needed in target tissues
- Mechanism source: OMIM CTNS 219800 (https://omim.org/entry/219800)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate-low privilege; renal immune surveillance is significant
- Promoter availability: Limited clinical-grade promoters validated for multisystem
- Route of administration: Delivery route to multisystem not well established in clinical programs
- ORGANELLE TARGETING: COMPATIBLE — CTNS standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Vector does not naturally cover all annotated disease tissues: kidney, multisystem
- No direct tissue overlap; treat this as weak precedent unless route or modality is changed
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- Gene annotation incomplete; packaging, protein class, and localization scores need manual confirmation
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone
