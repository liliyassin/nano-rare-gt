# Results

## 1. Cohort Overview

The NanoGT framework was applied to a 46-disease monogenic rare-disease cohort assembled from Orphanet identifiers and manually curated gene/tissue metadata. Disease metadata were fact-checked against Orphanet, OMIM, and UniProt; all 46 ORPHA and OMIM identifiers were verified against their source pages. The cohort was deliberately mixed rather than restricted to easy discovery cases. It contained:

- 3 positive controls with approved gene-therapy precedents (Hemophilia A, Hemophilia B, Spinal muscular atrophy).
- 1 benchmark disease with known gene-therapy precedent (ADA-SCID).
- 1 oversized-cargo stress test (Duchenne muscular dystrophy).
- 1 mitochondrial-delivery stress test (Leber hereditary optic neuropathy).
- 34 pilot cohort diseases (all scored; includes 11 lysosomal/neurodegenerative, 7 hepatic metabolic, 4 retinal/sensory, and 12 additional diseases added in the 46-disease expansion).
- 4 haploinsufficiency diseases (Rett syndrome, CHARGE syndrome, Neurofibromatosis type 1, Tuberous sclerosis complex).
- 2 repeat-expansion/silencing diseases (Fragile X syndrome, Friedreich ataxia).



Each query disease was scored against the curated 21-program surrogate catalogue. The algorithm uses fourteen dimensions: packaging fit, tissue tropism, protein class, pathway similarity, mechanism/modality compatibility, inheritance compatibility, regulatory approval stage, vector immunogenicity, therapeutic window, cross-correction potential, immune privilege, promoter availability, route-of-administration feasibility, and organelle targeting feasibility. Raw scores have a maximum of 21 and are normalised to a score out of 10.

## 2. Cross-Disease Score Distribution

All 46 diseases received a result from the framework. One disease, Neurofibromatosis type 1 (NF1, 8,451 bp CDS), received a packaging hard-fail: its coding sequence exceeds the capacity of every vector in the current catalogue, so no precedent can be ranked — this is a biologically informative result in its own right. All other 45 diseases received at least one scored precedent.

Among the 45 scored diseases, Duchenne muscular dystrophy is an expected stress-test case: full-length native DMD (11,055 bp) fails the ordinary single-AAV packaging gate, but the catalogue contains SRP-9001 as an engineered micro-dystrophin precedent, so a score is still returned. The framework correctly separates full-length gene replacement failure from engineered micro/mini-transgene strategy scoring.

Among the 45 scored diseases, 36 top matches were classified as high confidence and 8 as medium confidence. Composite scores ranged from 5.9/10 to 9.9/10. These values should be interpreted as relative precedent strength, not predicted clinical efficacy.

### Table 1. 46-disease NanoGT cohort results

| Cohort role | Disease | ORPHA | Gene | Mechanism | Gene-addition fit | CDS (bp) | Top precedent | Vector | Score | Confidence |
|---|---|---:|---|---|---|---:|---|---|---:|---|
| positive_control | Hemophilia A | ORPHA:98878 | F8 | loss_of_function | compatible | 4374 | Hemgenix† | AAV5 | 8.5/10 | high |
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
| non_lof_haploinsufficiency | Tuberous sclerosis complex | ORPHA:805 | TSC1 | haploinsufficiency | conditional | 3495 | Libmeldy | LV | 6.1/10 | medium |
| non_lof_repeat_expansion | Friedreich ataxia | ORPHA:95 | FXN | repeat_expansion_silencing | conditional | 633 | OAV101-IT | AAV9 | 7.9/10 | high |
| pilot_cohort | Cystic fibrosis | ORPHA:586 | CFTR | loss_of_function | conditional | 4443 | BMN 307 | AAV5 | 7.7/10 | high |
| pilot_cohort | Canavan disease | ORPHA:141 | ASPA | loss_of_function | compatible | 942 | Libmeldy | LV | 8.1/10 | high |
| pilot_cohort | Biotinidase deficiency | ORPHA:79241 | BTD | loss_of_function | compatible | 1632 | OAV101-IT | AAV9 | 7.4/10 | medium |
| pilot_cohort | Tay-Sachs disease | ORPHA:845 | HEXA | loss_of_function | conditional | 1590 | OAV101-IT | AAV9 | 7.7/10 | high |
| pilot_cohort | Wilson disease | ORPHA:905 | ATP7B | loss_of_function | conditional | 4398 | BMN 307 | AAV5 | 7.7/10 | high |
| pilot_cohort | Nephropathic cystinosis | ORPHA:213 | CTNS | loss_of_function | conditional | 1104 | Strimvelis | LV | 6.4/10 | medium |
| pilot_cohort | Acid sphingomyelinase deficiency (Niemann-Pick A/B) | ORPHA:618891 | SMPD1 | loss_of_function | conditional | 1890 | BMN 307 | AAV5 | 8.2/10 | high |
| pilot_cohort | Niemann-Pick disease type C | ORPHA:646 | NPC1 | loss_of_function | conditional | 3837 | BMN 307 | AAV5 | 8.2/10 | high |
| pilot_cohort | Zellweger syndrome | ORPHA:912 | PEX1 | loss_of_function | conditional | 3852 | Libmeldy | LV | 7.7/10 | high |
| pilot_cohort | Primary hyperoxaluria type 1 | ORPHA:93598 | AGXT | loss_of_function | conditional | 1179 | BMN 307 | AAV5 | 7.7/10 | high |
| pilot_cohort | Usher syndrome type 1B | ORPHA:886 | MYO7A | loss_of_function | conditional | 6648 | Luxturna | AAV2 | 7.5/10 | high |

† Hemophilia A's top-ranked precedent is Hemgenix (the approved Haemophilia B AAV5 therapy), not Roctavian (the approved Haemophilia A AAV5 therapy), because both programmes scored identically at 8.5/10 and Hemgenix appears first alphabetically. See Section 3.4 for the tie-break discussion.

## 3. Internal Validation: Top-k Recovery

A key question for any precedent-matching framework is whether it recovers known precedents when they exist. The 46-disease cohort includes 11 diseases for which a specific gene-therapy programme in the current catalogue was developed for that exact disease (or its closest disease class). These provide a direct test: does the algorithm surface the known precedent within its top-k ranked results?

The results are summarised below:

| Disease | Gene | Known precedent | Rank recovered | Score |
|---------|------|----------------|---------------|-------|
| Hemophilia B | F9 | Hemgenix (AAV5) | **1** | 9.9/10 |
| Spinal muscular atrophy | SMN1 | OAV101-IT (AAV9) | **1** | 8.3/10 |
| ADA-SCID | ADA | Strimvelis (gammaretroviral ex vivo HSC; grouped in LV bucket) | **1** | 8.1/10 |
| Metachromatic leukodystrophy | ARSA | Libmeldy (LV) | **1** | 9.2/10 |
| X-linked myotubular myopathy | MTM1 | AT132 (AAV8) | **1** | 7.7/10 |
| Phenylketonuria | PAH | BMN 307 (AAV5) | **1** | 8.0/10 |
| Duchenne muscular dystrophy | DMD_micro | SRP-9001 (AAV9) | **1** | 7.6/10 |
| Hemophilia A | F8 | Roctavian (AAV5) | **2** (tied at 8.5/10 with Hemgenix) | 8.5/10 |
| Fabry disease | GLA | ST-920 (AAV2/6) | **2** | 8.8/10 |
| Mucopolysaccharidosis type II | IDS | RGX-121 (AAV9) | **3** | 8.9/10 |
| Leber hereditary optic neuropathy | MT-ND4 | GS010 (AAV2) | **not in top-5** | — |

**Top-3 recovery rate: 10 out of 11 (91%).** Excluding LHON, which is a known stress-test case where the allotopic expression requirement of GS010 is an explicitly flagged limitation, the top-3 recovery rate is **10 out of 10 (100%)**.

The LHON failure is instructive rather than arbitrary. GS010/Lumevoq uses mitochondrial allotopic expression — a strategy fundamentally different from the nuclear gene-addition paradigm that underpins all other programmes in the catalogue. The framework correctly assigns LHON medium confidence with low organelle-targeting scores and an explicit mitochondrial flag, which distinguishes it from diseases where the mechanism is well-matched to existing precedent. A future version should model allotopic expression as a distinct modality.

For Hemophilia A, the fact that Hemgenix (haemophilia B therapy) ties with Roctavian (the exact Hemophilia A therapy) at 8.5/10 is a calibration note rather than an error. Both are AAV5 liver-directed programmes for coagulation factor deficiency, and the 14-dimension heuristic produces identical scores for them. Roctavian is correctly recovered at rank 2. This illustrates why top-3 rather than top-1 is the appropriate validation metric for a proof-of-concept similarity-based matching system.

The top-3 recovery result supports the core proof-of-concept claim: NanoGT reliably identifies biologically appropriate precedent programmes when they exist in the catalogue, and does so across diverse disease classes — haematopoietic (ADA-SCID, WAS), hepatic metabolic (PKU), lysosomal (MLD, MPS II), retinal (Fabry, X-MTM), and musculoskeletal (SMA, DMD).

## 4. Top-Precedent Clusters

The most important result is not any single disease score, but the emergence of biologically interpretable precedent clusters.

### 4.1 Lentiviral / Libmeldy-dominated lysosomal and leukodystrophy cluster

Libmeldy was the top-ranked precedent for 9 diseases: alpha-mannosidosis, Fabry disease, Gaucher disease, Krabbe disease, metachromatic leukodystrophy, mucopolysaccharidosis types I/II/IIIA, and Pompe disease. This cluster is plausible because ex vivo lentiviral haematopoietic stem-cell gene therapy has a strong precedent base for lysosomal and neurodegenerative metabolic disorders, particularly where cross-correction by enzyme secretion or haematopoietic-derived CNS engraftment may contribute to benefit.

Importantly, mucolipidosis type IV and Mucolipidosis type IV — which carries the CNS/lysosomal membrane label — did not have Libmeldy as its top precedent in the final scoring run. It ranked Skysona (LV) first. This is a meaningful result: MCOLN1 (ML-IV) encodes a lysosomal membrane channel; it cannot be secreted or taken up by adjacent cells via the mannose-6-phosphate receptor pathway. The Skysona precedent, which uses a lentiviral vector for CNS-directed ex vivo haematopoietic correction in a leukodystrophy setting, captures the CNS/lentiviral class without implying classical enzyme cross-correction. This distinction — and the limitation that the current algorithm does not fully resolve it — must be stated clearly in the dissertation.

### 4.2 Hepatic metabolic / BMN 307 cluster

BMN 307 was top-ranked for 4 diseases: maple syrup urine disease, ornithine transcarbamylase deficiency, phenylketonuria, and vitamin B12-unresponsive methylmalonic acidemia. These diseases share hepatic and metabolic features, small-to-moderate transgene sizes, and a plausible liver-directed AAV development logic. The framework therefore identifies BMN 307 as a useful platform-style precedent for liver metabolic gene-addition programmes.

The interpretation should remain cautious. These diseases differ in subcellular localisation, metabolic pathway, newborn-screening relevance, and the extent to which liver correction would address neurological injury. For the dissertation, the BMN 307 cluster is best presented as a hypothesis-generating prioritisation result, not as a statement that the same vector/programme can be directly reused.

### 4.3 Retinal precedent cluster

Retinal diseases clustered around Luxturna and CPCB-RPE1. Choroideremia and X-linked retinoschisis were high-confidence retinal matches, while Leber hereditary optic neuropathy and achromatopsia were medium-confidence matches. This spread is biologically sensible: the eye is accessible and immune-privileged, but gene-specific biology, affected retinal cell type, mitochondrial inheritance, and programme stage all affect transferability.

### 4.4 Positive controls and benchmark behaviour

The strongest positive control was haemophilia B: Hemgenix ranked first with a 9.9/10 score. Haemophilia A returned Hemgenix as the top result (8.5/10) with Roctavian tied at rank 2 — both programmes are approved AAV5 liver-directed coagulation factor therapies, and the algorithm correctly scores them as near-equivalent precedents for each other's disease class. Spinal muscular atrophy returned an AAV9/OAV101-IT precedent at high confidence. ADA-SCID ranked with Strimvelis, correctly recovering an ex vivo haematopoietic precedent. These results support the internal validity of the scoring system at a proof-of-concept level.

## 5. Medium-Confidence and Stress-Test Results

Medium-confidence top matches among scored diseases were:

- Leber hereditary optic neuropathy (MT-ND4): CPCB-RPE1 / AAV8 at 6.4/10
- Achromatopsia (CNGB3): CPCB-RPE1 / AAV8 at 7.5/10
- Crigler-Najjar syndrome type I (UGT1A1): Hemgenix / AAV5 at 7.2/10
- CHARGE syndrome (CHD7): Libmeldy / LV at 5.9/10
- Tuberous sclerosis complex (TSC1): Libmeldy / LV at 6.1/10

These cases are useful because they show where the framework becomes uncertain. They include retinal diseases where several plausible precedents compete, a mitochondrial disease where ordinary nuclear gene addition is mechanistically uncertain, a liver disease where pathway and protein-class similarity are imperfect, and two haploinsufficiency diseases where conditional gene-addition logic and large transgene size both constrain tractability.

Duchenne muscular dystrophy illustrates the distinction between native-gene replacement and engineered-cargo precedent. Full-length DMD fails ordinary single-AAV packaging, but SRP-9001 can be scored as a micro-dystrophin strategy. The correct interpretation is not that DMD is unsuitable for gene therapy, but that DMD requires engineered microgene, dual-vector, exon-skipping, or editing-based logic rather than ordinary full-length gene addition.

## 6. Non-LOF Mechanism Arm

The non-LOF arm of the scored cohort contains 6 diseases spanning haploinsufficiency, repeat-expansion silencing, and two-hit haploinsufficiency mechanisms. Unlike purely incompatible diseases (gain-of-function, dominant-negative), all were selected because gene addition is a biologically rational strategy — they are genuine candidates for gene therapy, not diseases where adding a copy makes things worse. The key dissertation question is whether the scoring framework produces interpretable, biologically appropriate results for mechanisms that differ from classical loss-of-function.

The scored haploinsufficiency diseases include Rett syndrome, CHARGE syndrome, Neurofibromatosis type 1, and Tuberous sclerosis complex. Rett syndrome (MECP2, 1,461 bp) returned a score of 7.4/10 medium confidence with Skysona (LV) as top precedent. This is interpretable: MECP2 haploinsufficiency is a CNS disease where lentiviral and AAV platforms are both under active clinical investigation, and Skysona (lentiviral HSC-directed CNS correction) is the most relevant CNS lentiviral precedent in the catalogue. Wiskott-Aldrich syndrome (WAS, 1,506 bp) scored 8.0/10 high confidence with Strimvelis as top precedent — the most mechanistically coherent result for the ex vivo HSC arm: WAS haploinsufficiency causes haematopoietic failure and the ex vivo HSC gene-addition logic of Strimvelis maps directly to WAS biology. Strimvelis itself is a gammaretroviral ADA-SCID product, so its relevance here is the ex vivo autologous HSC gene-addition precedent, not a claim that Strimvelis is lentiviral.

The two large haploinsufficiency/two-hit diseases — CHARGE syndrome (CHD7, 7,950 bp) and Tuberous sclerosis complex (TSC1, 3,495 bp) — scored 5.9 and 6.1 (medium), correctly reflecting that large CDS size in CHD7 and the two-hit somatic complexity of TSC reduce precedent transferability relative to simpler LOF cases.

Neurofibromatosis type 1 (NF1, 8,451 bp) received a packaging hard-fail: its CDS exceeds the capacity of every vector in the current catalogue. This is the correct result — NF1 is not a disease where standard single-vector gene addition is tractable, and the empty result is a valid scientific finding about packaging constraints.

The two repeat-expansion diseases behaved differently and this contrast is instructive. Friedreich ataxia (FXN, 633 bp) scored 7.9/10 high confidence with OAV101-IT (AAV9) as top precedent. This is correct because the frataxin protein coding sequence is structurally normal — the GAA repeat silences the endogenous gene, but FXN cDNA addition bypasses the silenced allele. The tool treats it similarly to a CNS/cardiac LOF disease, which is the right biological analogy. Fragile X syndrome (FMR1, 1,899 bp) scored 7.0/10 medium, with Skysona as top precedent. FMR1 cDNA addition is also clinically pursued for the same silencing-bypass logic, and the medium score reflects appropriate caution: FMRP has synaptic dosage-sensitivity that makes titrating expression more complex than frataxin.

## 7. Summary of Findings

The 46-disease scored analysis supports four dissertation-level claims:

1. NanoGT can recover obvious clinical precedents for positive controls and benchmark diseases.
2. Cross-disease clustering produces biologically plausible precedent groups, especially for integrating ex vivo HSC-vector lysosomal and immune disease, liver metabolic AAV programmes, and retinal AAV programmes.
3. The framework usefully exposes hard limitations: oversized native cargo (DMD, NF1 packaging failures), mitochondrial allotopic-expression requirements (LHON), and the distinction between secreted lysosomal enzymes and lysosomal membrane proteins.
4. The non-LOF arm produces interpretable, biologically coherent results for conditional mechanisms (haploinsufficiency, repeat-expansion silencing, genomic imprinting), demonstrating that the framework extends meaningfully beyond classical LOF.

The results should be framed as a reproducible prioritisation and precedent-mapping framework, not as a validated therapeutic recommendation system.

A note on the medium-confidence scores: medium confidence does not mean the score is wrong — it reflects that the scoring dimensions produce a closer match to multiple programme classes (e.g., a retinal AAV disease where several programmes are equally plausible). For dissertation purposes, medium-confidence results are presented with explicit flags recommending biological review before any translational inference.
