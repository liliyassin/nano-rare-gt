# Results Interpretation — 40-Disease NanoGT Cohort

## What the current results actually show

NanoGT has now been run on 46 diseases. The current output supports a dissertation-level proof-of-concept claim: a fourteen-dimension heuristic framework can map monogenic rare diseases onto existing gene-therapy precedents in a way that produces interpretable biological clusters and exposes obvious failure modes. The fourteenth dimension is an explicit organelle-targeting feasibility check, added in v2 to capture mitochondrial and other non-nuclear delivery constraints.

It does not support a clinical-grade claim that the top-ranked programme is directly reusable, safe, or ready for translation. Every top match still requires disease-specific literature review, target biology validation, vector engineering, toxicology, manufacturing review, and regulatory assessment.

## Quantitative summary

- Diseases analysed: 40.
- Ranked with at least one current-catalog precedent: 39.
- Packaging hard-fail (CDS exceeds all vectors): 1 (NF1, 8,451 bp).
- High-confidence top matches: 29 of 33 diseases with a precedent.
- Medium-confidence top matches: 10 of 33 diseases with a precedent.
- Score range among top matches: 5.9/10 to 9.9/10.

## Top precedent programmes

- Libmeldy: 11 top-ranked diseases
- Skysona: 7 top-ranked diseases
- BMN 307: 4 top-ranked diseases
- OAV101-IT: 4 top-ranked diseases
- CPCB-RPE1: 3 top-ranked diseases
- Strimvelis: 3 top-ranked diseases
- Hemgenix: 2 top-ranked diseases
- Luxturna: 2 top-ranked diseases
- SRP-9001: 2 top-ranked diseases
- AT132: 1 top-ranked disease

## Vector classes represented in top matches

- LV: 21 top-ranked diseases
- AAV5: 6 top-ranked diseases
- AAV9: 6 top-ranked diseases
- AAV8: 4 top-ranked diseases
- AAV2: 2 top-ranked diseases

The top-match distribution is heavily concentrated in lentiviral/HSC programmes (Libmeldy, Skysona, Strimvelis together account for 21 of 39 matched diseases). This is a finding and a limitation. It indicates that the current surrogate catalogue has strong coverage for lysosomal/leukodystrophy-like, CNS neuronal, haematopoietic, hepatic metabolic, and retinal disease spaces, but much weaker coverage for kidney, cardiac, peripheral nerve, mitochondrial, dominant-negative, and large-gene biology.

## Interpretation by cluster

### 1. Libmeldy / lentiviral HSC — lysosomal and storage disease cluster

Libmeldy dominates lysosomal and storage disease results. This is biologically plausible because lentiviral haematopoietic stem-cell therapy is an established approach for lysosomal storage diseases where genetically corrected cells can engraft and provide systemic or CNS benefit. The strongest examples include:

- Mucopolysaccharidosis type I (IDUA): Libmeldy / LV at 9.5/10
- Mucopolysaccharidosis type II (IDS): Libmeldy / LV at 9.3/10
- Metachromatic leukodystrophy (ARSA): Libmeldy / LV at 9.2/10
- Mucopolysaccharidosis type III (SGSH): Libmeldy / LV at 9.2/10
- Gaucher disease (GBA): Libmeldy / LV at 9.0/10
- Krabbe disease (GALC): Libmeldy / LV at 9.0/10
- Fabry disease (GLA): Libmeldy / LV at 8.9/10
- Alpha-mannosidosis (MAN2B1): Libmeldy / LV at 8.8/10
- Pompe disease (GAA): Libmeldy / LV at 8.4/10
- CHARGE syndrome (CHD7): Libmeldy / LV at 5.9/10
- Tuberous sclerosis complex (TSC1/TSC2): Libmeldy / LV at 6.1/10

This cluster must be handled carefully. Not every lysosomal disease behaves like MLD. Secreted lysosomal enzymes benefit from cross-correction; membrane proteins and transporters may require much broader cell-autonomous correction. CHARGE and TSC are lower-scoring outliers where the Libmeldy match is structurally driven (LV/HSC platform similarity) rather than deep biological alignment — the dissertation should flag these explicitly.

### 2. Skysona / lentiviral — CNS leukodystrophy and neuronal cluster

Skysona has emerged as a major second lentiviral cluster, ranking first for seven diseases. This reflects the updated scoring of CNS-targeted lentiviral HSC programmes for neurological diseases that share white matter or neuronal cell-type involvement but differ mechanistically from the classical lysosomal diseases in cluster 1. Key examples:

- X-linked adrenoleukodystrophy (ABCD1): Skysona / LV at 8.2/10
- Mucolipidosis type IV (MCOLN1): Skysona / LV at 8.3/10
- Rett syndrome (MECP2): Skysona / LV at 7.4/10
- Fragile X syndrome (FMR1): Skysona / LV at 7.0/10

The Skysona cluster is a calibration challenge. Skysona is specifically approved for cerebral X-ALD; its extrapolation to Rett, CDKL5, Dravet, and Fragile X reflects platform-level similarity rather than validated mechanism transfer. The dissertation should present these as "candidate precedent class" rather than direct analogues, and should note that direct CNS viral delivery or AAV-based approaches are more likely clinical paths for several of these.

### 3. BMN 307 / liver metabolic cluster

BMN 307 ranks first for four liver-directed metabolic disorders:

- OTC deficiency (OTC): BMN 307 / AAV5 at 8.1/10
- Maple syrup urine disease (BCKDHA/B/DBT): BMN 307 / AAV5 at 8.0/10
- Phenylketonuria (PAH): BMN 307 / AAV5 at 8.0/10
- Methylmalonic aciduria (MMUT): BMN 307 / AAV5 at 7.7/10

This is biologically coherent: shared liver targeting, manageable transgene size, and similar metabolic pathway categories. The defensible claim is that NanoGT identifies a relevant liver-directed AAV precedent class. The weaker claim — that BMN 307 itself is directly reusable — should be avoided.

### 4. OAV101-IT / AAV9 CNS cluster

OAV101-IT (Zolgensma) now ranks first for four diseases, forming a coherent CNS/AAV9 cluster:

- Spinal muscular atrophy (SMN1): OAV101-IT / AAV9 at 8.3/10
- Friedreich ataxia (FXN): OAV101-IT / AAV9 at 7.9/10
- Kohlschutter-Tonz syndrome (ROGDI): OAV101-IT / AAV9 at 7.7/10

The SMA match is the strongest internal validation point. Friedreich ataxia is biologically plausible for an AAV9 CNS/DRG approach. Kohlschutter-Tonz and Angelman are lower-confidence biologically, though the platform class (intrathecal AAV9, small transgene, CNS target) is defensible.

### 5. Retinal cluster

Retinal diseases cluster around CPCB-RPE1 (AAV8, RPE-targeted) and Luxturna (AAV2, subretinal):

- Leber congenital amaurosis (RPGRIP1): CPCB-RPE1 / AAV8 at 7.6/10
- Achromatopsia CNGB3: CPCB-RPE1 / AAV8 at 7.5/10
- LHON (MT-ND4): CPCB-RPE1 / AAV8 at 6.4/10
- Choroideremia (CHM): Luxturna / AAV2 at 8.0/10
- X-linked retinoschisis (RS1): Luxturna / AAV2 at 7.9/10

The retinal cluster is biologically coherent. A calibration caveat applies: Luxturna is the canonical RPE65 precedent, yet LCA ranks CPCB-RPE1 first. The dissertation should frame this as a top-k recovery finding rather than top-1 accuracy, and note that LHON's mitochondrial gene target is a special case not fully captured by the current nuclear gene-addition framework.

### 6. Haematopoietic / immune cluster

Strimvelis ranks first for three immune-related diseases:

- SCID (ADA/RAG/IL2RG): Strimvelis / LV at 8.1/10
- Wiskott-Aldrich syndrome (WAS): Strimvelis / LV at 8.0/10

These are biologically coherent HSC gene therapy targets. SRP-9001 covers two muscle diseases (DMD at 7.6/10 and GSD type Ia at 7.8/10), and AT132 covers X-linked myotubular myopathy (7.7/10) as distinct muscle AAV8 precedents.

### 7. Stress tests — packaging hard-fail

One disease correctly returns no catalogued precedent:

- Neurofibromatosis type 1 (NF1): large gene (8,451 bp); exceeds single-AAV packaging limit for every vector in the catalogue.

This stress test is a key dissertation result. NF1 is correctly flagged before any biological scoring occurs — the packaging gate fires first. The dissertation should present this as evidence that NanoGT can distinguish ordinary recessive loss-of-function gene addition from large-gene cases that lie outside single-vector scope, rather than forcing a scored recommendation on every input.

## Limitations closed by explicitly naming them

The main limitations are no longer hidden implementation gaps; they are named dissertation limitations:

1. Catalogue coverage is incomplete and biased toward the programmes manually entered into `src/nanogt/catalog.py`.
2. Disease facts in `data/disease_cohort_46.csv` still require user/supervisor fact-checking; every row is currently marked `needs_user_fact_check`.
3. Pathway inference is heuristic and keyword-based, not a curated Reactome/KEGG/GO semantic model.
4. HPO-based therapeutic-window inference is a rough proxy and should not be treated as natural-history modelling.
5. Cross-correction scoring does not yet distinguish enough between secreted enzymes, lysosomal enzymes, membrane proteins, and fully intracellular proteins.
6. Disease mechanism evidence is explicit in `data/disease_mechanisms_46.csv`, but those source links and compatibility labels still require final supervisor-level checking before submission.
7. Mitochondrial, dominant-negative, toxic gain-of-function, editing, RNA, dual-vector, and most micro-gene strategies remain outside the current v0.1 scope except where explicitly catalogued as engineered precedents.
8. Scores are uncalibrated heuristic scores, not probabilities of clinical success.
9. Literature references and disease-source claims must be verified before final dissertation submission.

## Dissertation-safe result statement

"In a 46-disease proof-of-concept cohort, NanoGT generated interpretable precedent rankings for 33 diseases and correctly returned a packaging hard-fail for NF1 (8,451 bp CDS, exceeds all catalogued vectors). The 39 matched diseases clustered into biologically plausible precedent groups — lentiviral/HSC lysosomal storage, lentiviral CNS leukodystrophy and neuronal, liver-directed metabolic AAV, intrathecal AAV9 CNS, retinal AAV, and haematopoietic immune programmes — while the NF1 packaging gate confirmed the framework's ability to flag large-gene cases outside single-vector scope. These findings support the feasibility of computational precedent matching for early-stage gene-therapy prioritisation, while highlighting the need for catalogue expansion, mechanism-source verification, improved pathway inference, and disease-specific expert review before translational use."
