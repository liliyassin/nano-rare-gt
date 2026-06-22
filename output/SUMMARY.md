# NanoGT Results: 46-Disease GT Precedent Matching Cohort

**Algorithm:** 14-dimension heuristic scoring (v2): packaging fit, tissue tropism, protein class, pathway similarity, mechanism/modality compatibility, inheritance compatibility, approval precedent, vector immunogenicity, therapeutic window, cross-correction, immune privilege, promoter availability, route-of-administration feasibility, and organelle targeting feasibility. Raw max = 21; composite normalised to /10.

**Interpretation:** The framework ranks which existing clinical gene-therapy program is the closest development precedent for the query disease. It does not claim the top precedent is directly reusable without disease-specific validation, vector engineering, toxicology, and regulatory review.

## Summary Table

| Cohort role | Disease | ORPHA | Gene | Mechanism | Gene-addition fit | CDS (bp) | #1 Precedent | Vector | Score | Confidence |
|-------------|---------|-------|------|-----------|-------------------|----------|--------------|--------|-------|------------|
| positive_control | Hemophilia A | ORPHA:98878 | F8 | loss_of_function | compatible | 4374 | Hemgenix | AAV5 | 8.5/10 | high |
| positive_control | Hemophilia B | ORPHA:98879 | F9 | loss_of_function | compatible | 1383 | Hemgenix | AAV5 | 9.9/10 | high |
| benchmark_with_known_gt_precedent | Severe combined immunodeficiency due to adenosine deaminase deficiency | ORPHA:277 | ADA | loss_of_function | compatible | 1092 | Strimvelis | LV | 8.1/10 | high |
| positive_control | Spinal Muscular Atrophy | ORPHA:70 | SMN1 | loss_of_function | compatible | 891 | OAV101-IT | AAV9 | 8.3/10 | high |
| oversized_cargo_stress_test | Duchenne muscular dystrophy | ORPHA:98896 | DMD | loss_of_function_oversized | conditional | 11055 | SRP-9001 | AAV9 | 7.6/10 | high |
| mitochondrial_stress_test | Leber hereditary optic neuropathy | ORPHA:104 | MT-ND4 | mitochondrial_loss_of_function | uncertain | 1377 | CPCB-RPE1 | AAV8 | 6.4/10 | medium |
| pilot_cohort | Achromatopsia | ORPHA:49382 | CNGB3 | loss_of_function | compatible | 2427 | CPCB-RPE1 | AAV8 | 7.5/10 | medium |
| pilot_cohort | Alpha-mannosidosis | ORPHA:61 | MAN2B1 | loss_of_function | compatible | 3033 | Libmeldy | LV | 8.8/10 | high |
| pilot_cohort | Choroideremia | ORPHA:180 | CHM | loss_of_function | compatible | 1962 | Luxturna | AAV2 | 8.0/10 | high |
| pilot_cohort | Crigler-Najjar syndrome type I | ORPHA:79234 | UGT1A1 | loss_of_function | compatible | 1596 | Hemgenix | AAV5 | 7.2/10 | medium |
| pilot_cohort | Fabry disease | ORPHA:324 | GLA | loss_of_function | compatible | 1290 | Libmeldy | LV | 8.9/10 | high |
| pilot_cohort | Gaucher disease | ORPHA:355 | GBA1 | loss_of_function | conditional | 1491 | Libmeldy | LV | 9.0/10 | high |
| pilot_cohort | Glycogen storage disease type Ia | ORPHA:79258 | G6PC1 | loss_of_function | compatible | 1071 | SRP-9001 | AAV9 | 7.8/10 | high |
| pilot_cohort | Kohlschutter-Tonz syndrome | ORPHA:1946 | ROGDI | loss_of_function | conditional | 861 | OAV101-IT | AAV9 | 7.7/10 | high |
| pilot_cohort | Krabbe disease | ORPHA:487 | GALC | loss_of_function | conditional | 2055 | Libmeldy | LV | 9.0/10 | high |
| pilot_cohort | Maple syrup urine disease | ORPHA:511 | BCKDHA | loss_of_function | conditional | 1335 | BMN 307 | AAV5 | 8.0/10 | high |
| pilot_cohort | Metachromatic leukodystrophy | ORPHA:512 | ARSA | loss_of_function | compatible | 1521 | Libmeldy | LV | 9.2/10 | high |
| pilot_cohort | Mucolipidosis type IV | ORPHA:578 | MCOLN1 | loss_of_function | conditional | 1740 | Skysona | LV | 8.3/10 | high |
| pilot_cohort | Mucopolysaccharidosis type I | ORPHA:579 | IDUA | loss_of_function | compatible | 1962 | Libmeldy | LV | 9.5/10 | high |
| pilot_cohort | Mucopolysaccharidosis type II | ORPHA:580 | IDS | loss_of_function | compatible | 1650 | Libmeldy | LV | 9.3/10 | high |
| pilot_cohort | Mucopolysaccharidosis type IIIA (Sanfilippo A) | ORPHA:79269 | SGSH | loss_of_function | compatible | 1674 | Libmeldy | LV | 9.2/10 | high |
| pilot_cohort | Ornithine transcarbamylase deficiency | ORPHA:664 | OTC | loss_of_function | compatible | 1065 | BMN 307 | AAV5 | 8.1/10 | high |
| pilot_cohort | Phenylketonuria | ORPHA:716 | PAH | loss_of_function | compatible | 1353 | BMN 307 | AAV5 | 8.0/10 | high |
| pilot_cohort | Pompe disease | ORPHA:365 | GAA | loss_of_function | conditional | 2856 | Libmeldy | LV | 8.4/10 | high |
| pilot_cohort | Vitamin B12-unresponsive methylmalonic acidemia | ORPHA:27 | MMUT | loss_of_function | conditional | 2250 | BMN 307 | AAV5 | 7.7/10 | high |
| pilot_cohort | Wiskott-Aldrich syndrome | ORPHA:906 | WAS | loss_of_function | compatible | 1506 | Strimvelis | LV | 8.0/10 | high |
| pilot_cohort | X-linked adrenoleukodystrophy | ORPHA:43 | ABCD1 | loss_of_function | conditional | 2235 | Skysona | LV | 8.2/10 | high |
| pilot_cohort | X-linked myotubular myopathy | ORPHA:596 | MTM1 | loss_of_function | compatible | 1878 | AT132 | AAV8 | 7.7/10 | high |
| pilot_cohort | X-linked retinoschisis | ORPHA:792 | RS1 | loss_of_function | compatible | 672 | Luxturna | AAV2 | 7.9/10 | high |
| non_lof_haploinsufficiency | Rett syndrome | ORPHA:778 | MECP2 | haploinsufficiency | conditional | 1461 | Skysona | LV | 7.4/10 | medium |
| non_lof_repeat_expansion | Fragile X syndrome | ORPHA:908 | FMR1 | repeat_expansion_silencing | conditional | 1899 | Skysona | LV | 7.0/10 | medium |
| non_lof_haploinsufficiency | CHARGE syndrome | ORPHA:138 | CHD7 | haploinsufficiency | conditional | 7950 | Libmeldy | LV | 5.9/10 | medium |
| non_lof_haploinsufficiency | Neurofibromatosis type 1 | ORPHA:636 | NF1 | haploinsufficiency | conditional | 8451 | — | — | — | packaging_hard_fail |
| non_lof_repeat_expansion | Friedreich ataxia | ORPHA:95 | FXN | repeat_expansion_silencing | conditional | 633 | OAV101-IT | AAV9 | 7.9/10 | high |
| non_lof_haploinsufficiency | Tuberous sclerosis complex | ORPHA:805 | TSC1 | haploinsufficiency | conditional | 3495 | Libmeldy | LV | 6.4/10 | medium |
| pilot_cohort | Cystic fibrosis | ORPHA:586 | CFTR | loss_of_function | conditional | 4443 | Skysona | LV | 6.7/10 | medium |
| pilot_cohort | Canavan disease | ORPHA:141 | ASPA | loss_of_function | compatible | 942 | Libmeldy | LV | 8.1/10 | high |
| pilot_cohort | Biotinidase deficiency | ORPHA:79241 | BTD | loss_of_function | compatible | 1632 | Libmeldy | LV | 8.3/10 | high |
| pilot_cohort | Tay-Sachs disease | ORPHA:845 | HEXA | loss_of_function | conditional | 1590 | Libmeldy | LV | 8.5/10 | high |
| pilot_cohort | Wilson disease | ORPHA:905 | ATP7B | loss_of_function | conditional | 4398 | Skysona | LV | 7.3/10 | medium |
| pilot_cohort | Nephropathic cystinosis | ORPHA:213 | CTNS | loss_of_function | conditional | 1104 | Libmeldy | LV | 6.6/10 | medium |
| pilot_cohort | Chronic neurovisceral acid sphingomyelinase deficiency | ORPHA:618891 | SMPD1 | loss_of_function | conditional | 1890 | Libmeldy | LV | 8.8/10 | high |
| pilot_cohort | Niemann-Pick disease type C | ORPHA:646 | NPC1 | loss_of_function | conditional | 3837 | Libmeldy | LV | 8.1/10 | high |
| pilot_cohort | Zellweger syndrome | ORPHA:912 | PEX1 | loss_of_function | conditional | 3852 | Skysona | LV | 7.6/10 | high |
| pilot_cohort | Primary hyperoxaluria type 1 | ORPHA:93598 | AGXT | loss_of_function | conditional | 1179 | BMN 307 | AAV5 | 7.3/10 | medium |
| pilot_cohort | Usher syndrome type 1B | ORPHA:886 | MYO7A | loss_of_function | conditional | 6648 | Strimvelis | LV | 6.5/10 | medium |

---

## Disease Sections

### Hemophilia A (ORPHA:98878)
**Gene:** F8 | **Mechanism:** loss_of_function | **CDS:** 4374 bp | **Inheritance:** X-linked recessive | **Tissues:** liver

**Mechanism evidence:** BioMarin Roctavian (valoctocogene roxaparvovec) approved for Hemophilia A; AAV5 liver-directed F8 expression precedent Source: OMIM Hemophilia A 306700 (https://omim.org/entry/306700)

1. **Hemgenix** (AAV5) — 8.5/10 [high]
2. **Roctavian** (AAV5) — 8.5/10 [high]
3. **SPK-8011** (AAVrh10) — 8.1/10 [high]
4. **DTX201** (AAV8) — 7.8/10 [high]
5. **Libmeldy** (LV) — 7.3/10 [medium]

### Hemophilia B (ORPHA:98879)
**Gene:** F9 | **Mechanism:** loss_of_function | **CDS:** 1383 bp | **Inheritance:** X-linked recessive | **Tissues:** liver

**Mechanism evidence:** Deficiency of coagulation factor IX is the therapeutic deficit; liver-directed F9 expression is an approved gene-addition precedent Source: OMIM Hemophilia B 306900 (https://omim.org/entry/306900)

1. **Hemgenix** (AAV5) — 9.9/10 [high]
2. **Roctavian** (AAV5) — 9.9/10 [high]
3. **SPK-8011** (AAVrh10) — 9.6/10 [high]
4. **DTX201** (AAV8) — 9.2/10 [high]
5. **ST-920** (AAV2/6) — 8.7/10 [high]

### Severe combined immunodeficiency due to adenosine deaminase deficiency (ORPHA:277)
**Gene:** ADA | **Mechanism:** loss_of_function | **CDS:** 1092 bp | **Inheritance:** Autosomal recessive | **Tissues:** hematopoietic

**Mechanism evidence:** ADA-SCID is a deficiency disorder with an approved ex vivo autologous CD34+ ADA gene-addition precedent (Strimvelis; gammaretroviral vector) Source: OMIM ADA-SCID 102700 (https://omim.org/entry/102700)

1. **Strimvelis** (LV) — 8.1/10 [high]
2. **Libmeldy** (LV) — 7.0/10 [medium]
3. **Skysona** (LV) — 6.8/10 [medium]
4. **AVR-RD-01** (LV) — 6.6/10 [medium]
5. **BMN 307** (AAV5) — 6.4/10 [medium]

### Spinal Muscular Atrophy (ORPHA:70)
**Gene:** SMN1 | **Mechanism:** loss_of_function | **CDS:** 891 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, muscle

**Mechanism evidence:** FDA Zolgensma indication is SMA with biallelic SMN1 mutations; product supplies functional SMN transgene Source: FDA Zolgensma product page (https://www.fda.gov/vaccines-blood-biologics/zolgensma)

1. **OAV101-IT** (AAV9) — 8.3/10 [high]
2. **Zolgensma** (AAV9) — 8.3/10 [high]
3. **AT132** (AAV8) — 8.1/10 [high]
4. **SRP-9001** (AAV9) — 7.7/10 [high]
5. **BMN 307** (AAV5) — 7.4/10 [medium]

### Duchenne muscular dystrophy (ORPHA:98896)
**Gene:** DMD | **Mechanism:** loss_of_function_oversized | **CDS:** 11055 bp | **Inheritance:** X-linked recessive | **Tissues:** muscle, heart

**Mechanism evidence:** DMD supports replacement logic but requires micro-dystrophin or other engineered strategies because full-length DMD exceeds AAV capacity Source: Chamberlain et al. 2023 microdystrophin review (https://pubmed.ncbi.nlm.nih.gov/36990339/)

1. **SRP-9001** (AAV9) — 7.6/10 [high]

### Leber hereditary optic neuropathy (ORPHA:104)
**Gene:** MT-ND4 | **Mechanism:** mitochondrial_loss_of_function | **CDS:** 1377 bp | **Inheritance:** Mitochondrial inheritance | **Tissues:** retina, CNS

**Mechanism evidence:** Mitochondrial DNA disease is not ordinary nuclear gene addition; allotopic AAV approaches are specialized and disease-specific Source: OMIM MT-ND4 gene entry (https://omim.org/entry/516003)

1. **CPCB-RPE1** (AAV8) — 6.4/10 [medium]
2. **Skysona** (LV) — 6.3/10 [medium]
3. **Luxturna** (AAV2) — 6.1/10 [medium]
4. **Libmeldy** (LV) — 5.9/10 [medium]
5. **Hemgenix** (AAV5) — 5.6/10 [medium]

### Achromatopsia (ORPHA:49382)
**Gene:** CNGB3 | **Mechanism:** loss_of_function | **CDS:** 2427 bp | **Inheritance:** Autosomal recessive | **Tissues:** retina

**Mechanism evidence:** Biallelic CNGB3 loss is compatible with photoreceptor-directed gene addition if target cells remain viable Source: OMIM CNGB3 gene entry (https://omim.org/entry/605080)

1. **CPCB-RPE1** (AAV8) — 7.5/10 [medium]
2. **Luxturna** (AAV2) — 7.1/10 [medium]
3. **Skysona** (LV) — 6.7/10 [medium]
4. **Libmeldy** (LV) — 6.3/10 [medium]
5. **Strimvelis** (LV) — 6.3/10 [medium]

### Alpha-mannosidosis (ORPHA:61)
**Gene:** MAN2B1 | **Mechanism:** loss_of_function | **CDS:** 3033 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, liver

**Mechanism evidence:** Lysosomal enzyme deficiency supports gene addition and possible cross-correction logic Source: OMIM MAN2B1 gene entry (https://omim.org/entry/609458)

1. **Libmeldy** (LV) — 8.8/10 [high]
2. **ST-920** (AAV2/6) — 8.1/10 [high]
3. **ABO-101** (AAV9) — 8.1/10 [high]
4. **RGX-121** (AAV9) — 8.1/10 [high]
5. **Hemgenix** (AAV5) — 7.9/10 [high]

### Choroideremia (ORPHA:180)
**Gene:** CHM | **Mechanism:** loss_of_function | **CDS:** 1962 bp | **Inheritance:** X-linked recessive | **Tissues:** retina

**Mechanism evidence:** CHM loss of function is a retinal gene-addition target if viable retina remains Source: OMIM CHM gene entry (https://omim.org/entry/300390)

1. **Luxturna** (AAV2) — 8.0/10 [high]
2. **Strimvelis** (LV) — 7.4/10 [medium]
3. **CPCB-RPE1** (AAV8) — 7.3/10 [medium]
4. **Skysona** (LV) — 7.0/10 [medium]
5. **BMN 307** (AAV5) — 7.0/10 [medium]

### Crigler-Najjar syndrome type I (ORPHA:79234)
**Gene:** UGT1A1 | **Mechanism:** loss_of_function | **CDS:** 1596 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver

**Mechanism evidence:** UGT1A1 deficiency supports hepatocyte-directed gene addition Source: OMIM UGT1A1 gene entry (https://omim.org/entry/191740)

1. **Hemgenix** (AAV5) — 7.2/10 [medium]
2. **Roctavian** (AAV5) — 7.2/10 [medium]
3. **BMN 307** (AAV5) — 7.2/10 [medium]
4. **Skysona** (LV) — 7.1/10 [medium]
5. **SPK-8011** (AAVrh10) — 6.9/10 [medium]

### Fabry disease (ORPHA:324)
**Gene:** GLA | **Mechanism:** loss_of_function | **CDS:** 1290 bp | **Inheritance:** X-linked dominant | **Tissues:** liver, kidney, heart, CNS

**Mechanism evidence:** Fabry is caused by deficient GLA enzyme activity; secreted enzyme strategies can support systemic cross-correction Source: OMIM GLA gene entry (https://omim.org/entry/300644)

1. **Libmeldy** (LV) — 8.9/10 [high]
2. **ST-920** (AAV2/6) — 8.8/10 [high]
3. **RGX-121** (AAV9) — 8.7/10 [high]
4. **Hemgenix** (AAV5) — 8.5/10 [high]
5. **Roctavian** (AAV5) — 8.5/10 [high]

### Gaucher disease (ORPHA:355)
**Gene:** GBA1 | **Mechanism:** loss_of_function | **CDS:** 1491 bp | **Inheritance:** Autosomal recessive | **Tissues:** hematopoietic, liver, CNS

**Mechanism evidence:** GBA deficiency supports replacement logic but neuronopathic disease and tissue access can limit simple systemic correction Source: OMIM GBA gene entry (https://omim.org/entry/606463)

1. **Libmeldy** (LV) — 9.0/10 [high]
2. **AVR-RD-01** (LV) — 8.6/10 [high]
3. **ST-920** (AAV2/6) — 8.1/10 [high]
4. **ABO-101** (AAV9) — 8.1/10 [high]
5. **RGX-121** (AAV9) — 8.1/10 [high]

### Glycogen storage disease type Ia (ORPHA:79258)
**Gene:** G6PC1 | **Mechanism:** loss_of_function | **CDS:** 1071 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, kidney

**Mechanism evidence:** G6PC deficiency is a metabolic enzyme loss where liver-directed expression is a plausible gene-addition strategy Source: OMIM G6PC gene entry (https://omim.org/entry/613742)

1. **SRP-9001** (AAV9) — 7.8/10 [high]
2. **ST-920** (AAV2/6) — 7.8/10 [high]
3. **RGX-121** (AAV9) — 7.7/10 [high]
4. **Hemgenix** (AAV5) — 7.6/10 [high]
5. **Roctavian** (AAV5) — 7.6/10 [high]

### Kohlschutter-Tonz syndrome (ORPHA:1946)
**Gene:** ROGDI | **Mechanism:** loss_of_function | **CDS:** 861 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

**Mechanism evidence:** Published KTS variants in ROGDI are consistent with loss of function (Schossig 2012) and gene addition is mechanistically plausible. However the molecular function of ROGDI protein is not fully resolved: proposed roles include V-ATPase regulation via the RAVE/Rabconnectin-3 complex and synaptic vesicle biology but no disease-specific in vivo model or gene addition rescue experiment has been published as of 2025. Scoring assumptions (LOF gene addition is sufficient) are unvalidated. Do not interpret the composite score as evidence of clinical tractability without independent confirmation of gene function and therapeutic rationale. Source: Schossig et al. 2012 Mutations in ROGDI Cause Kohlschutter-Tonz Syndrome (https://pubmed.ncbi.nlm.nih.gov/22482807/)

1. **OAV101-IT** (AAV9) — 7.7/10 [high]
2. **Zolgensma** (AAV9) — 7.7/10 [high]
3. **BMN 307** (AAV5) — 7.5/10 [medium]
4. **Libmeldy** (LV) — 7.4/10 [medium]
5. **Strimvelis** (LV) — 7.3/10 [medium]

### Krabbe disease (ORPHA:487)
**Gene:** GALC | **Mechanism:** loss_of_function | **CDS:** 2055 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

**Mechanism evidence:** GALC deficiency supports replacement logic but CNS delivery and toxic metabolite biology require disease-specific validation Source: OMIM GALC gene entry (https://omim.org/entry/606890)

1. **Libmeldy** (LV) — 9.0/10 [high]
2. **Skysona** (LV) — 8.4/10 [high]
3. **ABO-101** (AAV9) — 8.3/10 [high]
4. **RGX-121** (AAV9) — 8.3/10 [high]
5. **AVR-RD-01** (LV) — 8.1/10 [high]

### Maple syrup urine disease (ORPHA:511)
**Gene:** BCKDHA | **Mechanism:** loss_of_function | **CDS:** 1335 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, CNS

**Mechanism evidence:** BCKDHA deficiency supports replacement logic but the multi-subunit enzyme complex and CNS metabolic crises make liver-only rescue uncertain Source: OMIM BCKDHA gene entry (https://omim.org/entry/608348)

1. **BMN 307** (AAV5) — 8.0/10 [high]
2. **Luxturna** (AAV2) — 7.2/10 [medium]
3. **OAV101-IT** (AAV9) — 7.0/10 [medium]
4. **Zolgensma** (AAV9) — 7.0/10 [medium]
5. **Hemgenix** (AAV5) — 6.8/10 [medium]

### Metachromatic leukodystrophy (ORPHA:512)
**Gene:** ARSA | **Mechanism:** loss_of_function | **CDS:** 1521 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

**Mechanism evidence:** ARSA deficiency is compatible with gene addition and HSC-mediated enzyme delivery/cross-correction precedent Source: OMIM ARSA gene entry (https://omim.org/entry/607574)

1. **Libmeldy** (LV) — 9.2/10 [high]
2. **Skysona** (LV) — 8.6/10 [high]
3. **ABO-101** (AAV9) — 8.5/10 [high]
4. **RGX-121** (AAV9) — 8.5/10 [high]
5. **AVR-RD-01** (LV) — 8.3/10 [high]

### Mucolipidosis type IV (ORPHA:578)
**Gene:** MCOLN1 | **Mechanism:** loss_of_function | **CDS:** 1740 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, retina

**Mechanism evidence:** MCOLN1 encodes a lysosomal MEMBRANE CHANNEL (TRP family) not a soluble lysosomal enzyme. Cross-correction via M6P receptor uptake (the mechanism of Libmeldy/ARSA) is physically impossible for a membrane-anchored protein. Every target neuron must individually receive the vector. AAV-based CNS delivery is the appropriate strategy; HSC/LV programs are not transferable precedents for this protein class. Source: OMIM MCOLN1 gene entry (https://omim.org/entry/605248)

1. **Skysona** (LV) — 8.3/10 [high]
2. **Libmeldy** (LV) — 8.2/10 [high]
3. **ABO-101** (AAV9) — 7.5/10 [high]
4. **RGX-121** (AAV9) — 7.5/10 [high]
5. **AVR-RD-01** (LV) — 7.3/10 [medium]

### Mucopolysaccharidosis type I (ORPHA:579)
**Gene:** IDUA | **Mechanism:** loss_of_function | **CDS:** 1962 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, liver

**Mechanism evidence:** IDUA enzyme deficiency supports replacement and cross-correction biology Source: OMIM MPS I 252800 (https://omim.org/entry/252800)

1. **Libmeldy** (LV) — 9.5/10 [high]
2. **ST-920** (AAV2/6) — 8.9/10 [high]
3. **ABO-101** (AAV9) — 8.8/10 [high]
4. **RGX-121** (AAV9) — 8.8/10 [high]
5. **Hemgenix** (AAV5) — 8.6/10 [high]

### Mucopolysaccharidosis type II (ORPHA:580)
**Gene:** IDS | **Mechanism:** loss_of_function | **CDS:** 1650 bp | **Inheritance:** X-linked recessive | **Tissues:** CNS, liver

**Mechanism evidence:** IDS enzyme deficiency supports replacement and cross-correction biology Source: OMIM IDS gene entry (https://omim.org/entry/300823)

1. **Libmeldy** (LV) — 9.3/10 [high]
2. **ST-920** (AAV2/6) — 9.0/10 [high]
3. **RGX-121** (AAV9) — 8.9/10 [high]
4. **Hemgenix** (AAV5) — 8.8/10 [high]
5. **Roctavian** (AAV5) — 8.8/10 [high]

### Mucopolysaccharidosis type IIIA (Sanfilippo A) (ORPHA:79269)
**Gene:** SGSH | **Mechanism:** loss_of_function | **CDS:** 1674 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

**Mechanism evidence:** SGSH enzyme deficiency supports replacement logic but CNS delivery is central for Sanfilippo A Source: OMIM SGSH gene entry (https://omim.org/entry/605270)

1. **Libmeldy** (LV) — 9.2/10 [high]
2. **ABO-101** (AAV9) — 8.5/10 [high]
3. **RGX-121** (AAV9) — 8.5/10 [high]
4. **AVR-RD-01** (LV) — 8.3/10 [high]
5. **Hemgenix** (AAV5) — 7.9/10 [high]

### Ornithine transcarbamylase deficiency (ORPHA:664)
**Gene:** OTC | **Mechanism:** loss_of_function | **CDS:** 1065 bp | **Inheritance:** X-linked recessive | **Tissues:** liver, CNS

**Mechanism evidence:** OTC deficiency is a liver metabolic enzyme loss compatible with hepatocyte gene addition Source: OMIM OTC gene entry (https://omim.org/entry/300461)

1. **BMN 307** (AAV5) — 8.1/10 [high]
2. **DTX301** (AAV8) — 7.7/10 [high]
3. **Hemgenix** (AAV5) — 7.2/10 [medium]
4. **Roctavian** (AAV5) — 7.2/10 [medium]
5. **OAV101-IT** (AAV9) — 7.0/10 [medium]

### Phenylketonuria (ORPHA:716)
**Gene:** PAH | **Mechanism:** loss_of_function | **CDS:** 1353 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, CNS

**Mechanism evidence:** PAH deficiency is a liver enzyme loss compatible with hepatocyte gene addition Source: OMIM PAH gene entry (https://omim.org/entry/612349)

1. **BMN 307** (AAV5) — 8.0/10 [high]
2. **OAV101-IT** (AAV9) — 7.7/10 [high]
3. **Zolgensma** (AAV9) — 7.7/10 [high]
4. **Hemgenix** (AAV5) — 7.5/10 [high]
5. **Roctavian** (AAV5) — 7.5/10 [high]

### Pompe disease (ORPHA:365)
**Gene:** GAA | **Mechanism:** loss_of_function | **CDS:** 2856 bp | **Inheritance:** Autosomal recessive | **Tissues:** muscle, heart

**Mechanism evidence:** GAA deficiency supports replacement logic but skeletal and cardiac delivery needs broad tissue correction Source: OMIM GAA gene entry (https://omim.org/entry/606800)

1. **Libmeldy** (LV) — 8.4/10 [high]
2. **ABO-101** (AAV9) — 8.0/10 [high]
3. **AVR-RD-01** (LV) — 8.0/10 [high]
4. **RGX-121** (AAV9) — 8.0/10 [high]
5. **ST-920** (AAV2/6) — 7.9/10 [high]

### Vitamin B12-unresponsive methylmalonic acidemia (ORPHA:27)
**Gene:** MMUT | **Mechanism:** loss_of_function | **CDS:** 2250 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, CNS

**Mechanism evidence:** MUT is a nuclear-encoded mitochondrial matrix enzyme. Nuclear AAV delivery is theoretically feasible but the N-terminal mitochondrial targeting sequence (MTS) must be intact in the therapeutic construct for correct post-translational import into the matrix. MTS functionality and import efficiency must be validated experimentally before vector precedent scores can be applied. Liver-directed AAV programs in development (e.g. NCT03721861) confirm the approach is viable but disease-specific construct validation is required. Source: OMIM MUT gene entry (https://omim.org/entry/609058)

1. **BMN 307** (AAV5) — 7.7/10 [high]
2. **DTX301** (AAV8) — 7.1/10 [medium]
3. **Libmeldy** (LV) — 6.7/10 [medium]
4. **OAV101-IT** (AAV9) — 6.7/10 [medium]
5. **Zolgensma** (AAV9) — 6.7/10 [medium]

### Wiskott-Aldrich syndrome (ORPHA:906)
**Gene:** WAS | **Mechanism:** loss_of_function | **CDS:** 1506 bp | **Inheritance:** X-linked recessive | **Tissues:** hematopoietic

**Mechanism evidence:** WAS loss of function is compatible with autologous hematopoietic stem-cell gene addition Source: OMIM WAS gene entry (https://omim.org/entry/300392)

1. **Strimvelis** (LV) — 8.0/10 [high]
2. **Skysona** (LV) — 7.0/10 [medium]
3. **Libmeldy** (LV) — 6.8/10 [medium]
4. **AVR-RD-01** (LV) — 6.7/10 [medium]
5. **BMN 307** (AAV5) — 6.0/10 [medium]

### X-linked adrenoleukodystrophy (ORPHA:43)
**Gene:** ABCD1 | **Mechanism:** loss_of_function | **CDS:** 2235 bp | **Inheritance:** X-linked recessive | **Tissues:** CNS

**Mechanism evidence:** ABCD1 deficiency supports replacement logic but cerebral inflammatory disease relies on hematopoietic and CNS disease biology Source: OMIM ABCD1 gene entry (https://omim.org/entry/300371)

1. **Skysona** (LV) — 8.2/10 [high]
2. **Libmeldy** (LV) — 7.6/10 [high]
3. **RGX-121** (AAV9) — 7.2/10 [medium]
4. **AVR-RD-01** (LV) — 7.0/10 [medium]
5. **ABO-101** (AAV9) — 6.9/10 [medium]

### X-linked myotubular myopathy (ORPHA:596)
**Gene:** MTM1 | **Mechanism:** loss_of_function | **CDS:** 1878 bp | **Inheritance:** X-linked recessive | **Tissues:** muscle

**Mechanism evidence:** MTM1 loss of function is compatible with muscle-directed gene addition but dose toxicity must be reviewed Source: OMIM MTM1 gene entry (https://omim.org/entry/300415)

1. **AT132** (AAV8) — 7.7/10 [high]
2. **SRP-9001** (AAV9) — 7.3/10 [medium]
3. **OAV101-IT** (AAV9) — 7.1/10 [medium]
4. **Zolgensma** (AAV9) — 7.1/10 [medium]
5. **Strimvelis** (LV) — 6.8/10 [medium]

### X-linked retinoschisis (ORPHA:792)
**Gene:** RS1 | **Mechanism:** loss_of_function | **CDS:** 672 bp | **Inheritance:** X-linked recessive | **Tissues:** retina

**Mechanism evidence:** RS1 deficiency supports retinal gene addition if target retinal structure remains treatable Source: OMIM RS1 gene entry (https://omim.org/entry/300839)

1. **Luxturna** (AAV2) — 7.9/10 [high]
2. **CPCB-RPE1** (AAV8) — 7.7/10 [high]
3. **Hemgenix** (AAV5) — 7.7/10 [high]
4. **Roctavian** (AAV5) — 7.7/10 [high]
5. **Libmeldy** (LV) — 7.5/10 [high]

### Rett syndrome (ORPHA:778)
**Gene:** MECP2 | **Mechanism:** haploinsufficiency | **CDS:** 1461 bp | **Inheritance:** X-linked dominant | **Tissues:** CNS

**Mechanism evidence:** Amir RE et al. (1999 Nat Genet PMID 10508514) identified MECP2 as the causal gene; Van Esch H et al. (2005 Am J Hum Genet PMID 16080119) showed MECP2 duplication causes a separate severe disease — any AAV-MECP2 construct must use a regulated or low-expression promoter to stay within the narrow therapeutic dose window Source: Amir RE et al. 1999 Nat Genet PMID 10508514; Van Esch H et al. 2005 Am J Hum Genet PMID 16080119 (https://pubmed.ncbi.nlm.nih.gov/10508514/)

1. **Skysona** (LV) — 7.4/10 [medium]
2. **Libmeldy** (LV) — 7.3/10 [medium]
3. **OAV101-IT** (AAV9) — 7.3/10 [medium]
4. **Zolgensma** (AAV9) — 7.3/10 [medium]
5. **Strimvelis** (LV) — 7.2/10 [medium]

### Fragile X syndrome (ORPHA:908)
**Gene:** FMR1 | **Mechanism:** repeat_expansion_silencing | **CDS:** 1899 bp | **Inheritance:** X-linked dominant | **Tissues:** CNS

**Mechanism evidence:** Liu XS et al. (2018 Cell PMID 29456084) demonstrated methylation-dependent silencing of the FMR1 locus by the CGG repeat; FMR1 cDNA addition (lacking the expanded repeat-containing UTR) bypasses the silenced endogenous allele and is not subject to re-silencing — same logic as FXN in Friedreich ataxia Source: Liu XS et al. 2018 Cell PMID 29456084 (https://pubmed.ncbi.nlm.nih.gov/29456084/)

1. **Skysona** (LV) — 7.0/10 [medium]
2. **Libmeldy** (LV) — 6.8/10 [medium]
3. **OAV101-IT** (AAV9) — 6.8/10 [medium]
4. **Zolgensma** (AAV9) — 6.8/10 [medium]
5. **Strimvelis** (LV) — 6.7/10 [medium]

### CHARGE syndrome (ORPHA:138)
**Gene:** CHD7 | **Mechanism:** haploinsufficiency | **CDS:** 7950 bp | **Inheritance:** Autosomal dominant | **Tissues:** CNS, heart, eye

**Mechanism evidence:** Vissers et al. (2004 Nat Genet PMID 15300250) identified de novo CHD7 mutations and deletions confirming haploinsufficiency as the pathogenic mechanism; conditional because CHD7 CDS approaches LV capacity limits and cell-level transgene dosage must be carefully controlled Source: Vissers et al. 2004 Nat Genet PMID 15300250 (https://pubmed.ncbi.nlm.nih.gov/15300250/)

1. **Libmeldy** (LV) — 5.9/10 [medium]
2. **Skysona** (LV) — 5.9/10 [medium]
3. **Strimvelis** (LV) — 5.8/10 [medium]
4. **AVR-RD-01** (LV) — 5.1/10 [medium]

### Neurofibromatosis type 1 (ORPHA:636)
**Gene:** NF1 | **Mechanism:** haploinsufficiency | **CDS:** 8451 bp | **Inheritance:** Autosomal dominant | **Tissues:** CNS, skin, peripheral nerve

**Mechanism evidence:** Serra et al. (1997 Am J Hum Genet PMID 9326316) confirmed biallelic NF1 inactivation in neurofibromas by LOH analysis demonstrating the two-hit mechanism; gene addition is conditional because somatic second hits in independent cells cannot be globally prevented by a single-dose systemic vector Source: Serra et al. 1997 Am J Hum Genet PMID 9326316 (https://pubmed.ncbi.nlm.nih.gov/9326316/)

No single-vector precedent survived the packaging hard gate. For this disease, the likely development route requires an oversized-cargo strategy such as micro-gene design, dual-vector delivery, ex vivo/lentiviral delivery if tissue-appropriate, or non-viral/editing approaches outside the current v0.1 catalog.

### Friedreich ataxia (ORPHA:95)
**Gene:** FXN | **Mechanism:** repeat_expansion_silencing | **CDS:** 633 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, heart

**Mechanism evidence:** Campuzano et al. (1996 Science PMID 8596916) identified the intronic GAA expansion; Al-Mahdawi et al. (2008 Hum Mol Genet PMID 18045775) characterised the heterochromatin mechanism; FXN cDNA gene addition is actively pursued clinically because the normal frataxin protein sequence is preserved Source: Campuzano et al. 1996 Science PMID 8596916; Al-Mahdawi et al. 2008 Hum Mol Genet PMID 18045775 (https://pubmed.ncbi.nlm.nih.gov/8596916/)

1. **OAV101-IT** (AAV9) — 7.9/10 [high]
2. **Zolgensma** (AAV9) — 7.9/10 [high]
3. **SRP-9001** (AAV9) — 7.0/10 [medium]
4. **BMN 307** (AAV5) — 7.0/10 [medium]
5. **Libmeldy** (LV) — 7.0/10 [medium]

### Tuberous sclerosis complex (ORPHA:805)
**Gene:** TSC1 | **Mechanism:** haploinsufficiency | **CDS:** 3495 bp | **Inheritance:** Autosomal dominant | **Tissues:** CNS, kidney, skin

**Mechanism evidence:** Henske et al. (1995 Genes Chromosomes Cancer PMID 7547639) demonstrated LOH at the TSC2 locus in angiomyolipomas confirming two-hit tumour suppressor mechanism; gene addition is conditional because systemic delivery cannot prevent the many independent somatic second-hit events that initiate individual hamartomas Source: Henske et al. 1995 Genes Chromosomes Cancer PMID 7547639 (https://pubmed.ncbi.nlm.nih.gov/7547639/)

1. **Libmeldy** (LV) — 6.4/10 [medium]
2. **OAV101-IT** (AAV9) — 6.4/10 [medium]
3. **Skysona** (LV) — 6.4/10 [medium]
4. **Zolgensma** (AAV9) — 6.4/10 [medium]
5. **Strimvelis** (LV) — 6.3/10 [medium]

### Cystic fibrosis (ORPHA:586)
**Gene:** CFTR | **Mechanism:** loss_of_function | **CDS:** 4443 bp | **Inheritance:** Autosomal recessive | **Tissues:** lung, pancreas, liver

**Mechanism evidence:** CFTR LOF supports gene addition logic; lung delivery and transient episomal expression in cycling airway epithelium are the main challenges Source: OMIM CFTR 219700 (https://omim.org/entry/219700)

1. **Skysona** (LV) — 6.7/10 [medium]
2. **Hemgenix** (AAV5) — 6.5/10 [medium]
3. **Roctavian** (AAV5) — 6.5/10 [medium]
4. **BMN 307** (AAV5) — 6.5/10 [medium]
5. **Libmeldy** (LV) — 6.3/10 [medium]

### Canavan disease (ORPHA:141)
**Gene:** ASPA | **Mechanism:** loss_of_function | **CDS:** 942 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

**Mechanism evidence:** ASPA LOF supports CNS-directed gene addition; clinical AAV trials ongoing Source: OMIM ASPA 271900 (https://omim.org/entry/271900)

1. **Libmeldy** (LV) — 8.1/10 [high]
2. **Skysona** (LV) — 8.0/10 [high]
3. **ABO-101** (AAV9) — 7.7/10 [high]
4. **OAV101-IT** (AAV9) — 7.7/10 [high]
5. **RGX-121** (AAV9) — 7.7/10 [high]

### Biotinidase deficiency (ORPHA:79241)
**Gene:** BTD | **Mechanism:** loss_of_function | **CDS:** 1632 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, multisystem

**Mechanism evidence:** BTD LOF is a metabolic enzyme deficiency compatible with liver-directed gene addition Source: OMIM BTD 253260 (https://omim.org/entry/253260)

1. **Libmeldy** (LV) — 8.3/10 [high]
2. **Hemgenix** (AAV5) — 7.7/10 [high]
3. **Roctavian** (AAV5) — 7.7/10 [high]
4. **Skysona** (LV) — 7.7/10 [high]
5. **ABO-101** (AAV9) — 7.6/10 [high]

### Tay-Sachs disease (ORPHA:845)
**Gene:** HEXA | **Mechanism:** loss_of_function | **CDS:** 1590 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

**Mechanism evidence:** HEXA LOF supports gene addition; CNS delivery and heterodimer assembly with HEXB subunit are key considerations Source: OMIM HEXA 272800 (https://omim.org/entry/272800)

1. **Libmeldy** (LV) — 8.5/10 [high]
2. **ABO-101** (AAV9) — 7.8/10 [high]
3. **RGX-121** (AAV9) — 7.8/10 [high]
4. **Hemgenix** (AAV5) — 7.7/10 [high]
5. **Roctavian** (AAV5) — 7.7/10 [high]

### Wilson disease (ORPHA:905)
**Gene:** ATP7B | **Mechanism:** loss_of_function | **CDS:** 4398 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, CNS

**Mechanism evidence:** ATP7B LOF supports liver-directed gene addition; large CDS (~4.3 kb) fits within AAV capacity Source: OMIM ATP7B 277900 (https://omim.org/entry/277900)

1. **Skysona** (LV) — 7.3/10 [medium]
2. **Libmeldy** (LV) — 7.0/10 [medium]
3. **Hemgenix** (AAV5) — 6.6/10 [medium]
4. **Roctavian** (AAV5) — 6.6/10 [medium]
5. **BMN 307** (AAV5) — 6.5/10 [medium]

### Nephropathic cystinosis (ORPHA:213)
**Gene:** CTNS | **Mechanism:** loss_of_function | **CDS:** 1104 bp | **Inheritance:** Autosomal recessive | **Tissues:** kidney, multisystem

**Mechanism evidence:** CTNS encodes a lysosomal membrane transporter; cross-correction via M6P uptake is not applicable — per-cell delivery needed in target tissues Source: OMIM CTNS 219800 (https://omim.org/entry/219800)

1. **Libmeldy** (LV) — 6.6/10 [medium]
2. **AVR-RD-01** (LV) — 6.2/10 [medium]
3. **ST-920** (AAV2/6) — 6.0/10 [medium]
4. **Skysona** (LV) — 6.0/10 [medium]
5. **ABO-101** (AAV9) — 5.9/10 [medium]

### Chronic neurovisceral acid sphingomyelinase deficiency (ORPHA:618891)
**Gene:** SMPD1 | **Mechanism:** loss_of_function | **CDS:** 1890 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, spleen, lung, CNS

**Mechanism evidence:** SMPD1 is a secreted lysosomal enzyme; cross-correction may be feasible for visceral disease but CNS involvement complicates single-compartment delivery Source: OMIM SMPD1 607616 (https://omim.org/entry/607616)

1. **Libmeldy** (LV) — 8.8/10 [high]
2. **Hemgenix** (AAV5) — 8.4/10 [high]
3. **Roctavian** (AAV5) — 8.4/10 [high]
4. **ST-920** (AAV2/6) — 8.1/10 [high]
5. **ABO-101** (AAV9) — 8.1/10 [high]

### Niemann-Pick disease type C (ORPHA:646)
**Gene:** NPC1 | **Mechanism:** loss_of_function | **CDS:** 3837 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, liver

**Mechanism evidence:** NPC1 is a large (~1.3 kb) lysosomal membrane protein; not secretable; CNS delivery is the primary challenge Source: OMIM NPC1 257220 (https://omim.org/entry/257220)

1. **Libmeldy** (LV) — 8.1/10 [high]
2. **ST-920** (AAV2/6) — 7.4/10 [medium]
3. **Skysona** (LV) — 7.4/10 [medium]
4. **ABO-101** (AAV9) — 7.3/10 [medium]
5. **RGX-121** (AAV9) — 7.3/10 [medium]

### Zellweger syndrome (ORPHA:912)
**Gene:** PEX1 | **Mechanism:** loss_of_function | **CDS:** 3852 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, liver, kidney

**Mechanism evidence:** PEX1 LOF supports gene addition but broad multisystem disease and neonatal severity limit treatment window Source: OMIM PEX1 214100 (https://omim.org/entry/214100)

1. **Skysona** (LV) — 7.6/10 [high]
2. **Libmeldy** (LV) — 7.3/10 [medium]
3. **Hemgenix** (AAV5) — 6.4/10 [medium]
4. **Roctavian** (AAV5) — 6.4/10 [medium]
5. **BMN 307** (AAV5) — 6.4/10 [medium]

### Primary hyperoxaluria type 1 (ORPHA:93598)
**Gene:** AGXT | **Mechanism:** loss_of_function | **CDS:** 1179 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, kidney

**Mechanism evidence:** AGXT LOF supports liver-directed gene addition; peroxisomal targeting signal must be intact in the therapeutic construct Source: OMIM AGXT 259900 (https://omim.org/entry/259900)

1. **BMN 307** (AAV5) — 7.3/10 [medium]
2. **Libmeldy** (LV) — 6.9/10 [medium]
3. **Hemgenix** (AAV5) — 6.9/10 [medium]
4. **Roctavian** (AAV5) — 6.9/10 [medium]
5. **Skysona** (LV) — 6.8/10 [medium]

### Usher syndrome type 1B (ORPHA:886)
**Gene:** MYO7A | **Mechanism:** loss_of_function | **CDS:** 6648 bp | **Inheritance:** Autosomal recessive | **Tissues:** retina, cochlea

**Mechanism evidence:** MYO7A LOF supports gene addition logic but oversized CDS requires dual-AAV or lentiviral strategies for retinal and cochlear delivery Source: OMIM MYO7A 276900 (https://omim.org/entry/276900)

1. **Strimvelis** (LV) — 6.5/10 [medium]
2. **Libmeldy** (LV) — 6.0/10 [medium]
3. **Skysona** (LV) — 5.9/10 [medium]
4. **AVR-RD-01** (LV) — 5.6/10 [medium]
