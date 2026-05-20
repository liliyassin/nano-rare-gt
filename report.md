# Standardised Gene Therapy Protocol: Kohlschütter-Tönz syndrome / amelocerebrohypohidrotic syndrome

**Gene:** ROGDI (KIAA0267, FLJ22386, RAV2)  
**Disease:** Kohlschütter-Tönz syndrome / amelocerebrohypohidrotic syndrome (ORPHA:1946)  
**OMIM:** 226750  
**Inheritance:** autosomal recessive  
**Prevalence:** <1 / 1,000,000  
**Report Generated:** 2026-05-19T20:41:52.981956Z  
**Framework Version:** nano-rare-gt v0.2 source-audited  

---

## Executive Summary

This protocol evaluates ROGDI as a gene therapy target for Kohlschütter-Tönz syndrome / amelocerebrohypohidrotic syndrome using a systematic multi-parameter matching framework. The analysis assesses vector compatibility, target tissue accessibility, therapeutic rationale, regulatory precedent, and risk mitigations.

**Overall Assessment:** PROMISING CANDIDATE with manageable risks

---

## 1. Indication Summary

### Disease Description
Kohlschütter-Tönz syndrome (KTS), also described as amelocerebrohypohidrotic syndrome, is an ultra-rare autosomal recessive neuro-ectodermal disorder. The core clinical pattern is amelogenesis imperfecta, early-onset epilepsy, severe developmental delay or regression, spasticity, and variable hypohidrosis or nephrocalcinosis. Orphanet assigns KTS to ORPHA:1946; OMIM lists the phenotype as 226750 and the ROGDI gene as 614574.

### Unmet Need
No disease-modifying therapy exists. Current care is supportive: antiseizure medicines, developmental support, dental restoration, nutrition support, and management of respiratory or aspiration complications. A gene-addition strategy is biologically plausible because KTS is recessive, published pathogenic variants are consistent with loss of ROGDI function, and the coding sequence is small enough for an AAV cassette. The unresolved problem is delivery: ROGDI is intracellular and non-secreted, so affected cells probably require direct transduction rather than cross-correction.

### Clinical Course
Seizures often begin in infancy or early childhood and may be refractory. Dental enamel defects become evident as teeth erupt. Neurodevelopmental impairment can be severe and may progress with loss of skills; spasticity and profound intellectual disability have been reported. Hypohidrosis can cause heat intolerance, and nephrocalcinosis has been reported in some patients. Because enamel is formed during a time-limited developmental window, established dental defects may not be reversible even if CNS disease is modified.

---

## 2. Target Biology

### Gene & Protein

| Attribute | Value |
|-----------|-------|
| Gene Symbol | ROGDI |
| Aliases | KIAA0267, FLJ22386, RAV2 |
| Location | 16p12.1 |
| Exons | 11 |
| CDS Length | 861 bp |
| Protein Length | 287 aa |
| Molecular Weight | 32254.0 Da |
| UniProt | Q9GZN7 |

### Protein Function
ROGDI encodes Protein rogdi homolog (UniProt Q9GZN7), a 287 amino-acid, approximately 32.3 kDa intracellular protein. Structural and recent cell-biologic evidence support a non-enzymatic scaffolding or adaptor role. The solved human ROGDI structures (PDB 5XQH and 5XQI) show an atypical leucine-zipper-like fold, and a 2025 study identified ROGDI as a Rabconnectin-3-associated subunit linked to V-ATPase assembly or regulation in acidic organelle biology. This changes the potency strategy: assays should measure expression, localization, complex interaction, and V-ATPase/lysosomal rescue rather than catalytic activity.

### Cellular Localization
UniProt Q9GZN7 annotates ROGDI in the nuclear envelope and neuronal compartments including presynapse, axon, perikaryon, dendrite, and synaptic vesicle contexts. The KTS literature also links ROGDI to presynaptic biology. For gene therapy, this means that simply producing protein in the soma may not be enough; the construct and expression level must preserve endogenous intracellular localization and protein-complex stoichiometry.

### Expression Pattern
Human Protein Atlas and transcriptomic resources indicate broad ROGDI expression, including nervous system and other somatic tissues. The clinical phenotype shows that neurons and enamel-forming ameloblast-lineage cells are the high-priority therapeutic tissues. The broad expression pattern argues against assuming that one tissue-specific promoter can fully normalize every tissue, but CNS rescue is the clearest first therapeutic objective.

---

## 3. Therapeutic Rationale

### Why Gene Therapy is Appropriate
Gene therapy is appropriate to investigate because: (1) the ROGDI amino-acid coding region is about 861 bp, leaving large AAV packaging margin; (2) KTS is autosomal recessive and consistent with loss of function, making gene addition conceptually suitable; (3) the most life-limiting manifestations are CNS-driven epileptic and neurodevelopmental features, where AAV9 and related CNS-directed AAV approaches have clinical precedent; and (4) no approved disease-modifying therapy exists. The main caveat is that ROGDI is intracellular, so adequate cell-autonomous transduction is probably required.

### Inheritance & Mechanism
KTS follows autosomal recessive inheritance. Reported variants include nonsense, frameshift, and splice-site changes predicted to truncate or destabilize ROGDI. The Lee et al. crystal-structure paper mapped disease variants onto the protein fold and showed why truncations or exon loss would disrupt the four-helix/beta architecture. Supplying a wild-type ROGDI copy is therefore the correct first gene-therapy hypothesis, provided expression level and localization are controlled.

### Therapeutic Window
The CNS therapeutic window is uncertain but likely earliest in infancy, before seizure networks and neurodevelopmental injury consolidate. Dental enamel is a separate timing problem: once enamel has formed abnormally, systemic CNS-directed gene therapy is unlikely to repair it. A first-in-program strategy should define CNS endpoints as primary and treat dental outcomes as residual morbidity or as a separate delivery program.

---

## 4. Vector Assessment

### Cargo Size Gate

| Parameter | Value | Limit | Status |
|-----------|-------|-------|--------|
| Gene CDS | 861 bp | — | — |
| Estimated Total Cargo | 2361 bp | 4700 bp | PASS ✅ |

### Recommended Vector

| Attribute | Recommendation |
|-----------|----------------|
| Serotype | AAV9 |
| Promoter | Human synapsin-1 (hSYN1) promoter, approximately 470 bp, for the first CNS proof-of-concept. Rationale: hSYN1 restricts expression toward neurons, matching the epilepsy/neurodevelopmental objective and reducing unnecessary peripheral overexpression. A low-strength ubiquitous or endogenous-style promoter should only be considered after dose-response and stoichiometry studies show that broader expression is safe and necessary. |
| Delivery Route | CNS-prioritized AAV9 delivery, either neonatal/early-infant systemic IV or an intrathecal route depending on safety and biodistribution data. IV AAV9 has SMA precedent, but intrathecal delivery may reduce peripheral exposure. The selected route should be justified around brain rescue, not dental rescue, because no single plausible route is expected to restore both CNS neurons and formed enamel. |
| Dosing Age | As early as diagnosable, ideally neonatal or early infancy for CNS rescue. Earlier treatment is favored because seizures and neurodevelopmental injury may become self-reinforcing. Dental rescue would require an even earlier or separate ameloblast-targeted strategy and should not be assumed for the first CNS program. |

### Vector Justification
AAV9 is recommended for initial CNS-focused feasibility because it has clinical precedent for nervous-system gene delivery, a packaging limit of about 4700 bp, and enough capacity for ROGDI cDNA plus a compact neuronal promoter, ITRs, and polyadenylation signal. The cargo-size gate is strong; the main risk is not packaging but achieving enough direct transduction in the disease-relevant neurons while avoiding off-target stoichiometric toxicity.

---

## 5. Preclinical Strategy

### Milestone 1: Disease Modeling
Establish patient-derived iPSC neuronal models and, where possible, ameloblast- lineage or dental organoid assays. Confirm reduced or absent ROGDI protein, then measure baseline localization, Rabconnectin-3 interaction, acidic organelle/V-ATPase phenotypes, neuronal excitability, and synaptic-vesicle markers.

### Milestone 2: Vector Validation
Clone codon-optimized human ROGDI Q9GZN7 cDNA into an AAV9/hSYN1 backbone. Verify the vector genome by sequencing. Produce small-scale AAV9, titer by qPCR or ddPCR, and confirm protein expression, intracellular localization, complex interaction, and lysosomal/synaptic functional rescue in patient-derived neurons.

### Milestone 3: Efficacy in Rodents
Test AAV9-hSYN1-ROGDI in a Rogdi-deficient mouse model if available and validated. Assess vector biodistribution, brain ROGDI expression/localization, seizure burden by video-EEG, survival, behavior, and dental histology as an exploratory secondary endpoint. A meaningful go/no-go endpoint would be a reproducible reduction in seizure burden or neuronal functional phenotype versus untreated mutants.

### Milestone 4: Toxicology & Biodistribution
Run dose-ranging, biodistribution, and toxicology studies with special attention to liver exposure, dorsal-root-ganglion pathology, CNS inflammation, and abnormal ROGDI overexpression or mislocalization. Develop a release and potency package that includes vector genome integrity, expression, localization, protein-complex interaction, and cell-based rescue rather than enzyme activity.

---

## 6. Regulatory Pathway

### Designation Strategy
Orphan Drug Designation is strongly plausible because KTS is ultra-rare, serious, and lacks approved disease-modifying therapy. A pre-IND meeting should focus on the potency assay challenge for a non-secreted intracellular scaffold, the choice of CNS endpoint, whether dental disease is primary or secondary, and the adequacy of the animal model for epileptic and developmental phenotypes.

### Precedent Programs
- **Zolgensma (onasemnogene abeparvovec)** (Spinal muscular atrophy (SMA)): Single-dose systemic AAV9 gene replacement in infants; strongest precedent for an early-life CNS-prioritized AAV strategy.
- **Luxturna (voretigene neparvovec)** (RPE65-associated inherited retinal dystrophy): AAV gene-addition regulatory precedent and durability example; route and tissue are less relevant to ROGDI.
- **Resamirigene bilparvovec / AT132 precedent class** (X-linked myotubular myopathy programs): Illustrates risks and potency challenges for intracellular non-secreted proteins and the need for rigorous dose/tox controls.

### Expected IND Timeline
Estimated 4–6 years from corrected target validation to IND. Year 1: potency assay and patient-cell model development. Year 1–2: vector design, expression, localization, and cell rescue. Year 2–3: animal efficacy and dose selection. Year 3–5: GLP toxicology, biodistribution, CMC scale-up, and pre-IND engagement. Extra time may be needed because ROGDI lacks a simple catalytic potency assay.

---

## 7. Risk Assessment & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Cell-autonomous delivery failure | High | High | Quantify direct neuronal transduction and ROGDI localization; do not assume cross-correction from neighboring cells. |
| Dental/CNS delivery mismatch | High | Moderate | Define CNS rescue as the first primary objective; treat dental rescue as secondary, residual, or a separate local-delivery program. |
| Overexpression or stoichiometric toxicity | Moderate | Moderate | Use a compact neuronal promoter, dose-ranging, localization assays, and protein-complex interaction assays before broad expression strategies. |
| Potency assay uncertainty | High | High | Build orthogonal assays for expression, localization, Rabconnectin-3 interaction, acidic organelle function, and neuronal rescue. |
| Anti-capsid and systemic AAV toxicity | Moderate | High | Screen neutralizing antibodies; monitor liver, DRG, and CNS inflammation; compare IV and intrathecal exposure before clinical route lock. |

---

## 8. Framework Scoring Breakdown

The following scores evaluate ROGDI against the 12 dimensions of the nano-rare GT matching framework:

| Dimension | Score (0–1) | Weight | Weighted Score | Notes |
|-----------|-------------|--------|----------------|-------|
| Structural Homology | 0.50 | 1.0 | 0.50 | Solved human ROGDI structures exist, but there is no close approved gene-therapy cargo surrogate. |
| Sequence Identity | 0.35 | 1.0 | 0.35 | No strong approved-cargo paralog; precedent should be based on platform and intracellular scaffold risk rather than paralog identity. |
| Domain Similarity | 0.55 | 1.0 | 0.55 | RAVE2/Rogdi and Rogdi_lz annotations support mechanism, but the domain family is not a mature therapeutic precedent class. |
| Size Compatibility | 0.98 | 2.0 | 1.96 | About 861 bp for the amino-acid coding region; excellent AAV margin. Hard gate. |
| Tissue Tropism | 0.45 | 1.5 | 0.68 | AAV9 can support CNS strategy, but tooth/enamel biology creates a major mismatch. |
| RoA Precedent | 0.80 | 1.5 | 1.20 | Early-life AAV9 precedent is relevant for CNS rescue; route still needs disease-specific biodistribution. |
| Promoter Match | 0.70 | 1.0 | 0.70 | hSYN1 is reasonable for neuronal proof-of-concept but may not address non-neuronal disease tissues. |
| Localization Match | 0.45 | 1.0 | 0.45 | Intracellular localization and complex stoichiometry must be empirically verified after transduction. |
| Immunogenicity | 0.60 | 1.0 | 0.60 | Self-protein reduces transgene concern, but AAV capsid immunity and codon-optimized epitopes remain risks. |
| Therapeutic Window | 0.55 | 1.5 | 0.83 | CNS intervention is probably earliest-infant; dental disease may already be partly fixed by treatment time. |
| Codon Optimization | 0.85 | 0.5 | 0.42 | Short coding sequence makes optimization easy, but expression level should be tuned carefully. |
| Platform Depth | 0.70 | 1.0 | 0.70 | AAV9 CNS programs provide platform precedent, not direct ROGDI-specific efficacy precedent. |

**Composite Score:** 0.623
**Confidence:** medium  
**Gate Status:** PASS

---

## 9. Go / No-Go Decision Framework

### Critical Data Needed Before IND
- [ ] Live source verification reconfirms ROGDI maps to UniProt Q9GZN7 and Orphanet ORPHA:1946
- [ ] AAV construct expresses 287 aa ROGDI protein at controlled levels in patient-derived neurons
- [ ] ROGDI localizes to expected intracellular neuronal compartments after transduction
- [ ] Rabconnectin-3/V-ATPase-linked cellular phenotype or neuronal functional phenotype is rescued
- [ ] Dose-response is demonstrated without mislocalization or overexpression toxicity
- [ ] Rogdi-deficient animal model shows meaningful CNS functional benefit
- [ ] Potency assay package is accepted in pre-IND discussion as relevant to the non-enzymatic mechanism

### Kill Criteria
(1) Correctly mapped ROGDI protein cannot be expressed or localized in neurons; (2) functional assays show no rescue despite adequate expression; (3) therapeutic dose causes unacceptable liver, DRG, CNS, or overexpression toxicity; (4) CNS biodistribution is inadequate at a tolerable dose; (5) regulators reject the potency assay as unrelated to the disease mechanism.

### Green Light Criteria
(1) Q9GZN7 identity and transcript/coding sequence are locked; (2) AAV-ROGDI restores expression, localization, and at least one mechanism-linked functional readout in patient neurons; (3) animal data show CNS benefit and tolerable safety; (4) CMC can produce a consistent small-cargo AAV product; (5) orphan and pre-IND interactions support a feasible first-in-human path.

---

## 10. Conclusions & Recommendations

Corrected ROGDI biology makes the program still promising but more nuanced. The cargo-size gate is excellent, the inheritance model supports gene addition, and AAV9 provides a credible CNS-first route. However, ROGDI is a non-secreted intracellular scaffold/adaptor linked to Rabconnectin-3 and V-ATPase biology, so direct neuronal transduction and custom potency assays are the central bottlenecks. The recommended next step is a rigorous preclinical package centered on patient-derived neurons, localization and interaction assays, acidic organelle/synaptic functional rescue, and careful animal dose-response before any clinical claim.

---

*This protocol was generated by the nano-rare GT Framework. It is intended for research and strategic planning purposes and does not constitute clinical or regulatory advice. All claims should be independently verified against primary literature.*
