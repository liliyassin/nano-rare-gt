# nanogt Daily Recall — 2026-07-02

1. In plain terms, what is a "nano-rare" disease, and what is the core bet nanogt makes about how a regulator or developer could use an *existing* GT program when almost no trial data exists for the disease in front of them?

2. nanogt ranks precedents inside a deliberately narrow modality box. Name the modalities the catalog covers and at least three it explicitly excludes, and explain why a disease that needs one of the excluded modalities would be *unfairly* penalised if the tool's score were read naively.

3. The framework separates "confidence" from "review_flags." Explain the design intent: why can a program be the #1-ranked precedent with *high* confidence and still carry a review flag that should stop you reusing it as-is?

4. Give the raw-max values MATCH_RAW_MAX and TRACTABILITY_RAW_MAX, and show arithmetically how each is built from its dimensions and weights. Why must the two scores be normalised separately rather than summed?

5. The three 1.5×-weighted dimensions are described as "go/no-go gates." For each of packaging_fit, tropism_match and modality_compatibility, give a one-line reason (with the type of clinical failure it predicts) that justifies the extra weight.

6. score_immunogenicity maps seroprevalence to a score with cutoffs at 10%, 20% and 40%. State the score awarded in each band, and then explain the four real-world caveats the code lists that mean these numbers are a *relative ranking*, not an eligibility threshold.

7. Walk through why Hemophilia B scores essentially perfectly against Hemgenix (~9.9/10) while Fabry against the same enzyme-class precedents tops out lower (~8.7–8.9). Which specific dimensions separate them, and which score bucket (match vs tractability) does each live in?

8. Crigler-Najjar type I (UGT1A1, liver) lands around 7.2/10 with a Hemgenix-class liver precedent on top. It's a liver LOF disease just like Hemophilia B — so why is it a full ~2.7 points lower? Name the most likely dimension drivers.

9. Sanfilippo A (SGSH, ORPHA:79269) has CNS as essentially its only relevant target tissue, yet the top precedent is an HSC/LV program (Libmeldy), not an AAV9 CNS program. Explain mechanistically why a hematopoietic-delivery precedent can top the ranking for a CNS disease, and what review flag you'd still expect.

10. The `_aggregate_tissue_mean` helper backs three tractability dimensions. Which three, what changed in v4 about how they aggregate across tissues, and what does `--primary-tissue` do to that computation for a multi-system disease like Fabry (liver/kidney/heart/CNS)?

11. `score_organelle_targeting` returns 0.0 in two distinct trigger conditions. State both triggers (one by gene-symbol convention, one by inheritance field), and explain why the code deliberately catches the *inheritance* case even when the gene symbol wouldn't flag it.

12. `_packaging_gene_for_program` sometimes swaps the disease gene for the program's engineered construct before scoring packaging. What string markers trigger that swap, why is scoring "does the micro/mini construct fit" the *correct* question for oversized genes like DMD, and what would break if this swap didn't exist?

13. `score_protein_class` returns 1.0 (not 2.0) when a lysosomal *membrane* protein is matched against a lysosomal-enzyme precedent, but `score_cross_correction` returns 0.0 for the same protein. Why the asymmetry — why is the membrane protein given *partial* credit on protein class but *zero* on cross-correction?

14. The `_PATHWAY_GROUPS` map is built from an undirected edge list in v4 rather than a hand-written dictionary. What two concrete bugs did the old hand-written version have, and which disease's scoring was being propped up by one of the now-removed cross-links?

15. Define AAV *tropism* and explain, using AAV9 vs AAV5 vs AAV2 from the catalog, why serotype choice is effectively a delivery-address decision. Which catalog serotype is the CNS-penetrant workhorse, and which is the liver specialist used in the approved hemophilia products?

16. What is cross-correction via the mannose-6-phosphate (M6P) receptor pathway, and why does it let a *minority* of transduced cells rescue a whole tissue? Name one catalog disease/gene where it applies and one where it physically cannot.

17. The approval_weight table scores a *withdrawn* product (0.7) above an in-progress Phase 2 (0.6). Which catalog program is the withdrawn one, why was it withdrawn, and why does the code argue a commercially-withdrawn-after-approval product is *stronger* regulatory precedent than a mid-stage trial?

18. tractability_score is computed once per disease and is identical for every candidate program. Give a concrete argument for why that makes it useless for *ranking* precedents — and then a concrete argument for why it's still worth reporting to the user at all.

19. The therapeutic_window dimension was moved to consult curated natural-history data first, with the HPO-keyword heuristic as fallback. Beyond the PKU example, give a general argument for *why* keyword-matching HPO text is a fragile way to infer a therapeutic window — name at least two distinct failure modes.

20. A skeptical examiner says: "Your headline scores are just a weighted sum of hand-assigned numbers with hand-chosen weights — this is circular, you get out what you put in." Give the strongest honest defence of the framework's value *and* concede the two limitations that critique correctly identifies.
