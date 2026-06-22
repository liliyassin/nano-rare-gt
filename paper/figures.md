# Figure Captions and Notes

## Figure 1: 46-Disease Score Distribution

**Type:** Bar chart or lollipop plot.

**Data source:** `output/SUMMARY.md`.

**Required message:** Show all 46 diseases ordered by composite score. Colour-code high confidence, medium confidence, and packaging-gate failure. Label DMD separately as a native-gene packaging failure rather than a low-scoring compatible disease. NF1 is the only packaging hard-fail (CDS exceeds all vectors).

**Suggested caption:** "Composite NanoGT scores across the 46-disease proof-of-concept cohort. Forty-five diseases received scored precedents; NF1 received a packaging hard-fail because its 8,451 bp CDS exceeds the capacity of every vector in the catalogue. Duchenne muscular dystrophy remained an engineered-cargo stress test because full-length DMD exceeds standard AAV capacity and only the micro-dystrophin precedent is scoreable. Scores represent relative precedent strength, not predicted clinical efficacy."

---

## Figure 2: Top-Precedent Cluster Map

**Type:** Sankey diagram, bipartite network, or grouped bar chart.

**Data source:** `output/SUMMARY.md` top precedent and vector columns.

**Required message:** Diseases cluster around a small number of precedent programmes, especially Libmeldy/LV (multiple lysosomal diseases), BMN 307/AAV5 (liver metabolic disorders), OAV101-IT/AAV9 (CNS/muscle diseases), Luxturna/CPCB-RPE1 (retinal diseases), and Skysona/LV (lysosomal membrane transporter diseases). NF1 packaging hard-fail appears separately.

**Suggested caption:** "Disease-to-precedent clustering in the 46-disease cohort. Libmeldy/lentiviral HSC therapy is the top precedent for multiple lysosomal and leukodystrophy diseases; BMN 307 supports several liver metabolic disorders; AAV9-based programmes (OAV101-IT, SRP-9001) cluster neuromuscular diseases; and retinal diseases cluster around Luxturna/CPCB-RPE1-style AAV precedents. The clustering pattern emerges from the 14-dimension heuristic scoring rather than explicit disease-class rules."

---

## Figure 3: Validation and Stress-Test Examples

**Type:** Four-panel case-study figure.

**Panels:**
1. Hemophilia B positive control: Hemgenix top-ranked (9.9/10).
2. SMA positive control: OAV101-IT/AAV9 precedent recovered (8.3/10).
3. Hemophilia A positive control: Hemgenix and Roctavian tied at 8.5/10; Hemgenix appears first alphabetically (see Section 3.4 tie-break note).
4. DMD stress test: native full-length DMD fails AAV packaging; only engineered micro-dystrophin (SRP-9001) returns a score.

**Suggested caption:** "Representative validation and stress-test examples. Panels 1–3 show positive controls where the framework recovers expected clinical precedents; panel 3 illustrates a same-score tiebreak between Hemgenix and Roctavian for Hemophilia A. Panel 4 shows correct packaging hard-gate behaviour for native full-length DMD, with the engineered micro-dystrophin precedent (SRP-9001) as the only scoreable result."

---

## Supplementary Tables

### Supplementary Table 1: Cohort Metadata

Use `data/disease_cohort_46.csv`. Include disease name, ORPHA ID, gene, inheritance, tissues, prevalence, OMIM ID, cohort role, source URL, and fact-check status.

### Supplementary Table 2: Complete Scoring Results

Use `output/SUMMARY.md` plus the individual files in `output/match_*.md`. Include all top-five precedent rankings where space allows.

### Supplementary Table 3: Surrogate Catalogue

Use `src/nanogt/catalog.py`. Include programme name, disease, gene, vector, tissue target, CDS length, approval/trial stage, protein class, inheritance, and pathway.
