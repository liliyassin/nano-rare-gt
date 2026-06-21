# Dissertation TODO — NanoGT

Generated: Thursday 11 June 2026, BST.

Primary goal: submit a credible dissertation report in about one month. The poster is useful practice, but the dissertation report is the graded deliverable. Do not expand the project unless it directly improves the report.

## Critical path

1. Lock the project claim.
2. Verify the 40-disease dataset.
3. Make the Results/Discussion match the actual outputs.
4. Read and cite the references that support the claims.
5. Produce clean figures and tables.
6. Send supervisor updates early, not when everything feels perfect.
7. Write the dissertation in a defensible, limitation-aware way.

## By Sunday 14 June — minimum viable dissertation package

| Task | Estimate | Deadline | Done when |
|---|---:|---|---|
| Read `output/SUMMARY.md` and `output/RESULTS_INTERPRETATION.md` start to finish | 45 min | Fri 12 Jun | You can explain the 40-disease result without opening the file |
| Fact-check 10 highest-impact diseases in `data/disease_cohort_40.csv` | 3 h | Fri 12 Jun | ORPHA, gene, inheritance, tissues, OMIM, source URL checked |
| Fact-check remaining 20 diseases at quick-pass level | 4 h | Sat 13 Jun | Every row has been checked or marked with a problem note |
| Read and annotate 6 core papers already in `paper/references.md` | 5 h | Sat 13 Jun | You have notes for Dunbar/High/Naldini + Luxturna/Zolgensma/Hemgenix or closest equivalents |
| Replace any unsupported claims in paper sections | 2 h | Sat 13 Jun | No obvious claim says more than the code/output supports |
| Draft supervisor update email | 30 min | Sat 13 Jun | Email says: current result, limitation, next work, specific asks |
| Create/refresh Figure 1 score distribution from the 40-disease table | 2 h | Sun 14 Jun | Figure uses all 40 diseases, not an earlier pilot set |
| Create Figure 2 precedent-cluster visual | 2 h | Sun 14 Jun | Shows Libmeldy/LV, BMN307/AAV5, retinal cluster, DMD failure |
| Final Sunday review | 1 h | Sun 14 Jun evening | You know what is weak before the supervisor does |

## Week of 15–21 June — convert output into report evidence

| Task | Estimate | Deadline | Done when |
|---|---:|---|---|
| Send supervisor update | 30 min | Mon 15 Jun morning | Email sent with links/attachments if needed |
| Methods: verify every data source and scoring dimension | 5 h | Tue 16 Jun | Methods describes the actual implementation, not aspirational modules |
| Results: finish 40-disease narrative and tables | 5 h | Wed 17 Jun | Table, stats, clusters, stress tests included |
| Discussion: write limitations honestly | 4 h | Thu 18 Jun | Limitations include catalogue, heuristic scoring, fact-checking, modality scope |
| References: replace placeholders and mark what you have actually read | 5 h | Fri 19 Jun | No placeholder references; key claims have citations |
| Poster practice / extraction from dissertation | 3 h | Fri 19 Jun | Poster tells the same story as the dissertation, but shorter |
| Supervisor feedback triage | 2 h | Sun 21 Jun | Feedback converted into action list |

## Week of 22–28 June — strengthen dissertation quality

| Task | Estimate | Deadline | Done when |
|---|---:|---|---|
| Improve validation framing: top-k recovery instead of overclaiming top-1 | 3 h | Mon 22 Jun | Validation section is defensible despite LCA ranking issue |
| Build final figures in consistent style | 6 h | Tue 23 Jun | Figures export cleanly and captions explain the point |
| Add supplementary tables | 4 h | Wed 24 Jun | Cohort metadata, surrogate catalogue, scoring summary ready |
| Reference audit | 6 h | Thu 25 Jun | Every citation in text appears in references and vice versa |
| Full dissertation draft v1 | 8 h | Sun 28 Jun | Complete draft exists, even if rough |

## Week of 29 June–5 July — revision and evidence hardening

| Task | Estimate | Deadline | Done when |
|---|---:|---|---|
| Supervisor-requested changes | 6–10 h | Tue 30 Jun | All critical supervisor comments addressed |
| Tighten Methods for reproducibility | 4 h | Wed 1 Jul | Commands, data files, code paths, and scoring formula are explicit |
| Tighten Results for clarity | 4 h | Thu 2 Jul | Reader can follow the result without reading the code |
| Tighten Discussion for honest limits | 4 h | Fri 3 Jul | No hidden weak points remain |
| Format and style pass | 5 h | Sun 5 Jul | Headings, tables, figures, references consistent |

## Final week before submission — polish, not expansion

| Task | Estimate | Deadline | Done when |
|---|---:|---|---|
| Final code/test rerun | 1 h | Mon 6 Jul | `uv run pytest` and `uv run python run_results.py` complete |
| Final output freeze | 1 h | Mon 6 Jul | `output/SUMMARY.md` and figures frozen |
| Final proofread pass 1: logic | 4 h | Tue 7 Jul | Argument makes sense end-to-end |
| Final proofread pass 2: references | 3 h | Wed 8 Jul | No broken placeholders, missing refs, or unsupported claims |
| Final formatting/export | 3 h | Thu 9 Jul | PDF/docx exports checked |
| Buffer day | 4–8 h | Fri 10 Jul | Only emergencies, not new features |

## Do not spend time on unless supervisor explicitly asks

- Building a web dashboard.
- Expanding from 40 diseases to hundreds.
- Adding new therapeutic modalities.
- Perfecting mypy/ruff beyond what blocks confidence.
- Refactoring the whole codebase.
- Re-exporting old PDF reading packs before the Markdown report is coherent.
- Claiming clinical utility before validation is stronger.

## Supervisor update skeleton

Subject: NanoGT dissertation update — 40-disease proof-of-concept results (14-dimension v2 algorithm)

Hi [Supervisor],

I have refocused the project around the dissertation report rather than the poster. The current NanoGT implementation now runs on a 40-disease monogenic rare-disease cohort and produces a cross-disease summary plus individual reports. The safest framing is as a proof-of-concept precedent-mapping framework, not a clinical recommendation tool.

Current headline results:
- 40 diseases analysed across 14 scoring dimensions (v2 algorithm, raw max = 21).
- 39 receive scored precedents; NF1 receives a packaging hard-fail (8,451 bp, exceeds all vectors).
- 32 high-confidence, 7 medium-confidence matches.
- Non-LOF arm (10 diseases): haploinsufficiency, repeat-expansion, imprinting — all produce real ranked results with appropriate medium-confidence scores except GATA2 (7.6, high) and FA (7.9, high).
- DMD correctly fails the native-gene AAV packaging gate; scored via micro-dystrophin precedent.
- The results cluster into interpretable precedent groups: Libmeldy/LV for 9 lysosomal diseases, BMN 307/AAV5 for liver metabolic disease, Skysona/LV for leukodystrophies and lysosomal membrane proteins, retinal AAV precedents.
- The main limitations are catalogue coverage, heuristic pathway/window inference, fact-checking of disease metadata, and lack of calibrated clinical validation.

My next priorities are: disease fact-checking, reference verification, final figures/tables, and tightening the Methods/Results/Discussion around the actual output.

Could you please advise which part you think most needs strengthening for the dissertation: validation, disease/source verification, biological interpretation, or limitations/framing?

Best,
Suzie
