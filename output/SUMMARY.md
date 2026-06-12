# NanoGT Results: 30-Disease GT Precedent Matching Cohort

**Algorithm:** 12-dimension heuristic scoring: packaging fit, tissue tropism, protein class, pathway similarity, inheritance compatibility, approval precedent, vector immunogenicity, therapeutic window, cross-correction, immune privilege, promoter availability, and route-of-administration feasibility. Raw max = 18; composite is normalised to /10.

**Interpretation:** The framework ranks which existing clinical gene-therapy program is the closest development precedent for the query disease. It does not claim the top precedent is directly reusable without disease-specific validation, vector engineering, toxicology, and regulatory review.

## Summary Table

| Cohort role | Disease | ORPHA | Gene | CDS (bp) | #1 Precedent | Vector | Score | Confidence |
|-------------|---------|-------|------|----------|--------------|--------|-------|------------|
| positive_control | Hemophilia B | ORPHA:306 | F9 | 1383 | Hemgenix | AAV5 | 9.9/10 | high |
| benchmark_with_known_gt_precedent | Leber congenital amaurosis | ORPHA:65 | RPE65 | 1599 | CPCB-RPE1 | AAV8 | 7.2/10 | medium |
| benchmark_with_known_gt_precedent | Severe combined immunodeficiency due to adenosine deaminase deficiency | ORPHA:277 | ADA | 1092 | Strimvelis | LV | 7.8/10 | high |
| positive_control | Spinal Muscular Atrophy | ORPHA:70 | SMN1 | 891 | OAV101-IT | AAV9 | 8.1/10 | high |
| oversized_cargo_stress_test | Duchenne muscular dystrophy | ORPHA:98896 | DMD | 11055 | - | - | - | no compatible single-vector precedent |
| mitochondrial_stress_test | Leber hereditary optic neuropathy | ORPHA:104 | MT-ND4 | 1377 | CPCB-RPE1 | AAV8 | 6.9/10 | medium |
| pilot_cohort | Achromatopsia | ORPHA:49382 | CNGB3 | 2427 | CPCB-RPE1 | AAV8 | 7.1/10 | medium |
| pilot_cohort | Alpha-mannosidosis | ORPHA:61 | MAN2B1 | 3033 | Libmeldy | LV | 8.6/10 | high |
| pilot_cohort | Choroideremia | ORPHA:180 | CHM | 1962 | Luxturna | AAV2 | 7.6/10 | high |
| pilot_cohort | Crigler-Najjar syndrome type I | ORPHA:1060 | UGT1A1 | 1596 | Hemgenix | AAV5 | 6.8/10 | medium |
| pilot_cohort | Fabry disease | ORPHA:324 | GLA | 1290 | Libmeldy | LV | 8.7/10 | high |
| pilot_cohort | Gaucher disease | ORPHA:355 | GBA | 1491 | Libmeldy | LV | 9.1/10 | high |
| pilot_cohort | Glycogen storage disease type Ia | ORPHA:79258 | G6PC | 1071 | SRP-9001 | AAV9 | 7.4/10 | medium |
| pilot_cohort | Kohlschutter-Tonz syndrome | ORPHA:1946 | ROGDI | 861 | OAV101-IT | AAV9 | 7.6/10 | high |
| pilot_cohort | Krabbe disease | ORPHA:487 | GALC | 2055 | Libmeldy | LV | 9.1/10 | high |
| pilot_cohort | Maple syrup urine disease | ORPHA:511 | BCKDHA | 1335 | BMN 307 | AAV5 | 8.2/10 | high |
| pilot_cohort | Metachromatic leukodystrophy | ORPHA:512 | ARSA | 1521 | Libmeldy | LV | 9.1/10 | high |
| pilot_cohort | Mucolipidosis type IV | ORPHA:578 | MCOLN1 | 1740 | Libmeldy | LV | 9.2/10 | high |
| pilot_cohort | Mucopolysaccharidosis type I | ORPHA:579 | IDUA | 1962 | Libmeldy | LV | 9.4/10 | high |
| pilot_cohort | Mucopolysaccharidosis type II | ORPHA:580 | IDS | 1650 | Libmeldy | LV | 9.2/10 | high |
| pilot_cohort | Mucopolysaccharidosis type IIIA (Sanfilippo A) | ORPHA:79269 | SGSH | 1674 | Libmeldy | LV | 9.1/10 | high |
| pilot_cohort | Ornithine transcarbamylase deficiency | ORPHA:664 | OTC | 1065 | BMN 307 | AAV5 | 8.0/10 | high |
| pilot_cohort | Phenylketonuria | ORPHA:716 | PAH | 1353 | BMN 307 | AAV5 | 7.6/10 | high |
| pilot_cohort | Pompe disease | ORPHA:365 | GAA | 2856 | Libmeldy | LV | 8.4/10 | high |
| pilot_cohort | Salla disease | ORPHA:309 | SLC17A5 | 1485 | Libmeldy | LV | 9.0/10 | high |
| pilot_cohort | Vitamin B12-unresponsive methylmalonic acidemia | ORPHA:27 | MUT | 2250 | BMN 307 | AAV5 | 7.9/10 | high |
| pilot_cohort | Wiskott-Aldrich syndrome | ORPHA:906 | WAS | 1506 | Strimvelis | LV | 7.7/10 | high |
| pilot_cohort | X-linked adrenoleukodystrophy | ORPHA:43 | ABCD1 | 2235 | Skysona | LV | 8.4/10 | high |
| pilot_cohort | X-linked myotubular myopathy | ORPHA:596 | MTM1 | 1878 | AT132 | AAV8 | 7.3/10 | medium |
| pilot_cohort | X-linked retinoschisis | ORPHA:792 | RS1 | 672 | Luxturna | AAV2 | 7.5/10 | high |

---

## Disease Sections

### Hemophilia B (ORPHA:306)
**Gene:** F9 | **CDS:** 1383 bp | **Inheritance:** X-linked recessive | **Tissues:** liver

1. **Hemgenix** (AAV5) — 9.9/10 [high]
2. **Roctavian** (AAV5) — 9.9/10 [high]
3. **SPK-8011** (AAVrh10) — 9.5/10 [high]
4. **DTX201** (AAV8) — 9.1/10 [high]
5. **ST-920** (AAV2/6) — 8.5/10 [high]

### Leber congenital amaurosis (ORPHA:65)
**Gene:** RPE65 | **CDS:** 1599 bp | **Inheritance:** Autosomal recessive | **Tissues:** retina

1. **CPCB-RPE1** (AAV8) — 7.2/10 [medium]
2. **Luxturna** (AAV2) — 6.8/10 [medium]
3. **Skysona** (LV) — 6.6/10 [medium]
4. **Libmeldy** (LV) — 6.2/10 [medium]
5. **Strimvelis** (LV) — 6.2/10 [medium]

### Severe combined immunodeficiency due to adenosine deaminase deficiency (ORPHA:277)
**Gene:** ADA | **CDS:** 1092 bp | **Inheritance:** Autosomal recessive | **Tissues:** hematopoietic

1. **Strimvelis** (LV) — 7.8/10 [high]
2. **Libmeldy** (LV) — 6.4/10 [medium]
3. **Skysona** (LV) — 6.3/10 [medium]
4. **AVR-RD-01** (LV) — 6.0/10 [medium]
5. **BMN 307** (AAV5) — 5.8/10 [medium]

### Spinal Muscular Atrophy (ORPHA:70)
**Gene:** SMN1 | **CDS:** 891 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, muscle

1. **OAV101-IT** (AAV9) — 8.1/10 [high]
2. **Zolgensma** (AAV9) — 8.1/10 [high]
3. **AT132** (AAV8) — 7.8/10 [high]
4. **SRP-9001** (AAV9) — 7.3/10 [medium]
5. **BMN 307** (AAV5) — 7.0/10 [medium]

### Duchenne muscular dystrophy (ORPHA:98896)
**Gene:** DMD | **CDS:** 11055 bp | **Inheritance:** X-linked recessive | **Tissues:** muscle, heart

No single-vector precedent survived the packaging hard gate. For this disease, the likely development route requires an oversized-cargo strategy such as micro-gene design, dual-vector delivery, ex vivo/lentiviral delivery if tissue-appropriate, or non-viral/editing approaches outside the current v0.1 catalog.

### Leber hereditary optic neuropathy (ORPHA:104)
**Gene:** MT-ND4 | **CDS:** 1377 bp | **Inheritance:** Mitochondrial inheritance | **Tissues:** retina, CNS

1. **CPCB-RPE1** (AAV8) — 6.9/10 [medium]
2. **Skysona** (LV) — 6.8/10 [medium]
3. **Luxturna** (AAV2) — 6.6/10 [medium]
4. **Libmeldy** (LV) — 6.3/10 [medium]
5. **Hemgenix** (AAV5) — 6.0/10 [medium]

### Achromatopsia (ORPHA:49382)
**Gene:** CNGB3 | **CDS:** 2427 bp | **Inheritance:** Autosomal recessive | **Tissues:** retina

1. **CPCB-RPE1** (AAV8) — 7.1/10 [medium]
2. **Luxturna** (AAV2) — 6.7/10 [medium]
3. **Skysona** (LV) — 6.1/10 [medium]
4. **Libmeldy** (LV) — 5.7/10 [medium]
5. **Strimvelis** (LV) — 5.7/10 [medium]

### Alpha-mannosidosis (ORPHA:61)
**Gene:** MAN2B1 | **CDS:** 3033 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, liver

1. **Libmeldy** (LV) — 8.6/10 [high]
2. **ST-920** (AAV2/6) — 7.8/10 [high]
3. **ABO-101** (AAV9) — 7.7/10 [high]
4. **RGX-121** (AAV9) — 7.7/10 [high]
5. **Hemgenix** (AAV5) — 7.6/10 [high]

### Choroideremia (ORPHA:180)
**Gene:** CHM | **CDS:** 1962 bp | **Inheritance:** X-linked recessive | **Tissues:** retina

1. **Luxturna** (AAV2) — 7.6/10 [high]
2. **Strimvelis** (LV) — 6.9/10 [medium]
3. **CPCB-RPE1** (AAV8) — 6.9/10 [medium]
4. **GS010** (AAV2) — 6.6/10 [medium]
5. **Skysona** (LV) — 6.6/10 [medium]

### Crigler-Najjar syndrome type I (ORPHA:1060)
**Gene:** UGT1A1 | **CDS:** 1596 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver

1. **Hemgenix** (AAV5) — 6.8/10 [medium]
2. **Roctavian** (AAV5) — 6.8/10 [medium]
3. **BMN 307** (AAV5) — 6.7/10 [medium]
4. **Skysona** (LV) — 6.7/10 [medium]
5. **SPK-8011** (AAVrh10) — 6.4/10 [medium]

### Fabry disease (ORPHA:324)
**Gene:** GLA | **CDS:** 1290 bp | **Inheritance:** X-linked dominant | **Tissues:** liver, kidney, heart, CNS

1. **Libmeldy** (LV) — 8.7/10 [high]
2. **ST-920** (AAV2/6) — 8.6/10 [high]
3. **RGX-121** (AAV9) — 8.4/10 [high]
4. **Hemgenix** (AAV5) — 8.3/10 [high]
5. **Roctavian** (AAV5) — 8.3/10 [high]

### Gaucher disease (ORPHA:355)
**Gene:** GBA | **CDS:** 1491 bp | **Inheritance:** Autosomal recessive | **Tissues:** hematopoietic, liver, CNS

1. **Libmeldy** (LV) — 9.1/10 [high]
2. **AVR-RD-01** (LV) — 8.7/10 [high]
3. **ST-920** (AAV2/6) — 8.1/10 [high]
4. **ABO-101** (AAV9) — 8.0/10 [high]
5. **RGX-121** (AAV9) — 8.0/10 [high]

### Glycogen storage disease type Ia (ORPHA:79258)
**Gene:** G6PC | **CDS:** 1071 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, kidney

1. **SRP-9001** (AAV9) — 7.4/10 [medium]
2. **ST-920** (AAV2/6) — 7.4/10 [medium]
3. **RGX-121** (AAV9) — 7.3/10 [medium]
4. **Hemgenix** (AAV5) — 7.2/10 [medium]
5. **Roctavian** (AAV5) — 7.2/10 [medium]

### Kohlschutter-Tonz syndrome (ORPHA:1946)
**Gene:** ROGDI | **CDS:** 861 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

1. **OAV101-IT** (AAV9) — 7.6/10 [high]
2. **Zolgensma** (AAV9) — 7.6/10 [high]
3. **BMN 307** (AAV5) — 7.3/10 [medium]
4. **Libmeldy** (LV) — 7.3/10 [medium]
5. **Strimvelis** (LV) — 7.2/10 [medium]

### Krabbe disease (ORPHA:487)
**Gene:** GALC | **CDS:** 2055 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

1. **Libmeldy** (LV) — 9.1/10 [high]
2. **Skysona** (LV) — 8.4/10 [high]
3. **ABO-101** (AAV9) — 8.3/10 [high]
4. **RGX-121** (AAV9) — 8.3/10 [high]
5. **AVR-RD-01** (LV) — 8.0/10 [high]

### Maple syrup urine disease (ORPHA:511)
**Gene:** BCKDHA | **CDS:** 1335 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, CNS

1. **BMN 307** (AAV5) — 8.2/10 [high]
2. **Luxturna** (AAV2) — 7.3/10 [medium]
3. **OAV101-IT** (AAV9) — 7.0/10 [medium]
4. **Zolgensma** (AAV9) — 7.0/10 [medium]
5. **GS010** (AAV2) — 6.9/10 [medium]

### Metachromatic leukodystrophy (ORPHA:512)
**Gene:** ARSA | **CDS:** 1521 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

1. **Libmeldy** (LV) — 9.1/10 [high]
2. **Skysona** (LV) — 8.4/10 [high]
3. **ABO-101** (AAV9) — 8.3/10 [high]
4. **RGX-121** (AAV9) — 8.3/10 [high]
5. **AVR-RD-01** (LV) — 8.0/10 [high]

### Mucolipidosis type IV (ORPHA:578)
**Gene:** MCOLN1 | **CDS:** 1740 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, retina

1. **Libmeldy** (LV) — 9.2/10 [high]
2. **Skysona** (LV) — 8.8/10 [high]
3. **ABO-101** (AAV9) — 8.4/10 [high]
4. **RGX-121** (AAV9) — 8.4/10 [high]
5. **AVR-RD-01** (LV) — 8.1/10 [high]

### Mucopolysaccharidosis type I (ORPHA:579)
**Gene:** IDUA | **CDS:** 1962 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS, liver

1. **Libmeldy** (LV) — 9.4/10 [high]
2. **ST-920** (AAV2/6) — 8.7/10 [high]
3. **ABO-101** (AAV9) — 8.6/10 [high]
4. **RGX-121** (AAV9) — 8.6/10 [high]
5. **Hemgenix** (AAV5) — 8.4/10 [high]

### Mucopolysaccharidosis type II (ORPHA:580)
**Gene:** IDS | **CDS:** 1650 bp | **Inheritance:** X-linked recessive | **Tissues:** CNS, liver

1. **Libmeldy** (LV) — 9.2/10 [high]
2. **ST-920** (AAV2/6) — 8.8/10 [high]
3. **RGX-121** (AAV9) — 8.7/10 [high]
4. **Hemgenix** (AAV5) — 8.6/10 [high]
5. **Roctavian** (AAV5) — 8.6/10 [high]

### Mucopolysaccharidosis type IIIA (Sanfilippo A) (ORPHA:79269)
**Gene:** SGSH | **CDS:** 1674 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

1. **Libmeldy** (LV) — 9.1/10 [high]
2. **ABO-101** (AAV9) — 8.3/10 [high]
3. **RGX-121** (AAV9) — 8.3/10 [high]
4. **AVR-RD-01** (LV) — 8.0/10 [high]
5. **Hemgenix** (AAV5) — 7.6/10 [high]

### Ornithine transcarbamylase deficiency (ORPHA:664)
**Gene:** OTC | **CDS:** 1065 bp | **Inheritance:** X-linked recessive | **Tissues:** liver, CNS

1. **BMN 307** (AAV5) — 8.0/10 [high]
2. **DTX301** (AAV8) — 7.6/10 [high]
3. **Hemgenix** (AAV5) — 7.0/10 [medium]
4. **Roctavian** (AAV5) — 7.0/10 [medium]
5. **OAV101-IT** (AAV9) — 6.8/10 [medium]

### Phenylketonuria (ORPHA:716)
**Gene:** PAH | **CDS:** 1353 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, CNS

1. **BMN 307** (AAV5) — 7.6/10 [high]
2. **OAV101-IT** (AAV9) — 7.3/10 [medium]
3. **Zolgensma** (AAV9) — 7.3/10 [medium]
4. **Hemgenix** (AAV5) — 7.1/10 [medium]
5. **Roctavian** (AAV5) — 7.1/10 [medium]

### Pompe disease (ORPHA:365)
**Gene:** GAA | **CDS:** 2856 bp | **Inheritance:** Autosomal recessive | **Tissues:** muscle, heart

1. **Libmeldy** (LV) — 8.4/10 [high]
2. **ABO-101** (AAV9) — 7.9/10 [high]
3. **AVR-RD-01** (LV) — 7.9/10 [high]
4. **RGX-121** (AAV9) — 7.9/10 [high]
5. **ST-920** (AAV2/6) — 7.8/10 [high]

### Salla disease (ORPHA:309)
**Gene:** SLC17A5 | **CDS:** 1485 bp | **Inheritance:** Autosomal recessive | **Tissues:** CNS

1. **Libmeldy** (LV) — 9.0/10 [high]
2. **Skysona** (LV) — 8.6/10 [high]
3. **ABO-101** (AAV9) — 8.2/10 [high]
4. **RGX-121** (AAV9) — 8.2/10 [high]
5. **AVR-RD-01** (LV) — 7.9/10 [high]

### Vitamin B12-unresponsive methylmalonic acidemia (ORPHA:27)
**Gene:** MUT | **CDS:** 2250 bp | **Inheritance:** Autosomal recessive | **Tissues:** liver, CNS

1. **BMN 307** (AAV5) — 7.9/10 [high]
2. **DTX301** (AAV8) — 7.2/10 [medium]
3. **Libmeldy** (LV) — 6.7/10 [medium]
4. **OAV101-IT** (AAV9) — 6.7/10 [medium]
5. **Zolgensma** (AAV9) — 6.7/10 [medium]

### Wiskott-Aldrich syndrome (ORPHA:906)
**Gene:** WAS | **CDS:** 1506 bp | **Inheritance:** X-linked recessive | **Tissues:** hematopoietic

1. **Strimvelis** (LV) — 7.7/10 [high]
2. **Skysona** (LV) — 6.4/10 [medium]
3. **Libmeldy** (LV) — 6.3/10 [medium]
4. **AVR-RD-01** (LV) — 6.2/10 [medium]
5. **BMN 307** (AAV5) — 5.4/10 [medium]

### X-linked adrenoleukodystrophy (ORPHA:43)
**Gene:** ABCD1 | **CDS:** 2235 bp | **Inheritance:** X-linked recessive | **Tissues:** CNS

1. **Skysona** (LV) — 8.4/10 [high]
2. **Libmeldy** (LV) — 7.7/10 [high]
3. **RGX-121** (AAV9) — 7.2/10 [medium]
4. **AVR-RD-01** (LV) — 6.9/10 [medium]
5. **ABO-101** (AAV9) — 6.8/10 [medium]

### X-linked myotubular myopathy (ORPHA:596)
**Gene:** MTM1 | **CDS:** 1878 bp | **Inheritance:** X-linked recessive | **Tissues:** muscle

1. **AT132** (AAV8) — 7.3/10 [medium]
2. **SRP-9001** (AAV9) — 6.8/10 [medium]
3. **OAV101-IT** (AAV9) — 6.7/10 [medium]
4. **Zolgensma** (AAV9) — 6.7/10 [medium]
5. **Strimvelis** (LV) — 6.3/10 [medium]

### X-linked retinoschisis (ORPHA:792)
**Gene:** RS1 | **CDS:** 672 bp | **Inheritance:** X-linked recessive | **Tissues:** retina

1. **Luxturna** (AAV2) — 7.5/10 [high]
2. **CPCB-RPE1** (AAV8) — 7.3/10 [medium]
3. **Hemgenix** (AAV5) — 7.3/10 [medium]
4. **Roctavian** (AAV5) — 7.3/10 [medium]
5. **Libmeldy** (LV) — 7.1/10 [medium]
