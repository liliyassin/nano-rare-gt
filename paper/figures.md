# Figure Captions and Notes

## Figure 1: Thirty-Disease Score Distribution

**Type:** Bar chart or lollipop plot.

**Data source:** `output/SUMMARY.md`.

**Required message:** Show all 30 diseases ordered by composite score. Colour-code high confidence, medium confidence, and packaging-gate failure. Label DMD separately as a native-gene packaging failure rather than a low-scoring compatible disease.

**Suggested caption:** "Composite NanoGT scores across the 30-disease proof-of-concept cohort. All diseases had at least one ranked current-catalog precedent, while Duchenne muscular dystrophy remained an engineered-cargo stress test because full-length DMD exceeds standard AAV capacity and only the micro-dystrophin precedent is scoreable. Scores represent relative precedent strength, not predicted clinical efficacy."

---

## Figure 2: Top-Precedent Cluster Map

**Type:** Sankey diagram, bipartite network, or grouped bar chart.

**Data source:** `output/SUMMARY.md` top precedent and vector columns.

**Required message:** Diseases cluster around a small number of precedent programmes, especially Libmeldy/LV, BMN 307/AAV5, retinal AAV programmes, and AAV9 CNS/muscle precedents.

**Suggested caption:** "Disease-to-precedent clustering in the 30-disease cohort. Libmeldy/lentiviral HSC therapy dominates lysosomal and leukodystrophy-like diseases, BMN 307 supports several liver metabolic disorders, and retinal diseases cluster around Luxturna/CPCB-RPE1-style AAV precedents."

---

## Figure 3: Validation and Stress-Test Examples

**Type:** Four-panel case-study figure.

**Panels:**
1. Hemophilia B positive control: Hemgenix top-ranked.
2. SMA positive control: AAV9/Zolgensma/OAV101 precedent recovered.
3. LCA calibration issue: Luxturna appears near top but not necessarily rank 1 in current scoring.
4. DMD stress test: native full-length DMD fails AAV packaging.

**Suggested caption:** "Representative validation and stress-test behaviour. The framework recovers several expected clinical precedents, reveals a retinal calibration issue where exact disease identity should be weighted more strongly, and correctly flags full-length DMD as outside standard single-vector scope."

---

## Supplementary Tables

### Supplementary Table 1: Cohort Metadata

Use `data/disease_cohort_30.csv`. Include disease name, ORPHA ID, gene, inheritance, tissues, prevalence, OMIM ID, cohort role, source URL, and fact-check status.

### Supplementary Table 2: Complete Scoring Results

Use `output/SUMMARY.md` plus the individual files in `output/match_*.md`. Include all top-five precedent rankings where space allows.

### Supplementary Table 3: Surrogate Catalogue

Use `src/nanogt/catalog.py`. Include programme name, disease, gene, vector, tissue target, CDS length, approval/trial stage, protein class, inheritance, and pathway.
