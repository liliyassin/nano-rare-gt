# Abstract

## Background

Most monogenic rare diseases have no disease-modifying treatment, even when the causal gene is known. Gene therapy is partly a platform technology: vector tropism, manufacturing, route of administration, safety monitoring, and regulatory precedent from one programme can reduce uncertainty for another biologically adjacent disease. The unresolved problem is how to identify defensible precedents systematically rather than by ad hoc expert review.

## Methods

NanoGT was implemented as a Python command-line framework that matches Orphanet-indexed monogenic diseases to a curated catalogue of approved or clinical-stage gene therapy programmes. Each disease-program pair is scored across fourteen dimensions: packaging fit, tissue tropism, protein class, pathway similarity, molecular mechanism/modality compatibility, inheritance compatibility, approval precedent, vector immunogenicity, therapeutic window, cross-correction potential, immune privilege, promoter availability, route-of-administration feasibility, and organelle targeting feasibility. Scores are summed to a raw maximum of 21 and normalised to a 10-point composite confidence score. The current dissertation cohort contains 46 diseases: three positive controls with approved gene-therapy precedents (Hemophilia A, Hemophilia B, Spinal muscular atrophy), one benchmark disease with a known gene-therapy precedent (ADA-SCID), one oversized-cargo stress test (Duchenne muscular dystrophy), one mitochondrial-delivery stress test (Leber hereditary optic neuropathy), 34 pilot cohort diseases spanning lysosomal, hepatic metabolic, retinal, and neuromuscular indications, four haploinsufficiency diseases, and two repeat-expansion/silencing diseases.

## Results

The framework generated scored precedents for 45 of 46 diseases; Neurofibromatosis type 1 received a packaging hard-fail because its 8,451 bp coding sequence exceeds the capacity of every vector in the catalogue. Among the 45 scored diseases, 36 received high-confidence top matches and 8 received medium-confidence top matches. Duchenne muscular dystrophy failed the ordinary full-length native-gene packaging gate but was ranked through an engineered micro-dystrophin precedent. Composite scores ranged from 5.9/10 to 9.9/10. Libmeldy/lentiviral haematopoietic stem-cell therapy dominated lysosomal and leukodystrophy-like diseases, BMN 307 supported hepatic metabolic disorders, retinal diseases clustered around Luxturna/CPCB-RPE1 precedents, and the non-LOF arm produced biologically coherent medium-confidence matches for haploinsufficiency and repeat-expansion diseases.

## Conclusions

NanoGT supports dissertation-level proof-of-concept claims: it recovers expected clinical precedents at a 91% top-3 rate across 11 known-precedent diseases, identifies coherent cross-disease precedent clusters, and correctly exposes cases where a standard single-vector gene-addition strategy is physically infeasible or mechanistically mismatched. It should not be framed as a clinical recommendation engine; composite scores represent relative precedent strength, not probabilities of therapeutic success.

**Keywords:** gene therapy, rare disease, monogenic disease, Orphanet, AAV, lentiviral vector, precedent matching, computational biology
