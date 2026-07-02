# nanogt Daily Recall — 2026-06-26

1. In one or two sentences, what does the `nanogt` tool actually do, and what is the regulatory argument for why ranking *existing* GT programmes against a query disease is useful for a "nano-rare" disease?

2. The v4 scoring engine deliberately abolished the single composite score and replaced it with two separate scores. Name them, say what each one measures, and explain the conceptual flaw in v3 that this split was designed to fix.

3. Which of the two v4 scores drives the ranking and the confidence tier, and why must the other score be kept *out* of the ranking?

4. List the eight program-comparative (match) dimensions and state which three carry the 1.5× weight. What is the shared justification for those three being weighted most heavily?

5. The six tractability dimensions are weighted at 1.0× in the v4 `TRACTABILITY_WEIGHTS`, but the v3 changelog describes a 0.75× tier. What kind of dimensions were assigned 0.75× in v3, and what was the rationale for that lower weight?

6. What are the numeric values of `MATCH_RAW_MAX` and `TRACTABILITY_RAW_MAX`, and how is a raw weighted sum converted into a 0–10 score?

7. State the confidence-tier thresholds applied to `match_score` (high / medium / low) and the tractability-tier thresholds applied to `tractability_score` (amenable / conditional / challenging).

8. In v4 the two hard-fail gates were reordered. Which gate is now checked first, what triggers it, and why is checking it first the more correct design (use Huntington/HTT as your worked example)?

9. The packaging dimension subtracts a `_CASSETTE_OVERHEAD_BP` value before grading fill. What is that value, what regulatory/expression elements does it represent, and why does the *absolute* hard-fail still fire only on the bare CDS?

10. Explain the difference, in the scoring logic, between a lysosomal **enzyme** (e.g. ARSA) and a lysosomal **membrane** protein (e.g. MCOLN1). What protein-class and cross-correction scores does each receive, and what is the biological reason?

11. Why does Hemophilia B (F9, ~1383 bp, liver, secreted, delivered by AAV5) score so highly as a match for Hemgenix? Walk through which match dimensions max out and why.

12. SMA (SMN1, 891 bp) returns OAV101-IT and Zolgensma as joint top matches with identical scores. Why are they tied, and what does that tie reveal about which dimensions the match score is and isn't sensitive to?

13. Crigler-Najjar type I (UGT1A1, liver) lands its top precedents in the medium-confidence band rather than high. Given that the gene packages easily and the tissue is liver, what is the most likely set of dimensions dragging the match score down?

14. Glybera has an `approval_status` of "withdrawn" yet `score_approval` gives it 0.7 — above phase2's 0.6. Justify this scoring choice in regulatory-precedent terms, and state the one circumstance under which a withdrawn product should *not* be scored this way.

15. Describe how `score_immunogenicity` converts a vector serotype into a 0–2 score. Why does LV score best and AAV2 worst, and name two documented limitations of using these fixed seroprevalence values.

16. The organelle-targeting dimension assigns 0.0 to mtDNA-encoded genes (e.g. MT-ND4 in LHON), 0.5 to nuclear-encoded mitochondrial matrix proteins (e.g. MUT), and 0.7 to peroxisomal proteins. Explain the biological basis for these three tiers and what "allotopic expression" means.

17. In v4 the tissue-aggregated tractability dimensions (immune privilege, promoter availability, route feasibility) switched from taking the *most favourable* tissue to taking the **mean** across all annotated tissues. What problem did this fix, and what CLI flag lets a user score a single declared tissue instead?

18. The pathway-similarity dimension was rebuilt in v4 from an undirected edge list rather than a hand-written dict. What two concrete bugs did the old hand-written dict have, and why does building from `_PATHWAY_EDGES` guarantee one of them can't recur?

19. The `score_therapeutic_window` function now consults curated natural-history data *before* falling back to the HPO-keyword heuristic. Give the specific clinical example from the changelog where the old keyword heuristic produced a clinically wrong answer, and explain why it failed.

20. Give two distinct, defensible criticisms of using this catalog-precedent framework to make real go/no-go decisions for a nano-rare disease — one about the **catalog's scope** and one about the **scoring methodology** — and for each say how you would respond to it in a viva.
