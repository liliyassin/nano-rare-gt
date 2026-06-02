# Results

## 1. Dataset Overview

The NanoGT framework was applied to ten monogenic rare diseases: two retrospective validation cases with existing approved gene therapies, and eight prospective discovery cases for which no approved gene therapy currently exists. Across all ten diseases, 180 disease-program pairs were scored (10 diseases × 18 surrogate programs). The curated surrogate database comprised 18 gene therapy programs delivered via 8 vector serotypes, spanning six disease areas: coagulation disorders, motor neuron disease, lysosomal storage disorders, retinal dystrophies, metabolic liver diseases, and myopathies. Approved programs accounted for 7 of the 18 database entries; the remainder were in Phase 1 through Phase 3 clinical trials.

---

## 2. Retrospective Validation

To assess whether the scoring engine correctly identifies known gene therapy solutions, the framework was applied to two diseases for which approved therapies exist: Spinal Muscular Atrophy (SMA, ORPHA:70) and Haemophilia B (ORPHA:306).

### 2.1 Spinal Muscular Atrophy (ORPHA:70)

SMA is caused by loss-of-function mutations in *SMN1* (CDS: 891 bp, autosomal recessive), encoding the survival motor neuron protein. The approved gene therapy is onasemnogene abeparvovec (Zolgensma, AAV9), which delivers a functional *SMN1* transgene to motor neurons via intravenous or intrathecal injection.

The framework ranked OAV101-IT (the intrathecal formulation of Zolgensma, AAV9) and Zolgensma jointly as the top matches, each scoring 7.7/10 (high confidence). The two programs are functionally equivalent — same vector serotype, same transgene, differing only in route of administration — and their joint top ranking reflects this equivalence. The correct identification of the approved therapy as the top-ranked match constitutes a successful positive control. Dimension scores showed perfect matches across packaging fit (2.0/2.0: 891 bp gene utilising 19% of AAV9 capacity), tissue tropism (2.0/2.0: AAV9 reaches CNS and motor neurons), biological pathway (2.0/2.0: motor neuron pathway match), inheritance compatibility (1.0/1.0: AR-to-AR match), and regulatory approval (1.0/1.0: approved). The composite score was primarily limited by the cross-correction score (0.2/1.0), reflecting the intracellular nature of the SMN1 protein, and the therapeutic window score (0.5/2.0), which correctly flagged SMA as a neonatal-onset disease requiring very early intervention.

### 2.2 Haemophilia B (ORPHA:306)

Haemophilia B is caused by loss-of-function mutations in *F9* (CDS: 1,383 bp, X-linked recessive), encoding coagulation Factor IX, a secreted protein produced by the liver. The approved gene therapy is etranacogene dezaparvovec (Hemgenix, AAV5), which delivers a high-activity *FIX* variant to liver cells via intravenous infusion.

The framework ranked Hemgenix as the joint top match at 9.1/10 (high confidence), tied with Roctavian (also AAV5, liver-targeted, approved for the closely related Haemophilia A). Hemgenix received the highest composite score of any match across all ten diseases tested. Perfect scores were achieved for packaging fit (2.0/2.0: 29% cargo utilisation), tissue tropism (2.0/2.0), protein class (2.0/2.0: both secreted coagulation factors), biological pathway (2.0/2.0: exact coagulation pathway match), inheritance (1.0/1.0: XL-to-XL), regulatory approval (1.0/1.0), immunogenicity (2.0/2.0: AAV5 seroprevalence ~9%), cross-correction (1.0/1.0: secreted protein), promoter availability (1.0/1.0), and route of administration (1.0/1.0). The score was reduced only by therapeutic window (0.5/2.0) and immune privilege (0.8/1.0). The therapeutic window score reflects the absence of explicit adult-onset HPO keywords in the Haemophilia B dataset — a known limitation of HPO-based window inference for episodic bleeding disorders, discussed further in the Discussion. The correct top-ranking of the approved therapy at 9.1/10 confirms successful framework validation.

---

## 3. Prospective Discovery Results

The framework was applied to eight diseases for which no approved gene therapy currently exists. Composite scores ranged from 7.6/10 to 8.6/10 across seven diseases, with one outlier at 6.8/10. Seven of eight diseases received a high-confidence classification (≥7.5/10). All results are summarised in Table 2.

### 3.1 Fabry Disease (ORPHA:324) — Score: 8.6/10

Fabry disease results from loss-of-function mutations in *GLA* (CDS: 1,290 bp, X-linked dominant), encoding alpha-galactosidase A, a secreted lysosomal enzyme. The framework identified ST-920 (AAV2/6, liver-targeted, Phase 1/2) as the top precedent match at 8.6/10, the highest score among all eight discovery diseases. The result was driven by strong performance across protein class (2.0/2.0: both secreted lysosomal enzymes with cross-correction potential via the mannose-6-phosphate receptor pathway), biological pathway (2.0/2.0: lysosomal storage), and cross-correction (1.0/1.0). The multi-tissue involvement of Fabry disease (liver, kidney, heart, CNS) additionally contributed to full scores for promoter availability and route of administration. These findings are consistent with the current clinical landscape, in which ST-920 and AVR-RD-01 (the second and third ranked matches) are both active clinical programs specifically for Fabry disease, providing independent corroboration of the framework's output.

### 3.2 Mucolipidosis Type IV (ORPHA:578) — Score: 8.4/10

Mucolipidosis type IV is caused by loss-of-function mutations in *MCOLN1* (CDS: 1,740 bp, autosomal recessive), encoding mucolipin-1, a lysosomal membrane ion channel affecting the CNS and retina. ABO-101 and RGX-121 (both AAV9, intrathecal CNS delivery) were jointly ranked as top matches at 8.4/10. The high score reflects a strong tropism match (AAV9 crosses the blood-brain barrier), matching lysosomal protein class, high immune privilege of CNS and retinal tissues (0.9/1.0 and 1.0/1.0 respectively), and full scores for promoter availability and route of administration. No active gene therapy program currently exists for Mucolipidosis type IV; the framework identifies an AAV9-based intrathecal approach modelled on the MPS III precedent as the most scientifically supported development pathway.

### 3.3 Mucopolysaccharidosis Type IIIA / Sanfilippo A (ORPHA:79269) — Score: 8.3/10

Sanfilippo A is caused by loss-of-function mutations in *SGSH* (CDS: 1,674 bp, autosomal recessive), encoding a lysosomal sulphohydrolase. The top match was ABO-101 (AAV9, CNS-targeted, 8.3/10), an active clinical program for the closely related disorder Sanfilippo B (MPS IIIB, caused by *NAGLU* deficiency). The framework correctly identified a closely related lysosomal storage disorder sharing the same target tissue, vector serotype, and protein class. The therapeutic window score of 1.5/2.0 correctly reflects the progressive neurodegeneration characteristic of Sanfilippo syndrome, where early intervention substantially alters outcome but neonatal delivery is not strictly required.

### 3.4 Salla Disease (ORPHA:309) — Score: 8.2/10

Salla disease is caused by loss-of-function mutations in *SLC17A5* (CDS: 1,485 bp, autosomal recessive), encoding sialin, a lysosomal sialic acid transporter expressed in the CNS. The top matches were ABO-101 and RGX-121 (both AAV9, 8.2/10). CNS-only tissue involvement, lysosomal transporter protein class, and AR inheritance drove the strong match to existing CNS lysosomal storage precedents. No gene therapy program currently exists for Salla disease.

### 3.5 Alpha-Mannosidosis (ORPHA:61) — Score: 7.8/10

Alpha-mannosidosis results from loss-of-function mutations in *MAN2B1* (CDS: 3,033 bp, autosomal recessive), encoding lysosomal alpha-mannosidase. The top match was AVR-RD-01 (lentiviral vector, ex vivo haematopoietic stem cell delivery, 7.8/10), tied with ST-920 (AAV2/6, liver-targeted). The relatively large gene size (3,033 bp, 65% of AAV9 cargo capacity) reduced the packaging score compared to smaller-gene diseases but did not trigger a hard packaging fail. The lentiviral approach scored well because it is unconstrained by AAV packaging limits, carries near-zero pre-existing human immunity (seroprevalence ~2%), and targets haematopoietic stem cells capable of providing lysosomal enzyme cross-correction throughout the body. This recommendation is consistent with the ex vivo lentiviral strategy used in approved programs for other lysosomal storage diseases.

### 3.6 Maple Syrup Urine Disease (ORPHA:511) — Score: 7.6/10

Maple syrup urine disease (MSUD) is caused by loss-of-function mutations in *BCKDHA* (CDS: 1,335 bp, autosomal recessive), encoding a subunit of the mitochondrial branched-chain keto acid dehydrogenase complex. The top match was BMN 307 (AAV5, liver-targeted, Phase 2), a clinical program for phenylketonuria (PKU) — another amino acid metabolism disorder sharing the same hepatic target tissue and pathway grouping. The cross-correction score was low (0.2/1.0), reflecting the intracellular mitochondrial localisation of BCKDHA. The framework identifies a liver-directed AAV5 approach modelled on PKU precedent as the best-supported strategy.

### 3.7 Kohlschütter-Tönz Syndrome (ORPHA:1946) — Score: 7.6/10

Kohlschütter-Tönz syndrome (KTS) is caused by loss-of-function mutations in *ROGDI* (CDS: 861 bp, autosomal recessive), encoding a synaptic scaffolding protein associated with Rabconnectin-3 and V-ATPase biology. The top matches were OAV101-IT and Zolgensma (both AAV9, CNS-targeted, 7.6/10). The small gene (861 bp, 18% of AAV9 capacity) conferred a perfect packaging score. However, the absence of a clear pathway match — ROGDI biology does not map to any of the predefined pathway groups — and the intracellular nature of the protein limited the composite score. This case illustrates a constraint of the current framework: diseases involving novel or poorly characterised biological pathways have no exact pathway precedent, and receive a neutral rather than a positive pathway score.

### 3.8 Crigler-Najjar Syndrome Type I (ORPHA:1060) — Score: 6.8/10 (Medium Confidence)

Crigler-Najjar syndrome type I is caused by loss-of-function mutations in *UGT1A1* (CDS: 1,596 bp, autosomal recessive), encoding UDP-glucuronosyltransferase 1-1, an intracellular endoplasmic reticulum membrane enzyme responsible for hepatic bilirubin conjugation. The top match was Hemgenix (AAV5, liver-targeted, 6.8/10) — the only disease in this study to receive a medium rather than high confidence rating.

The lower score reflects a fundamental biological distinction from the other liver-targeted diseases in this study. UGT1A1 is an intracellular, membrane-bound enzyme that cannot be secreted or cross-correct neighbouring hepatocytes (cross-correction score: 0.2/1.0). The majority of approved liver gene therapy precedents target secreted proteins — Factor IX, Factor VIII — creating a protein class mismatch for Crigler-Najjar (class match score: 0.5/2.0 for the top match). Pathway similarity was also limited, as UGT1A1 participates in glucuronidation with no direct analogue in the current database (pathway score: 1.0/2.0, neutral). The medium confidence rating does not indicate that gene therapy is infeasible for Crigler-Najjar — liver-directed AAV delivery of *UGT1A1* has been investigated in clinical trials — but indicates that no existing approved program offers a close biological precedent across all twelve dimensions simultaneously, and that the development path carries a higher degree of novelty than for diseases scoring in the high-confidence range.

---

## 4. Score Distribution and Summary

Composite scores across all ten diseases ranged from 6.8/10 to 9.1/10, with a mean of 7.97/10. Nine of ten diseases achieved high confidence (≥7.5/10). The two validation diseases were correctly identified as top-ranked matches by the framework, with Haemophilia B producing the highest overall score (9.1/10) and SMA producing a high-confidence match at 7.7/10. Among the eight discovery diseases, scores clustered in the 7.6–8.6/10 range, with Crigler-Najjar as the sole medium-confidence outlier at 6.8/10.

**Table 2: NanoGT results across all ten diseases (12-dimension scoring, normalised to 10).**

| Disease | ORPHA | Gene | CDS (bp) | Top Precedent | Vector | Score | Confidence |
|---------|-------|------|----------|---------------|--------|-------|-----------|
| Haemophilia B *(validation)* | 306 | F9 | 1,383 | Hemgenix | AAV5 | 9.1 | High |
| Spinal Muscular Atrophy *(validation)* | 70 | SMN1 | 891 | OAV101-IT | AAV9 | 7.7 | High |
| Fabry disease | 324 | GLA | 1,290 | ST-920 | AAV2/6 | 8.6 | High |
| Mucolipidosis type IV | 578 | MCOLN1 | 1,740 | ABO-101 | AAV9 | 8.4 | High |
| Mucopolysaccharidosis type IIIA | 79269 | SGSH | 1,674 | ABO-101 | AAV9 | 8.3 | High |
| Salla disease | 309 | SLC17A5 | 1,485 | ABO-101 | AAV9 | 8.2 | High |
| Alpha-mannosidosis | 61 | MAN2B1 | 3,033 | AVR-RD-01 | LV | 7.8 | High |
| Maple syrup urine disease | 511 | BCKDHA | 1,335 | BMN 307 | AAV5 | 7.6 | High |
| Kohlschütter-Tönz syndrome | 1946 | ROGDI | 861 | OAV101-IT | AAV9 | 7.6 | High |
| Crigler-Najjar syndrome type I | 1060 | UGT1A1 | 1,596 | Hemgenix | AAV5 | 6.8 | Medium |

*Scores rounded to one decimal place. Validation cases in italics.*
