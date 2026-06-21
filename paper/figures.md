# Figure Captions and Notes

## Figure 1: Forty-Disease Score Distribution

**Type:** Bar chart or lollipop plot.

**Data source:** `output/SUMMARY.md`.

**Required message:** Show all 40 diseases ordered by composite score. Colour-code high confidence, medium confidence, and packaging-gate failure. Label DMD separately as a native-gene packaging failure rather than a low-scoring compatible disease. NF1 is the only packaging hard-fail (CDS exceeds all vectors).

**Suggested caption:** "Composite NanoGT scores across the 40-disease proof-of-concept cohort. Thirty-nine diseases received scored precedents; NF1 received a packaging hard-fail because its 8,451 bp CDS exceeds the capacity of every vector in the catalogue. Duchenne muscular dystrophy remained an engineered-cargo stress test because full-length DMD exceeds standard AAV capacity and only the micro-dystrophin precedent is scoreable. Scores represent relative precedent strength, not predicted clinical efficacy."

---

## Figure 2: Top-Precedent Cluster Map

**Type:** Sankey diagram, bipartite network, or grouped bar chart.

**Data source:** `output/SUMMARY.md` top precedent and vector columns.

**Required message:** Diseases cluster around a small number of precedent programmes, especially Libmeldy/LV (9 diseases), Skysona/LV (3 diseases including ML-IV and Salla), BMN 307/AAV5, retinal AAV programmes, and AAV9 CNS/muscle precedents. Mechanism hard-fail diseases appear as a separate arm.

**Suggested caption:** "Disease-to-precedent clustering in the 40-disease cohort. Libmeldy/lentiviral HSC therapy is the top precedent for 9 lysosomal and leukodystrophy diseases; Skysona covers three diseases with lysosomal membrane or transporter biology; BMN 307 supports several liver metabolic disorders; and retinal diseases cluster around Luxturna/CPCB-RPE1-style AAV precedents."

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

Use `data/disease_cohort_40.csv`. Include disease name, ORPHA ID, gene, inheritance, tissues, prevalence, OMIM ID, cohort role, source URL, and fact-check status.

### Supplementary Table 2: Complete Scoring Results

Use `output/SUMMARY.md` plus the individual files in `output/match_*.md`. Include all top-five precedent rankings where space allows.

### Supplementary Table 3: Surrogate Catalogue

Use `src/nanogt/catalog.py`. Include programme name, disease, gene, vector, tissue target, CDS length, approval/trial stage, protein class, inheritance, and pathway.
