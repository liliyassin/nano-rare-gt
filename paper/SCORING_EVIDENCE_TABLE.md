# NanoGT Scoring Evidence Table

Working document for linking each NanoGT scoring rule to evidence, rationale,
and limitations. This should be treated as a dissertation audit trail, not as a
claim that every threshold is statistically calibrated.

## Bottom Line

NanoGT currently uses an evidence-informed heuristic score. Some parameters are
directly grounded in literature or clinical practice, especially AAV packaging
capacity, vector seroprevalence, clinical-stage maturity, and known routes of
administration. Other parts are expert-rule bins chosen to make the model
interpretable across a small proof-of-concept cohort.

Use this wording in the dissertation:

> Scoring dimensions and thresholds were selected from literature-supported
> biological and development constraints where available, supplemented by
> transparent heuristic bins where no validated quantitative weighting scheme
> exists for rare-disease gene-therapy precedent matching. Composite scores
> therefore represent relative precedent strength, not calibrated probabilities
> of clinical success.

## Evidence Status Key

| Status | Meaning |
|---|---|
| Direct evidence | The parameter itself is supported by literature or clinical/regulatory fact. |
| Evidence-informed heuristic | The biological direction is supported, but the exact score or cutoff is a modelling choice. |
| Heuristic | The rule is mainly an interpretive choice and needs sensitivity analysis or expert validation. |
| Needs audit | Plausible, but the current project needs a checked paper, page note, or stronger citation. |

## Scoring Weights

| Dimension group | Current max score | Current interpretation | Evidence status | Rationale | Limitation |
|---|---:|---|---|---|---|
| Packaging, tropism, protein class, pathway, mechanism/modality compatibility, immunogenicity, therapeutic window | 2.0 each | Higher-weight determinants | Evidence-informed heuristic | These are major feasibility constraints: the gene must fit, vector must reach tissue, biology must be transferable, disease mechanism must suit the therapeutic modality, immune barriers matter, and timing affects trial feasibility. | The choice to give exactly double weight is not statistically derived. |
| Inheritance, approval, cross-correction, immune privilege, promoter availability, route feasibility | 1.0 each | Lower-weight determinants | Heuristic | These modify precedent strength but are not treated as full feasibility gates in v0.1. | Some of these may deserve higher weight in specific diseases, especially route, cross-correction, and approval precedent. |
| Organelle targeting | 1.0 | Penalises diseases where standard nuclear AAV delivery cannot produce a functional protein at the correct subcellular compartment (e.g. mtDNA-encoded genes, nuclear-encoded mitochondrial matrix proteins) | Evidence-informed heuristic | Added in v2 after MT-ND4/LHON received a plausible-looking 6.8/10 without any flag that allotopic expression is an entirely different paradigm from standard nuclear gene addition. MUT/MMA similarly received no penalty for the unvalidated MTS import requirement. | Only scores the two most common organelle-targeting failure modes (mtDNA and nuclear-encoded mitochondrial matrix). Peroxisomal and lysosomal membrane targeting are captured separately by the protein-class and cross-correction dimensions. |
| Raw total | 21.0 (v2, +1.0 for organelle targeting) | Sum of all dimension maxima | Heuristic | Convenient normalisation denominator. Organelle targeting added in v2 to penalise mitochondrial DNA-encoded genes and nuclear-encoded mitochondrial matrix proteins. | Not a trained model; weights were not fitted to outcome data. |
| Confidence tiers | High >= 7.5, medium >= 5.0, low < 5.0 | Interpretive score bands | Heuristic | Makes outputs easier to discuss and compare. | Needs sensitivity analysis; does not correspond to probability of success. |

## Dimension-Level Evidence Map

| # | Dimension | Current rule | Evidence status | Evidence/rationale sources | Dissertation-safe wording | Limitation/action |
|---:|---|---|---|---|---|---|
| 1 | Packaging fit | CDS > vector cargo gives hard fail. Otherwise utilisation <=30% = 2.0; 31-60% = 1.5; 61-85% = 1.0; 86-100% = 0.5. | Direct evidence for hard gate; heuristic for bins. | AAV practical packaging limit is supported by Grieger and Samulski 2005 and AAV reviews such as Naso et al. 2017 and Wang et al. 2024. Chamberlain et al. 2016 supports alternative strategies for oversized genes. Chamberlain et al. 2023 supports DMD microdystrophin logic. | The hard gate reflects a physical single-vector packaging constraint. Sub-bins represent increasing engineering risk as cargo approaches capacity. | Current score uses coding sequence only, not full vector genome including promoter, polyA, ITRs, regulatory elements, and codon optimisation. Add sensitivity analysis around 70%, 85%, and full cassette size. |
| 2 | Tissue tropism | 2.0 if vector tropism and precedent target both match disease tissue; 1.5 for target match or multi-tissue tropism overlap; 1.0 for single vector overlap; 0.3 for no overlap. | Evidence-informed heuristic. | Zincarelli et al. 2008 supports serotype-dependent tissue tropism. Foust et al. 2009 supports AAV9 CNS relevance. Walkey et al. 2025 provides a broad AAV tropism atlas in mouse. Clinical precedent entries in the catalog also support tissue-route pairings. | Tissue overlap is used as a practical proxy for vector transferability. Higher scores require both biological tropism and precedent-program targeting. | Tropism is species-, dose-, promoter-, route-, age-, and capsid-engineering dependent. Mouse atlas evidence does not directly translate to human efficacy. Consider separating natural tropism from route-specific clinical evidence. |
| 3 | Protein class | Lysosomal or secreted exact match = 2.0; intracellular or membrane match = 1.5; partial secreted/lysosomal component = 1.0; mismatch = 0.5. | Evidence-informed heuristic. | Gene therapy reviews and lysosomal storage disease precedents support differences between secreted/cross-correctable proteins and cell-autonomous intracellular proteins. UniProt supports protein localisation annotations. | Protein class is used as a proxy for whether the precedent's mechanism transfers to the query disease. | Current categories are coarse. It should distinguish secreted lysosomal enzymes, non-secreted lysosomal membrane proteins, cytosolic proteins, nuclear proteins, mitochondrial proteins, and structural membrane proteins. |
| 4 | Mechanism/modality compatibility | Compatible gene addition = 2.0; conditional = 1.5; uncertain = 1.0; incompatible = 0.0. | Evidence-informed heuristic with source-linked disease facts. | `data/disease_mechanisms_46.csv` stores the disease/gene mechanism category, gene-addition fit, evidence summary, and evidence URL. General gene therapy reviews support gene addition as most straightforward for loss-of-function disease, while dominant-negative, toxic gain-of-function, mitochondrial, repeat-expansion, and RNA/splicing disorders may need other modalities. | The framework now checks whether the disease mechanism supports ordinary gene addition before treating vector precedent as transferable. | The curated mechanism table is only as good as its citations. Conditional labels still require expert review and should not be converted into clinical recommendations. |
| 5 | Inheritance compatibility | Exact AR/XL match = 1.0; shared loss-of-function = 0.7; mismatch/dominant/mitochondrial = 0.3. | Evidence-informed heuristic. | General gene therapy reviews, including High and Roncarolo 2019 and Kirschner and Cathomen 2020, support gene addition as most straightforward for loss-of-function monogenic disease. | Inheritance remains useful context, but it is no longer treated as sufficient evidence for mechanism. | Exact scores are heuristic. Inheritance can mislead: dominant disease can be haploinsufficiency or dominant-negative; X-linked disease can still require tissue-specific interpretation. |
| 6 | Pathway similarity | Exact or grouped pathway match = 2.0; related pathway = 1.5; different pathway = 0.5; unknown = 1.0. | Evidence-informed heuristic. | Pathway labels are curated from disease biology, UniProt/GO/HPO terms, and clinical precedent groupings. Disease-similarity literature in the Zotero export, including Wei et al. 2024 and Lagorce et al. 2024, supports phenotype/pathway similarity as a computational strategy in rare disease analysis. | Shared pathway increases precedent relevance because potency assays, biomarkers, natural history, and regulatory analogies may transfer better. | Groupings are hand-coded and not learned from ontology distances. Consider using HPO/ORDO/GO semantic similarity rather than manual pathway buckets. |
| 7 | Regulatory approval weight | Approved = 1.0; phase3 = 0.8; withdrawn/phase2-3 = 0.7; phase2 = 0.6; phase1-2 = 0.5; phase1 = 0.4; unknown = 0.3. | Evidence-informed heuristic. | Clinical-stage maturity is a reasonable proxy for precedent strength. Lomash et al. 2023 and Lomash et al. 2025 support the importance of regulatory planning, ODD/RPDD, TPP, and FDA interaction in rare-disease AAV development. FDA/EMA guidance in the bibliography supports regulatory maturity as a development constraint. | Later-stage or approved programs are stronger development precedents than early-stage programs. | Numerical spacing is heuristic. Withdrawn status is ambiguous: it may still prove technical feasibility but can signal commercial, safety, or efficacy limitations. |
| 8 | Vector immunogenicity | Seroprevalence <10% = 2.0; 10-19% = 1.5; 20-39% = 1.0; >=40% = 0.5. | Direct evidence for seroprevalence values; heuristic for bins. | Boutin et al. 2010, Calcedo and Wilson 2013, Mingozzi and High 2013, Verdera et al. 2020, and Wang et al. 2024 support AAV humoral immunity as a barrier. Current code values: AAV5 9%, AAVrh10 10%, AAV2/6 17%, AAV1 20%, AAV9 22%, AAV8 30%, AAV2 55%, LV 2%. | Pre-existing anti-capsid immunity is treated as a vector-level eligibility and development risk. Lower estimated seroprevalence receives a higher score. | Seroprevalence varies by geography, age, assay, neutralisation threshold, population, and cross-reactivity. Does not model dose, complement, T-cell responses, steroid regimen, anti-transgene immunity, or redosing. |
| 9 | Therapeutic window | Adult/chronic = 2.0; progressive childhood = 1.5; early childhood = 1.2; neonatal = 0.8; congenital/rapidly fatal = 0.5. | Evidence-informed heuristic. | Kirschner and Cathomen 2020 supports timing importance, including stronger effects when SMA gene therapy is administered before symptoms. Natural-history logic and HPO terms support using disease timing as a trial-feasibility constraint. | Diseases needing very early treatment are not impossible, but clinical translation is harder because irreversible damage may occur before dosing. | Exact bins are heuristic and disease-name keyword matching is crude. Should use disease-specific natural history, newborn screening availability, and age at irreversible pathology when possible. |
| 10 | Cross-correction | Secreted or secreted lysosomal = 1.0; lysosomal non-secreted = 0.8; intracellular/membrane = 0.2. | Direct biological rationale; heuristic numeric bins. | Lysosomal storage disease and ex vivo HSC literature, including Biffi et al. 2013, supports cross-correction as a powerful mechanism for secreted/lysosomal enzymes. General gene therapy biology supports lower rescue potential for intracellular/membrane proteins. | Cross-correctable proteins can benefit untransduced cells, reducing the required fraction of target-cell transduction. | Current code is too coarse. Some lysosomal membrane proteins, secreted proteins with poor uptake, and structural membrane proteins need separate treatment. |
| 11 | Immune privilege | Retina = 1.0; CNS = 0.9; liver = 0.8; muscle/heart = 0.6; kidney = 0.5; hematopoietic = 0.3. | Evidence-informed heuristic. | Retina, CNS, and liver immune environments are widely discussed in gene therapy reviews and clinical precedent. Wang et al. 2024 reviews immune responses and safety concerns in AAV gene therapy. | Target tissues differ in immune surveillance and durability risk, so tissue context modifies precedent strength. | Needs stronger tissue-specific citations. Current values do not model route, dose, capsid, promoter, inflammation, immunosuppression, or disease-specific immune activation. |
| 12 | Promoter availability | Liver/retina = 1.0; CNS/muscle = 0.8; hematopoietic = 0.7; heart = 0.6; kidney = 0.4. | Evidence-informed heuristic. | Clinical programs in the catalog support promoter/tissue precedent: liver AAV programs, Luxturna/retinal programs, Elevidys/MHCK7-style muscle expression, lentiviral HSC programs. PaVe-GT papers support the importance of vector design and product planning. | Tissues with multiple clinically used promoters are treated as easier to engineer safely and effectively. | Needs explicit citations per promoter. Current score does not distinguish cell-type specificity, promoter size, expression strength, disease cell type, or silencing risk. |
| 13 | Route of administration feasibility | Liver = 1.0; muscle = 0.9; hematopoietic = 0.9; retina = 0.8; CNS = 0.7; heart = 0.6; kidney = 0.4. | Evidence-informed heuristic. | Approved/late-stage program routes support this: IV liver AAV for hemophilia/metabolic programs, subretinal/intravitreal ocular programs, ex vivo HSC lentiviral programs, intrathecal/ICV CNS programs, systemic/IM muscle programs. Wang et al. 2024 and PaVe-GT papers support route and development planning as major constraints. | Established clinical delivery routes increase precedent transferability. | Values are heuristic. Route feasibility depends on target cell type, required biodistribution, procedural risk, age, dose, immune toxicity, and whether partial tissue correction is sufficient. |
| 14 | Organelle targeting feasibility | mtDNA-encoded gene (MT-* symbol or mitochondrial inheritance) = 0.0; nuclear-encoded mitochondrial matrix protein (UniProt annotation + MTS signal) = 0.5; peroxisomal targeting required = 0.7; no special organelle targeting required = 1.0. | Evidence-informed heuristic with source-linked disease facts. | Standard nuclear AAV delivers a transgene to the nucleus where it is transcribed and translated by cytoplasmic ribosomes. For most disease genes this is sufficient. mtDNA-encoded genes require allotopic expression: cytoplasmic recoding plus an artificial MTS (real-world precedent: GS010/Lumevoq for MT-ND4 LHON; EMA MAA withdrawn April 2023 after primary endpoint not met). Nuclear-encoded mitochondrial matrix proteins (e.g. MUT in MMA) require the therapeutic construct to include an intact N-terminal MTS for correct post-translational import. Without this dimension, LHON received 6.8/10 and MMA received 7.8/10 based solely on vector/tissue comparisons — a category error that this dimension corrects. | Makes a fundamental delivery mismatch numerically visible in the composite score. | Only models mtDNA and nuclear-encoded mitochondrial matrix failure modes explicitly. Peroxisomal (PTS1/PTS2) and lysosomal membrane protein issues are partially captured by other dimensions. Does not model partial allotopic success, heteroplasmy level, or tissue-specific mtDNA copy number. |

## Source Mapping From Zotero Export

The exported Zotero file is `Reading Literature/Reading Literature.bib`.
The PDFs have also been extracted to searchable text files in
`Reading Literature/text/` using `extract_pdfs.py`.

| Zotero key | Useful for | Evidence use |
|---|---|---|
| `chamberlain_microdystrophin_2023` | DMD microdystrophin, oversized native DMD, accelerated approval/surrogate endpoint | Supports the DMD micro/mini-transgene exception and the statement that full-length dystrophin exceeds single AAV capacity. |
| `brooks_platform_2020` | PaVe-GT platform development | Supports platform-vector rationale and standardised rare-disease AAV development framing. |
| `lomash_successfully_2023` | Orphan drug and rare pediatric disease designations | Supports regulatory-development dimension and rare disease program constraints. |
| `lomash_adeno-associated_2025` | AAV development planning, TPP, FDA INTERACT | Supports regulatory planning, early development, and product design constraints. |
| `wang_adeno-associated_2024` | AAV review, immune responses, clinical use, manufacturing and safety concerns | Supports immunogenicity, vector safety, AAV clinical breadth, and delivery-vector limitations. |
| `walkey_comprehensive_2025` | AAV tropism atlas | Supports tropism as a real vector property, while requiring caution about mouse-to-human translation. |
| `kirschner_gene_2020` | Monogenic gene therapy overview | Supports gene addition framing, timing importance, and in vivo/ex vivo distinction. |
| `rath_representation_2012` | Orphanet methodology | Supports use of Orphanet as rare disease source. |
| `lagorce_phenotypic_2024` | HPO/ORDO phenotypic similarity | Supports using phenotype similarity methods in rare disease computational pipelines. |
| `wei_dismvc_2024` | Disease similarity modelling | Supports computational disease-similarity framing, but not gene therapy-specific scoring. |
| `georgeson_bionitio_2019` | Bioinformatics command-line tool practices | Supports CLI, packaging, documentation, tests, reproducibility framing. |
| `leprevost_best_2014` | Bioinformatics software best practices | Supports software engineering/reproducibility methods. |

## Page-Checked Local Text Anchors

These local text anchors come from the extracted Zotero PDFs. Use them to trace
the strongest scoring claims back to exact readable passages.

| Claim | Local extracted-text anchor | How it supports the scoring table |
|---|---|---|
| Full-length dystrophin exceeds single-AAV packaging capacity; microdystrophin is the relevant engineered strategy. | `Reading Literature/text/chamberlain-et-al-2023-microdystrophin-expression-as-a-surrogate-endpoint-for-duchenne-muscular-dystrophy-clinical-trial.txt`, lines 24-29 and 214-218. | Supports the DMD native-gene hard fail and the `DMD_micro` exception added to NanoGT. |
| Microdystrophin constructs are shortened functional dystrophin genes intended to retain key function. | Same Chamberlain text file, lines 95-97, 218-226, and 253-255. | Supports treating SRP-9001/DMD_micro as an engineered-cargo precedent rather than as ordinary full-length gene replacement. |
| AAV therapy faces immune barriers including pre-existing immunity and neutralising antibodies. | `Reading Literature/text/wang-et-al-2024-adeno-associated-virus-as-a-delivery-vector-for-gene-therapy-of-human-diseases.txt`, lines 2200-2208 and 2297-2308. | Supports including vector immunogenicity as a scoring dimension. |
| AAV antibody interactions can block target-cell entry; complement activation is observed with high-dose rAAV. | Same Wang text file, lines 2329-2337 and 2377-2419. | Supports the limitation that immunogenicity is broader than simple seroprevalence and includes complement/toxicity risks. |
| AAV tropism is tissue- and cell-type dependent and varies across species. | `Reading Literature/text/walkey-et-al-2025-a-comprehensive-atlas-of-aav-tropism-in-the-mouse.txt`, lines 145-152 and 888-900. | Supports using tropism while explicitly warning that mouse tropism is not directly human efficacy. |
| AAV tropism studies measure biodistribution and functional transduction across tissues. | Same Walkey text file, lines 180-189, 324-326, and 350-362. | Supports treating vector/tissue overlap as evidence-informed rather than arbitrary. |
| Target Product Profile and early FDA interaction guide AAV gene therapy development. | `Reading Literature/text/lomash-et-al-2025-adeno-associated-virus-gene-therapy-development-early-planning-and-regulatory-considerations-to-adv.txt`, lines 21-34 and 187-208. | Supports the regulatory maturity/planning dimension as a development constraint. |
| FDA INTERACT meetings can address preclinical models, safety, biodistribution, CMC, immunogenicity, and clinical design. | Same Lomash text file, lines 217-231 and 424-436. | Supports interpreting approval/regulatory stage as more than a label: it reflects accumulated development evidence and regulator interaction. |

## Sources Already In `paper/references.md`

These are not all in the Zotero export, but they are already in the project
bibliography and map directly to scoring claims.

| Reference number | Source | Scoring relevance |
|---:|---|---|
| 5 | Russell et al. 2017 | Luxturna, retinal route, AAV2 precedent. |
| 6-7 | Mendell et al. 2017; Day et al. 2021 | Zolgensma/SMA, AAV9, timing of early treatment. |
| 8 | Pipe et al. 2023 | Hemgenix, liver AAV5 precedent. |
| 9 | Pasi et al. 2020 | Roctavian/large AAV cargo hepatic precedent. |
| 10 | Mendell et al. 2020 | DMD microdystrophin clinical precedent. |
| 13 | Zincarelli et al. 2008 | AAV serotype tropism. |
| 14 | Foust et al. 2009 | AAV9 CNS relevance. |
| 15 | Grieger and Samulski 2005 | AAV packaging capacity. |
| 16 | Naso et al. 2017 | AAV vector review. |
| 17 | Chamberlain et al. 2016 | Oversized transgenes and engineering strategies. |
| 22-25 | Boutin et al. 2010; Calcedo and Wilson 2013; Mingozzi and High 2013; Verdera et al. 2020 | AAV immunogenicity and seroprevalence. |
| 26 | Biffi et al. 2013 | Lentiviral HSC and lysosomal/leukodystrophy cross-correction precedent. |
| 34-36 | FDA/EMA guidance | Regulatory maturity, CMC, and clinical/non-clinical development framing. |

## Methods Text To Add

Suggested paragraph for `paper/methods.md`, after the sentence introducing the
14 scoring dimensions:

> The scoring scheme was not trained against clinical outcome data. Instead,
> thresholds were selected using a transparent evidence-informed heuristic
> approach. Where quantitative constraints were available, such as approximate
> vector cargo capacity and published AAV seroprevalence estimates, these were
> used directly. Where no validated quantitative weighting scheme exists, such
> as assigning relative importance to pathway similarity, promoter availability,
> or route feasibility, rule-based bins were chosen to preserve interpretability
> and allow sensitivity analysis. Scores should therefore be interpreted as
> relative precedent-strength estimates rather than probabilities of clinical
> efficacy.

## Immediate Gaps To Fix Before Submission

1. Add page-checked citations for promoter availability by tissue.
2. Add page-checked citations for immune privilege by tissue.
3. Add page-checked citations for route feasibility categories.
4. Source-audit every row in `data/disease_mechanisms_46.csv` beyond the currently checked cohort-level links.
5. Run a sensitivity analysis with alternate weights, for example equal weights
   for all dimensions and a stricter route/tropism weighting.
6. Move exact threshold values into a documented configuration or methods table
   if the project continues beyond the dissertation proof-of-concept.
