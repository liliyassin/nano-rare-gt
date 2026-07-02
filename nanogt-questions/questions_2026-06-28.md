# nanogt Daily Recall — 2026-06-28

1. The v4 algorithm replaced the single composite score with two separate scores. Name both, say what each one measures, and state which one drives the ranking and the confidence tier — and why the other one must NOT be blended into the ranking.

2. In one or two sentences, what regulatory/translational question is nanogt actually trying to answer for a nano-rare disease, and why is "find the closest existing GT program as a precedent" a useful framing for it?

3. The tool explicitly does NOT claim the top program is reusable as-is. What mechanisms does the framework attach to keep that interpretation honest (think review_flags, the tractability tier, and the catalog scope note)?

4. Why does the catalog deliberately restrict itself to AAV and ex vivo lentiviral / integrating-HSC gene-addition programs, and what does a LOW score therefore NOT prove about a disease's gene-therapy prospects?

5. match_score is built from eight weighted dimensions. Which three carry the 1.5× weight, what conceptual category do they share, and why are they weighted above the rest?

6. Give the confidence-tier thresholds (high / medium / low) and the tractability-tier thresholds (amenable / conditional / challenging), and state which score each tier is set on.

7. In v4 the two hard gates were reordered. Which gate is now checked FIRST, why is that ordering more correct, and give a disease example the reorder fixes.

8. score_packaging() grades "fill" against CDS + ~1.5 kb of cassette overhead, but the absolute hard-fail still fires only on the bare CDS. Explain why the two checks use different lengths, and give the fill-% bands that map to scores 2.0 / 1.5 / 1.0 / 0.5.

9. For SMA (ORPHA:70), SMN1 is an 891 bp intracellular protein. Walk through why OAV101-IT / Zolgensma top the ranking, why SMN1's protein class limits cross-correction, and which score (match vs tractability) each of those facts feeds.

10. Fabry (GLA) and Mucolipidosis IV (MCOLN1) are both "lysosomal," yet they score very differently against an enzyme-replacement precedent like Libmeldy. Explain the protein-class distinction the v2 fix introduced and its mechanistic basis.

11. Leber hereditary optic neuropathy (MT-ND4) receives organelle_targeting = 0.0. Explain why standard AAV cannot treat it, name the real-world strategy/program that is the relevant precedent, and say how the framework now surfaces this instead of producing a falsely high score.

12. lookup_mechanism() returns an explicit "missing / uncertain" record for uncurated disease/gene pairs rather than inferring from inheritance. What modality_compatibility score does that yield, and why is deliberately under-scoring the right design choice?

13. Both disease.py and gene.py use a two-tier fetch but try the curated local fallback FIRST for cohort entries. Why prefer the local data over the live Orphanet/UniProt API for known genes, given the tool can call those APIs at all?

14. There is a concrete inconsistency between the v4 scoring engine and the CLI/report/DB layer. Identify it, and state what would happen if you ran `nanogt match ORPHA:324` today.

15. The immunogenicity dimension scores vectors by pre-existing neutralising-antibody seroprevalence. Rank AAV2, AAV5, AAV9 and LV from best to worst score, and explain why low seroprevalence earns a HIGH score clinically.

16. gene.py estimates CDS length as aa_length × 3 from the UniProt canonical isoform. What does this under-count, and why does that matter specifically for genes near the AAV packaging limit?

17. Define cross-correction in AAV/HSC gene therapy, name the receptor pathway that makes it work for soluble lysosomal enzymes, and explain why a lysosomal membrane transporter (e.g. CTNS, MCOLN1) cannot benefit from it.

18. The v4 changelog says the old composite "let disease-intrinsic dimensions inflate the headline number and the confidence tier without affecting the ranking at all." Unpack why a dimension identical across all candidate programs cannot change their rank order — yet can still distort confidence.

19. The tissue-aggregated tractability dimensions (immune privilege, promoter availability, route feasibility) switched from "best tissue" to "mean across all tissues" in v4. What failure mode did "best tissue" cause for multi-system diseases, which CLI flag overrides the mean, and what is a trade-off of using the mean?

20. score_therapeutic_window() now consults curated natural-history data first and only falls back to an HPO-keyword heuristic. Give the textbook disease where the heuristic was clinically wrong, explain why it failed, and state why even a wrong window value cannot reorder the precedent ranking.
