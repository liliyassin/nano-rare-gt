# Results

<!-- Results total target: ~2300 words (split across files, assembled later) -->

## 1. Pipeline Coverage and Performance
<!-- Target: ~800 words -->

### Database Statistics
<!-- Disease coverage (Orphanet), surrogate count, API success rates. -->

### Query Speed Benchmarks
<!-- Median, 95th percentile, full pipeline end-to-end. -->

### Data Completeness
<!-- Fraction with primary data vs inferred per dimension. Table. -->

### Score Distribution
<!-- Figure 4 description. Composite score histogram or violin plot across tested diseases. -->

## 2. Retrospective Validation
<!-- Target: ~700 words -->

### Positive Control: Luxturna (RPE65)
<!-- Expected vs observed. Score breakdown. AAV2, subretinal, CMV/CBA. -->

### Positive Control: Zolgensma (SMN1)
<!-- Expected vs observed. SMN2 duplication complexity handling. -->

### Negative Control: Discontinued Program
<!-- Program name and failure mode. Algorithm correctly flagged dimension. -->

### Accuracy Metrics
<!-- Top-k retrieval, rank correlation (Kendall tau). Table. -->

## 3. Prospective Case Studies
<!-- Target: ~800 words -->

### Case Study 1: CNS Ultra-Rare Disease
<!-- Disease name, Orpha ID, gene. Homozygous LOF rationale. -->

#### Score Breakdown
<!-- Table with all 11 dimensions. -->

#### Recommended Protocol
<!-- Serotype, promoter, RoA, dosing rationale. -->

#### Risk Flags and Mitigations
<!-- Predicted risks and how the pipeline suggests mitigating them. -->

### Case Study 2: Metabolic Hepatic Disease
<!-- Disease name, Orpha ID, gene. Hepatic targeting rationale. -->

#### Score Breakdown
<!-- Table. -->

#### Recommended Protocol
<!-- AAV8/AAV9, TBG, IV. -->

#### Risk Flags and Mitigations
<!-- Hepatic expression cross-check. AAV dosing considerations. -->

### Comparison and Synthesis
<!-- Both protocols derived automatically in <2 minutes. Literature consistency. -->

## Tables Required
<!-- - Table 1: Surrogate database summary (optional — may move to supplementary) -->
<!-- - Table 2: Retrospective validation results (program, expected rank, observed rank, composite score) -->
<!-- - Table 3: Prospective case study score breakdowns -->
