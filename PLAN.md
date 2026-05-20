# Bridging the Nano-Rare Gap: A Computational Framework for Accelerating Gene Therapy Development via Structural Homology and Clinical Surrogates

## Problem Statement

Nano-rare monogenic diseases (especially homozygous loss-of-function) affect small patient populations but collectively represent a massive unmet need. Each disease individually is commercially unviable for a dedicated gene therapy program, yet many could be treated by repurposing vectors, cargo designs, and delivery strategies already validated in approved or late-stage therapies.

The core problem: there is no systematic computational framework that matches untreated nano-rare monogenic diseases with viable gene therapy surrogates — considering biology, engineering, regulatory, and commercial dimensions simultaneously.

## Goal

Create a systematic multi-parameter computational framework that matches untreated nano-rare monogenic diseases with approved or late-stage gene therapies, to dramatically de-risk and accelerate development using surrogate precedents.

## Primary Case Study: ROGDI / Kohlschütter-Tönz Syndrome

**Why ROGDI:** Requested by supervisor as the illustrative deep-dive. KTS represents a strong but challenging nano-rare target: AR inheritance, well-defined gene (ROGDI; UniProt Q9GZN7; 287 aa; amino-acid coding region ~861 bp / 864 bp including stop codon — well under AAV capacity), CNS + dental phenotype, no current disease-modifying therapy, and emerging biology linking ROGDI to Rabconnectin-3 / V-ATPase-associated intracellular function. The framework must produce a full Standardised Gene Therapy Protocol for ROGDI as its first validated output, while being explicit that this is a CNS-first, cell-autonomous rescue problem rather than a simple enzyme-replacement program.

**ROGDI Quick Facts:**
- Gene: ROGDI (aliases include KIAA0267, FLJ22386, RAV2) — chr16p12.1, 11 exons
- Orphanet: ORPHA:1946 (Kohlschütter-Tönz syndrome / amelocerebrohypohidrotic syndrome)
- OMIM phenotype: 226750; OMIM gene: 614574
- UniProt: Q9GZN7 — Protein rogdi homolog
- Protein: 287 aa, ~32.3 kDa, intracellular/non-secreted
- Structural/domain evidence: PDB 5XQH/5XQI; InterPro IPR028241; Pfam PF10259; ROGDI/RAVE2-like scaffold/adaptor biology
- Estimated amino-acid coding region: ~861 bp, or 864 bp if including stop codon — **well within AAV packaging**
- Relevant tissues/cells: CNS neurons/presynaptic compartments, ameloblast-lineage tooth tissue during enamel development, possibly renal tubules in cases with nephrocalcinosis
- Phenotype: Amelogenesis imperfecta, early-onset epilepsy, severe developmental delay / intellectual disability / regression, spasticity, hypohidrosis, nephrocalcinosis reported in some cases
- Inheritance: Autosomal recessive loss-of-function-compatible target
- No active gene therapy clinical trials identified for ROGDI/KTS

**Cell types to target:**
1. **Neurons** (CNS) — presynaptic terminals (hippocampus, cortex)
2. **Ameloblasts** — dental enamel formation
3. **Renal tubule cells** — nephrocalcinosis

**Delivery challenge:** CNS rescue and dental/enamel rescue are mismatched problems. ROGDI is intracellular/non-secreted, so cross-correction is expected to be low. A CNS-directed AAV route may address neurological morbidity but is unlikely to reverse established enamel defects; ameloblast targeting/timing remains unresolved.

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
