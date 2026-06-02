# Discussion

## 1. Summary of Principal Findings

A twelve-dimension computational scoring framework was developed and applied to ten monogenic rare diseases to identify the most scientifically supported gene therapy development pathways. The two retrospective validation diseases — Spinal Muscular Atrophy and Haemophilia B — were correctly identified, with their respective approved therapies (Zolgensma and Hemgenix) ranked first in each case. Across eight prospective discovery diseases, seven received high-confidence scores (≥7.5/10), and the single medium-confidence result (Crigler-Najjar syndrome type I, 6.8/10) reflected a genuine and explainable biological constraint. The framework produced actionable precedent recommendations for eight diseases that currently lack an approved gene therapy, in each case identifying specific vector serotypes, delivery routes, and precedent programs that could inform a clinical development strategy.

---

## 2. Validation and Framework Accuracy

The successful top-ranking of both approved therapies in the validation cohort supports the utility of the multi-dimensional scoring approach. The Haemophilia B result is particularly noteworthy: Hemgenix achieved a composite score of 9.1/10, the highest in the entire dataset, driven by near-maximum scores across ten of twelve dimensions. This high score reflects the unusually favourable biology of hepatic coagulation factor replacement — the target tissue (liver) is accessible via intravenous infusion, tolerogenic, well-supplied with validated promoters, and the secreted protein biology enables broad cross-correction. The framework correctly captured this convergence of favourable characteristics.

The SMA validation result is more instructive about the framework's behaviour. Zolgensma scored 7.7/10 — lower than the Haemophilia B match — for reasons that are biologically meaningful. The SMN1 protein is intracellular (zero cross-correction potential), SMA has a very narrow neonatal therapeutic window, and no pathway group precisely matches SMN1 biology. These constraints are real clinical challenges: neonatal dosing and the absence of cross-correction are precisely the features that made Zolgensma's development complex and expensive. The framework therefore not only correctly identified the approved therapy but encoded the reasons why SMA gene therapy is harder than haemophilia gene therapy.

The external corroboration of the Fabry disease result warrants specific comment. The framework identified ST-920 and AVR-RD-01 as the top two matches for Fabry disease; both are real active clinical programs developed specifically for Fabry disease. This convergence — arrived at independently by the scoring algorithm — provides evidence beyond the two planned validation cases that the framework captures clinically relevant biological similarity. It is notable that this result was not engineered: Fabry disease was included as a discovery case and the scoring proceeded identically to all other diseases.

---

## 3. Generalisability Across Disease Classes

A key requirement for a framework of this kind is that it should perform across biologically diverse disease classes without disease-specific tuning. The ten diseases tested span five distinct tissue targets (liver, CNS, retina, haematopoietic, multi-tissue), four inheritance patterns (AR, XL recessive, XL dominant, and a disease without clean inheritance classification), three biological pathways (lysosomal storage, coagulation, motor neuron/metabolic), and a range of gene sizes from 861 bp to 3,033 bp. The framework produced high-confidence results across this diversity using identical scoring logic in every case, suggesting that the twelve dimensions selected capture features that generalise across monogenic disease biology rather than being tuned to a specific disease class.

The alpha-mannosidosis result illustrates this generalisability particularly well. The gene's relatively large CDS (3,033 bp) shifted the framework's recommendation away from standard AAV approaches toward a lentiviral ex vivo strategy, without any disease-specific programming. The algorithm independently identified the same development logic that has been applied to other large-gene lysosomal storage diseases where AAV packaging constraints make ex vivo haematopoietic stem cell delivery the most viable option.

---

## 4. Limitations

### 4.1 Surrogate Database Coverage

The surrogate database in its current form contains 18 gene therapy programs. While this covers the principal approved and late-stage programs across the most common disease categories, it provides limited coverage of rare tissue types such as kidney, lung, and peripheral nervous system. Diseases affecting these tissues will receive reduced scores on tropism, immune privilege, promoter availability, and route of administration dimensions due to the scarcity of relevant precedents rather than due to genuine biological barriers. Expanding the database to include a broader range of programs — including Phase 1 programs and those targeting underrepresented tissues — would improve the framework's coverage for ultra-rare diseases with unusual tissue tropism requirements.

### 4.2 HPO-Based Therapeutic Window Inference

The therapeutic window dimension is inferred from HPO term keyword analysis, which is a crude approximation of natural history. The most significant consequence of this limitation was observed in Haemophilia B, where the absence of explicit "adult onset" or "chronic" HPO keywords resulted in a therapeutic window score of 0.5/2.0 — flagging a neonatal-onset disease — when haemophilia is in fact a disorder compatible with treatment at multiple life stages. This occurred because the HPO terms in the Haemophilia B fallback dataset ("prolonged bleeding", "joint haemorrhage", "liver coagulation") do not contain the positive onset keywords that the scoring function uses to recognise a wide therapeutic window. More precise window inference would require integration of structured natural history data from OMIM or Orphanet clinical summaries, including explicit age-of-onset and disease progression fields.

### 4.3 Pathway Coverage and Novel Biology

The biological pathway dimension relies on a pre-defined set of pathway groups. Diseases involving poorly characterised or novel pathways — such as Kohlschütter-Tönz syndrome, where *ROGDI* participates in synaptic V-ATPase regulation with no direct analogue in the approved GT literature — receive a neutral pathway score of 1.0/2.0 rather than a positive match score. This is preferable to a false negative penalty, but it means the framework cannot distinguish between a genuinely novel disease and one where pathway inference simply failed. Future versions should incorporate formal pathway database linkages (for example, KEGG or Reactome pathway IDs) to improve coverage and reduce dependence on keyword inference.

### 4.4 Population-Average Seroprevalence

The immunogenicity dimension uses published population-average seroprevalence estimates for each AAV serotype. In practice, seroprevalence varies substantially between geographic populations, age groups, and individuals [CITATION]. A patient with high-titre neutralising antibodies against a recommended vector would be ineligible for that approach regardless of the framework's score. The current implementation correctly stratifies vectors by their general immunogenicity risk profile, but patient-specific NAb testing before treatment initiation remains essential. The framework should therefore be interpreted as a population-level risk indicator rather than an individual eligibility predictor.

### 4.5 Restriction to Loss-of-Function Disease

The current framework and surrogate database are designed for autosomal recessive and X-linked loss-of-function diseases amenable to gene replacement — providing a functional copy of a defective gene. Autosomal dominant diseases, gain-of-function mutations, and haploinsufficiency conditions where overexpression of the transgene could itself cause harm require fundamentally different therapeutic strategies, including RNA interference, antisense oligonucleotides, or base editing. The framework's inheritance compatibility dimension partially captures this distinction by penalising dominant disease matches, but the framework should not be applied to dominant or gain-of-function diseases without substantial modification to the scoring logic and the surrogate database.

### 4.6 Absence of Structural Homology

The framework does not incorporate protein structural similarity as a scoring dimension. Three-dimensional protein structural similarity, as quantified by tools such as Foldseek or TM-score comparison of AlphaFold models, could improve the identification of biologically analogous precedents in cases where primary sequence or pathway similarity is low. This is particularly relevant for novel-pathway diseases such as Kohlschütter-Tönz syndrome, where structural similarity might reveal undiscovered functional analogues in the approved GT literature. Structural homology was identified as a priority addition for future framework development.

---

## 5. Clinical Translation Implications

For the diseases highlighted in this study, the framework produces outputs that are immediately actionable in the context of early-stage development planning. A researcher or clinician seeking to initiate a gene therapy program for Salla disease, Mucolipidosis type IV, or Sanfilippo A can use the framework's outputs to identify: a recommended vector serotype and delivery route supported by clinical precedent; a specific approved or late-stage program whose regulatory package, manufacturing process, and safety data could serve as an IND-enabling reference; and a ranked list of alternative approaches in the event that the top-ranked strategy encounters unexpected barriers.

The time and resource savings are substantial. A traditional feasibility study covering vector selection, tissue tropism literature review, packaging assessment, promoter evaluation, and immunogenicity risk would typically require weeks of expert analysis per disease. The framework generates this analysis in under two minutes per disease query, enabling systematic screening across large numbers of candidate diseases — a capability that is particularly valuable for academic research groups and patient advocacy organisations that lack the resources of large pharmaceutical companies.

The medium-confidence result for Crigler-Najjar syndrome type I is itself a clinically meaningful output. Rather than generating a false high-confidence recommendation for a disease where existing precedents are imperfect, the framework correctly identifies that the development path requires greater novelty — specifically, that a liver enzyme replacement program targeting an intracellular, non-secreted protein will face challenges not encountered by the approved coagulation factor programs that represent the closest available precedents. This calibrated uncertainty is more useful to a clinical developer than an artificially inflated confidence score.

---

## 6. Future Directions

Several directions were identified for extending the framework. First, expansion of the surrogate database to include a broader range of programs — encompassing additional tissue types, emerging delivery platforms such as lipid nanoparticles (LNPs) for liver and lung delivery, and ex vivo editing approaches — would improve coverage for diseases currently underserved by the database. Second, integration of protein structural similarity scoring using AlphaFold models and established structure comparison tools would strengthen the framework for novel-biology diseases where sequence and pathway matching are insufficient. Third, the therapeutic window dimension would benefit from integration of structured natural history data sources such as OMIM clinical synopsis fields, which provide explicit age-of-onset and progression information beyond what is captured in HPO term names. Fourth, extension to gain-of-function and dominant negative diseases — incorporating siRNA, antisense oligonucleotide, and base editing approaches into the surrogate database — would substantially broaden the framework's applicability across the monogenic disease landscape. Finally, retrospective calibration of dimension weights against clinical trial outcomes, as outcome data accumulates for the programs in the current database, would enable evidence-based weight optimisation beyond the equal-within-tier weighting used in this study.
