# Discussion

## 1. Principal Findings

This dissertation developed and tested NanoGT, a computational framework for matching monogenic rare diseases to existing gene-therapy precedents. The current implementation was applied to a 46-disease cohort and produced interpretable scored results for 45 diseases. The one exception, Neurofibromatosis type 1, received a packaging hard-fail because NF1 (8,451 bp) exceeds the capacity of every vector in the catalogue — a biologically informative result in its own right. Duchenne muscular dystrophy remains biologically informative: the native DMD coding sequence fails the ordinary single-vector packaging gate, while SRP-9001 is surfaced only as an engineered micro-dystrophin precedent. This distinction prevents microgene strategies from being mistaken for ordinary full-length gene replacement.

The central finding is that the framework does not return random high scores. Instead, it organises diseases into recognisable precedent clusters: lentiviral haematopoietic stem-cell therapy for lysosomal/leukodystrophy-like disorders, liver-directed AAV programmes for metabolic diseases, and retinal AAV programmes for inherited retinal disorders. These clusters are plausible given the underlying biology, vector delivery history, and regulatory precedent landscape.

## 2. Internal Validation

The positive-control behaviour supports the proof-of-concept value of the scoring system. Haemophilia B ranked Hemgenix as the top precedent with the highest score in the cohort. ADA-SCID mapped to Strimvelis, correctly identifying an ex vivo haematopoietic approach. Spinal muscular atrophy mapped to the AAV9/Zolgensma/OAV101 precedent space. These results show that the framework can recover obvious known precedents when they exist in the catalogue.

However, validation is not perfect. Fabry disease (GLA) ranked Libmeldy (lentiviral ex vivo HSC, 8.9/10) above ST-920 (AAV2/6 liver-directed GLA replacement, 8.8/10), despite ST-920 being the disease-specific programme developed for Fabry disease. A similar pattern appears in Mucopolysaccharidosis type II, where Libmeldy (9.3/10) ranked ahead of RGX-121 (AAV9 intrathecal IDS, 8.9/10), the disease-specific programme. In both cases the disease-specific programme is recovered within the top three, so top-k recovery succeeds; but the approved lentiviral HSC precedent scores marginally higher than the disease-matched AAV programme because the current formula gives shared delivery class and regulatory approval stage significant weight. This reflects a genuine calibration issue: the framework slightly over-weights broad precedent class features relative to exact disease identity. It is an important limitation to state honestly rather than conceal, and it reinforces why validation should be reported using top-k recovery and qualitative biological plausibility rather than top-1 accuracy alone.

## 3. Biological and Translational Interpretation

The dominance of Libmeldy as a precedent for lysosomal and leukodystrophy-like disorders is one of the most coherent outputs of the 46-disease run. Ex vivo lentiviral haematopoietic stem-cell therapy is a strong development precedent for diseases where corrected cells can engraft, migrate, or provide cross-correcting enzyme. This supports the idea that NanoGT can surface regulatory and delivery precedents that may not be obvious from disease name alone.

At the same time, the Libmeldy cluster demonstrates why the tool must remain interpretive rather than automatic. Some lysosomal labels refer to secreted enzymes with cross-correction potential; others refer to lysosomal membrane channels or transporters that require cell-autonomous correction. Treating those as equivalent would overstate the translational readiness of several matches. The dissertation should use this cluster as both a success and a limitation: the framework identifies the right neighbourhood, but expert biological interpretation is needed before moving from neighbourhood to development plan.

A concrete example of this residual limitation is nephropathic cystinosis (CTNS, 6.4/10), which returned Strimvelis (ex vivo HSC/LV) as its top precedent. CTNS encodes cystinosin, a lysosomal membrane transporter — the same protein class as MCOLN1 in mucolipidosis type IV and SLC17A5 in Salla disease. Like those cases, cystinosin cannot be secreted or taken up by neighbouring cells via the mannose-6-phosphate receptor pathway, so the HSC/Strimvelis precedent captures the integrating ex vivo HSC delivery class but not the cell-autonomous, tissue-specific correction logic that renal cystinosis actually requires. This is the same limitation already flagged for ML-IV in the v2 scoring notes, and it demonstrates that the lysosomal membrane protein classification issue persists for newly added diseases where the fix was not explicitly applied. The score should be interpreted as "integrating HSC-vector precedent feasibility" rather than "per-cell renal delivery precedent", and the cystinosis report should be accompanied by the same membrane-transporter caveat used for ML-IV.

The hepatic metabolic cluster around BMN 307 is similarly useful but not definitive. Liver-directed AAV is a plausible precedent class for several metabolic diseases, but each disease differs in newborn-screening availability, subcellular localisation, disease reversibility, toxic metabolite kinetics, and whether liver correction alone is sufficient. The retinal cluster is clinically plausible because the eye has established delivery routes and immune privilege, but exact target cell type and disease mechanism remain critical. For this reason, the current implementation now includes a source-linked mechanism/modality layer rather than relying on inheritance alone as a proxy for loss of function.

## 4. Limitations

### 4.1 Catalogue coverage

The current surrogate catalogue contains 21 gene-therapy programmes. This gives useful coverage of AAV and lentiviral precedents, but it is not a comprehensive clinical-trial landscape. The catalogue is biased toward better-known approved or late-stage programmes and under-represents kidney, cardiac, peripheral nervous system, mitochondrial, dominant-negative, RNA, editing, and non-viral delivery approaches. Any disease whose best precedent lies outside the catalogue may receive a misleadingly weak or indirect match.

### 4.2 Manual disease facts and source verification

The 46-disease CSV (`disease_cohort_46.csv`) serves as the primary reproducibility artefact for the cohort. All 46 ORPHA identifiers, OMIM cross-references, gene symbols, and inheritance patterns were fact-checked against live Orphanet and OMIM source pages; each row is now marked `source_checked` with the verified Orphanet URL. UniProt accession numbers and canonical CDS lengths (bp) have been added as additional columns to support future packaging-score auditing.

The same applies to the mechanism evidence table. `data/disease_mechanisms_46.csv` prevents the framework from pretending that inheritance equals molecular mechanism, but each source link and compatibility label should be treated as an auditable claim. Where the mechanism is poorly understood or the evidence is indirect, the correct label is unknown, uncertain, or conditional rather than a forced loss-of-function assignment.

### 4.3 Heuristic pathway and therapeutic-window inference

Pathway similarity and therapeutic window are currently inferred by keyword-style heuristics. This is acceptable for a proof-of-concept dissertation if stated honestly, but it is not equivalent to curated pathway modelling or formal natural-history extraction. Future work should integrate Reactome/KEGG/GO identifiers and structured natural-history fields from Orphanet or OMIM.

### 4.4 Cross-correction and protein localisation

The current cross-correction score is too coarse. It does not fully separate secreted proteins, secreted lysosomal enzymes, non-secreted lysosomal enzymes, lysosomal membrane proteins, cytosolic proteins, nuclear proteins, and mitochondrial proteins. This matters because vector spread and required transduction fraction differ dramatically across these categories.

### 4.5 Scope restriction to gene addition

NanoGT v0.1 is fundamentally a gene-addition precedent matcher with limited engineered-cargo handling. It is not designed for dominant-negative disease, toxic gain-of-function disease, repeat-expansion disease, RNA knockdown, antisense therapy, base editing, prime editing, dual-AAV reconstruction, or mitochondrial replacement strategies. DMD and LHON illustrate this boundary: DMD requires explicit microgene/engineering logic, while LHON depends on specialised mitochondrial or allotopic-expression assumptions rather than ordinary nuclear gene addition.

### 4.6 Score calibration

Composite scores are heuristic relative scores, not calibrated probabilities of success. The framework has not yet been trained or validated against a large set of clinical outcomes. Therefore, scores should be used for prioritisation and explanation, not for go/no-go decisions.

## 5. Implications for the Dissertation

The strongest dissertation framing is not "NanoGT solves rare-disease gene therapy selection." The defensible framing is:

- NanoGT is a reproducible proof-of-concept framework for precedent mapping.
- It integrates biological, vector, clinical, and regulatory dimensions in one scoring system across fourteen dimensions.
- It can recover several known precedents and generate interpretable disease clusters across a 46-disease cohort.
- It explicitly exposes failure modes: oversized cargo, mitochondrial allotopic requirements, and NF1's packaging hard-fail; and it produces interpretable conditional-confidence results for the non-LOF arm.

This is enough for a strong dissertation if the report is honest, well-referenced, and clear about limitations.

## 6. Future Work

The next version should prioritise: expansion and versioning of the surrogate catalogue; formal source provenance for every disease fact; exact-target bonus scoring for validation cases; better cross-correction/protein-localisation classes; Reactome/KEGG/GO pathway mapping; natural-history extraction; top-k validation metrics; and support for non-standard therapeutic modalities such as micro-gene, dual-vector, editing, RNA, and mitochondrial strategies.
