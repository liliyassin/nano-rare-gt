# Results

## 1. Cohort Overview

The NanoGT framework was applied to a 30-disease monogenic rare-disease cohort assembled from Orphanet identifiers and manually curated gene/tissue metadata. The cohort was deliberately mixed rather than restricted to easy discovery cases. It contained:

- 2 positive controls with approved gene-therapy precedents.
- 2 benchmark diseases with known gene-therapy precedent.
- 1 oversized-cargo stress test.
- 1 mitochondrial-delivery stress test.
- 24 pilot discovery or extension diseases.

Each query disease was scored against the curated 21-program surrogate catalogue. The algorithm uses twelve dimensions: packaging fit, tissue tropism, protein class, pathway similarity, inheritance compatibility, regulatory approval stage, vector immunogenicity, therapeutic window, cross-correction potential, immune privilege, promoter availability, and route-of-administration feasibility. Raw scores have a maximum of 18 and are normalised to a score out of 10.

## 2. Cross-Disease Score Distribution

The framework produced at least one compatible single-vector precedent for 29 of 30 diseases. The exception was Duchenne muscular dystrophy, where the native DMD coding sequence exceeded the single-vector AAV cargo limit and therefore failed the packaging gate. This is an expected and useful stress-test result rather than an execution failure: current DMD gene therapy development relies on micro-dystrophin or other non-native cargo strategies, which are outside the v0.1 matching model.

Among the 29 compatible diseases, 23 were classified as high confidence and 6 as medium confidence. Composite scores ranged from 6.8/10 to 9.9/10. The mean score was 8.20/10 and the median was 8.1/10. These values should be interpreted as relative precedent strength, not predicted clinical efficacy.

### Table 1. Thirty-disease NanoGT cohort results

| Cohort role | Disease | ORPHA | Gene | CDS (bp) | Top precedent | Vector | Score | Confidence |
|---|---|---:|---|---:|---|---|---:|---|
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

## 3. Top-Precedent Clusters

The most important result is not any single disease score, but the emergence of biologically interpretable precedent clusters.

### 3.1 Lentiviral / Libmeldy-dominated lysosomal and leukodystrophy cluster

Libmeldy was the top-ranked precedent for 11 diseases, making it the dominant precedent in the current cohort. The diseases in this group include several lysosomal storage disorders and leukodystrophy-like CNS diseases: alpha-mannosidosis, Fabry disease, Gaucher disease, Krabbe disease, metachromatic leukodystrophy, mucolipidosis type IV, mucopolysaccharidosis types I/II/IIIA, Pompe disease, and Salla disease. This cluster is plausible because ex vivo lentiviral haematopoietic stem-cell gene therapy has a strong precedent base for lysosomal and neurodegenerative metabolic disorders, particularly where cross-correction by enzyme secretion or haematopoietic-derived CNS engraftment may contribute to benefit.

This cluster is also a limitation signal. Some members, such as Salla disease and mucolipidosis type IV, involve membrane or transporter biology rather than classical secreted lysosomal enzyme replacement. The algorithm currently recognises broad lysosomal/CNS similarity but does not fully separate secreted enzymes with mannose-6-phosphate-mediated cross-correction from cell-autonomous lysosomal membrane proteins. This must be stated clearly in the dissertation.

### 3.2 Hepatic metabolic / BMN 307 cluster

BMN 307 was top-ranked for 4 diseases: maple syrup urine disease, ornithine transcarbamylase deficiency, phenylketonuria, and vitamin B12-unresponsive methylmalonic acidemia. These diseases share hepatic and metabolic features, small-to-moderate transgene sizes, and a plausible liver-directed AAV development logic. The framework therefore identifies BMN 307 as a useful platform-style precedent for liver metabolic gene-addition programmes.

The interpretation should remain cautious. These diseases differ in subcellular localisation, metabolic pathway, newborn-screening relevance, and the extent to which liver correction would address neurological injury. For the dissertation, the BMN 307 cluster is best presented as a hypothesis-generating prioritisation result, not as a statement that the same vector/programme can be directly reused.

### 3.3 Retinal precedent cluster

Retinal diseases clustered around Luxturna and CPCB-RPE1. Choroideremia and X-linked retinoschisis were high-confidence retinal matches, while Leber congenital amaurosis, Leber hereditary optic neuropathy, and achromatopsia were medium-confidence matches. This spread is biologically sensible: the eye is accessible and immune-privileged, but gene-specific biology, affected retinal cell type, mitochondrial inheritance, and programme stage all affect transferability.

### 3.4 Positive controls and benchmark behaviour

The strongest positive control was haemophilia B: Hemgenix ranked first with a 9.9/10 score. Spinal muscular atrophy also returned an AAV9/Zolgensma/OAV101-style precedent at high confidence. ADA-SCID ranked with Strimvelis, correctly recovering an ex vivo haematopoietic precedent. These results support the internal validity of the scoring system at a proof-of-concept level.

Leber congenital amaurosis did not rank Luxturna first in the current run; CPCB-RPE1 ranked first at 7.2/10, with Luxturna second in the generated summary. This is not a trivial detail to hide. It indicates that the current scoring formula may over-weight vector/tissue/programme-stage similarity relative to exact disease identity for some retinal cases. In the dissertation, this should be discussed as a calibration issue and a motivation for either exact-target bonus scoring or a clearer validation metric.

## 4. Medium-Confidence and Stress-Test Results

Medium-confidence diseases were:

- Leber congenital amaurosis (RPE65): CPCB-RPE1 / AAV8 at 7.2/10
- Leber hereditary optic neuropathy (MT-ND4): CPCB-RPE1 / AAV8 at 6.9/10
- Achromatopsia (CNGB3): CPCB-RPE1 / AAV8 at 7.1/10
- Crigler-Najjar syndrome type I (UGT1A1): Hemgenix / AAV5 at 6.8/10
- Glycogen storage disease type Ia (G6PC): SRP-9001 / AAV9 at 7.4/10
- X-linked myotubular myopathy (MTM1): AT132 / AAV8 at 7.3/10

These cases are useful because they show where the framework becomes uncertain. They include retinal diseases where several plausible precedents compete; liver diseases where pathway and protein-class similarity are imperfect; and myopathy/mitochondrial cases where delivery and mechanism are less well represented by the current catalogue.

Duchenne muscular dystrophy failed the single-vector packaging gate. The correct interpretation is that NanoGT v0.1 cannot model micro-dystrophin engineering, dual-AAV delivery, exon skipping, or editing-based strategies. This is a limitation of current framework scope, not evidence that DMD is unsuitable for gene therapy.

## 5. Summary of Findings

The 30-disease analysis supports three dissertation-level claims:

1. NanoGT can recover obvious clinical precedents for several positive controls and benchmarks.
2. Cross-disease clustering produces biologically plausible precedent groups, especially for lentiviral/HSC lysosomal disease, liver metabolic AAV programmes, and retinal AAV programmes.
3. The framework usefully exposes limitations: oversized cargo, mitochondrial delivery, uncertain pathway inference, cell-autonomous protein biology, and incomplete catalogue coverage.

The results should be framed as a reproducible prioritisation and precedent-mapping framework, not as a validated therapeutic recommendation system.
