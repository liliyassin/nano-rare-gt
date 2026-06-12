# Abstract

## Background

Most monogenic rare diseases have no disease-modifying treatment, even when the causal gene is known. Gene therapy is partly a platform technology: vector tropism, manufacturing, route of administration, safety monitoring, and regulatory precedent from one programme can reduce uncertainty for another biologically adjacent disease. The unresolved problem is how to identify defensible precedents systematically rather than by ad hoc expert review.

## Methods

NanoGT was implemented as a Python command-line framework that matches Orphanet-indexed monogenic diseases to a curated catalogue of approved or clinical-stage gene therapy programmes. Each disease-program pair is scored across twelve dimensions: packaging fit, tissue tropism, protein class, pathway similarity, inheritance compatibility, approval precedent, vector immunogenicity, therapeutic window, cross-correction potential, immune privilege, promoter availability, and route-of-administration feasibility. Scores are summed to a raw maximum of 18 and normalised to a 10-point composite confidence score. The current dissertation cohort contains 30 diseases: four positive/benchmark controls, one oversized-cargo stress test, one mitochondrial stress test, and 24 pilot discovery diseases.

## Results

The framework generated results for all 30 diseases. Twenty-nine diseases had at least one compatible single-vector precedent; Duchenne muscular dystrophy failed the native-gene packaging gate, as expected for an 11,055 bp dystrophin coding sequence. Among compatible diseases, 23 of 29 received high-confidence matches and 6 received medium-confidence matches. Scores ranged from 6.8/10 to 9.9/10, with mean 8.20/10 and median 8.1/10. Libmeldy/lentiviral haematopoietic stem-cell therapy dominated lysosomal and leukodystrophy-like diseases, while BMN 307 supported several hepatic metabolic disorders and retinal diseases clustered around Luxturna/CPCB-RPE1 precedents.

## Conclusions

NanoGT currently supports dissertation-level proof-of-concept claims: it can reproduce obvious clinical precedents, identify coherent cross-disease precedent clusters, and expose cases where a standard single-vector gene-addition strategy is weak or physically infeasible. It should not be framed as a clinical recommendation engine. The next month of work must prioritise source verification, reference reading, limitation handling, figure quality, and report writing rather than further scope expansion.

**Keywords:** gene therapy, rare disease, monogenic disease, Orphanet, AAV, lentiviral vector, precedent matching, computational biology
