# Results Interpretation — 30-Disease NanoGT Cohort

## What the current results actually show

NanoGT has now been run on 30 diseases rather than the earlier 10-disease pilot. The current output supports a dissertation-level proof-of-concept claim: a thirteen-dimension heuristic framework can map monogenic rare diseases onto existing gene-therapy precedents in a way that produces interpretable biological clusters and exposes obvious failure modes. The thirteenth dimension is an explicit mechanism/modality compatibility check, so the framework no longer assumes inheritance alone proves loss-of-function gene-addition suitability.

It does not support a clinical-grade claim that the top-ranked programme is directly reusable, safe, or ready for translation. Every top match still requires disease-specific literature review, target biology validation, vector engineering, toxicology, manufacturing review, and regulatory assessment.

## Quantitative summary

- Diseases analysed: 30.
- Ranked with at least one current-catalog precedent: 30.
- Full-length native DMD still fails ordinary single-AAV packaging; SRP-9001 is scored separately as an engineered micro-dystrophin precedent.
- High-confidence top matches: 27 of 30 diseases.
- Medium-confidence top matches: 3 of 30 diseases.
- Score range among top matches: 6.8/10 to 9.9/10.

## Top precedent programmes

- Libmeldy: 11 top-ranked diseases
- BMN 307: 4 top-ranked diseases
- CPCB-RPE1: 3 top-ranked diseases
- Hemgenix: 2 top-ranked diseases
- Strimvelis: 2 top-ranked diseases
- OAV101-IT: 2 top-ranked diseases
- Luxturna: 2 top-ranked diseases
- SRP-9001: 2 top-ranked diseases
- Skysona: 1 top-ranked diseases
- AT132: 1 top-ranked diseases

## Vector classes represented in top matches

- LV: 14 top-ranked diseases
- AAV5: 6 top-ranked diseases
- AAV8: 4 top-ranked diseases
- AAV9: 4 top-ranked diseases
- AAV2: 2 top-ranked diseases

The top-match distribution is heavily concentrated in lentiviral/HSC and AAV liver/retina programmes. This is a finding and a limitation. It indicates that the current surrogate catalogue has strong coverage for lysosomal/leukodystrophy-like, hepatic metabolic, and retinal disease spaces, but much weaker coverage for kidney, cardiac, peripheral nerve, dental/enamel, mitochondrial, and dominant-negative biology.

## Interpretation by cluster

### 1. Libmeldy / lentiviral HSC cluster

Libmeldy dominates the lysosomal and leukodystrophy-like disease results. This is biologically plausible because lentiviral haematopoietic stem-cell therapy is an established approach for some lysosomal storage diseases where genetically corrected cells can engraft and provide systemic or CNS benefit. The strongest high-scoring examples include:

- Hemophilia B (F9): Hemgenix / AAV5 at 9.9/10
- Mucopolysaccharidosis type I (IDUA): Libmeldy / LV at 9.4/10
- Mucopolysaccharidosis type II (IDS): Libmeldy / LV at 9.3/10
- Metachromatic leukodystrophy (ARSA): Libmeldy / LV at 9.2/10
- Mucopolysaccharidosis type IIIA (Sanfilippo A) (SGSH): Libmeldy / LV at 9.2/10
- Mucolipidosis type IV (MCOLN1): Libmeldy / LV at 9.1/10
- Gaucher disease (GBA): Libmeldy / LV at 8.9/10
- Krabbe disease (GALC): Libmeldy / LV at 8.9/10
- Salla disease (SLC17A5): Libmeldy / LV at 8.8/10
- Fabry disease (GLA): Libmeldy / LV at 8.8/10

However, this cluster must be handled carefully in the report. Not every lysosomal disease behaves like metachromatic leukodystrophy. Secreted lysosomal enzymes can benefit from cross-correction; membrane proteins and transporters may require much broader cell-autonomous correction. The dissertation should explicitly separate these cases rather than treating all lysosomal labels as equivalent.

### 2. BMN 307 / liver metabolic cluster

BMN 307 appears as a recurring precedent for liver metabolic disorders. This reflects shared liver targeting, manageable transgene size, and metabolic pathway similarity. The most defensible claim is that NanoGT can identify a relevant liver-directed AAV precedent class. The weaker claim, which should be avoided, is that BMN 307 itself is directly reusable across unrelated metabolic diseases.

### 3. Retinal cluster

The retinal diseases form a coherent AAV precedent cluster, but exact rankings expose calibration issues. For example, Leber congenital amaurosis currently ranks CPCB-RPE1 above Luxturna, even though Luxturna is the obvious approved RPE65 precedent. This means the dissertation should not overstate top-1 validation accuracy. A stronger and more honest metric is top-k recovery: whether the known precedent appears in the top few matches and whether the ranking explanation is biologically coherent.

### 4. Stress tests

DMD correctly fails the native full-length single-AAV packaging gate, while SRP-9001 is surfaced as a separate engineered micro-dystrophin precedent. LHON remains medium-confidence because mitochondrial gene delivery is a special case not well represented by a standard nuclear gene-addition framework. These stress tests are valuable because they demonstrate that the tool can distinguish ordinary gene addition from specialised modalities rather than forcing a simple high-confidence recommendation.

## Limitations closed by explicitly naming them

The main limitations are no longer hidden implementation gaps; they are now named dissertation limitations:

1. Catalogue coverage is incomplete and biased toward the programmes manually entered into `src/nanogt/catalog.py`.
2. Disease facts in `data/disease_cohort_30.csv` still require user/supervisor fact-checking; every row is currently marked `needs_user_fact_check`.
3. Pathway inference is heuristic and keyword-based, not a curated Reactome/KEGG/GO semantic model.
4. HPO-based therapeutic-window inference is a rough proxy and should not be treated as natural-history modelling.
5. Cross-correction scoring does not yet distinguish enough between secreted enzymes, lysosomal enzymes, membrane proteins, and fully intracellular proteins.
6. Disease mechanism evidence is now explicit in `data/disease_mechanisms.csv`, but those source links and compatibility labels still require final supervisor-level checking before submission.
7. Mitochondrial, dominant-negative, toxic gain-of-function, editing, RNA, dual-vector, and most micro-gene strategies remain outside the current v0.1 scope except where explicitly catalogued as engineered precedents.
8. Scores are uncalibrated heuristic scores, not probabilities of clinical success.
9. Literature references and disease-source claims must be verified before final dissertation submission.

## Dissertation-safe result statement

A safe wording for the report is:

"In a 30-disease proof-of-concept cohort, NanoGT generated interpretable precedent rankings for all diseases while explicitly recording source-linked molecular mechanism evidence and gene-addition compatibility. The resulting rankings clustered diseases into biologically plausible precedent groups, including lentiviral/HSC lysosomal disease, liver-directed metabolic AAV programmes, and retinal AAV programmes, while stress-test cases such as DMD and LHON exposed the boundary between ordinary gene addition and specialised modalities. These findings support the feasibility of computational precedent mapping for early-stage gene-therapy prioritisation, while highlighting the need for catalogue expansion, mechanism-source verification, improved pathway inference, and disease-specific expert review before translational use."
