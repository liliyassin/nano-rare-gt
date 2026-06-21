# Abstract

## Background

Most monogenic rare diseases have no disease-modifying treatment, even when the causal gene is known. Gene therapy is partly a platform technology: vector tropism, manufacturing, route of administration, safety monitoring, and regulatory precedent from one programme can reduce uncertainty for another biologically adjacent disease. The unresolved problem is how to identify defensible precedents systematically rather than by ad hoc expert review.

## Methods

NanoGT was implemented as a Python command-line framework that matches Orphanet-indexed monogenic diseases to a curated catalogue of approved or clinical-stage gene therapy programmes. Each disease-program pair is scored across fourteen dimensions: packaging fit, tissue tropism, protein class, pathway similarity, molecular mechanism/modality compatibility, inheritance compatibility, approval precedent, vector immunogenicity, therapeutic window, cross-correction potential, immune privilege, promoter availability, route-of-administration feasibility, and organelle targeting feasibility. Scores are summed to a raw maximum of 21 and normalised to a 10-point composite confidence score. The current dissertation cohort contains 40 diseases: two positive controls, two benchmark diseases with known gene-therapy precedents, one oversized-cargo stress test, one mitochondrial stress test, 24 pilot discovery diseases, six haploinsufficiency diseases, two repeat-expansion/silencing diseases, one genomic imprinting disease, and one two-hit haploinsufficiency disease.

## Results

The framework generated scored precedents for 39 of 40 diseases; Neurofibromatosis type 1 received a packaging hard-fail because its 8,451 bp coding sequence exceeds the capacity of every vector in the catalogue. Among the 39 scored diseases, 32 received high-confidence top matches and 7 received medium-confidence top matches. Duchenne muscular dystrophy failed the ordinary full-length native-gene packaging gate but was ranked through an engineered micro-dystrophin precedent. Composite scores ranged from 5.9/10 to 9.9/10. Libmeldy/lentiviral haematopoietic stem-cell therapy dominated lysosomal and leukodystrophy-like diseases, BMN 307 supported hepatic metabolic disorders, retinal diseases clustered around Luxturna/CPCB-RPE1 precedents, and the non-LOF arm produced biologically coherent medium-confidence matches for haploinsufficiency, repeat-expansion, and imprinting diseases.

## Conclusions

NanoGT currently supports dissertation-level proof-of-concept claims: it can reproduce obvious clinical precedents, identify coherent cross-disease precedent clusters, and expose cases where a standard single-vector gene-addition strategy is weak or physically infeasible. It should not be framed as a clinical recommendation engine. The next month of work must prioritise source verification, reference reading, limitation handling, figure quality, and report writing rather than further scope expansion.

**Keywords:** gene therapy, rare disease, monogenic disease, Orphanet, AAV, lentiviral vector, precedent matching, computational biology
