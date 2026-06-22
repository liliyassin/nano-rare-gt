# Methods

## 1. System Overview

A computational framework was developed to systematically match untreated monogenic diseases to approved or late-stage gene therapy programs that could serve as regulatory and scientific precedents. The framework, designated NanoGT, accepts an Orphanet disease identifier as input and produces a ranked list of gene therapy precedents alongside a structured match report. The pipeline operates in three sequential stages: (1) disease and gene characterisation from public databases, (2) multi-dimensional scoring of each candidate precedent program against the query disease, and (3) report generation with per-dimension score breakdowns and plain-language rationales.

The system was implemented in Python 3 using a modular architecture. Disease metadata was retrieved from the Orphanet REST API (api.orphacode.org). Gene and protein annotations were retrieved from the UniProt REST API (rest.uniprot.org/uniprotkb). All external API responses were cached in-session to minimise redundant network requests. A static SQLite database was used to store the curated gene therapy surrogate catalog, vector properties, and generated match results. In the event of API unavailability, a manually curated static fallback dataset covering all tested diseases was used to ensure reproducibility without internet access.

---

## 2. Disease and Gene Characterisation

### 2.1 Disease Metadata (Orphanet)

For each query disease, the Orphanet REST API was queried using the disease's Orphanet numeric code to retrieve the canonical disease name, gene associations, and inheritance pattern. A separate endpoint was queried to obtain cross-references to the Online Mendelian Inheritance in Man (OMIM) database. HPO (Human Phenotype Ontology) terms were supplied as part of a manually curated fallback dataset constructed from Orphanet phenotypic summaries and published literature for each tested disease.

### 2.2 Tissue Mapping from HPO Terms

Affected tissues were derived from HPO term names using keyword mapping. Each HPO term was searched for tissue-indicative keywords: for example, "hepat", "liver", and "jaundice" mapped to liver; "brain", "cerebr", "seizure", and "neurodegenerat" mapped to CNS; "muscul" and "myopathy" mapped to muscle; "retina", "visual", and "optic" mapped to retina. This mapping produced a list of affected tissues used as input to tropism, immune privilege, promoter availability, and route of administration scoring.

### 2.3 Gene and Protein Characterisation (UniProt)

For each causal gene associated with the query disease, the UniProt REST API was queried using the gene symbol with a filter for human (organism ID 9606) manually reviewed Swiss-Prot entries. The following fields were retrieved: UniProt accession, protein name, amino acid sequence length, subcellular localisation, Gene Ontology (GO) terms, UniProt keyword tags, and annotated domain features. Coding sequence (CDS) length in base pairs was estimated by multiplying amino acid sequence length by three. A protein was classified as secreted if any subcellular localisation entry contained "secreted" or "extracellular". Lysosomal localisation was identified by the presence of "lysosom" in any localisation entry or in the UniProt keyword list.

---

## 3. Gene Therapy Surrogate Database

A static database of 21 approved or late-stage gene therapy programs was manually curated from published literature, regulatory approval documents, and ClinicalTrials.gov. Programs were included if they targeted a monogenic, loss-of-function rare disease using an AAV or lentiviral vector. Each entry recorded: program name, target disease, causal gene symbol, vector serotype, primary tissue target, transgene CDS length in base pairs, approval or trial stage, approval year (where applicable), protein class (secreted, lysosomal, membrane, intracellular, or secreted_lysosomal), inheritance pattern (AR or XL), and biological pathway label.

Eight delivery vectors were catalogued: AAV1, AAV2, AAV5, AAV8, AAV9, AAVrh10, AAV2/6, and lentiviral vector (LV). For each vector, the following properties were recorded: cargo limit in base pairs, tissue tropism, CNS/retinal/hepatic/muscle tropism flags, number of existing clinical programs using that serotype, and patent restriction status. The standard cargo limit for all AAV serotypes was set at 4,700 bp, consistent with the established packaging limit for single-stranded AAV. The lentiviral vector cargo limit was set at 8,000 bp, reflecting the larger capacity of lentiviral constructs used in approved haematopoietic stem cell programs.

---

## 4. Fourteen-Dimension Scoring Engine

For each query disease and causal gene pair, every program in the surrogate database was scored across fourteen independent dimensions. Raw scores were summed and normalised to a composite score out of ten, as described in Section 5. Each dimension and its scoring logic is described below.

The scoring scheme was not trained against clinical outcome data. Instead, thresholds were selected using a transparent evidence-informed heuristic approach. Where quantitative constraints were available, such as approximate vector cargo capacity and published AAV seroprevalence estimates, these were used directly. Where no validated quantitative weighting scheme exists, such as assigning relative importance to pathway similarity, promoter availability, or route feasibility, rule-based bins were chosen to preserve interpretability and allow sensitivity analysis. Scores should therefore be interpreted as relative precedent-strength estimates rather than probabilities of clinical efficacy. A separate scoring evidence audit table was maintained to distinguish directly literature-supported parameters from heuristic score bins and to record local text anchors from the reviewed PDFs.

### 4.1 Packaging Fit (max 2.0)

The CDS length of the query gene was compared against the cargo limit of the vector used in the precedent program. If the query gene CDS exceeded the vector cargo limit, a hard fail was returned (score 0.0) and the program was excluded from ranking without further scoring. Otherwise, the utilisation ratio (CDS / cargo limit) was calculated and scored: ≤30% utilisation = 2.0; 31–60% = 1.5; 61–85% = 1.0; 86–100% = 0.5. For explicitly engineered same-gene micro/mini constructs, such as DMD_micro in a Duchenne muscular dystrophy precedent, the construct CDS was used for the packaging score while the report retained a note that native full-length gene replacement remained oversized. This distinction prevents an engineered micro-transgene strategy from being misclassified as ordinary full-length gene replacement.

### 4.2 Tissue Tropism (max 2.0)

The set of disease-affected tissues was compared against the vector's tissue tropism list and the precedent program's tissue target description. A score of 2.0 was assigned if at least one affected tissue appeared in both the vector tropism list and the precedent program's tissue target. A score of 1.5 was assigned if the precedent program's tissue target matched at least one affected tissue, or if the vector tropism overlapped with two or more affected tissues. A score of 1.0 was assigned for a single tissue overlap with vector tropism. A score of 0.3 was assigned where no overlap was identified. Tropism was treated as an evidence-informed proxy rather than a direct prediction of human biodistribution, because AAV tropism varies by species, route, dose, promoter, and cell type.

### 4.3 Protein Class (max 2.0)

The protein class of the query gene was inferred from UniProt subcellular localisation and keyword annotations, then compared to the protein class of the precedent program. A critical distinction was introduced in scoring version 2 between lysosomal enzymes (soluble, secretable proteins such as ARSA and IDUA that can cross-correct via the mannose-6-phosphate receptor pathway) and lysosomal membrane proteins (channels and transporters such as MCOLN1/mucolipin-1 and SLC17A5/sialin that are anchored in the lysosomal membrane and cannot be secreted or taken up by neighbouring cells). A score of 2.0 was assigned for an exact match between two soluble lysosomal enzymes or two secreted proteins. A score of 1.5 was assigned for a match between two intracellular or two membrane proteins. A score of 1.0 was assigned where the query gene encoded a lysosomal membrane protein matched against a lysosomal enzyme precedent (lysosomal pathway shared, but the cross-correction mechanism inapplicable), or where the query gene had some secreted or extracellular component in a mismatch context. A score of 0.5 was assigned for a clear class mismatch. Prior to this distinction, lysosomal membrane proteins received the same 2.0 score as lysosomal enzymes when matched against programmes such as Libmeldy, inflating composite scores for diseases such as mucolipidosis type IV (MCOLN1) and Salla disease (SLC17A5).

### 4.4 Mechanism and Modality Compatibility (max 2.0)

The molecular mechanism of the query disease was treated as a distinct evidence layer rather than inferred automatically from inheritance. A curated mechanism table (`data/disease_mechanisms_46.csv`) records, for each disease/gene pair in the 46-disease cohort, the mechanism category, a source-linked evidence summary, the preferred therapeutic modality class, and whether ordinary gene addition is compatible, conditional, uncertain, or incompatible. Compatible loss-of-function diseases received 2.0. Conditional cases, such as intracellular cell-autonomous proteins, oversized genes requiring engineered constructs, mitochondrial enzymes, or multi-system metabolic diseases, received 1.5. Uncertain cases received 1.0. An incompatible mechanism constitutes a second hard gate: the program is assigned a composite score of 0.0 and a confidence classification of "fail" and excluded from ranking entirely, analogous to the packaging hard gate in dimension 4.1. This prevents gain-of-function, dominant-negative, or RNA-toxic diseases from receiving plausible-looking scores on vector precedents that would be therapeutically counterproductive. Missing evidence is treated as uncertain and flagged for manual review; inheritance alone is not treated as proof of gene-addition suitability.

### 4.5 Inheritance Compatibility (max 1.0)

The inheritance pattern of the query disease was compared to the inheritance pattern of the precedent program. An exact match between autosomal recessive (AR) or X-linked (XL) patterns received 1.0. A shared loss-of-function pattern received 0.7. A mismatch — for example, a dominant or mitochondrial disease against a recessive precedent — received 0.3. This dimension captures the distinction between loss-of-function diseases (amenable to gene replacement) and gain-of-function or dominant negative diseases (which would require silencing or editing strategies not represented in the current database).

### 4.6 Biological Pathway Similarity (max 2.0)

The biological pathway of the query disease was inferred from gene keywords, GO terms, subcellular localisation, and HPO terms. Pathways considered included lysosomal storage, coagulation, motor neuron, myopathy, retinal visual cycle, retinal phototransduction, mitochondrial complex, amino acid metabolism, urea cycle, and lipid metabolism. A score of 2.0 was assigned for an exact pathway match. A score of 1.5 was assigned for a related pathway, defined by pre-specified groupings of mechanistically adjacent pathways (for example, amino acid metabolism and urea cycle). A score of 0.5 was assigned for a clearly different pathway. Where the pathway could not be inferred, a neutral score of 1.0 was assigned.

### 4.7 Regulatory Approval Weight (max 1.0)

The regulatory stage of the precedent program was used to weight the strength of its precedent value. Scores were assigned as follows: approved = 1.0; withdrawn (previously approved) = 0.7; Phase 3 = 0.8; Phase 2/3 = 0.7; Phase 2 = 0.6; Phase 1/2 = 0.5; Phase 1 = 0.4. This dimension was interpreted as a proxy for accumulated development evidence, including manufacturing, toxicology, clinical design, endpoint, and regulator-interaction experience, not as a guarantee of efficacy.

### 4.8 Vector Immunogenicity (max 2.0)

Pre-existing neutralising antibodies (NAbs) against AAV capsids in the general population are a well-established barrier to treatment eligibility, as patients with NAb titres above defined thresholds are typically excluded from many AAV clinical trials. Population seroprevalence estimates for each vector serotype were sourced from published studies and reviews of AAV humoral immunity [22–25] and used to score immunogenicity risk. Scores were assigned based on approximate seroprevalence: <10% = 2.0; 10–19% = 1.5; 20–39% = 1.0; ≥40% = 0.5. Lentiviral vectors were assigned minimum seroprevalence (~2%) as they are immunologically distinct from AAV serotypes. This dimension captured only vector-level pre-existing humoral immunity; it did not explicitly model complement activation, dose-related toxicity, anti-transgene immunity, T-cell responses, immunosuppression protocols, or redosing feasibility.

### 4.9 Therapeutic Window (max 2.0)

The therapeutic window dimension assessed whether gene therapy could feasibly be administered before irreversible cellular damage occurs. This was inferred from HPO terms and disease name using keyword analysis. Diseases with adult or slowly progressive onset received 2.0. Progressive childhood-onset diseases with neurodegeneration received 1.5. Diseases with early childhood onset where newborn screening integration would substantially improve outcomes received 1.2. Neonatal-onset diseases requiring delivery within weeks of birth received 0.8. Congenital or rapidly fatal early-onset diseases requiring in utero or immediate neonatal delivery received 0.5. This dimension does not penalise the match per se but flags where clinical trial design is substantially more complex.

### 4.10 Cross-Correction Potential (max 1.0)

Cross-correction describes the ability of a transduced cell to secrete the therapeutic protein and thereby correct adjacent untransduced cells. This mechanism amplifies the effective reach of gene delivery without requiring every target cell to receive the vector individually, enabling lower doses and broader tissue coverage. Secreted proteins and secreted lysosomal enzymes (taken up by neighbouring cells via the mannose-6-phosphate receptor pathway) received 1.0. Non-secreted soluble lysosomal enzymes with partial cross-correction capacity received 0.8. Lysosomal membrane proteins (channels and transporters, e.g. MCOLN1, SLC17A5) received 0.0: these proteins are anchored in the lysosomal membrane and cannot be released as soluble cargo, so every target cell must individually receive the vector — no bystander rescue is possible. Intracellular and non-lysosomal membrane-bound proteins, for which no cross-correction is possible, received 0.2. This correction was introduced in scoring version 2; prior to it, lysosomal membrane proteins were erroneously assigned 0.8 as if they were soluble lysosomal enzymes.

### 4.11 Immune Privilege of Target Tissue (max 1.0)

Certain tissues are immunologically privileged: they are partially sequestered from systemic immune surveillance by physical barriers or local immunosuppressive signals. High immune privilege is associated with reduced risk of cytotoxic T-lymphocyte-mediated clearance of transduced cells and more durable long-term transgene expression. Scores were assigned by tissue: retina = 1.0 (blood-retinal barrier, FasL expression, local TGF-β2); CNS = 0.9 (blood-brain barrier); liver = 0.8 (tolerogenic microenvironment: Kupffer cells, IL-10, PD-L1); muscle and heart = 0.6; kidney = 0.5; haematopoietic tissue = 0.3.

### 4.12 Promoter Availability (max 1.0)

The availability of validated, tissue-specific promoters was scored based on the disease's primary target tissue. Validated promoters are essential for restricting transgene expression to the intended cell type and for ensuring therapeutic expression levels. Liver and retinal targets received 1.0, reflecting the availability of multiple clinically validated promoters used in approved programs (ApoE/hAAT, TBG, and transthyretin for liver; VMD2, GRK1, and CRX for retina). CNS and muscle targets received 0.8 (Synapsin-1 and CaMKII for CNS; MHCK7 and CK8 for muscle). Haematopoietic targets received 0.7. Cardiac targets received 0.6. Renal targets received 0.4, reflecting the near-absence of validated kidney-specific promoters in clinical programs.

### 4.13 Route of Administration Feasibility (max 1.0)

The feasibility of delivering the vector to the target tissue via an established clinical route was scored based on the disease's affected tissues. Hepatic delivery via intravenous infusion received 1.0, reflecting its use in all approved hepatic gene therapy programs. Muscle delivery via intravenous or intramuscular injection received 0.9. Haematopoietic delivery via ex vivo haematopoietic stem cell modification and reinfusion received 0.9. Retinal delivery via subretinal or intravitreal injection received 0.8, reflecting the established surgical approach used in Luxturna and GS010. CNS delivery via intrathecal or intracerebroventricular injection received 0.7, reflecting higher procedural risk. Cardiac delivery received 0.6. Renal delivery received 0.4, reflecting the absence of an established kidney-specific delivery route in approved programs.

### 4.14 Organelle Targeting Feasibility (max 1.0)

This dimension assesses whether standard nuclear AAV delivery can produce a functional protein at the correct subcellular compartment for the query disease. It was introduced in scoring version 2 to address a category error in the original implementation: certain diseases were receiving scores based on comparison to nuclear gene-addition programs even when the causal gene requires a fundamentally different delivery logic.

Mitochondrial DNA-encoded genes (MT-* genes, identified by HGNC symbol convention) received a score of 0.0. These genes reside in the mitochondrial genome, use a non-standard genetic code, and are translated by mitochondrial ribosomes inside the organelle. Standard nuclear AAV delivery is inapplicable without allotopic expression: the gene must be recoded for cytoplasmic translation and given an artificial mitochondrial targeting sequence. This strategy is disease-specific and not represented in the current surrogate catalogue. Leber hereditary optic neuropathy (MT-ND4) is the primary example; GS010/Lumevoq (lenadogene nolparvovec) uses this allotopic approach as a real-world precedent, though its EMA marketing authorisation application was voluntarily withdrawn in April 2023 after Phase 3 trials did not demonstrate statistically significant efficacy versus sham injection.

Nuclear-encoded mitochondrial matrix or inner-membrane proteins received a score of 0.5. Nuclear AAV delivery is theoretically feasible, as the gene resides in the nuclear genome, but the N-terminal mitochondrial targeting sequence (MTS) in the therapeutic construct must be intact and functional for correct post-translational import. MTS integrity is not validated by any other scoring dimension and requires disease-specific experimental confirmation. Methylmalonic acidemia (MUT) is the primary example.

Other nuclear-encoded mitochondrial proteins (outer membrane, intermembrane space) received 0.6. Peroxisomal proteins received 0.7, reflecting that AAV delivery is feasible but the peroxisomal targeting signal (PTS1/PTS2) must be preserved in the construct. Proteins with standard subcellular localisation (cytoplasmic, nuclear, secreted, lysosomal, endoplasmic reticulum, plasma membrane) received 1.0, as nuclear AAV delivery directly produces functional protein at the correct location.

---

## 5. Score Normalisation and Confidence Classification

Raw scores across all fourteen dimensions were summed to produce a raw composite with a theoretical maximum of 21.0. This was normalised to a score out of ten using the formula:

**Composite score = (raw sum / 21.0) × 10**

Programs were classified into confidence tiers based on the normalised composite score: high confidence (≥7.5), medium confidence (5.0–7.49), and low confidence (<5.0). Programs that failed the packaging gate (dimension 4.1) received a composite score of 0.0 and a classification of "fail", indicating physical incompatibility between the query gene and the candidate vector.

---

## 6. Cohort Design

The current dissertation analysis used a 46-disease proof-of-concept cohort stored in `data/disease_cohort_46.csv`, with source-linked mechanism evidence stored separately in `data/disease_mechanisms_46.csv`. The cohort was intentionally structured to test more than one success mode: positive controls with approved precedents, benchmark diseases with known gene-therapy precedent, an oversized native-cargo stress test, a mitochondrial-delivery stress test, and a broader pilot cohort of monogenic diseases spanning liver, CNS, retina, muscle, heart, and haematopoietic involvement. Each cohort row records the Orphanet identifier, disease name, causal gene, inheritance pattern, affected tissues, prevalence class, OMIM cross-reference, cohort role, source URL, and fact-check status. Each mechanism row records the disease/gene mechanism category, gene-addition compatibility, preferred modality class, evidence summary, evidence URL, citation label, and evidence verification status.

The cohort should be interpreted as a reproducible dissertation test set rather than a statistically representative sample of all rare diseases. Its purpose is to demonstrate whether the scoring framework produces interpretable precedent rankings and useful failure modes across diverse disease classes.

---

## 7. Output and Report Generation

Results were sorted in descending order of composite score for each disease query. A structured Markdown report was generated containing: source-linked disease mechanism evidence; a ranked summary table of top matches with composite score and confidence tier; a per-match breakdown table showing the score for each of the fourteen dimensions; plain-language rationale notes for each dimension; manual review flags; and a log of packaging-excluded programs. Reports were saved to a standardised output directory using filenames incorporating the Orphanet ID and disease name. A cross-disease summary report was generated to allow comparison of top matches, mechanism categories, gene-addition compatibility labels, and score distributions across all queried diseases.

Each report includes a review flags section that captures translational caveats not reflected in composite rank alone. Version 2 of the framework expanded the flag categories to include: lysosomal membrane protein flags (identifying diseases where the M6P cross-correction mechanism of haematopoietic stem cell precedent programmes is not applicable); mitochondrial DNA gene flags (identifying MT-* genes requiring allotopic expression rather than standard nuclear gene addition); mitochondrial matrix enzyme flags (identifying nuclear-encoded mitochondrial proteins where intact mitochondrial targeting sequence function must be validated); multi-subunit enzyme complex flags (identifying diseases where a single subunit delivered by the vector may not reconstitute full enzymatic activity without co-delivery of other subunits); unresolved disease biology flags (identifying genes whose molecular function is not fully characterised in the curated evidence); and disease heterogeneity flags (identifying diseases such as Gaucher disease and Fabry disease where neuronopathic and non-neuronopathic subtypes require fundamentally different therapeutic strategies and scores should be interpreted subtype-specifically). These flags are designed to be read alongside composite scores and not suppressed: a high-ranking match can legitimately carry several flags requiring review before it is used as a development template.
