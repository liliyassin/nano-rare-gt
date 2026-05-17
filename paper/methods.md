# Methods

<!-- Methods total target: ~2400 words (split across files, assembled later) -->

## 1. System Overview
<!-- Target: ~600 words -->

### Pipeline Architecture
<!-- Describe the 9-stage pipeline with reference to Figure 1. -->

### Data Sources and APIs
<!-- Orphanet, OMIM, ClinicalTrials.gov, UniProt, AlphaFold DB, GTEx, IEDB, TiProD. -->

### Software Stack
<!-- Python 3.11, Pydantic v2, SQLite, requests-cache, Typer, Jinja2, pandas, matplotlib, seaborn. -->

### Ethical and Data Statement
<!-- All public data. No patient identifiable information used. -->

## 2. Disease and Gene Characterization
<!-- Target: ~400 words -->

### Orphanet Integration
<!-- API query, fields parsed, phenotype mapping. -->

### OMIM Cross-Reference
<!-- Gene mapping, allelic disorders, inheritance confirmation. -->

### ClinicalTrials.gov Active Trial Filtering
<!-- Query logic, exclusion/deprioritization gate. -->

### Disease Severity and Morbidity Flagging
<!-- How Orphanet classification maps to severity. -->

## 3. Structural Homology and Surrogate Database
<!-- Target: ~500 words -->

### Surrogate Database Curation
<!-- Manually extracted approved/phase-3 programs. 25+ entries. Sources and fields. -->

### Sequence Homology
<!-- BLASTp / EBI NCBIblast API. Scoring: % identity, coverage. -->

### Domain Architecture Similarity
<!-- Pfam / InterPro overlap. Jaccard-like ratio. -->

### Structural Similarity
<!-- AlphaFold model linkage. TM-score proxy. pLDDT confidence weighting. -->

### Composite Structural Score
<!-- Weighted combination formula. -->

## 4. Vector Compatibility and Delivery
<!-- Target: ~500 words -->

### AAV Packaging Limit
<!-- 4.7 kb hard threshold. ITR minigene extension to 4.9 kb noted. -->

### Cargo Sizing and Oversized Gene Handling
<!-- CDS length query. Branch logic for dual-AAV, lentivirus, minigene. -->

### Serotype Selection
<!-- Static tissue-to-serotype map. CNS, retina, liver, muscle, other tissues. -->

### Tissue Tropism Scoring
<!-- Exact match, related tissue, no match. -->

### Freedom-to-Operate Flag
<!-- Patent status of serotypes and promoters. -->

## 5. Expression, Promoter, and Regulatory Matching
<!-- Target: ~500 words -->

### GTEx Tissue Expression Analysis
<!-- Median TPM thresholds. On-target and off-target expression scoring. -->

### Promoter Selection
<!-- Tissue-specific vs ubiquitous. RHO, MHCK7, TBG, GfaABC1D, CAG, CBA. -->

### Promoter Precedence Scoring
<!-- Exact precedent vs ubiquitous vs novel. -->

### Regulatory Element Mining
<!-- TiProD and literature sources for enhancer selection. -->

## 6. Immunogenicity, Codon Optimization, and Therapeutic Window
<!-- Target: ~500 words -->

### MHC-I Epitope Prediction
<!-- netMHCpan / MHCflurry if available. Fallback heuristic. HLA alleles tested. -->

### Self-Similarity Correction
<!-- BLAST transgene vs human proteome. Immunogenicity penalty reduction for self-like sequences. -->

### Codon Adaptation Index
<!-- Human codon usage table. CAI threshold. -->

### Therapeutic Window Assessment
<!-- OMIM/ClinVar overexpression toxicity check. Wild-type duplication phenotypes. Scoring. -->

## 7. Multi-Parameter Scoring Engine
<!-- Target: ~400 words -->

### Scoring Dimensions
<!-- List all 11 dimensions. -->

### Normalization
<!-- Per-disease percentile or absolute thresholds. -->

### Weighted Composite Formula
<!-- Exact weights from ADR-002. -->

### Hard Gates
<!-- Size compatibility. Auto-reject conditions. -->

### Confidence Tiers
<!-- High, medium, low — criteria for each. -->

### Protocol Synthesis
<!-- Jinja2 template output. Sections auto-generated. -->
