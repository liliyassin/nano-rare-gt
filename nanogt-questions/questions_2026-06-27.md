# nanogt Daily Recall — 2026-06-27

*20 questions across six categories. Cover the answer sheet and write or say your answer before checking. Aim for the level of detail you'd give a viva examiner. (Today's set deliberately probes parts of the v4 engine not covered on the 25th/26th.)*

---

1. `match_score` is built from two conceptually distinct halves: "biological fit" and "precedent strength." Which dimensions sit in each half, and why is it defensible to fold both into one ranking number — rather than splitting them the way `match_score` and `tractability_score` were split?

2. Beyond ranking, `recommend_strategy` synthesises an explicit starting hypothesis. What labelled fields does it return, where does each field come from, and what does the `modality` field say when the disease mechanism is curated as "incompatible"?

3. `review_flags` are deliberately kept separate from the confidence tier. Explain the design principle: how can a program be the top-ranked precedent at "high" confidence and still carry serious review flags? Give one concrete example flag.

4. State the full `_APPROVAL_SCORES` ladder (approved through phase1, plus the default for an unrecognised status). Which half of `match_score` does `approval_weight` live in, and why is it there and not in "biological fit"?

5. The inheritance dimension does more than reward an AR/XL match. What score does `score_inheritance` give for (a) a clean AR/XL match, (b) a detected dominant-negative allele with no inheritance match, and (c) a haploinsufficient dosage-sensitive gene — and why is this dimension kept separate from the modality gate?

6. Walk through the four tiers of `score_tropism` (2.0 / 1.5 / 1.0 / 0.3). What exact combination earns the full 2.0, how does the CNS keyword expansion work, and what score is returned when the disease carries no tissue annotation at all?

7. `score_immune_privilege` ranks tissues retina > CNS > liver > muscle/heart > kidney > hematopoietic. Give the immunological basis for the two extremes (why retina scores highest, why hematopoietic scores lowest), and say why this is a tractability dimension rather than a match dimension.

8. Fabry disease (GLA) is annotated across liver, kidney, heart and CNS. How does the v4 mean-tissue aggregation change its tractability relative to the old "best tissue" rule, why does GLA still earn a high cross-correction score, and what does the disease-heterogeneity review flag warn about specifically for Fabry?

9. Fabry and Sanfilippo A (MPS IIIA, SGSH) are both lysosomal-storage loss-of-function diseases, yet Fabry's strong precedents include liver/HSC programmes while Sanfilippo A's leading AAV precedent is ABO-101 (AAV9, CNS). What single disease property drives that divergence, and through which dimension(s) does it act?

10. Crigler-Najjar type I (UGT1A1) and the haemophilias are all liver-directed loss-of-function diseases. Which dimensions does UGT1A1 *share* with F9 that keep it competitive at all — and why is UGT1A1's protein class a weaker match (and weaker for cross-correction) than secreted Factor IX?

11. `rank_programs` ends with `scores.sort(key=lambda s: (-s.match_score, s.program_name))`. Explain both parts of that sort key, where hard-failed programs end up in the ordering, and how a program whose vector serotype is missing from the vectors table is handled.

12. `load_mechanism_evidence` is wrapped in `@lru_cache`, and `lookup_mechanism` has a special fallback when no gene symbol is supplied. Describe that gene-less fallback and explain why it only fires when *exactly one* curated record exists for the ORPHA ID.

13. `build_review_flags` can raise a "MULTI-SUBUNIT ENZYME" flag. What keyword/protein-name signals trigger it, which cohort disease is the textbook case, and what clinical question does the flag tell the user to resolve before trusting the precedent?

14. `score_approval` gives a fully approved product 1.0 but a positive Phase 3 only 0.8. In regulatory terms, what does *approval* demonstrate that a successful Phase 3 read-out does not yet — and why is that gap a legitimate basis for a *precedent*-strength score?

15. Promoter availability scores liver and retina at 1.0 but kidney at only 0.4. Why do liver and retina have such rich validated-promoter catalogues while kidney has almost none — and what does this dimension's stated limitation say it explicitly does NOT capture (think about a strong CAG/CMV promoter)?

16. Define "orphan designation" and "surrogate endpoint," and explain how each concept connects to what nanogt is trying to do for a nano-rare disease that can never run a large randomised trial.

17. In the catalog, AAV5 is patent-restricted (`freely_available: 0`) while LV carries the most clinical precedents (20) and an 8000 bp cargo limit. Beyond tissue tropism, name three practical development considerations — think IP/licensing, cargo capacity, and integration vs episomal persistence — that distinguish choosing an in vivo AAV from an ex vivo lentiviral platform.

18. Because `tractability_score` never affects the ranking, two different diseases can return the same #1 precedent at the same "high" confidence yet sit in very different tractability tiers. Construct such a pair and explain how a careful reader should combine the two numbers to avoid being misled.

19. `score_packaging` computes `gene_cds = disease_gene.cds_length_bp or program_cds` — it falls back to the *program's* CDS size when the query gene's length is unknown. Why is that an optimistic assumption, and in what situation could it hide a real packaging problem for the query disease?

20. The 46-disease `output/SUMMARY.md` still reports a single composite score per disease (e.g. "9.9/10"), but the live v4 engine no longer produces a composite. What does this mismatch tell you about keeping generated artefacts in sync with code, and how would you regenerate the cohort results defensibly for the dissertation (note what must be fixed first)?
