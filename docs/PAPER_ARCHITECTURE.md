# Paper Architecture — NanoGT Dissertation Report

Updated: Sunday 21 June 2026.

## Working title

NanoGT: A Computational Framework for Mapping Monogenic Rare Diseases to Gene-Therapy Development Precedents

## Core dissertation claim

NanoGT is a proof-of-concept framework for computational gene-therapy precedent mapping. In a 40-disease monogenic rare-disease cohort, it generated interpretable disease-precedent clusters, recovered several expected clinical precedents, and correctly flagged NF1 as a packaging hard-fail (8,451 bp CDS exceeds all catalogued vectors).

Do not claim clinical readiness, regulatory acceptance, or therapeutic efficacy.

## Section plan

| Section | Target words | Current priority |
|---|---:|---|
| Abstract | 250–300 | Match the 40-disease results |
| Introduction | 1,000–1,300 | Rare disease treatment gap + gene therapy platform precedent problem |
| Methods | 1,800–2,300 | Actual Python implementation, data sources, 14 scoring dimensions |
| Results | 1,800–2,300 | 40-disease table, clusters, validation, stress tests |
| Discussion | 1,800–2,300 | Interpretation, limits, future work, dissertation-safe framing |
| References | As required | Only cite papers/sources actually checked |
| Supplementary | As needed | Cohort CSV, surrogate catalogue, full scoring outputs |

## Figures needed

1. Forty-disease score distribution.
2. Disease-to-precedent cluster visual.
3. Validation/stress-test examples: Hemophilia B, SMA, LCA calibration issue, DMD packaging failure.

## Tables needed

1. 40-disease cohort result table.
2. Surrogate catalogue table.
3. Scoring dimensions table.
4. Limitations/future-work mapping table.

## Must-fix before final submission

- Every disease fact in `data/disease_cohort_40.csv` must be source-checked.
- Reference section must not contain placeholders.
- Results must use the 40-disease output, not an earlier pilot output.
- Validation must be framed honestly, including the LCA/Luxturna calibration issue.
- Limitations must be explicit and not hidden in vague "future work" language.
