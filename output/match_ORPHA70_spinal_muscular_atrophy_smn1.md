# NanoGT Match Report: Spinal Muscular Atrophy

**Disease:** Spinal Muscular Atrophy (ORPHA:70)  
**Primary gene:** SMN1  
**Gene CDS:** 891 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** CNS, muscle  
**Gene selection note:** this disease has multiple listed genes (SMN1, SMN2); this report scores SMN1 only.  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: Multiple causal genes listed; score is gene-specific and should be repeated for each molecular subtype; Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints; Cell-autonomous protein across multiple tissues; high transduction coverage may be required.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** SMN protein deficiency from biallelic SMN1 mutation  
**Gene-addition compatibility:** compatible  
**Preferred modality class:** gene addition  
**Evidence level/status:** direct / source_linked_needs_review  
**Evidence summary:** FDA Zolgensma indication is SMA with biallelic SMN1 mutations; product supplies functional SMN transgene  
**Evidence source:** [FDA Zolgensma product page](https://www.fda.gov/vaccines-blood-biologics/zolgensma)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint risk: CNS/neurodevelopmental outcomes may require natural-history data, age-stratified endpoints, and long follow-up because short-term clinical change can be hard to interpret.
- Endpoint risk: muscle/cardiac diseases may need functional, respiratory, imaging, or cardiac endpoints that progress slowly and vary by age/stage.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | OAV101-IT | AAV9 | 8.2/10 | 🟢 High | approved |
| 2 | Zolgensma | AAV9 | 8.2/10 | 🟢 High | approved |
| 3 | AT132 | AAV8 | 8.0/10 | 🟢 High | phase3 |
| 4 | SRP-9001 | AAV9 | 7.6/10 | 🟢 High | approved |
| 5 | BMN 307 | AAV5 | 7.3/10 | 🟡 Medium | phase2 |

---

## Match #1: OAV101-IT

**Precedent disease:** Spinal Muscular Atrophy  
**Vector:** AAV9  
**Tissue target:** CNS/spinal cord  
**Composite score:** 8.2 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.20 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **8.25** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 891bp / cargo 4700bp (19% utilized)
- Vector tropism plus precedent target match: cns
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: motor_neuron
- Disease mechanism: loss of function — SMN protein deficiency from biallelic SMN1 mutation
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: FDA Zolgensma indication is SMA with biallelic SMN1 mutations; product supplies functional SMN transgene
- Mechanism source: FDA Zolgensma product page (https://www.fda.gov/vaccines-blood-biologics/zolgensma)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate-to-narrow window — early childhood onset; newborn screening integration would significantly improve outcomes
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: IV systemic or intramuscular injection — well established; used in SMA, DMD, Glybera

### Manual Review Flags

- Multiple causal genes listed; score is gene-specific and should be repeated for each molecular subtype
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Therapeutic window is not wide; natural-history timing and irreversible damage should be reviewed
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #2: Zolgensma

**Precedent disease:** Spinal Muscular Atrophy  
**Vector:** AAV9  
**Tissue target:** CNS/motor neuron  
**Composite score:** 8.2 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.20 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **8.25** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 891bp / cargo 4700bp (19% utilized)
- Vector tropism plus precedent target match: cns
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: motor_neuron
- Disease mechanism: loss of function — SMN protein deficiency from biallelic SMN1 mutation
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: FDA Zolgensma indication is SMA with biallelic SMN1 mutations; product supplies functional SMN transgene
- Mechanism source: FDA Zolgensma product page (https://www.fda.gov/vaccines-blood-biologics/zolgensma)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate-to-narrow window — early childhood onset; newborn screening integration would significantly improve outcomes
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: IV systemic or intramuscular injection — well established; used in SMA, DMD, Glybera

### Manual Review Flags

- Multiple causal genes listed; score is gene-specific and should be repeated for each molecular subtype
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Therapeutic window is not wide; natural-history timing and irreversible damage should be reviewed
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #3: AT132

**Precedent disease:** X-linked myotubular myopathy  
**Vector:** AAV8  
**Tissue target:** muscle  
**Composite score:** 8.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.80 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.20 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **8.00** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 891bp / cargo 4700bp (19% utilized)
- Vector tropism plus precedent target match: muscle
- Both intracellular proteins
- LOF inheritance — compatible for gene replacement
- Pathway match: myopathy
- Disease mechanism: loss of function — SMN protein deficiency from biallelic SMN1 mutation
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: FDA Zolgensma indication is SMA with biallelic SMN1 mutations; product supplies functional SMN transgene
- Mechanism source: FDA Zolgensma product page (https://www.fda.gov/vaccines-blood-biologics/zolgensma)
- Approval status: phase3
- Vector immunogenicity (AAV8): high (~30%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate-to-narrow window — early childhood onset; newborn screening integration would significantly improve outcomes
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: IV systemic or intramuscular injection — well established; used in SMA, DMD, Glybera

### Manual Review Flags

- Multiple causal genes listed; score is gene-specific and should be repeated for each molecular subtype
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: cns
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Therapeutic window is not wide; natural-history timing and irreversible damage should be reviewed
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: SRP-9001

**Precedent disease:** Duchenne muscular dystrophy  
**Vector:** AAV9  
**Tissue target:** muscle  
**Composite score:** 7.6 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.20 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **7.60** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 891bp / cargo 4700bp (19% utilized)
- Vector tropism plus precedent target match: muscle
- Protein class mismatch
- LOF inheritance — compatible for gene replacement
- Pathway match: myopathy
- Disease mechanism: loss of function — SMN protein deficiency from biallelic SMN1 mutation
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: FDA Zolgensma indication is SMA with biallelic SMN1 mutations; product supplies functional SMN transgene
- Mechanism source: FDA Zolgensma product page (https://www.fda.gov/vaccines-blood-biologics/zolgensma)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate-to-narrow window — early childhood onset; newborn screening integration would significantly improve outcomes
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: IV systemic or intramuscular injection — well established; used in SMA, DMD, Glybera

### Manual Review Flags

- Multiple causal genes listed; score is gene-specific and should be repeated for each molecular subtype
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Therapeutic window is not wide; natural-history timing and irreversible damage should be reviewed
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #5: BMN 307

**Precedent disease:** Phenylketonuria  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 7.3 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 2.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.60 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.20 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **7.30** | **10.0** | Raw sum / 20 × 10 |

### Rationale

- Gene CDS 891bp / cargo 4700bp (19% utilized)
- Vector tropism overlaps cns, but precedent target is liver
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Different pathway (motor_neuron vs amino_acid_metabolism)
- Disease mechanism: loss of function — SMN protein deficiency from biallelic SMN1 mutation
- Gene-addition modality compatibility: supports gene addition
- Mechanism evidence: FDA Zolgensma indication is SMA with biallelic SMN1 mutations; product supplies functional SMN transgene
- Mechanism source: FDA Zolgensma product page (https://www.fda.gov/vaccines-blood-biologics/zolgensma)
- Approval status: phase2
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Moderate-to-narrow window — early childhood onset; newborn screening integration would significantly improve outcomes
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: IV systemic or intramuscular injection — well established; used in SMA, DMD, Glybera

### Manual Review Flags

- Multiple causal genes listed; score is gene-specific and should be repeated for each molecular subtype
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: muscle
- Only partial tissue match; verify target-cell transduction and delivery route manually
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Therapeutic window is not wide; natural-history timing and irreversible damage should be reviewed
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone
