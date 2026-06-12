# Paper Architecture — NanoGT Dissertation Report

Updated: Thursday 11 June 2026.

## Working title

NanoGT: A Computational Framework for Mapping Monogenic Rare Diseases to Gene-Therapy Development Precedents

## Core dissertation claim

NanoGT is a proof-of-concept framework for computational gene-therapy precedent mapping. In a 30-disease monogenic rare-disease cohort, it generated interpretable disease-precedent clusters, recovered several expected clinical precedents, and flagged obvious scope failures such as full-length DMD packaging incompatibility.

Do not claim clinical readiness, regulatory acceptance, or therapeutic efficacy.

## Section plan

| Section | Target words | Current priority |
|---|---:|---|
| Abstract | 250–300 | Match the 30-disease results |
| Introduction | 1,000–1,300 | Rare disease treatment gap + gene therapy platform precedent problem |
| Methods | 1,800–2,300 | Actual Python implementation, data sources, 12 scoring dimensions |
| Results | 1,800–2,300 | 30-disease table, clusters, validation, stress tests |
| Discussion | 1,800–2,300 | Interpretation, limits, future work, dissertation-safe framing |
| References | As required | Only cite papers/sources actually checked |
| Supplementary | As needed | Cohort CSV, surrogate catalogue, full scoring outputs |

## Figures needed

1. Thirty-disease score distribution.
2. Disease-to-precedent cluster visual.
3. Validation/stress-test examples: Hemophilia B, SMA, LCA calibration issue, DMD packaging failure.

## Tables needed

1. 30-disease cohort result table.
2. Surrogate catalogue table.
3. Scoring dimensions table.
4. Limitations/future-work mapping table.

## Must-fix before final submission

- Every disease fact in `data/disease_cohort_30.csv` must be source-checked.
- Reference section must not contain placeholders.
- Results must use the 30-disease output, not an earlier pilot output.
- Validation must be framed honestly, including the LCA/Luxturna calibration issue.
- Limitations must be explicit and not hidden in vague "future work" language.
