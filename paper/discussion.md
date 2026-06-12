# Discussion

## 1. Principal Findings

This dissertation developed and tested NanoGT, a computational framework for matching monogenic rare diseases to existing gene-therapy precedents. The current implementation was applied to a 30-disease cohort and produced interpretable rankings for 29 diseases. One disease, Duchenne muscular dystrophy, failed the single-vector packaging gate because the native DMD coding sequence substantially exceeds standard AAV capacity. This failure is expected and biologically informative: DMD requires micro-dystrophin, dual-vector, editing, or other alternative strategies outside the current v0.1 model.

The central finding is that the framework does not return random high scores. Instead, it organises diseases into recognisable precedent clusters: lentiviral haematopoietic stem-cell therapy for lysosomal/leukodystrophy-like disorders, liver-directed AAV programmes for metabolic diseases, and retinal AAV programmes for inherited retinal disorders. These clusters are plausible given the underlying biology, vector delivery history, and regulatory precedent landscape.

## 2. Internal Validation

The positive-control behaviour supports the proof-of-concept value of the scoring system. Haemophilia B ranked Hemgenix as the top precedent with the highest score in the cohort. ADA-SCID mapped to Strimvelis, correctly identifying an ex vivo haematopoietic approach. Spinal muscular atrophy mapped to the AAV9/Zolgensma/OAV101 precedent space. These results show that the framework can recover obvious known precedents when they exist in the catalogue.

However, validation is not perfect. Leber congenital amaurosis did not return Luxturna as the single top-ranked result in the current summary, despite Luxturna being the canonical approved RPE65 therapy. CPCB-RPE1 ranked first, with Luxturna close behind. This is an important calibration issue rather than something to conceal. The current scoring formula can over-weight shared vector/tissue/programme-stage features relative to exact disease identity. In the final dissertation, validation should therefore be reported using top-k recovery and qualitative biological plausibility, not only top-1 accuracy.

## 3. Biological and Translational Interpretation

The dominance of Libmeldy as a precedent for lysosomal and leukodystrophy-like disorders is one of the most coherent outputs of the 30-disease run. Ex vivo lentiviral haematopoietic stem-cell therapy is a strong development precedent for diseases where corrected cells can engraft, migrate, or provide cross-correcting enzyme. This supports the idea that NanoGT can surface regulatory and delivery precedents that may not be obvious from disease name alone.

At the same time, the Libmeldy cluster demonstrates why the tool must remain interpretive rather than automatic. Some lysosomal labels refer to secreted enzymes with cross-correction potential; others refer to lysosomal membrane channels or transporters that require cell-autonomous correction. Treating those as equivalent would overstate the translational readiness of several matches. The dissertation should use this cluster as both a success and a limitation: the framework identifies the right neighbourhood, but expert biological interpretation is needed before moving from neighbourhood to development plan.

The hepatic metabolic cluster around BMN 307 is similarly useful but not definitive. Liver-directed AAV is a plausible precedent class for several metabolic diseases, but each disease differs in newborn-screening availability, subcellular localisation, disease reversibility, toxic metabolite kinetics, and whether liver correction alone is sufficient. The retinal cluster is clinically plausible because the eye has established delivery routes and immune privilege, but exact target cell type and disease mechanism remain critical.

## 4. Limitations

### 4.1 Catalogue coverage

The current surrogate catalogue contains 21 gene-therapy programmes. This gives useful coverage of AAV and lentiviral precedents, but it is not a comprehensive clinical-trial landscape. The catalogue is biased toward better-known approved or late-stage programmes and under-represents kidney, cardiac, peripheral nervous system, mitochondrial, dominant-negative, RNA, editing, and non-viral delivery approaches. Any disease whose best precedent lies outside the catalogue may receive a misleadingly weak or indirect match.

### 4.2 Manual disease facts and source verification

The 30-disease CSV is useful for reproducibility, but every row is still marked as requiring fact-checking. Before final submission, the disease name, ORPHA identifier, causal gene, inheritance, tissues, prevalence class, and OMIM cross-reference must be checked against Orphanet, OMIM, UniProt, and at least one disease-specific review or primary paper. This is now a dissertation-critical work item, not a cosmetic clean-up task.

### 4.3 Heuristic pathway and therapeutic-window inference

Pathway similarity and therapeutic window are currently inferred by keyword-style heuristics. This is acceptable for a proof-of-concept dissertation if stated honestly, but it is not equivalent to curated pathway modelling or formal natural-history extraction. Future work should integrate Reactome/KEGG/GO identifiers and structured natural-history fields from Orphanet or OMIM.

### 4.4 Cross-correction and protein localisation

The current cross-correction score is too coarse. It does not fully separate secreted proteins, secreted lysosomal enzymes, non-secreted lysosomal enzymes, lysosomal membrane proteins, cytosolic proteins, nuclear proteins, and mitochondrial proteins. This matters because vector spread and required transduction fraction differ dramatically across these categories.

### 4.5 Scope restriction to gene addition

NanoGT v0.1 is fundamentally a gene-addition precedent matcher. It is not designed for dominant-negative disease, toxic gain-of-function disease, repeat-expansion disease, RNA knockdown, antisense therapy, base editing, prime editing, dual-AAV reconstruction, micro-gene engineering, or mitochondrial replacement strategies. DMD and LHON illustrate this boundary.

### 4.6 Score calibration

Composite scores are heuristic relative scores, not calibrated probabilities of success. The framework has not yet been trained or validated against a large set of clinical outcomes. Therefore, scores should be used for prioritisation and explanation, not for go/no-go decisions.

## 5. Implications for the Dissertation

The strongest dissertation framing is not "NanoGT solves rare-disease gene therapy selection." The defensible framing is:

- NanoGT is a reproducible proof-of-concept framework for precedent mapping.
- It integrates biological, vector, clinical, and regulatory dimensions in one scoring system.
- It can recover several known precedents and generate interpretable disease clusters across a 30-disease cohort.
- It explicitly exposes failure modes where current gene-addition precedent is weak or infeasible.

This is enough for a strong dissertation if the report is honest, well-referenced, and clear about limitations.

## 6. Future Work

The next version should prioritise: expansion and versioning of the surrogate catalogue; formal source provenance for every disease fact; exact-target bonus scoring for validation cases; better cross-correction/protein-localisation classes; Reactome/KEGG/GO pathway mapping; natural-history extraction; top-k validation metrics; and support for non-standard therapeutic modalities such as micro-gene, dual-vector, editing, RNA, and mitochondrial strategies.
