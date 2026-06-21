# NanoGT Match Report: Vitamin B12-unresponsive methylmalonic acidemia

**Disease:** Vitamin B12-unresponsive methylmalonic acidemia (ORPHA:27)  
**Primary gene:** MUT  
**Gene CDS:** 2250 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** liver, CNS  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: MITOCHONDRIAL MATRIX ENZYME (MUT): nuclear-encoded but the protein must be imported into the mitochondrial matrix post-translation via its N-terminal mitochondrial targeting sequence (MTS). Nuclear AAV delivery is theoretically feasible, but the therapeutic construct must preserve the intact MTS. MTS functionality is not captured by any other scoring dimension — this is an additional disease-specific development step requiring experimental validation.; Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints; Cell-autonomous protein across multiple tissues; high transduction coverage may be required.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function  
**Mechanistic detail:** Methylmalonyl-CoA mutase — nuclear-encoded mitochondrial MATRIX enzyme requiring post-translational import via intact N-terminal MTS  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** liver aav with mts validation  
**Evidence level/status:** direct / source_linked_needs_review  
**Evidence summary:** MUT is a nuclear-encoded mitochondrial matrix enzyme. Nuclear AAV delivery is theoretically feasible but the N-terminal mitochondrial targeting sequence (MTS) must be intact in the therapeutic construct for correct post-translational import into the matrix. MTS functionality and import efficiency must be validated experimentally before vector precedent scores can be applied. Liver-directed AAV programs in development (e.g. NCT03721861) confirm the approach is viable but disease-specific construct validation is required.  
**Evidence source:** [OMIM MUT gene entry](https://omim.org/entry/609058)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint readiness: liver/metabolic targets may have biochemical biomarkers, but biomarker correction must be linked to clinical benefit.
- Endpoint risk: CNS/neurodevelopmental outcomes may require natural-history data, age-stratified endpoints, and long follow-up because short-term clinical change can be hard to interpret.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | BMN 307 | AAV5 | 7.7/10 | 🟢 High | phase2 |
| 2 | DTX301 | AAV8 | 7.1/10 | 🟡 Medium | phase2 |
| 3 | Libmeldy | LV | 6.7/10 | 🟡 Medium | approved |
| 4 | OAV101-IT | AAV9 | 6.7/10 | 🟡 Medium | approved |
| 5 | Zolgensma | AAV9 | 6.7/10 | 🟡 Medium | approved |

---

## Match #1: BMN 307

**Precedent disease:** Phenylketonuria  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 7.7 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.60 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.50 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.71** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 2250bp / cargo 4700bp (48% utilized)
- Vector tropism plus precedent target match: liver
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: amino_acid_metabolism
- Disease mechanism: loss of function — Methylmalonyl-CoA mutase — nuclear-encoded mitochondrial MATRIX enzyme requiring post-translational import via intact N-terminal MTS
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: MUT is a nuclear-encoded mitochondrial matrix enzyme. Nuclear AAV delivery is theoretically feasible but the N-terminal mitochondrial targeting sequence (MTS) must be intact in the therapeutic construct for correct post-translational import into the matrix. MTS functionality and import efficiency must be validated experimentally before vector precedent scores can be applied. Liver-directed AAV programs in development (e.g. NCT03721861) confirm the approach is viable but disease-specific construct validation is required.
- Mechanism source: OMIM MUT gene entry (https://omim.org/entry/609058)
- Approval status: phase2
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: CONDITIONAL — MUT is a nuclear-encoded mitochondrial matrix protein. Nuclear AAV delivery is theoretically feasible (the gene is in the nuclear genome) but the N-terminal mitochondrial targeting sequence (MTS) must be preserved intact in the therapeutic construct for correct post-translational import into the mitochondrial matrix. MTS functionality is not validated by any other dimension in this framework. Confirm import efficiency with disease-specific in vitro/in vivo data before treating vector precedent scores as directly transferable.

### Manual Review Flags

- MITOCHONDRIAL MATRIX ENZYME (MUT): nuclear-encoded but the protein must be imported into the mitochondrial matrix post-translation via its N-terminal mitochondrial targeting sequence (MTS). Nuclear AAV delivery is theoretically feasible, but the therapeutic construct must preserve the intact MTS. MTS functionality is not captured by any other scoring dimension — this is an additional disease-specific development step requiring experimental validation.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #2: DTX301

**Precedent disease:** Ornithine transcarbamylase deficiency  
**Vector:** AAV8  
**Tissue target:** liver  
**Composite score:** 7.1 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.60 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.50 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.10** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 2250bp / cargo 4700bp (48% utilized)
- Vector tropism plus precedent target match: liver
- Both intracellular proteins
- LOF inheritance — compatible for gene replacement
- Pathway match: urea_cycle
- Disease mechanism: loss of function — Methylmalonyl-CoA mutase — nuclear-encoded mitochondrial MATRIX enzyme requiring post-translational import via intact N-terminal MTS
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: MUT is a nuclear-encoded mitochondrial matrix enzyme. Nuclear AAV delivery is theoretically feasible but the N-terminal mitochondrial targeting sequence (MTS) must be intact in the therapeutic construct for correct post-translational import into the matrix. MTS functionality and import efficiency must be validated experimentally before vector precedent scores can be applied. Liver-directed AAV programs in development (e.g. NCT03721861) confirm the approach is viable but disease-specific construct validation is required.
- Mechanism source: OMIM MUT gene entry (https://omim.org/entry/609058)
- Approval status: phase2
- Vector immunogenicity (AAV8): high (~30%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: CONDITIONAL — MUT is a nuclear-encoded mitochondrial matrix protein. Nuclear AAV delivery is theoretically feasible (the gene is in the nuclear genome) but the N-terminal mitochondrial targeting sequence (MTS) must be preserved intact in the therapeutic construct for correct post-translational import into the mitochondrial matrix. MTS functionality is not validated by any other dimension in this framework. Confirm import efficiency with disease-specific in vitro/in vivo data before treating vector precedent scores as directly transferable.

### Manual Review Flags

- MITOCHONDRIAL MATRIX ENZYME (MUT): nuclear-encoded but the protein must be imported into the mitochondrial matrix post-translation via its N-terminal mitochondrial targeting sequence (MTS). Nuclear AAV delivery is theoretically feasible, but the therapeutic construct must preserve the intact MTS. MTS functionality is not captured by any other scoring dimension — this is an additional disease-specific development step requiring experimental validation.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: cns
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #3: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.7 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.50 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.71** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 2250bp / cargo 8000bp (28% utilized)
- Precedent target match: cns
- Protein class mismatch
- Inheritance match (Autosomal recessive <-> AR)
- Different pathway (amino_acid_metabolism vs leukodystrophy)
- Disease mechanism: loss of function — Methylmalonyl-CoA mutase — nuclear-encoded mitochondrial MATRIX enzyme requiring post-translational import via intact N-terminal MTS
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: MUT is a nuclear-encoded mitochondrial matrix enzyme. Nuclear AAV delivery is theoretically feasible but the N-terminal mitochondrial targeting sequence (MTS) must be intact in the therapeutic construct for correct post-translational import into the matrix. MTS functionality and import efficiency must be validated experimentally before vector precedent scores can be applied. Liver-directed AAV programs in development (e.g. NCT03721861) confirm the approach is viable but disease-specific construct validation is required.
- Mechanism source: OMIM MUT gene entry (https://omim.org/entry/609058)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: CONDITIONAL — MUT is a nuclear-encoded mitochondrial matrix protein. Nuclear AAV delivery is theoretically feasible (the gene is in the nuclear genome) but the N-terminal mitochondrial targeting sequence (MTS) must be preserved intact in the therapeutic construct for correct post-translational import into the mitochondrial matrix. MTS functionality is not validated by any other dimension in this framework. Confirm import efficiency with disease-specific in vitro/in vivo data before treating vector precedent scores as directly transferable.

### Manual Review Flags

- MITOCHONDRIAL MATRIX ENZYME (MUT): nuclear-encoded but the protein must be imported into the mitochondrial matrix post-translation via its N-terminal mitochondrial targeting sequence (MTS). Nuclear AAV delivery is theoretically feasible, but the therapeutic construct must preserve the intact MTS. MTS functionality is not captured by any other scoring dimension — this is an additional disease-specific development step requiring experimental validation.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: cns, liver
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable

## Match #4: OAV101-IT

**Precedent disease:** Spinal Muscular Atrophy  
**Vector:** AAV9  
**Tissue target:** CNS/spinal cord  
**Composite score:** 6.7 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.50 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.71** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 2250bp / cargo 4700bp (48% utilized)
- Vector tropism plus precedent target match: cns
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Different pathway (amino_acid_metabolism vs motor_neuron)
- Disease mechanism: loss of function — Methylmalonyl-CoA mutase — nuclear-encoded mitochondrial MATRIX enzyme requiring post-translational import via intact N-terminal MTS
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: MUT is a nuclear-encoded mitochondrial matrix enzyme. Nuclear AAV delivery is theoretically feasible but the N-terminal mitochondrial targeting sequence (MTS) must be intact in the therapeutic construct for correct post-translational import into the matrix. MTS functionality and import efficiency must be validated experimentally before vector precedent scores can be applied. Liver-directed AAV programs in development (e.g. NCT03721861) confirm the approach is viable but disease-specific construct validation is required.
- Mechanism source: OMIM MUT gene entry (https://omim.org/entry/609058)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: CONDITIONAL — MUT is a nuclear-encoded mitochondrial matrix protein. Nuclear AAV delivery is theoretically feasible (the gene is in the nuclear genome) but the N-terminal mitochondrial targeting sequence (MTS) must be preserved intact in the therapeutic construct for correct post-translational import into the mitochondrial matrix. MTS functionality is not validated by any other dimension in this framework. Confirm import efficiency with disease-specific in vitro/in vivo data before treating vector precedent scores as directly transferable.

### Manual Review Flags

- MITOCHONDRIAL MATRIX ENZYME (MUT): nuclear-encoded but the protein must be imported into the mitochondrial matrix post-translation via its N-terminal mitochondrial targeting sequence (MTS). Nuclear AAV delivery is theoretically feasible, but the therapeutic construct must preserve the intact MTS. MTS functionality is not captured by any other scoring dimension — this is an additional disease-specific development step requiring experimental validation.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #5: Zolgensma

**Precedent disease:** Spinal Muscular Atrophy  
**Vector:** AAV9  
**Tissue target:** CNS/motor neuron  
**Composite score:** 6.7 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.50 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 1.00 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.50 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.71** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 2250bp / cargo 4700bp (48% utilized)
- Vector tropism plus precedent target match: cns
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Different pathway (amino_acid_metabolism vs motor_neuron)
- Disease mechanism: loss of function — Methylmalonyl-CoA mutase — nuclear-encoded mitochondrial MATRIX enzyme requiring post-translational import via intact N-terminal MTS
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: MUT is a nuclear-encoded mitochondrial matrix enzyme. Nuclear AAV delivery is theoretically feasible but the N-terminal mitochondrial targeting sequence (MTS) must be intact in the therapeutic construct for correct post-translational import into the matrix. MTS functionality and import efficiency must be validated experimentally before vector precedent scores can be applied. Liver-directed AAV programs in development (e.g. NCT03721861) confirm the approach is viable but disease-specific construct validation is required.
- Mechanism source: OMIM MUT gene entry (https://omim.org/entry/609058)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: ApoE/hAAT, TBG, transthyretin, albumin — extensively validated; used in Hemgenix, Roctavian, DTX301
- Route of administration: IV systemic — established, minimally invasive; used in all hepatic GT programs
- ORGANELLE TARGETING: CONDITIONAL — MUT is a nuclear-encoded mitochondrial matrix protein. Nuclear AAV delivery is theoretically feasible (the gene is in the nuclear genome) but the N-terminal mitochondrial targeting sequence (MTS) must be preserved intact in the therapeutic construct for correct post-translational import into the mitochondrial matrix. MTS functionality is not validated by any other dimension in this framework. Confirm import efficiency with disease-specific in vitro/in vivo data before treating vector precedent scores as directly transferable.

### Manual Review Flags

- MITOCHONDRIAL MATRIX ENZYME (MUT): nuclear-encoded but the protein must be imported into the mitochondrial matrix post-translation via its N-terminal mitochondrial targeting sequence (MTS). Nuclear AAV delivery is theoretically feasible, but the therapeutic construct must preserve the intact MTS. MTS functionality is not captured by any other scoring dimension — this is an additional disease-specific development step requiring experimental validation.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone
