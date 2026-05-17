
# Standardised Gene Therapy Protocol: Kohlschütter-Tönz syndrome

**Gene:** ROGDI (GMPR2, KIAA0267, FLJ22386, RAV2)  
**Disease:** Kohlschütter-Tönz syndrome (ORPHA:916)  
**OMIM:** 226750  
**Inheritance:** autosomal recessive  
**Prevalence:** <1 / 1,000,000  
**Report Generated:** 2026-05-14T17:05:37.645593Z  
**Framework Version:** nano-rare-gt v0.1  

---

## Executive Summary

This protocol evaluates ROGDI as a gene therapy target for Kohlschütter-Tönz syndrome using a systematic multi-parameter matching framework. The analysis assesses vector compatibility, target tissue accessibility, therapeutic rationale, regulatory precedent, and risk mitigations.

**Overall Assessment:** PROMISING CANDIDATE with manageable risks

---

## 1. Indication Summary

### Disease Description
Kohlschütter-Tönz syndrome (KTS) is a rare autosomal recessive disorder characterized by the triad of amelogenesis imperfecta (defective enamel), early-onset epilepsy, and progressive psychomotor regression. First described in 1974, it belongs to the ectodermal dysplasias. Affected children develop yellow-brown, hypoplastic teeth and experience severe intellectual disability, often accompanied by spasticity and autistic features. Survival into adulthood is uncommon; most patients die from status epilepticus or aspiration pneumonia.

### Unmet Need
No disease-modifying therapy exists. Current management is entirely supportive: multiple antiepileptic drugs, physical therapy, dental restoration, and nutritional support. The underlying genetic defect has never been addressed therapeutically. Gene therapy offers a rational path to disease modification because the gene is small, the inheritance is autosomal recessive with loss-of-function mutations, and the most disabling manifestations (CNS) are potentially rescuable with a single systemic vector dose.

### Clinical Course
Seizures typically begin in infancy (often within the first year). Dental abnormalities become visible in early childhood. Psychomotor delay is progressive; many patients lose previously acquired skills. Nephrocalcinosis has been reported in some cases. Hypohidrosis (reduced sweating) may cause heat intolerance. Life expectancy is significantly shortened.

---

## 2. Target Biology

### Gene & Protein

| Attribute | Value |
|-----------|-------|
| Gene Symbol | ROGDI |
| Aliases | GMPR2, KIAA0267, FLJ22386, RAV2 |
| Location | 16p12.1 |
| Exons | 11 |
| CDS Length | 1044 bp |
| Protein Length | 348 aa |
| Molecular Weight | 37874.0 Da |
| UniProt | Q9P2T1 |

### Protein Function
ROGDI encodes GMP reductase 2, an enzyme that catalyzes the NADPH-dependent deamination of GMP to IMP. It functions in purine nucleotide interconversion. Recent evidence (2025) reveals that ROGDI is also a Rabconnectin-3 subunit (Rav2 homolog), regulating V-ATPase assembly in lysosomes and synaptic vesicles. This dual function may explain the multi-system phenotype: GMP reductase loss causes metabolic imbalance, while V-ATPase dysregulation affects enamel acid handling and synaptic vesicle acidification.

### Cellular Localization
Primarily cytosolic (GO:0005829). Critically, ROGDI is presynaptically localized in neurons — a 2017 study showed GFP-tagged recombinant ROGDI enriches at presynaptic boutons. This means therapeutic transgene expression must achieve sufficient levels in presynaptic terminals, not just neuronal soma.

### Expression Pattern
Highly expressed in brain (hippocampus, cortex), heart, skeletal muscle, kidney, liver, and testis. Low expression in colon, thymus, and peripheral blood. The broad expression pattern is consistent with its metabolic housekeeping function but complicates tissue-specific targeting.

---

## 3. Therapeutic Rationale

### Why Gene Therapy is Appropriate
Gene therapy is appropriate because: (1) ROGDI is a small gene (≈1044 bp) that fits comfortably within AAV packaging limits; (2) KTS results from autosomal recessive loss-of-function mutations, making simple gene addition theoretically curative; (3) the most disabling manifestations (epilepsy, neurodevelopmental delay) occur in tissues accessible to systemically administered AAV9; (4) there is no known dominant-negative mechanism; (5) a Rogdi knockout mouse exists, providing a preclinical model.

### Inheritance & Mechanism
KTS follows autosomal recessive inheritance. Pathogenic variants include nonsense mutations, splice-site disruptions, and frameshift deletions. Compound heterozygosity is common. The protein is truncated or absent in affected individuals, consistent with a loss-of-function mechanism. Gene replacement therapy (supplying a wild-type copy) is the canonical approach for AR LoF disorders and has succeeded in SMA (SMN1), LCA2 (RPE65), and MLD (ARSA).

### Therapeutic Window
The therapeutic window is uncertain but likely exists. In SMA (Zolgensma), neonatal treatment produces the best outcomes, but treatment in infants up to 6 months still yields meaningful benefit. For KTS, early intervention before irreversible neurodegeneration is likely critical—ideally in the first weeks of life, though pre-symptomatic newborn screening does not yet exist. Dental enamel defects may be irreversible once formed, suggesting that even perfect CNS rescue would leave residual dental morbidity.

---

## 4. Vector Assessment

### Cargo Size Gate

| Parameter | Value | Limit | Status |
|-----------|-------|-------|--------|
| Gene CDS | 1044 bp | — | — |
| Estimated Total Cargo | 2544 bp | 4700 bp | PASS ✅ |

### Recommended Vector

| Attribute | Recommendation |
|-----------|----------------|
| Serotype | AAV9 |
| Promoter | Human synapsin-1 (hSYN1) promoter, ~470 bp. Rationale: neuron-specific expression minimizes off-target expression in liver and muscle; hSYN1 is the most widely used neuronal promoter in AAV GT programs (including CNS clinical trials); it drives expression in both excitatory and inhibitory neurons, essential for epilepsy control. Alternative: CamKIIα if forebrain bias is desired. |
| Delivery Route | Systemic intravenous (IV) infusion, preferably in the neonatal or early infant period. Rationale: AAV9 efficiently crosses the blood-brain barrier in young patients (Zolgensma precedent); provides brain-wide distribution; minimally invasive; avoids neurosurgical risks of intracranial injection. Backup: intrathecal delivery if systemic dosing is limited by liver toxicity concerns. |
| Dosing Age | Neonatal (birth to 14 days) or early infancy (<3 months). Rationale: BBB permeability to AAV9 is highest in neonates; neuronal circuitry is still plastic; seizure threshold may be modifiable before hyperexcitable networks consolidate. |

### Vector Justification
AAV9 is recommended based on: (1) proven CNS tropism with 25 clinical programs providing safety and regulatory precedent; (2) efficient BBB crossing in infants (Zolgensma model); (3) non-replicative, non-pathogenic profile well-established in >1000 treated patients; (4) cargo limit (4700 bp) comfortably exceeds ROGDI CDS + promoter + regulatory elements.

---

## 5. Preclinical Strategy

### Milestone 1: Disease Modeling
Establish patient-derived iPSC lines from KTS probands (available from dent pulp or skin fibroblasts). Differentiate to cortical and hippocampal neurons. Confirm ROGDI protein absence by Western blot and immunofluorescence. Verify presynaptic targeting deficit and V-ATPase dysfunction (LysoTracker assays).

### Milestone 2: Vector Validation
Clone codon-optimized human ROGDI cDNA into AAV9/hSYN1 backbone. Verify vector genome integrity by restriction digest and Sanger sequencing. Produce small-scale AAV9 vector using triple-transfection in HEK293. Titrate by qPCR (vg/mL). Confirm ROGDI expression and presynaptic trafficking in iPSC-neurons.

### Milestone 3: Efficacy in Rodents
Inject Rogdi knockout mice (available from JAX or literature) with AAV9-hSYN1-ROGDI via IV (neonatal) or intracerebroventricular (ICV). Assess: (a) survival and seizure frequency (video-EEG), (b) dental enamel histology, (c) brain ROGDI protein levels by WB/IF, (d) behavioral tests (rotarod, open field). Primary endpoint: ≥50% reduction in seizure burden vs. untreated KO at 8 weeks.

### Milestone 4: Toxicology & Biodistribution
Biodistribution study in immunocompetent mice: qPCR vector genome in brain, liver, spleen, heart, kidney. Toxicology in rats: single ascending dose with 28-day observation. Assess: liver enzymes (ALT/AST), histopathology, anti-capsid antibody titers. Dose-finding: bracket around proposed clinical dose scaled by brain:body weight ratio.

---

## 6. Regulatory Pathway

### Designation Strategy
Orphan Drug Designation (ODD) is strongly recommended and likely achievable: prevalence <200,000 in US; no approved therapy; serious/life-threatening. RMAT (Regenerative Medicine Advanced Therapy) may be sought if preclinical data shows substantial improvement over existing care. Pediatric Investigation Plan (PIP) will be required in EU. Fast Track and Breakthrough Therapy are feasible if clinical data shows dramatic efficacy in a small open-label study.

### Precedent Programs

- **Zolgensma (onasemnogene abeparvovec)** (Spinal muscular atrophy (SMA)): Single-dose IV AAV9 gene replacement in infants. Proves BBB crossing, CNS rescue, and neonatal dosing safety. Regulatory pathway (ODD, priority review) is directly applicable.

- **Luxturna (voretigene neparvovec)** (RPE65-associated retinal dystrophy): First FDA-approved in vivo GT. Less relevant for CNS but demonstrates AAV gene replacement regulatory precedent and long-term durability data.

- **Elevidys (delandistrogene moxeparvovec)** (Duchenne muscular dystrophy): AAVrh74 capsid with micro-dystrophin. Demonstrates systemic IV delivery to muscle + CNS and accelerated approval pathway under subpart H.


### Expected IND Timeline
Estimated 4–5 years from target validation to IND: Year 1–2: vector design, iPSC validation, small-scale AAV production. Year 2–3: rodent efficacy, dose-finding, GLP tox. Year 3–4: NHP biodistribution (if required for CNS). Year 4–5: CMC scale-up, regulatory pre-submission meeting, IND filing.

---

## 7. Risk Assessment & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|

| Immunogenicity (anti-capsid) | High | Moderate | Pre-screen for AAV9 NABs; corticosteroid prophylaxis (as in Zolgensma program); transient immunosuppression if needed. |

| Overexpression toxicity | Moderate | Moderate | Use neuron-specific promoter (hSYN1) to restrict expression; scAAV for lower expression; incorporate miRNA de-targeting of liver. |

| Delivery failure (dental paradox) | High | Moderate | Accept dental morbidity as secondary; focus CNS rescue as primary endpoint; consider dual-vector approach for ameloblasts. |

| Preclinical model failure | Moderate | High | Use both Rogdi KO mouse AND patient-derived iPSC neurons; validate rescue in both systems before IND. |

| Regulatory uncertainty (novel mechanism) | Moderate | Moderate | Engage FDA CBER early (pre-IND Type B meeting); frame as GT for epileptic encephalopathy, a well-understood indication class. |


---

## 8. Framework Scoring Breakdown

The following scores evaluate ROGDI against the 9 dimensions of the nano-rare GT matching framework:

| Dimension | Score (0–1) | Weight | Weighted Score | Notes |
|-----------|-------------|--------|----------------|-------|

| Structural Homology | 0.55 | 1.0 | 0.55 | IMPDH/GMPR family has extensive structural precedent but exact ROGDI 3D fold is rare. |

| Sequence Identity | 0.65 | 1.0 | 0.65 | GMPR1 ~65% identity provides partial functional redundancy evidence. |

| Domain Similarity | 0.70 | 1.0 | 0.70 | Single IMPDH/GMPR domain — well-characterized catalytic fold. |

| Size Compatibility | 0.95 | 2.0 | 1.90 | ~1044 bp is excellent; leaves margin for regulatory elements. Hard gate. |

| Tissue Tropism | 0.45 | 1.5 | 0.68 | AAV9 reaches CNS but not ameloblasts. Partial tissue match. |

| RoA Precedent | 0.80 | 1.5 | 1.20 | IV neonatal AAV9 precedent established by Zolgensma. |

| Promoter Match | 0.75 | 1.0 | 0.75 | hSYN1 is well-validated for CNS neurons. |

| Localization Match | 0.50 | 1.0 | 0.50 | Presynaptic trafficking may require endogenous localization signals in transgene. |

| Immunogenicity | 0.60 | 1.0 | 0.60 | Self-protein but codon-optimization may expose new epitopes. |

| Therapeutic Window | 0.55 | 1.5 | 0.83 | Likely exists in infancy before neurodegeneration consolidates. |

| Codon Optimization | 0.85 | 0.5 | 0.42 | Standard practice; minimal risk. |

| Platform Depth | 0.75 | 1.0 | 0.75 | AAV9 + hSYN1 combination has 8+ clinical programs. |


**Composite Score:** 0.675  
**Confidence:** medium  
**Gate Status:** PASS

---

## 9. Go / No-Go Decision Framework

### Critical Data Needed Before IND

- [ ] ROGDI protein expression confirmed in presynaptic terminals of transduced iPSC-neurons

- [ ] Seizure burden reduction ≥50% in Rogdi KO mouse after AAV9-hSYN1-ROGDI

- [ ] No unacceptable toxicity in GLP rodent study ( Grade ≤2 )

- [ ] CMC: scalable AAV9 production meeting ≥1e15 vg/dose in Sf9 or HEK system

- [ ] Regulatory: pre-IND Type B meeting minutes from FDA CBER

- [ ] Anti-AAV9 NAB prevalence established in target population

- [ ] Natural history data published (at least 20-patient cohort)


### Kill Criteria
(1) No measurable ROGDI protein in brain after systemic AAV9 at tolerated dose; (2) Seizure burden worsens or mortality increases in treated vs. untreated KO mice; (3) Severe hepatotoxicity (ALT >10× ULN) at therapeutic dose in NHP or rodent; (4) Immunogenicity prevents redosing and initial dose shows <6-month durability; (5) Regulatory pathway requires >5-year pivotal trial (not feasible for ultra-rare disease).

### Green Light Criteria
(1) Robust presynaptic ROGDI expression in brain at ≥1% of WT levels; (2) ≥50% seizure reduction + improved survival in rodent model; (3) Dose-response relationship confirming efficacy in at least two species; (4) GLP tox package clean with NOAEL ≥5× projected clinical dose; (5) ODD granted; FDA CBER agreeable to accelerated approval based on biomarker + functional endpoint.

---

## 10. Conclusions & Recommendations

ROGDI is a compelling but challenging gene therapy candidate for Kohlschütter-Tönz syndrome. The gene is small, the inheritance is straightforward AR LoF, and AAV9 systemic delivery has precedent for CNS rescue in infants. However, the multi-system nature (brain + teeth + kidney), the intracellular presynaptic localization, and the lack of any GT clinical data for ROGDI make this a high-risk, high-reward program. The recommended path forward is a focused preclinical program centered on iPSC-neuron and Rogdi KO mouse rescue, with a clear go/no-go decision at 18 months based on efficacy and safety in the rodent model.

---

*This protocol was generated by the nano-rare GT Framework. It is intended for research and strategic planning purposes and does not constitute clinical or regulatory advice. All claims should be independently verified against primary literature.*