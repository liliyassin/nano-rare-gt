# NanoGT Results: 40-Disease GT Precedent Matching Cohort

**Algorithm:** 14-dimension heuristic scoring (v2): packaging fit, tissue tropism, protein class, pathway similarity, mechanism/modality compatibility, inheritance compatibility, approval precedent, vector immunogenicity, therapeutic window, cross-correction, immune privilege, promoter availability, route-of-administration feasibility, and organelle targeting feasibility. Raw max = 21; composite normalised to /10.

**Interpretation:** The framework ranks which existing clinical gene-therapy program is the closest development precedent for the query disease. It does not claim the top precedent is directly reusable without disease-specific validation, vector engineering, toxicology, and regulatory review.

## Summary Table

| Cohort role | Disease | ORPHA | Gene | Mechanism | Gene-addition fit | CDS (bp) | #1 Precedent | Vector | Score | Confidence |
|-------------|---------|-------|------|-----------|-------------------|----------|--------------|--------|-------|------------|
| positive_control | Hemophilia B | ORPHA:306 | F9 | loss_of_function | compatible | 1383 | Hemgenix | AAV5 | 9.9/10 | high |
| benchmark_with_known_gt_precedent | Leber congenital amaurosis | ORPHA:65 | RPE65 | loss_of_function | compatible | 1599 | CPCB-RPE1 | AAV8 | 7.6/10 | high |
| benchmark_with_known_gt_precedent | Severe combined immunodeficiency due to adenosine deaminase deficiency | ORPHA:277 | ADA | loss_of_function | compatible | 1092 | Strimvelis | LV | 8.1/10 | high |
| positive_control | Spinal Muscular Atrophy | ORPHA:70 | SMN1 | loss_of_function | compatible | 891 | OAV101-IT | AAV9 | 8.3/10 | high |
| oversized_cargo_stress_test | Duchenne muscular dystrophy | ORPHA:98896 | DMD | loss_of_function_oversized | conditional | 11055 | SRP-9001 | AAV9 | 7.6/10 | high |
| mitochondrial_stress_test | Leber hereditary optic neuropathy | ORPHA:104 | MT-ND4 | mitochondrial_loss_of_function | uncertain | 1377 | CPCB-RPE1 | AAV8 | 6.4/10 | medium |
| pilot_cohort | Achromatopsia | ORPHA:49382 | CNGB3 | loss_of_function | compatible | 2427 | CPCB-RPE1 | AAV8 | 7.5/10 | medium |
| pilot_cohort | Alpha-mannosidosis | ORPHA:61 | MAN2B1 | loss_of_function | compatible | 3033 | Libmeldy | LV | 8.8/10 | high |
| pilot_cohort | Choroideremia | ORPHA:180 | CHM | loss_of_function | compatible | 1962 | Luxturna | AAV2 | 8.0/10 | high |
| pilot_cohort | Crigler-Najjar syndrome type I | ORPHA:1060 | UGT1A1 | loss_of_function | compatible | 1596 | Hemgenix | AAV5 | 7.2/10 | medium |
| pilot_cohort | Fabry disease | ORPHA:324 | GLA | loss_of_function | compatible | 1290 | Libmeldy | LV | 8.9/10 | high |
| pilot_cohort | Gaucher disease | ORPHA:355 | GBA | loss_of_function | conditional | 1491 | Libmeldy | LV | 9.0/10 | high |
| pilot_cohort | Glycogen storage disease type Ia | ORPHA:79258 | G6PC | loss_of_function | compatible | 1071 | SRP-9001 | AAV9 | 7.8/10 | high |
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
| pilot_cohort | Salla disease | ORPHA:309 | SLC17A5 | loss_of_function | conditional | 1485 | Skysona | LV | 8.1/10 | high |
| pilot_cohort | Vitamin B12-unresponsive methylmalonic acidemia | ORPHA:27 | MUT | loss_of_function | conditional | 2250 | BMN 307 | AAV5 | 7.7/10 | high |
| pilot_cohort | Wiskott-Aldrich syndrome | ORPHA:906 | WAS | loss_of_function | compatible | 1506 | Strimvelis | LV | 8.0/10 | high |
| pilot_cohort | X-linked adrenoleukodystrophy | ORPHA:43 | ABCD1 | loss_of_function | conditional | 2235 | Skysona | LV | 8.2/10 | high |
| pilot_cohort | X-linked myotubular myopathy | ORPHA:596 | MTM1 | loss_of_function | compatible | 1878 | AT132 | AAV8 | 7.7/10 | high |
| pilot_cohort | X-linked retinoschisis | ORPHA:792 | RS1 | loss_of_function | compatible | 672 | Luxturna | AAV2 | 7.9/10 | high |
| non_lof_haploinsufficiency | Rett syndrome | ORPHA:778 | MECP2 | haploinsufficiency | conditional | 1461 | Skysona | LV | 7.4/10 | medium |
| non_lof_haploinsufficiency | Dravet syndrome | ORPHA:1306 | SCN1A | haploinsufficiency | conditional | 6027 | Skysona | LV | 7.1/10 | medium |
| non_lof_repeat_expansion | Fragile X syndrome | ORPHA:908 | FMR1 | repeat_expansion_silencing | conditional | 1899 | Skysona | LV | 7.0/10 | medium |
| non_lof_imprinting | Angelman syndrome | ORPHA:72 | UBE3A | genomic_imprinting | conditional | 2598 | OAV101-IT | AAV9 | 7.1/10 | medium |
| non_lof_haploinsufficiency | CDKL5 deficiency disorder | ORPHA:163934 | CDKL5 | haploinsufficiency | conditional | 3093 | Skysona | LV | 7.2/10 | medium |
| non_lof_haploinsufficiency | GATA2 deficiency | ORPHA:247770 | GATA2 | haploinsufficiency | conditional | 1443 | Strimvelis | LV | 7.6/10 | high |
| non_lof_haploinsufficiency | CHARGE syndrome | ORPHA:138 | CHD7 | haploinsufficiency | conditional | 7950 | Libmeldy | LV | 5.9/10 | medium |
| non_lof_haploinsufficiency | Neurofibromatosis type 1 | ORPHA:636 | NF1 | haploinsufficiency | conditional | 8451 | — | — | — | packaging_hard_fail |
| non_lof_repeat_expansion | Friedreich ataxia | ORPHA:95 | FXN | repeat_expansion_silencing | conditional | 633 | OAV101-IT | AAV9 | 7.9/10 | high |
| non_lof_haploinsufficiency | Tuberous sclerosis complex | ORPHA:805 | TSC2 | haploinsufficiency | conditional | 5694 | Libmeldy | LV | 6.1/10 | medium |

---

## Disease Sections

### Hemophilia B (ORPHA:306)
**Gene:** F9 | **Mechanism:** loss_of_function | **CDS:** 1383 bp | **Inheritance:** X-linked recessive | **Tissues:** liver

**Mechanism evidence:** Deficiency of coagulation factor IX is the therapeutic deficit; liver-directed F9 expression is an approved gene-addition precedent Source: OMIM Hemophilia B 306900 (https://omim.org/entry/306900)

1. **Hemgenix** (AAV5) — 9.9/10 [high]
2. **Roctavian** (AAV5) — 9.9/10 [high]
3. **SPK-8011** (AAVrh10) — 9.6/10 [high]
4. **DTX201** (AAV8) — 9.2/10 [high]
5. **ST-920** (AAV2/6) — 8.7/10 [high]

### Leber congenital amaurosis (ORPHA:65)
**Gene:** RPE65 | **Mechanism:** loss_of_function | **CDS:** 1599 bp | **Inheritance:** Autosomal recessive | **Tissues:** retina

**Mechanism evidence:** Biallelic RPE65 disease is treated by supplying functional RPE65 to retinal pigment epithelium Source: FDA Luxturna product information (https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/luxturna)

1. **CPCB-RPE1** (AAV8) — 7.6/10 [high]
2. **Luxturna** (AAV2) — 7.3/10 [medium]
3. **Skysona** (LV) — 7.0/10 [medium]
4. **Libmeldy** (LV) — 6.7/10 [medium]
5. **Strimvelis** (LV) — 6.7/10 [medium]

### Severe combined immunodeficiency due to adenosine deaminase deficiency (ORPHA:277)
**Gene:** ADA | **Mechanism:** loss_of_function | **CDS:** 1092 bp | **Inheritance:** Autosomal recessive | **Tissues:** hematopoietic

**Mechanism evidence:** ADA-SCID is a deficiency disorder with approved ex vivo gene-addition precedent Source: OMIM ADA-SCID 102700 (https://omim.org/entry/102700)

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

### Crigler-Najjar syndrome type I (ORPHA:1060)
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
**Gene:** GBA | **Mechanism:** loss_of_function | **CDS:** 1491 bp | **Inheritance:** Autosomal recessive | **Tissues:** hematopoietic, liver, CNS

**Mechanism evidence:** GBA deficiency supports replacement logic but neuronopathic disease and tissue access can limit simple systemic correction Source: OMIM GBA gene entry (https://omim.org/entry/606463)

1. **Libmeldy** (LV) — 9.0/10 [high]
2. **AVR-RD-01** (LV) — 8.6/10 [high]
3. **ST-920** (AAV2/6) — 8.1/10 [high]
4. **ABO-101** (AAV9) — 8.1/10 [high]
5. **RGX-121** (AAV9) — 8.1/10 [high]

### Glycogen storage disease type Ia (ORPHA:79258)
**Gene:** G6PC | **Mechanism:** loss_of_function | **CDS:** 1071 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, kidney

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

### Salla disease (ORPHA:309)
**Gene:** SLC17A5 | **Mechanism:** loss_of_function | **CDS:** 1485 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

**Mechanism evidence:** SLC17A5 encodes sialin a lysosomal MEMBRANE TRANSPORTER for sialic acid efflux. Like MCOLN1 in ML-IV it is anchored in the lysosomal membrane and cannot be secreted or taken up via M6P receptor by neighbouring cells. HSC/LV cross-correction programs (Libmeldy) are not applicable as direct therapeutic precedents. Per-cell CNS delivery is required. Source: OMIM SLC17A5 gene entry (https://omim.org/entry/604322)

1. **Skysona** (LV) — 8.1/10 [high]
2. **Libmeldy** (LV) — 8.1/10 [high]
3. **ABO-101** (AAV9) — 7.3/10 [medium]
4. **RGX-121** (AAV9) — 7.3/10 [medium]
5. **AVR-RD-01** (LV) — 7.1/10 [medium]

### Vitamin B12-unresponsive methylmalonic acidemia (ORPHA:27)
**Gene:** MUT | **Mechanism:** loss_of_function | **CDS:** 2250 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, CNS

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

### Dravet syndrome (ORPHA:1306)
**Gene:** SCN1A | **Mechanism:** haploinsufficiency | **CDS:** 6027 bp | **Inheritance:** Autosomal dominant | **Tissues:** CNS

**Mechanism evidence:** Claes L et al. (2003 Hum Mutat PMID 12754708) established de novo SCN1A haploinsufficiency as the primary mechanism; Colasante G et al. (2020 Mol Ther PMID 31607539) demonstrated that cell-type-specific SCN1A upregulation restores interneuron excitability; gene addition is conditional because ectopic expression in excitatory neurons would worsen seizures Source: Claes L et al. 2003 Hum Mutat PMID 12754708; Colasante G et al. 2020 Mol Ther PMID 31607539 (https://pubmed.ncbi.nlm.nih.gov/12754708/)

1. **Skysona** (LV) — 7.1/10 [medium]
2. **Libmeldy** (LV) — 6.6/10 [medium]
3. **Strimvelis** (LV) — 6.0/10 [medium]
4. **AVR-RD-01** (LV) — 5.8/10 [medium]

### Fragile X syndrome (ORPHA:908)
**Gene:** FMR1 | **Mechanism:** repeat_expansion_silencing | **CDS:** 1899 bp | **Inheritance:** X-linked dominant | **Tissues:** CNS

**Mechanism evidence:** Liu XS et al. (2018 Cell PMID 29456084) demonstrated methylation-dependent silencing of the FMR1 locus by the CGG repeat; FMR1 cDNA addition (lacking the expanded repeat-containing UTR) bypasses the silenced endogenous allele and is not subject to re-silencing — same logic as FXN in Friedreich ataxia Source: Liu XS et al. 2018 Cell PMID 29456084 (https://pubmed.ncbi.nlm.nih.gov/29456084/)

1. **Skysona** (LV) — 7.0/10 [medium]
2. **Libmeldy** (LV) — 6.8/10 [medium]
3. **OAV101-IT** (AAV9) — 6.8/10 [medium]
4. **Zolgensma** (AAV9) — 6.8/10 [medium]
5. **Strimvelis** (LV) — 6.7/10 [medium]

### Angelman syndrome (ORPHA:72)
**Gene:** UBE3A | **Mechanism:** genomic_imprinting | **CDS:** 2598 bp | **Inheritance:** Autosomal dominant | **Tissues:** CNS

**Mechanism evidence:** Mabb AM et al. (2011 Trends Neurosci PMID 21592595) described the dual-allele loss mechanism — maternal deletion plus neuronal antisense silencing of the paternal allele; an AAV transgene under a neuronal promoter restores UBE3A expression independently of both silenced endogenous alleles Source: Mabb AM et al. 2011 Trends Neurosci PMID 21592595 (https://pubmed.ncbi.nlm.nih.gov/21592595/)

1. **OAV101-IT** (AAV9) — 7.1/10 [medium]
2. **Zolgensma** (AAV9) — 7.1/10 [medium]
3. **BMN 307** (AAV5) — 6.9/10 [medium]
4. **Libmeldy** (LV) — 6.9/10 [medium]
5. **Skysona** (LV) — 6.9/10 [medium]

### CDKL5 deficiency disorder (ORPHA:163934)
**Gene:** CDKL5 | **Mechanism:** haploinsufficiency | **CDS:** 3093 bp | **Inheritance:** X-linked dominant | **Tissues:** CNS

**Mechanism evidence:** Van Bergen NJ et al. (2022 Biochem Soc Trans PMID 35997111) reviewed CDKL5 molecular pathogenicity and the rationale for AAV9-CDKL5 gene therapy; gene addition is conditional because CDKL5 exhibits dose- and isoform-dependent substrate specificity — expression must match endogenous neuronal levels Source: Van Bergen NJ et al. 2022 Biochem Soc Trans PMID 35997111 (https://pubmed.ncbi.nlm.nih.gov/35997111/)

1. **Skysona** (LV) — 7.2/10 [medium]
2. **Libmeldy** (LV) — 7.0/10 [medium]
3. **OAV101-IT** (AAV9) — 7.0/10 [medium]
4. **Zolgensma** (AAV9) — 7.0/10 [medium]
5. **Strimvelis** (LV) — 7.0/10 [medium]

### GATA2 deficiency (ORPHA:247770)
**Gene:** GATA2 | **Mechanism:** haploinsufficiency | **CDS:** 1443 bp | **Inheritance:** Autosomal dominant | **Tissues:** hematopoietic

**Mechanism evidence:** Spinner MA et al. (2014 Blood PMID 24227816) characterised the full clinical spectrum of GATA2 haploinsufficiency; gene addition is conditional via ex vivo HSC transduction because systemic in vivo delivery risks ectopic GATA2 expression in non-haematopoietic tissues where dosage must be precisely regulated Source: Spinner MA et al. 2014 Blood PMID 24227816 (https://pubmed.ncbi.nlm.nih.gov/24227816/)

1. **Strimvelis** (LV) — 7.6/10 [high]
2. **Libmeldy** (LV) — 6.4/10 [medium]
3. **Skysona** (LV) — 6.4/10 [medium]
4. **AVR-RD-01** (LV) — 6.1/10 [medium]
5. **BMN 307** (AAV5) — 5.6/10 [medium]

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
**Gene:** TSC2 | **Mechanism:** haploinsufficiency | **CDS:** 5694 bp | **Inheritance:** Autosomal dominant | **Tissues:** CNS, kidney, skin

**Mechanism evidence:** Henske et al. (1995 Genes Chromosomes Cancer PMID 7547639) demonstrated LOH at the TSC2 locus in angiomyolipomas confirming two-hit tumour suppressor mechanism; gene addition is conditional because systemic delivery cannot prevent the many independent somatic second-hit events that initiate individual hamartomas Source: Henske et al. 1995 Genes Chromosomes Cancer PMID 7547639 (https://pubmed.ncbi.nlm.nih.gov/7547639/)

1. **Libmeldy** (LV) — 6.1/10 [medium]
2. **Skysona** (LV) — 6.1/10 [medium]
3. **Strimvelis** (LV) — 6.0/10 [medium]
4. **AVR-RD-01** (LV) — 5.3/10 [medium]
