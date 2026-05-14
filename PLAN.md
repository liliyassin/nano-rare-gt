# Bridging the Nano-Rare Gap: A Computational Framework for Accelerating Gene Therapy Development via Structural Homology and Clinical Surrogates

## Problem Statement

Nano-rare monogenic diseases (especially homozygous loss-of-function) affect small patient populations but collectively represent a massive unmet need. Each disease individually is commercially unviable for a dedicated gene therapy program, yet many could be treated by repurposing vectors, cargo designs, and delivery strategies already validated in approved or late-stage therapies.

The core problem: there is no systematic computational framework that matches untreated nano-rare monogenic diseases with viable gene therapy surrogates — considering biology, engineering, regulatory, and commercial dimensions simultaneously.

## Goal

Create a systematic multi-parameter computational framework that matches untreated nano-rare monogenic diseases with approved or late-stage gene therapies, to dramatically de-risk and accelerate development using surrogate precedents.

## Dimensions to Evaluate (The Algorithm)

1. Structural and sequence homology + domain similarity (AlphaFold / Foldseek)
2. Gene / CDS size compatibility (AAV packaging limits ~4.7kb)
3. Target cell types and tissue tropism (Schilder-style mapping, single-cell data)
4. Route of Administration (RoA) and delivery precedent
5. Promoter / regulatory element matching (expression patterns via TiProD, GEO/GTEx)
6. Protein localization and function (intracellular vs secreted, cross-correction potential)
7. Immunogenicity risk (IEDB epitope prediction for the transgene)
8. Therapeutic window and overexpression toxicity risks
9. Codon optimization feasibility (CAI scoring)

## Data Sources to Mine

- Orphanet — high-morbidity monogenic diseases with no active clinical trials
- OMIM — gene-disease relationships, inheritance patterns
- ClinVar — pathogenic variant validation
- UniProt / AlphaFold DB — structural and sequence data
- GTEx / GEO / TiProD — expression and promoter data
- IEDB — immunogenicity prediction
- ClinicalTrials.gov — active/pending gene therapy trials to identify surrogate precedents
- FDA/EMA approvals — approved GT products as gold-standard precedents

## Outputs Required

1. Scoring matrix + ranking system for disease-GT surrogate matches
2. Detailed "Standardised Gene Therapy Protocol" for top-ranked matches
3. Retrospective validation case study (≥1 known successful repurposing)
4. Regulatory, manufacturing, and IP analysis section
5. Risk mitigation framework per match

## Key Risks / Open Questions

- What is the minimum acceptable structural homology threshold for functional surrogacy?
- How to weight cross-correction potential vs direct protein replacement?
- Which regulatory pathway is fastest for a "surrogate precedent" claim?
- Platform designation eligibility (RMAT, PRIME, Breakthrough Therapy)
- CMC requirements when switching cargo in an established AAV serotype
- IP constraints on vector serotypes, promoters, and regulatory elements
