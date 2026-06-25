# nanogt Daily Recall — 2026-06-25

*20 questions across six categories. Cover the answer sheet and write or say your answer before checking. Aim for the level of detail you'd give a viva examiner.*

---

1. In two or three sentences, state what `nanogt` takes as input, what it produces as output, and the central premise that makes the ranking meaningful.

2. Frame the regulatory argument: why is "which approved or clinical-stage GT programme is the closest precedent?" a useful question for an ultra-rare ("nano-rare") disease — and what does a high score explicitly NOT claim?

3. Version 4 replaced the single composite score with two scores, `match_score` and `tractability_score`. What distinct question does each one answer, why is tractability computed only once per disease, and what was wrong with the old composite?

4. Name the modality classes the catalog actually covers and at least three it explicitly excludes. Why must every score be read as "catalog-relative"?

5. Three dimensions carry a 1.5× weight while the rest carry 1.0×. Which three are they, what do they have in common, and what is the evidence-based justification for weighting them most heavily?

6. Walk through how `match_score` is turned into a 0–10 number from the eight program-comparative dimensions. Why is the raw maximum exactly 17.0?

7. State the confidence tiers and their thresholds, and the tractability tiers and their thresholds. Which underlying score is each tier set on, and why does that distinction matter?

8. The scorer has two hard-fail gates. Name them, give their v4 order, and explain why the mechanism/modality gate is checked *before* the packaging gate. Use a worked example of a disease the reordering fixes.

9. Spinal Muscular Atrophy (ORPHA:70, SMN1) ranks Zolgensma and OAV101-IT at the top. Identify the specific dimension-level features of the gene, vector and disease that drive that result.

10. Crigler-Najjar type I is a liver-directed deficiency much like haemophilia, yet it lands lower than the haemophilia diseases. What property of its gene product (UGT1A1) pulls the score down, and through which dimension(s)?

11. Leber hereditary optic neuropathy (MT-ND4) — why does the organelle-targeting dimension score it 0.0, which real-world programme illustrates the approach actually required, and why does the tool label all its precedent scores "cross-paradigm"?

12. What specific situation triggers the helper `_packaging_gene_for_program`, and how does it change what actually gets graded for packaging? Use micro-dystrophin / DMD as the example.

13. The tractability dimensions for immune privilege, promoter availability and route feasibility call `_aggregate_tissue_mean`. What did this calculation do before v4, what does it do now, and which CLI flag lets you override it?

14. If you query a disease/gene pair that is NOT in the curated mechanism CSV, what `evidence_status` and `gene_addition_compatibility` come back, what modality-dimension score results, and what review flag is raised? Why is "uncertain" the deliberate default?

15. Why was AAV9 the serotype chosen for SMA, and more generally why is vector tropism treated as a primary (1.5×) selection criterion rather than a secondary one?

16. Pre-existing neutralising antibodies (NAbs): what is the clinical consequence of high seroprevalence, why does the model score LV and AAV5 favourably but AAV2 worst, and name two limitations of using fixed Western-adult seroprevalence values.

17. Explain cross-correction via the mannose-6-phosphate (M6P) receptor pathway. Why does it let a minority of transduced cells rescue a whole tissue for a soluble lysosomal enzyme, but score 0.0 for a lysosomal *membrane* protein such as MCOLN1 or CTNS?

18. `report.py` and `cli.py` still reference `s.composite_score`, but the v4 `ScoreBreakdown` no longer defines that attribute. What happens when those code paths run, and what is the correct fix?

19. CDS length is approximated as (amino acids × 3) from the canonical UniProt isoform. Why is this an optimistic *lower bound* for whether a construct fits an AAV, and for which catalog genes does the gap matter most?

20. Across the cohort, lysosomal and CNS diseases very often top out with the lentiviral HSC programmes (Libmeldy, Skysona). Is that a genuine biological signal or partly an artefact of the catalog — and what does the tool do to keep you honest about the difference?
