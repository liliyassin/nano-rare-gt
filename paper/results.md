# Results

## 1. Cohort Overview

The NanoGT framework was applied to a 40-disease monogenic rare-disease cohort assembled from Orphanet identifiers and manually curated gene/tissue metadata. The cohort was deliberately mixed rather than restricted to easy discovery cases. It contained:

- 2 positive controls with approved gene-therapy precedents.
- 2 benchmark diseases with known gene-therapy precedent.
- 1 oversized-cargo stress test.
- 1 mitochondrial-delivery stress test.
- 24 pilot discovery or extension diseases.
- 6 haploinsufficiency diseases (Rett syndrome, Dravet syndrome, CDKL5 deficiency, GATA2 deficiency, CHARGE syndrome, Neurofibromatosis type 1).
- 2 repeat-expansion/silencing diseases (Fragile X syndrome, Friedreich ataxia).
- 1 genomic imprinting disease (Angelman syndrome).
- 1 two-hit haploinsufficiency disease (Tuberous sclerosis complex).

Each query disease was scored against the curated 21-program surrogate catalogue. The algorithm uses fourteen dimensions: packaging fit, tissue tropism, protein class, pathway similarity, mechanism/modality compatibility, inheritance compatibility, regulatory approval stage, vector immunogenicity, therapeutic window, cross-correction potential, immune privilege, promoter availability, route-of-administration feasibility, and organelle targeting feasibility. Raw scores have a maximum of 21 and are normalised to a score out of 10.

## 2. Cross-Disease Score Distribution

All 40 diseases received at least some result from the framework — there are no mechanism hard-fails in this cohort because the non-LOF arm was deliberately designed from conditional diseases (haploinsufficiency, repeat-expansion silencing, genomic imprinting) where gene addition remains a biologically rational strategy. One disease, Neurofibromatosis type 1 (NF1, 8,451 bp CDS), received a packaging hard-fail: its coding sequence exceeds the capacity of every vector in the current catalogue, so no precedent can be ranked. All other 39 diseases received at least one scored precedent.

Among the 39 scored diseases, Duchenne muscular dystrophy remains an expected stress-test case: full-length native DMD fails the ordinary single-AAV packaging gate, but the catalogue contains SRP-9001 as an engineered micro-dystrophin precedent, so a score is still returned. The framework separates ordinary full-length gene replacement failure from engineered micro/mini-transgene strategy scoring.

Among the 39 scored diseases, 32 top matches were classified as high confidence and 7 as medium confidence. Composite scores ranged from 5.9/10 to 9.9/10. These values should be interpreted as relative precedent strength, not predicted clinical efficacy.

### Table 1. Forty-disease NanoGT cohort results

| Cohort role | Disease | ORPHA | Gene | Mechanism | Gene-addition fit | CDS (bp) | Top precedent | Vector | Score | Confidence |
|---|---|---:|---|---|---|---:|---|---|---:|---|
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
| non_lof_haploinsufficiency | Tuberous sclerosis complex | ORPHA:805 | TSC2 | haploinsufficiency | conditional | 5694 | Libmeldy | LV | 6.1/10 | medium |
| non_lof_repeat_expansion | Friedreich ataxia | ORPHA:95 | FXN | repeat_expansion_silencing | conditional | 633 | OAV101-IT | AAV9 | 7.9/10 | high |

## 3. Top-Precedent Clusters

The most important result is not any single disease score, but the emergence of biologically interpretable precedent clusters.

### 3.1 Lentiviral / Libmeldy-dominated lysosomal and leukodystrophy cluster

Libmeldy was the top-ranked precedent for 9 diseases: alpha-mannosidosis, Fabry disease, Gaucher disease, Krabbe disease, metachromatic leukodystrophy, mucopolysaccharidosis types I/II/IIIA, and Pompe disease. This cluster is plausible because ex vivo lentiviral haematopoietic stem-cell gene therapy has a strong precedent base for lysosomal and neurodegenerative metabolic disorders, particularly where cross-correction by enzyme secretion or haematopoietic-derived CNS engraftment may contribute to benefit.

Importantly, mucolipidosis type IV and Salla disease — which share the CNS/lysosomal surface label — did not have Libmeldy as their top precedent in the final scoring run. Both ranked Skysona (LV) first. This is a meaningful result: MCOLN1 (ML-IV) encodes a lysosomal membrane channel and SLC17A5 (Salla) encodes a lysosomal membrane transporter; neither protein can be secreted or taken up by adjacent cells via the mannose-6-phosphate receptor pathway. The Skysona precedent, which uses a lentiviral vector for CNS-directed ex vivo haematopoietic correction in a leukodystrophy setting, captures the CNS/lentiviral class without implying classical enzyme cross-correction. This distinction — and the limitation that the current algorithm does not fully resolve it — must be stated clearly in the dissertation.

### 3.2 Hepatic metabolic / BMN 307 cluster

BMN 307 was top-ranked for 4 diseases: maple syrup urine disease, ornithine transcarbamylase deficiency, phenylketonuria, and vitamin B12-unresponsive methylmalonic acidemia. These diseases share hepatic and metabolic features, small-to-moderate transgene sizes, and a plausible liver-directed AAV development logic. The framework therefore identifies BMN 307 as a useful platform-style precedent for liver metabolic gene-addition programmes.

The interpretation should remain cautious. These diseases differ in subcellular localisation, metabolic pathway, newborn-screening relevance, and the extent to which liver correction would address neurological injury. For the dissertation, the BMN 307 cluster is best presented as a hypothesis-generating prioritisation result, not as a statement that the same vector/programme can be directly reused.

### 3.3 Retinal precedent cluster

Retinal diseases clustered around Luxturna and CPCB-RPE1. Choroideremia and X-linked retinoschisis were high-confidence retinal matches, while Leber congenital amaurosis, Leber hereditary optic neuropathy, and achromatopsia were medium-confidence matches. This spread is biologically sensible: the eye is accessible and immune-privileged, but gene-specific biology, affected retinal cell type, mitochondrial inheritance, and programme stage all affect transferability.

### 3.4 Positive controls and benchmark behaviour

The strongest positive control was haemophilia B: Hemgenix ranked first with a 9.9/10 score. Spinal muscular atrophy also returned an AAV9/Zolgensma/OAV101-style precedent at high confidence. ADA-SCID ranked with Strimvelis, correctly recovering an ex vivo haematopoietic precedent. These results support the internal validity of the scoring system at a proof-of-concept level.

Leber congenital amaurosis did not rank Luxturna first in the current run; CPCB-RPE1 ranked first at 7.5/10, with Luxturna second in the generated disease report. This is not a trivial detail to hide. It indicates that the current scoring formula may over-weight vector/tissue/programme-stage similarity relative to exact disease identity for some retinal cases. In the dissertation, this should be discussed as a calibration issue and a motivation for either exact-target bonus scoring or a clearer validation metric.

## 4. Medium-Confidence and Stress-Test Results

Medium-confidence top matches among scored diseases were:

- Leber hereditary optic neuropathy (MT-ND4): CPCB-RPE1 / AAV8 at 6.4/10
- Achromatopsia (CNGB3): CPCB-RPE1 / AAV8 at 7.5/10
- Crigler-Najjar syndrome type I (UGT1A1): Hemgenix / AAV5 at 7.2/10
- CHARGE syndrome (CHD7): Libmeldy / LV at 5.9/10
- Tuberous sclerosis complex (TSC2): Libmeldy / LV at 6.1/10

These cases are useful because they show where the framework becomes uncertain. They include retinal diseases where several plausible precedents compete, a mitochondrial disease where ordinary nuclear gene addition is mechanistically uncertain, a liver disease where pathway and protein-class similarity are imperfect, and two haploinsufficiency diseases where conditional gene-addition logic and large transgene size both constrain tractability.

Duchenne muscular dystrophy illustrates the distinction between native-gene replacement and engineered-cargo precedent. Full-length DMD fails ordinary single-AAV packaging, but SRP-9001 can be scored as a micro-dystrophin strategy. The correct interpretation is not that DMD is unsuitable for gene therapy, but that DMD requires engineered microgene, dual-vector, exon-skipping, or editing-based logic rather than ordinary full-length gene addition.

## 5. Non-LOF Mechanism Arm

The non-LOF arm contains 10 diseases spanning haploinsufficiency, repeat-expansion silencing, genomic imprinting, and two-hit haploinsufficiency mechanisms. Unlike purely incompatible diseases (gain-of-function, dominant-negative), all 10 were selected because gene addition is a biologically rational strategy — they are genuine candidates for gene therapy, not diseases where adding a copy makes things worse. The key dissertation question is whether the scoring framework produces interpretable, biologically appropriate results for mechanisms that differ from classical loss-of-function.

The six haploinsufficiency CNS diseases (Rett, Dravet, CDKL5, GATA2, CHARGE, plus TSC as a two-hit variant) all returned medium-to-high confidence matches. The four CNS haploinsufficiency diseases with small-to-moderate gene size (Rett/MECP2, Dravet/SCN1A, CDKL5/CDKL5, Angelman/UBE3A) returned scores of 7.1–7.4, with Skysona (LV) or OAV101-IT (AAV9) as top precedents. These scores are interpretable: the diseases share CNS involvement, small-to-moderate gene size, and a case for ex vivo or in vivo CNS lentiviral delivery. The Skysona precedent is appropriate because it is a CNS-targeted lentiviral program, even though the precise mechanism differs.

GATA2 deficiency scored 7.6/10 (high confidence), with Strimvelis (LV) as top precedent. This is the most mechanistically coherent non-LOF result: GATA2 haploinsufficiency causes haematopoietic failure and the ex vivo HSC gene-addition logic of Strimvelis maps cleanly to GATA2 biology.

The two large haploinsufficiency/two-hit diseases — CHARGE syndrome (CHD7, 7,950 bp) and Tuberous sclerosis complex (TSC2, 5,694 bp) — scored 5.9 and 6.1 (medium), correctly reflecting that large CDS size and the two-hit nature of TSC reduce precedent transferability.

Neurofibromatosis type 1 (NF1, 8,451 bp) received a packaging hard-fail: its CDS exceeds the capacity of every vector in the current catalogue. This is the correct result — NF1 is not a disease where standard single-vector gene addition is tractable, and the empty result is a valid scientific finding about packaging constraints.

The two repeat-expansion diseases behaved differently and this contrast is instructive. Friedreich ataxia (FXN, 633 bp) scored 7.9/10 high confidence with OAV101-IT (AAV9) as top precedent. This is correct because the frataxin protein coding sequence is structurally normal — the GAA repeat silences the endogenous gene, but FXN cDNA addition bypasses the silenced allele. The tool treats it similarly to a CNS/cardiac LOF disease, which is the right biological analogy. Fragile X syndrome (FMR1, 1,908 bp) scored 7.0/10 medium, with Skysona as top precedent. FMR1 cDNA addition is also clinically pursued for the same silencing-bypass logic, and the medium score reflects appropriate caution: FMRP has synaptic dosage-sensitivity that makes titrating expression more complex than frataxin.

## 6. Summary of Findings

The 40-disease analysis supports four dissertation-level claims:

1. NanoGT can recover obvious clinical precedents for positive controls and benchmark diseases.
2. Cross-disease clustering produces biologically plausible precedent groups, especially for lentiviral/HSC lysosomal disease, liver metabolic AAV programmes, and retinal AAV programmes.
3. The framework usefully exposes hard limitations: oversized native cargo (DMD, NF1 packaging failures), mitochondrial allotopic-expression requirements (LHON), and the distinction between secreted lysosomal enzymes and lysosomal membrane proteins.
4. The non-LOF arm produces interpretable, biologically coherent results for conditional mechanisms (haploinsufficiency, repeat-expansion silencing, genomic imprinting), demonstrating that the framework extends meaningfully beyond classical LOF.

The results should be framed as a reproducible prioritisation and precedent-mapping framework, not as a validated therapeutic recommendation system.
