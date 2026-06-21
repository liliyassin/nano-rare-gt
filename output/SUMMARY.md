# NanoGT Results: 30-Disease GT Precedent Matching Cohort

**Algorithm:** 13-dimension heuristic scoring: packaging fit, tissue tropism, protein class, pathway similarity, mechanism/modality compatibility, inheritance compatibility, approval precedent, vector immunogenicity, therapeutic window, cross-correction, immune privilege, promoter availability, and route-of-administration feasibility. Raw max = 20; composite is normalised to /10.

**Interpretation:** The framework ranks which existing clinical gene-therapy program is the closest development precedent for the query disease. It does not claim the top precedent is directly reusable without disease-specific validation, vector engineering, toxicology, and regulatory review.

## Summary Table

| Cohort role | Disease | ORPHA | Gene | Mechanism | Gene-addition fit | CDS (bp) | #1 Precedent | Vector | Score | Confidence |
|-------------|---------|-------|------|-----------|-------------------|----------|--------------|--------|-------|------------|
| positive_control | Hemophilia B | ORPHA:306 | F9 | loss_of_function | compatible | 1383 | Hemgenix | AAV5 | 9.9/10 | high |
| benchmark_with_known_gt_precedent | Leber congenital amaurosis | ORPHA:65 | RPE65 | loss_of_function | compatible | 1599 | CPCB-RPE1 | AAV8 | 7.5/10 | high |
| benchmark_with_known_gt_precedent | Severe combined immunodeficiency due to adenosine deaminase deficiency | ORPHA:277 | ADA | loss_of_function | compatible | 1092 | Strimvelis | LV | 8.1/10 | high |
| positive_control | Spinal Muscular Atrophy | ORPHA:70 | SMN1 | loss_of_function | compatible | 891 | OAV101-IT | AAV9 | 8.2/10 | high |
| oversized_cargo_stress_test | Duchenne muscular dystrophy | ORPHA:98896 | DMD | loss_of_function_oversized | conditional | 11055 | SRP-9001 | AAV9 | 7.5/10 | high |
| mitochondrial_stress_test | Leber hereditary optic neuropathy | ORPHA:104 | MT-ND4 | mitochondrial_loss_of_function | uncertain | 1377 | CPCB-RPE1 | AAV8 | 6.8/10 | medium |
| pilot_cohort | Achromatopsia | ORPHA:49382 | CNGB3 | loss_of_function | compatible | 2427 | CPCB-RPE1 | AAV8 | 7.3/10 | medium |
| pilot_cohort | Alpha-mannosidosis | ORPHA:61 | MAN2B1 | loss_of_function | compatible | 3033 | Libmeldy | LV | 8.7/10 | high |
| pilot_cohort | Choroideremia | ORPHA:180 | CHM | loss_of_function | compatible | 1962 | Luxturna | AAV2 | 7.8/10 | high |
| pilot_cohort | Crigler-Najjar syndrome type I | ORPHA:1060 | UGT1A1 | loss_of_function | compatible | 1596 | Hemgenix | AAV5 | 7.1/10 | medium |
| pilot_cohort | Fabry disease | ORPHA:324 | GLA | loss_of_function | compatible | 1290 | Libmeldy | LV | 8.8/10 | high |
| pilot_cohort | Gaucher disease | ORPHA:355 | GBA | loss_of_function | conditional | 1491 | Libmeldy | LV | 8.9/10 | high |
| pilot_cohort | Glycogen storage disease type Ia | ORPHA:79258 | G6PC | loss_of_function | compatible | 1071 | SRP-9001 | AAV9 | 7.7/10 | high |
| pilot_cohort | Kohlschutter-Tonz syndrome | ORPHA:1946 | ROGDI | loss_of_function | conditional | 861 | OAV101-IT | AAV9 | 7.5/10 | high |
| pilot_cohort | Krabbe disease | ORPHA:487 | GALC | loss_of_function | conditional | 2055 | Libmeldy | LV | 8.9/10 | high |
| pilot_cohort | Maple syrup urine disease | ORPHA:511 | BCKDHA | loss_of_function | conditional | 1335 | BMN 307 | AAV5 | 8.1/10 | high |
| pilot_cohort | Metachromatic leukodystrophy | ORPHA:512 | ARSA | loss_of_function | compatible | 1521 | Libmeldy | LV | 9.2/10 | high |
| pilot_cohort | Mucolipidosis type IV | ORPHA:578 | MCOLN1 | loss_of_function | conditional | 1740 | Libmeldy | LV | 9.1/10 | high |
| pilot_cohort | Mucopolysaccharidosis type I | ORPHA:579 | IDUA | loss_of_function | compatible | 1962 | Libmeldy | LV | 9.4/10 | high |
| pilot_cohort | Mucopolysaccharidosis type II | ORPHA:580 | IDS | loss_of_function | compatible | 1650 | Libmeldy | LV | 9.3/10 | high |
| pilot_cohort | Mucopolysaccharidosis type IIIA (Sanfilippo A) | ORPHA:79269 | SGSH | loss_of_function | compatible | 1674 | Libmeldy | LV | 9.2/10 | high |
| pilot_cohort | Ornithine transcarbamylase deficiency | ORPHA:664 | OTC | loss_of_function | compatible | 1065 | BMN 307 | AAV5 | 8.2/10 | high |
| pilot_cohort | Phenylketonuria | ORPHA:716 | PAH | loss_of_function | compatible | 1353 | BMN 307 | AAV5 | 7.8/10 | high |
| pilot_cohort | Pompe disease | ORPHA:365 | GAA | loss_of_function | conditional | 2856 | Libmeldy | LV | 8.3/10 | high |
| pilot_cohort | Salla disease | ORPHA:309 | SLC17A5 | loss_of_function | conditional | 1485 | Libmeldy | LV | 8.8/10 | high |
| pilot_cohort | Vitamin B12-unresponsive methylmalonic acidemia | ORPHA:27 | MUT | loss_of_function | conditional | 2250 | BMN 307 | AAV5 | 7.8/10 | high |
| pilot_cohort | Wiskott-Aldrich syndrome | ORPHA:906 | WAS | loss_of_function | compatible | 1506 | Strimvelis | LV | 7.9/10 | high |
| pilot_cohort | X-linked adrenoleukodystrophy | ORPHA:43 | ABCD1 | loss_of_function | conditional | 2235 | Skysona | LV | 8.3/10 | high |
| pilot_cohort | X-linked myotubular myopathy | ORPHA:596 | MTM1 | loss_of_function | compatible | 1878 | AT132 | AAV8 | 7.5/10 | high |
| pilot_cohort | X-linked retinoschisis | ORPHA:792 | RS1 | loss_of_function | compatible | 672 | Luxturna | AAV2 | 7.8/10 | high |

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

1. **CPCB-RPE1** (AAV8) — 7.5/10 [high]
2. **Luxturna** (AAV2) — 7.2/10 [medium]
3. **Skysona** (LV) — 6.9/10 [medium]
4. **Libmeldy** (LV) — 6.5/10 [medium]
5. **Strimvelis** (LV) — 6.5/10 [medium]

### Severe combined immunodeficiency due to adenosine deaminase deficiency (ORPHA:277)
**Gene:** ADA | **Mechanism:** loss_of_function | **CDS:** 1092 bp | **Inheritance:** Autosomal recessive | **Tissues:** hematopoietic

**Mechanism evidence:** ADA-SCID is a deficiency disorder with approved ex vivo gene-addition precedent Source: OMIM ADA-SCID 102700 (https://omim.org/entry/102700)

1. **Strimvelis** (LV) — 8.1/10 [high]
2. **Libmeldy** (LV) — 6.8/10 [medium]
3. **Skysona** (LV) — 6.7/10 [medium]
4. **AVR-RD-01** (LV) — 6.4/10 [medium]
5. **BMN 307** (AAV5) — 6.2/10 [medium]

### Spinal Muscular Atrophy (ORPHA:70)
**Gene:** SMN1 | **Mechanism:** loss_of_function | **CDS:** 891 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, muscle

**Mechanism evidence:** FDA Zolgensma indication is SMA with biallelic SMN1 mutations; product supplies functional SMN transgene Source: FDA Zolgensma product page (https://www.fda.gov/vaccines-blood-biologics/zolgensma)

1. **OAV101-IT** (AAV9) — 8.2/10 [high]
2. **Zolgensma** (AAV9) — 8.2/10 [high]
3. **AT132** (AAV8) — 8.0/10 [high]
4. **SRP-9001** (AAV9) — 7.6/10 [high]
5. **BMN 307** (AAV5) — 7.3/10 [medium]

### Duchenne muscular dystrophy (ORPHA:98896)
**Gene:** DMD | **Mechanism:** loss_of_function_oversized | **CDS:** 11055 bp | **Inheritance:** X-linked recessive | **Tissues:** muscle, heart

**Mechanism evidence:** DMD supports replacement logic but requires micro-dystrophin or other engineered strategies because full-length DMD exceeds AAV capacity Source: Chamberlain et al. 2023 microdystrophin review (https://pubmed.ncbi.nlm.nih.gov/36990339/)

1. **SRP-9001** (AAV9) — 7.5/10 [high]

### Leber hereditary optic neuropathy (ORPHA:104)
**Gene:** MT-ND4 | **Mechanism:** mitochondrial_loss_of_function | **CDS:** 1377 bp | **Inheritance:** Mitochondrial inheritance | **Tissues:** retina, CNS

**Mechanism evidence:** Mitochondrial DNA disease is not ordinary nuclear gene addition; allotopic AAV approaches are specialized and disease-specific Source: OMIM MT-ND4 gene entry (https://omim.org/entry/516003)

1. **CPCB-RPE1** (AAV8) — 6.8/10 [medium]
2. **Skysona** (LV) — 6.7/10 [medium]
3. **Luxturna** (AAV2) — 6.4/10 [medium]
4. **Libmeldy** (LV) — 6.2/10 [medium]
5. **Hemgenix** (AAV5) — 5.9/10 [medium]

### Achromatopsia (ORPHA:49382)
**Gene:** CNGB3 | **Mechanism:** loss_of_function | **CDS:** 2427 bp | **Inheritance:** Autosomal recessive | **Tissues:** retina

**Mechanism evidence:** Biallelic CNGB3 loss is compatible with photoreceptor-directed gene addition if target cells remain viable Source: OMIM CNGB3 gene entry (https://omim.org/entry/605080)

1. **CPCB-RPE1** (AAV8) — 7.3/10 [medium]
2. **Luxturna** (AAV2) — 7.0/10 [medium]
3. **Skysona** (LV) — 6.5/10 [medium]
4. **Libmeldy** (LV) — 6.2/10 [medium]
5. **Strimvelis** (LV) — 6.2/10 [medium]

### Alpha-mannosidosis (ORPHA:61)
**Gene:** MAN2B1 | **Mechanism:** loss_of_function | **CDS:** 3033 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, liver

**Mechanism evidence:** Lysosomal enzyme deficiency supports gene addition and possible cross-correction logic Source: OMIM MAN2B1 gene entry (https://omim.org/entry/609458)

1. **Libmeldy** (LV) — 8.7/10 [high]
2. **ST-920** (AAV2/6) — 8.1/10 [high]
3. **ABO-101** (AAV9) — 8.0/10 [high]
4. **RGX-121** (AAV9) — 8.0/10 [high]
5. **Hemgenix** (AAV5) — 7.8/10 [high]

### Choroideremia (ORPHA:180)
**Gene:** CHM | **Mechanism:** loss_of_function | **CDS:** 1962 bp | **Inheritance:** X-linked recessive | **Tissues:** retina

**Mechanism evidence:** CHM loss of function is a retinal gene-addition target if viable retina remains Source: OMIM CHM gene entry (https://omim.org/entry/300390)

1. **Luxturna** (AAV2) — 7.8/10 [high]
2. **Strimvelis** (LV) — 7.2/10 [medium]
3. **CPCB-RPE1** (AAV8) — 7.2/10 [medium]
4. **GS010** (AAV2) — 6.9/10 [medium]
5. **Skysona** (LV) — 6.9/10 [medium]

### Crigler-Najjar syndrome type I (ORPHA:1060)
**Gene:** UGT1A1 | **Mechanism:** loss_of_function | **CDS:** 1596 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver

**Mechanism evidence:** UGT1A1 deficiency supports hepatocyte-directed gene addition Source: OMIM UGT1A1 gene entry (https://omim.org/entry/191740)

1. **Hemgenix** (AAV5) — 7.1/10 [medium]
2. **Roctavian** (AAV5) — 7.1/10 [medium]
3. **BMN 307** (AAV5) — 7.0/10 [medium]
4. **Skysona** (LV) — 7.0/10 [medium]
5. **SPK-8011** (AAVrh10) — 6.8/10 [medium]

### Fabry disease (ORPHA:324)
**Gene:** GLA | **Mechanism:** loss_of_function | **CDS:** 1290 bp | **Inheritance:** X-linked dominant | **Tissues:** liver, kidney, heart, CNS

**Mechanism evidence:** Fabry is caused by deficient GLA enzyme activity; secreted enzyme strategies can support systemic cross-correction Source: OMIM GLA gene entry (https://omim.org/entry/300644)

1. **Libmeldy** (LV) — 8.8/10 [high]
2. **ST-920** (AAV2/6) — 8.7/10 [high]
3. **RGX-121** (AAV9) — 8.6/10 [high]
4. **Hemgenix** (AAV5) — 8.4/10 [high]
5. **Roctavian** (AAV5) — 8.4/10 [high]

### Gaucher disease (ORPHA:355)
**Gene:** GBA | **Mechanism:** loss_of_function | **CDS:** 1491 bp | **Inheritance:** Autosomal recessive | **Tissues:** hematopoietic, liver, CNS

**Mechanism evidence:** GBA deficiency supports replacement logic but neuronopathic disease and tissue access can limit simple systemic correction Source: OMIM GBA gene entry (https://omim.org/entry/606463)

1. **Libmeldy** (LV) — 8.9/10 [high]
2. **AVR-RD-01** (LV) — 8.6/10 [high]
3. **ST-920** (AAV2/6) — 8.1/10 [high]
4. **ABO-101** (AAV9) — 8.0/10 [high]
5. **RGX-121** (AAV9) — 8.0/10 [high]

### Glycogen storage disease type Ia (ORPHA:79258)
**Gene:** G6PC | **Mechanism:** loss_of_function | **CDS:** 1071 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, kidney

**Mechanism evidence:** G6PC deficiency is a metabolic enzyme loss where liver-directed expression is a plausible gene-addition strategy Source: OMIM G6PC gene entry (https://omim.org/entry/613742)

1. **SRP-9001** (AAV9) — 7.7/10 [high]
2. **ST-920** (AAV2/6) — 7.7/10 [high]
3. **RGX-121** (AAV9) — 7.6/10 [high]
4. **Hemgenix** (AAV5) — 7.5/10 [medium]
5. **Roctavian** (AAV5) — 7.5/10 [medium]

### Kohlschutter-Tonz syndrome (ORPHA:1946)
**Gene:** ROGDI | **Mechanism:** loss_of_function | **CDS:** 861 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

**Mechanism evidence:** Published KTS variants in ROGDI are consistent with loss of function; gene addition is plausible but ROGDI is intracellular and disease biology is not fully resolved Source: Schossig et al. 2012 Mutations in ROGDI Cause Kohlschutter-Tonz Syndrome (https://pubmed.ncbi.nlm.nih.gov/22482807/)

1. **OAV101-IT** (AAV9) — 7.5/10 [high]
2. **Zolgensma** (AAV9) — 7.5/10 [high]
3. **BMN 307** (AAV5) — 7.3/10 [medium]
4. **Libmeldy** (LV) — 7.3/10 [medium]
5. **Strimvelis** (LV) — 7.2/10 [medium]

### Krabbe disease (ORPHA:487)
**Gene:** GALC | **Mechanism:** loss_of_function | **CDS:** 2055 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

**Mechanism evidence:** GALC deficiency supports replacement logic but CNS delivery and toxic metabolite biology require disease-specific validation Source: OMIM GALC gene entry (https://omim.org/entry/606890)

1. **Libmeldy** (LV) — 8.9/10 [high]
2. **Skysona** (LV) — 8.3/10 [high]
3. **ABO-101** (AAV9) — 8.2/10 [high]
4. **RGX-121** (AAV9) — 8.2/10 [high]
5. **AVR-RD-01** (LV) — 8.0/10 [high]

### Maple syrup urine disease (ORPHA:511)
**Gene:** BCKDHA | **Mechanism:** loss_of_function | **CDS:** 1335 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, CNS

**Mechanism evidence:** BCKDHA deficiency supports replacement logic but the multi-subunit enzyme complex and CNS metabolic crises make liver-only rescue uncertain Source: OMIM BCKDHA gene entry (https://omim.org/entry/608348)

1. **BMN 307** (AAV5) — 8.1/10 [high]
2. **Luxturna** (AAV2) — 7.3/10 [medium]
3. **OAV101-IT** (AAV9) — 7.0/10 [medium]
4. **Zolgensma** (AAV9) — 7.0/10 [medium]
5. **GS010** (AAV2) — 7.0/10 [medium]

### Metachromatic leukodystrophy (ORPHA:512)
**Gene:** ARSA | **Mechanism:** loss_of_function | **CDS:** 1521 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

**Mechanism evidence:** ARSA deficiency is compatible with gene addition and HSC-mediated enzyme delivery/cross-correction precedent Source: OMIM ARSA gene entry (https://omim.org/entry/607574)

1. **Libmeldy** (LV) — 9.2/10 [high]
2. **Skysona** (LV) — 8.6/10 [high]
3. **ABO-101** (AAV9) — 8.4/10 [high]
4. **RGX-121** (AAV9) — 8.4/10 [high]
5. **AVR-RD-01** (LV) — 8.2/10 [high]

### Mucolipidosis type IV (ORPHA:578)
**Gene:** MCOLN1 | **Mechanism:** loss_of_function | **CDS:** 1740 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, retina

**Mechanism evidence:** MCOLN1 loss supports gene addition but membrane-channel biology is cell-autonomous and not a strong cross-correction case Source: OMIM MCOLN1 gene entry (https://omim.org/entry/605248)

1. **Libmeldy** (LV) — 9.1/10 [high]
2. **Skysona** (LV) — 8.7/10 [high]
3. **ABO-101** (AAV9) — 8.3/10 [high]
4. **RGX-121** (AAV9) — 8.3/10 [high]
5. **AVR-RD-01** (LV) — 8.1/10 [high]

### Mucopolysaccharidosis type I (ORPHA:579)
**Gene:** IDUA | **Mechanism:** loss_of_function | **CDS:** 1962 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, liver

**Mechanism evidence:** IDUA enzyme deficiency supports replacement and cross-correction biology Source: OMIM MPS I 252800 (https://omim.org/entry/252800)

1. **Libmeldy** (LV) — 9.4/10 [high]
2. **ST-920** (AAV2/6) — 8.8/10 [high]
3. **ABO-101** (AAV9) — 8.7/10 [high]
4. **RGX-121** (AAV9) — 8.7/10 [high]
5. **Hemgenix** (AAV5) — 8.6/10 [high]

### Mucopolysaccharidosis type II (ORPHA:580)
**Gene:** IDS | **Mechanism:** loss_of_function | **CDS:** 1650 bp | **Inheritance:** X-linked recessive | **Tissues:** CNS, liver

**Mechanism evidence:** IDS enzyme deficiency supports replacement and cross-correction biology Source: OMIM IDS gene entry (https://omim.org/entry/300823)

1. **Libmeldy** (LV) — 9.3/10 [high]
2. **ST-920** (AAV2/6) — 8.9/10 [high]
3. **RGX-121** (AAV9) — 8.8/10 [high]
4. **Hemgenix** (AAV5) — 8.7/10 [high]
5. **Roctavian** (AAV5) — 8.7/10 [high]

### Mucopolysaccharidosis type IIIA (Sanfilippo A) (ORPHA:79269)
**Gene:** SGSH | **Mechanism:** loss_of_function | **CDS:** 1674 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

**Mechanism evidence:** SGSH enzyme deficiency supports replacement logic but CNS delivery is central for Sanfilippo A Source: OMIM SGSH gene entry (https://omim.org/entry/605270)

1. **Libmeldy** (LV) — 9.2/10 [high]
2. **ABO-101** (AAV9) — 8.4/10 [high]
3. **RGX-121** (AAV9) — 8.4/10 [high]
4. **AVR-RD-01** (LV) — 8.2/10 [high]
5. **Hemgenix** (AAV5) — 7.8/10 [high]

### Ornithine transcarbamylase deficiency (ORPHA:664)
**Gene:** OTC | **Mechanism:** loss_of_function | **CDS:** 1065 bp | **Inheritance:** X-linked recessive | **Tissues:** liver, CNS

**Mechanism evidence:** OTC deficiency is a liver metabolic enzyme loss compatible with hepatocyte gene addition Source: OMIM OTC gene entry (https://omim.org/entry/300461)

1. **BMN 307** (AAV5) — 8.2/10 [high]
2. **DTX301** (AAV8) — 7.8/10 [high]
3. **Hemgenix** (AAV5) — 7.3/10 [medium]
4. **Roctavian** (AAV5) — 7.3/10 [medium]
5. **OAV101-IT** (AAV9) — 7.2/10 [medium]

### Phenylketonuria (ORPHA:716)
**Gene:** PAH | **Mechanism:** loss_of_function | **CDS:** 1353 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, CNS

**Mechanism evidence:** PAH deficiency is a liver enzyme loss compatible with hepatocyte gene addition Source: OMIM PAH gene entry (https://omim.org/entry/612349)

1. **BMN 307** (AAV5) — 7.8/10 [high]
2. **OAV101-IT** (AAV9) — 7.5/10 [high]
3. **Zolgensma** (AAV9) — 7.5/10 [high]
4. **Hemgenix** (AAV5) — 7.4/10 [medium]
5. **Roctavian** (AAV5) — 7.4/10 [medium]

### Pompe disease (ORPHA:365)
**Gene:** GAA | **Mechanism:** loss_of_function | **CDS:** 2856 bp | **Inheritance:** Autosomal recessive | **Tissues:** muscle, heart

**Mechanism evidence:** GAA deficiency supports replacement logic but skeletal and cardiac delivery needs broad tissue correction Source: OMIM GAA gene entry (https://omim.org/entry/606800)

1. **Libmeldy** (LV) — 8.3/10 [high]
2. **ABO-101** (AAV9) — 7.9/10 [high]
3. **AVR-RD-01** (LV) — 7.9/10 [high]
4. **RGX-121** (AAV9) — 7.9/10 [high]
5. **ST-920** (AAV2/6) — 7.8/10 [high]

### Salla disease (ORPHA:309)
**Gene:** SLC17A5 | **Mechanism:** loss_of_function | **CDS:** 1485 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

**Mechanism evidence:** SLC17A5 transporter deficiency supports replacement logic but membrane transporter biology is mostly cell-autonomous Source: OMIM SLC17A5 gene entry (https://omim.org/entry/604322)

1. **Libmeldy** (LV) — 8.8/10 [high]
2. **Skysona** (LV) — 8.4/10 [high]
3. **ABO-101** (AAV9) — 8.1/10 [high]
4. **RGX-121** (AAV9) — 8.1/10 [high]
5. **AVR-RD-01** (LV) — 7.8/10 [high]

### Vitamin B12-unresponsive methylmalonic acidemia (ORPHA:27)
**Gene:** MUT | **Mechanism:** loss_of_function | **CDS:** 2250 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, CNS

**Mechanism evidence:** MUT deficiency supports replacement logic but mitochondrial enzyme import and multi-system metabolic disease require validation Source: OMIM MUT gene entry (https://omim.org/entry/609058)

1. **BMN 307** (AAV5) — 7.8/10 [high]
2. **DTX301** (AAV8) — 7.2/10 [medium]
3. **Libmeldy** (LV) — 6.8/10 [medium]
4. **OAV101-IT** (AAV9) — 6.8/10 [medium]
5. **Zolgensma** (AAV9) — 6.8/10 [medium]

### Wiskott-Aldrich syndrome (ORPHA:906)
**Gene:** WAS | **Mechanism:** loss_of_function | **CDS:** 1506 bp | **Inheritance:** X-linked recessive | **Tissues:** hematopoietic

**Mechanism evidence:** WAS loss of function is compatible with autologous hematopoietic stem-cell gene addition Source: OMIM WAS gene entry (https://omim.org/entry/300392)

1. **Strimvelis** (LV) — 7.9/10 [high]
2. **Skysona** (LV) — 6.8/10 [medium]
3. **Libmeldy** (LV) — 6.7/10 [medium]
4. **AVR-RD-01** (LV) — 6.5/10 [medium]
5. **BMN 307** (AAV5) — 5.8/10 [medium]

### X-linked adrenoleukodystrophy (ORPHA:43)
**Gene:** ABCD1 | **Mechanism:** loss_of_function | **CDS:** 2235 bp | **Inheritance:** X-linked recessive | **Tissues:** CNS

**Mechanism evidence:** ABCD1 deficiency supports replacement logic but cerebral inflammatory disease relies on hematopoietic and CNS disease biology Source: OMIM ABCD1 gene entry (https://omim.org/entry/300371)

1. **Skysona** (LV) — 8.3/10 [high]
2. **Libmeldy** (LV) — 7.7/10 [high]
3. **RGX-121** (AAV9) — 7.2/10 [medium]
4. **AVR-RD-01** (LV) — 7.0/10 [medium]
5. **ABO-101** (AAV9) — 6.9/10 [medium]

### X-linked myotubular myopathy (ORPHA:596)
**Gene:** MTM1 | **Mechanism:** loss_of_function | **CDS:** 1878 bp | **Inheritance:** X-linked recessive | **Tissues:** muscle

**Mechanism evidence:** MTM1 loss of function is compatible with muscle-directed gene addition but dose toxicity must be reviewed Source: OMIM MTM1 gene entry (https://omim.org/entry/300415)

1. **AT132** (AAV8) — 7.5/10 [high]
2. **SRP-9001** (AAV9) — 7.2/10 [medium]
3. **OAV101-IT** (AAV9) — 7.0/10 [medium]
4. **Zolgensma** (AAV9) — 7.0/10 [medium]
5. **Strimvelis** (LV) — 6.7/10 [medium]

### X-linked retinoschisis (ORPHA:792)
**Gene:** RS1 | **Mechanism:** loss_of_function | **CDS:** 672 bp | **Inheritance:** X-linked recessive | **Tissues:** retina

**Mechanism evidence:** RS1 deficiency supports retinal gene addition if target retinal structure remains treatable Source: OMIM RS1 gene entry (https://omim.org/entry/300839)

1. **Luxturna** (AAV2) — 7.8/10 [high]
2. **CPCB-RPE1** (AAV8) — 7.6/10 [high]
3. **Hemgenix** (AAV5) — 7.5/10 [high]
4. **Roctavian** (AAV5) — 7.5/10 [high]
5. **Libmeldy** (LV) — 7.4/10 [medium]
