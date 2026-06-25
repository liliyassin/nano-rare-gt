# NanoGT 46-Disease Cohort — Full Overview

Merged from `data/disease_cohort_46.csv` and `data/disease_mechanisms_46.csv`.

Every source link is clickable. Diseases are grouped by their role in the cohort.

**Total diseases: 46 across 7 groups.**

## Group Summary

| Group | Count |
|---|---:|
| Positive Controls | 3 |
| Benchmark (Known GT Precedent) | 1 |
| Stress Test — Oversized Cargo | 1 |
| Stress Test — Mitochondrial Delivery | 1 |
| Pilot Cohort | 34 |
| Non-LOF — Haploinsufficiency | 4 |
| Non-LOF — Repeat Expansion / Silencing | 2 |

---

## Positive Controls (3 diseases)

### Hemophilia A

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:98878](https://www.orpha.net/en/disease/detail/98878) |
| **Gene** | [F8](https://www.uniprot.org/uniprotkb/P00451) |
| **Gene CDS** | 4374 bp |
| **Inheritance** | X-linked recessive |
| **Primary tissues** | liver |
| **Prevalence** | 1-5/10000 |
| **OMIM** | [306700](https://omim.org/entry/306700) |
| **Cohort notes** | approved AAV gene therapy precedent (Roctavian); positive control |
| **Mechanism** | loss_of_function — Factor VIII deficiency from pathogenic F8 variants; liver-directed F8 expression is an approved gene-addition precedent (Roctavian) |
| **Gene-addition fit** | compatible |
| **Preferred modality** | gene_addition_or_factor_expression |
| **Mechanism evidence** | BioMarin Roctavian (valoctocogene roxaparvovec) approved for Hemophilia A; AAV5 liver-directed F8 expression precedent |
| **Evidence source** | [FDA Approval 2023](https://www.fda.gov/news-events/press-announcements/fda-approves-first-gene-therapy-adults-severe-hemophilia) |
| **Evidence status** | x |

### Hemophilia B

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:98879](https://www.orpha.net/en/disease/detail/98879) |
| **Gene** | [F9](https://www.uniprot.org/uniprotkb/P00740) |
| **Gene CDS** | 1383 bp |
| **Inheritance** | X-linked recessive |
| **Primary tissues** | liver |
| **Prevalence** | 1-5/100000 |
| **OMIM** | [306900](https://omim.org/entry/306900) |
| **Cohort notes** | approved AAV5 liver precedent (Hemgenix); positive control |
| **Mechanism** | loss_of_function — Factor IX deficiency from pathogenic F9 variants |
| **Gene-addition fit** | compatible |
| **Preferred modality** | gene_addition_or_factor_expression |
| **Mechanism evidence** | Deficiency of coagulation factor IX is the therapeutic deficit; liver-directed F9 expression is an approved gene-addition precedent |
| **Evidence source** | [FDA Approval](https://www.fda.gov/vaccines-blood-biologics/vaccines/hemgenix) |
| **Evidence status** | x |

### Spinal Muscular Atrophy

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:70](https://www.orpha.net/en/disease/detail/70) |
| **Gene** | [SMN1](https://www.uniprot.org/uniprotkb/Q16637) |
| **Gene CDS** | 891 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | CNS; muscle |
| **Prevalence** | 1-5/10000 |
| **OMIM** | [253300](https://omim.org/entry/253300) |
| **Cohort notes** | approved AAV9 precedent; positive control |
| **Mechanism** | loss_of_function — SMN protein deficiency from biallelic SMN1 mutation |
| **Gene-addition fit** | compatible |
| **Preferred modality** | gene_addition |
| **Mechanism evidence** | FDA Zolgensma indication is SMA with biallelic SMN1 mutations; product supplies functional SMN transgene |
| **Evidence source** | [FDA Zolgensma product page](https://www.fda.gov/vaccines-blood-biologics/zolgensma); [Announcement page](https://www.fda.gov/news-events/press-announcements/fda-approves-innovative-gene-therapy-treat-pediatric-patients-spinal-muscular-atrophy-rare-disease); [*my SMA match ranks OAV101-IT first and Zolgensma second -> Nov 2025, FDA approved Itvisma / onasemnogene abeparvovec-brve, an intrathecal formulation for SMA patients aged 2 years and older with confirmed SMN1 mutation. That is the cleanest regulatory source for the OAV101-IT precedent](https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/itvisma) |
| **Evidence status** | x |

---

## Benchmark (Known GT Precedent) (1 disease)

### Severe combined immunodeficiency due to adenosine deaminase deficiency

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:277](https://www.orpha.net/en/disease/detail/277) |
| **Gene** | [ADA](https://www.uniprot.org/uniprotkb/P00813) |
| **Gene CDS** | 1092 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | hematopoietic |
| **Prevalence** | 1-9/1000000 |
| **OMIM** | [102700](https://omim.org/entry/102700) |
| **Cohort notes** | approved ex vivo/lentiviral HSC precedent; positive control |
| **Mechanism** | loss_of_function — ADA enzyme deficiency causing toxic purine metabolite accumulation |
| **Gene-addition fit** | compatible |
| **Preferred modality** | ex_vivo_hsc_gene_addition |
| **Mechanism evidence** | ADA-SCID is a deficiency disorder with approved ex vivo gene-addition precedent |
| **Evidence source** | [EMA](https://www.ema.europa.eu/en/documents/product-information/strimvelis-epar-product-information_en.pdf) |
| **Evidence status** | x |

---

## Stress Test — Oversized Cargo (1 disease)

### Duchenne muscular dystrophy

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:98896](https://www.orpha.net/en/disease/detail/98896) |
| **Gene** | [DMD](https://www.uniprot.org/uniprotkb/P11532) |
| **Gene CDS** | 11055 bp |
| **Inheritance** | X-linked recessive |
| **Primary tissues** | muscle; heart |
| **Prevalence** | 1-5/10000 |
| **OMIM** | [310200](https://omim.org/entry/310200) |
| **Cohort notes** | oversized native gene; micro-dystrophin precedent tests cargo-limit handling |
| **Mechanism** | loss_of_function_oversized — Dystrophin loss with native DMD too large for single AAV |
| **Gene-addition fit** | conditional |
| **Preferred modality** | engineered_microgene_or_dual_vector |
| **Mechanism evidence** | DMD supports replacement logic but requires micro-dystrophin or other engineered strategies because full-length DMD exceeds AAV capacity |
| **Evidence source** | [Chamberlain et al. 2023 Microdystrophin Expression as a Surrogate Endpoint for DMD Clinical Trials](https://pmc.ncbi.nlm.nih.gov/articles/PMC10210223/); [FDA Approval](https://www.fda.gov/news-events/press-announcements/fda-expands-approval-gene-therapy-patients-duchenne-muscular-dystrophy) |
| **Evidence status** | x |

---

## Stress Test — Mitochondrial Delivery (1 disease)

### Leber hereditary optic neuropathy

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:104](https://www.orpha.net/en/disease/detail/104) |
| **Gene** | [MT-ND4](https://www.uniprot.org/uniprotkb/P03905) |
| **Gene CDS** | 1377 bp |
| **Inheritance** | Mitochondrial inheritance |
| **Primary tissues** | retina; CNS |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [535000](https://omim.org/entry/535000) |
| **Cohort notes** | mitochondrial gene delivery stress test |
| **Mechanism** | mitochondrial_loss_of_function — Mitochondrial complex I dysfunction from MT-ND4 variant |
| **Gene-addition fit** | uncertain |
| **Preferred modality** | specialized_allotopic_expression_or_mitochondrial_strategy |
| **Mechanism evidence** | Mitochondrial DNA disease is not ordinary nuclear gene addition; allotopic AAV approaches are specialized and disease-specific |
| **Evidence source** | [5-year Phase 3 RCT follow-up of RESCUE/REVERSE. Sustained bilateral BCVA improvement (+4 lines), good safety profile. The pivotal long-term efficacy paper supporting approval.](https://jamanetwork.com/journals/jamaophthalmology/fullarticle/2828184) |
| **Evidence status** | x |

---

## Pilot Cohort (34 diseases)

### Achromatopsia

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:49382](https://www.orpha.net/en/disease/detail/49382) |
| **Gene** | [CNGB3](https://www.uniprot.org/uniprotkb/Q9NQW8) |
| **Gene CDS** | 2427 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | retina |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [262300](https://omim.org/entry/262300) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Cone cyclic nucleotide-gated channel beta-subunit loss |
| **Gene-addition fit** | compatible |
| **Preferred modality** | retinal_gene_addition |
| **Mechanism evidence** | Biallelic CNGB3 loss is compatible with photoreceptor-directed gene addition if target cells remain viable |
| **Evidence source** | [Phenotyping and genotyping inherited retinal diseases](https://www.sciencedirect.com/science/article/pii/S1350946224000090?via%3Dihub) |
| **Evidence status** | x |

### Alpha-mannosidosis

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:61](https://www.orpha.net/en/disease/detail/61) |
| **Gene** | [MAN2B1](https://www.uniprot.org/uniprotkb/O00754) |
| **Gene CDS** | 3033 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | CNS; liver |
| **Prevalence** | 1-9/1000000 |
| **OMIM** | [248500](https://omim.org/entry/248500) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Lysosomal alpha-mannosidase enzyme deficiency |
| **Gene-addition fit** | compatible |
| **Preferred modality** | gene_addition_or_cross_correction |
| **Mechanism evidence** | Lysosomal enzyme deficiency supports gene addition and possible cross-correction logic |
| **Evidence source** | [Efficacy and safety of Velmanase alfa in the treatment of patients with alpha-mannosidosis](https://onlinelibrary.wiley.com/doi/10.1007/s10545-018-0185-0) |
| **Evidence status** | x |

### Biotinidase deficiency

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:79241](https://www.orpha.net/en/disease/detail/79241) |
| **Gene** | [BTD](https://www.uniprot.org/uniprotkb/P43251) |
| **Gene CDS** | 1632 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | CNS; multisystem |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [253260](https://omim.org/entry/253260) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Biotinidase enzyme deficiency prevents biotin recycling; liver-expressed BTD deficiency supports systemic gene addition |
| **Gene-addition fit** | compatible |
| **Preferred modality** | liver_gene_addition |
| **Mechanism evidence** | BTD LOF is a metabolic enzyme deficiency compatible with liver-directed gene addition |
| **Evidence source** | [Evaluating reproductive carrier screening using biotinidase deficiency as a model](https://www.gimjournal.org/article/S1098-3600(24)00279-X/fulltext) |
| **Evidence status** | x |

### Canavan disease

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:141](https://www.orpha.net/en/disease/detail/141) |
| **Gene** | [ASPA](https://www.uniprot.org/uniprotkb/P45381) |
| **Gene CDS** | 942 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | CNS |
| **Prevalence** | <1/1000000 |
| **OMIM** | [271900](https://omim.org/entry/271900) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Aspartoacylase enzyme deficiency leads to N-acetylaspartate accumulation and CNS white matter destruction |
| **Gene-addition fit** | compatible |
| **Preferred modality** | cns_gene_addition |
| **Mechanism evidence** | ASPA LOF supports CNS-directed gene addition; clinical AAV trials ongoing |
| **Evidence source** | [Oligodendrocyte-targeted adeno-associated virus gene therapy for Canavan disease in children: a phase 1/2 trial](https://www.nature.com/articles/s41591-025-03919-w) |
| **Evidence status** | x |

### Choroideremia

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:180](https://www.orpha.net/en/disease/detail/180) |
| **Gene** | [CHM](https://www.uniprot.org/uniprotkb/P24386) |
| **Gene CDS** | 1962 bp |
| **Inheritance** | X-linked recessive |
| **Primary tissues** | retina |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [303100](https://omim.org/entry/303100) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — REP1 deficiency affecting retinal cells |
| **Gene-addition fit** | compatible |
| **Preferred modality** | retinal_gene_addition |
| **Mechanism evidence** | CHM loss of function is a retinal gene-addition target if viable retina remains |
| **Evidence source** | [Subretinal timrepigene emparvovec in adult men with choroideremia: a randomized phase 3 trial](https://omim.org/entry/300390) |
| **Evidence status** | x |

### Chronic neurovisceral acid sphingomyelinase deficiency (Niemann-Pick A/B)

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:618891](https://www.orpha.net/en/disease/detail/618891) |
| **Gene** | [SMPD1](https://www.uniprot.org/uniprotkb/P17405) |
| **Gene CDS** | 1890 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | liver; spleen; lung; CNS |
| **Prevalence** | <1/1000000 |
| **OMIM** | [607616](https://omim.org/entry/607616) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Acid sphingomyelinase deficiency causes sphingomyelin accumulation in liver, spleen, lung, and CNS |
| **Gene-addition fit** | conditional |
| **Preferred modality** | liver_or_cns_gene_addition_or_cross_correction |
| **Mechanism evidence** | SMPD1 is a secreted lysosomal enzyme; cross-correction may be feasible for visceral disease but CNS involvement complicates single-compartment delivery |
| **Evidence source** | [OMIM SMPD1 607616](https://omim.org/entry/607616) |
| **Evidence status** | needs_user_fact_check |

### Crigler-Najjar syndrome type I

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:79234](https://www.orpha.net/en/disease/detail/79234) |
| **Gene** | [UGT1A1](https://www.uniprot.org/uniprotkb/P22309) |
| **Gene CDS** | 1596 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | liver |
| **Prevalence** | <1/1000000 |
| **OMIM** | [218800](https://omim.org/entry/218800) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Absent or severe deficiency of bilirubin UDP-glucuronosyltransferase |
| **Gene-addition fit** | compatible |
| **Preferred modality** | liver_gene_addition |
| **Mechanism evidence** | UGT1A1 deficiency supports hepatocyte-directed gene addition |
| **Evidence source** | [OMIM UGT1A1 gene entry](https://omim.org/entry/191740) |
| **Evidence status** | source_linked_needs_review |

### Cystic fibrosis

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:586](https://www.orpha.net/en/disease/detail/586) |
| **Gene** | [CFTR](https://www.uniprot.org/uniprotkb/P13569) |
| **Gene CDS** | 4443 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | lung; pancreas; liver |
| **Prevalence** | 1-5/10000 |
| **OMIM** | [219700](https://omim.org/entry/219700) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — CFTR chloride channel dysfunction; gene addition must achieve sufficient cell-surface expression in airway epithelium |
| **Gene-addition fit** | conditional |
| **Preferred modality** | airway_gene_addition |
| **Mechanism evidence** | CFTR LOF supports gene addition logic; lung delivery and transient episomal expression in cycling airway epithelium are the main challenges |
| **Evidence source** | [OMIM CFTR 219700](https://omim.org/entry/219700) |
| **Evidence status** | needs_user_fact_check |

### Fabry disease

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:324](https://www.orpha.net/en/disease/detail/324) |
| **Gene** | [GLA](https://www.uniprot.org/uniprotkb/P06280) |
| **Gene CDS** | 1290 bp |
| **Inheritance** | X-linked dominant |
| **Primary tissues** | liver; kidney; heart; CNS |
| **Prevalence** | 1-5/10000 |
| **OMIM** | [301500](https://omim.org/entry/301500) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Alpha-galactosidase A lysosomal enzyme deficiency |
| **Gene-addition fit** | compatible |
| **Preferred modality** | gene_addition_or_cross_correction |
| **Mechanism evidence** | Fabry is caused by deficient GLA enzyme activity; secreted enzyme strategies can support systemic cross-correction |
| **Evidence source** | [OMIM GLA gene entry](https://omim.org/entry/300644) |
| **Evidence status** | source_linked_needs_review |

### Gaucher disease type 1

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:355](https://www.orpha.net/en/disease/detail/355) |
| **Gene** | [GBA1](https://www.uniprot.org/uniprotkb/P04062) |
| **Gene CDS** | 1491 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | hematopoietic; liver; CNS |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [230800](https://omim.org/entry/230800) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Beta-glucocerebrosidase lysosomal enzyme deficiency |
| **Gene-addition fit** | conditional |
| **Preferred modality** | gene_addition_or_cross_correction |
| **Mechanism evidence** | GBA deficiency supports replacement logic but neuronopathic disease and tissue access can limit simple systemic correction |
| **Evidence source** | [OMIM GBA gene entry](https://pmc.ncbi.nlm.nih.gov/articles/PMC10579095/) |
| **Evidence status** | source_linked_needs_review |

### Glycogen storage disease type Ia

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:79258](https://www.orpha.net/en/disease/detail/79258) |
| **Gene** | [G6PC1](https://www.uniprot.org/uniprotkb/P35575) |
| **Gene CDS** | 1071 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | liver; kidney |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [232200](https://omim.org/entry/232200) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Glucose-6-phosphatase catalytic subunit deficiency |
| **Gene-addition fit** | compatible |
| **Preferred modality** | liver_kidney_gene_addition |
| **Mechanism evidence** | G6PC deficiency is a metabolic enzyme loss where liver-directed expression is a plausible gene-addition strategy |
| **Evidence source** | [OMIM G6PC gene entry](https://omim.org/entry/613742) |
| **Evidence status** | source_linked_needs_review |

### Kohlschutter-Tonz syndrome

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:1946](https://www.orpha.net/en/disease/detail/1946) |
| **Gene** | [ROGDI](https://www.uniprot.org/uniprotkb/Q9GZN7) |
| **Gene CDS** | 861 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | CNS |
| **Prevalence** | <1/1000000 |
| **OMIM** | [226750](https://omim.org/entry/226750) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — ROGDI loss of function — gene addition is plausible by genetics but molecular function is not fully resolved and disease biology has not been established |
| **Gene-addition fit** | conditional |
| **Preferred modality** | cns_gene_addition_pending_mechanism_validation |
| **Mechanism evidence** | Published KTS variants in ROGDI are consistent with loss of function (Schossig 2012) and gene addition is mechanistically plausible. However the molecular function of ROGDI protein is not fully resolved: proposed roles include V-ATPase regulation via the RAVE/Rabconnectin-3 complex and synaptic vesicle biology but no disease-specific in vivo model or gene addition rescue experiment has been published as of 2025. Scoring assumptions (LOF gene addition is sufficient) are unvalidated. Do not interpret the composite score as evidence of clinical tractability without independent confirmation of gene function and therapeutic rationale. |
| **Evidence source** | [Schossig et al. 2012 Mutations in ROGDI Cause Kohlschutter-Tonz Syndrome](https://pubmed.ncbi.nlm.nih.gov/22482807/) |
| **Evidence status** | source_checked |

### Krabbe disease

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:487](https://www.orpha.net/en/disease/detail/487) |
| **Gene** | [GALC](https://www.uniprot.org/uniprotkb/P54803) |
| **Gene CDS** | 2055 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | CNS |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [245200](https://omim.org/entry/245200) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Galactocerebrosidase lysosomal enzyme deficiency |
| **Gene-addition fit** | conditional |
| **Preferred modality** | gene_addition_or_hsc_cross_correction |
| **Mechanism evidence** | GALC deficiency supports replacement logic but CNS delivery and toxic metabolite biology require disease-specific validation |
| **Evidence source** | [OMIM GALC gene entry](https://omim.org/entry/606890) |
| **Evidence status** | source_linked_needs_review |

### Maple syrup urine disease

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:511](https://www.orpha.net/en/disease/detail/511) |
| **Gene** | [BCKDHA](https://www.uniprot.org/uniprotkb/P12694) |
| **Gene CDS** | 1335 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | liver; CNS |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [248600](https://omim.org/entry/248600) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Branched-chain alpha-ketoacid dehydrogenase E1 alpha deficiency |
| **Gene-addition fit** | conditional |
| **Preferred modality** | liver_gene_addition_or_enzyme_complex_rescue |
| **Mechanism evidence** | BCKDHA deficiency supports replacement logic but the multi-subunit enzyme complex and CNS metabolic crises make liver-only rescue uncertain |
| **Evidence source** | [OMIM BCKDHA gene entry](https://omim.org/entry/608348) |
| **Evidence status** | source_linked_needs_review |

### Metachromatic leukodystrophy

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:512](https://www.orpha.net/en/disease/detail/512) |
| **Gene** | [ARSA](https://www.uniprot.org/uniprotkb/P15289) |
| **Gene CDS** | 1521 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | CNS |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [250100](https://omim.org/entry/250100) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Arylsulfatase A lysosomal enzyme deficiency |
| **Gene-addition fit** | compatible |
| **Preferred modality** | ex_vivo_hsc_or_cns_gene_addition |
| **Mechanism evidence** | ARSA deficiency is compatible with gene addition and HSC-mediated enzyme delivery/cross-correction precedent |
| **Evidence source** | [OMIM ARSA gene entry](https://omim.org/entry/607574) |
| **Evidence status** | source_linked_needs_review |

### Mucolipidosis type IV

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:578](https://www.orpha.net/en/disease/detail/578) |
| **Gene** | [MCOLN1](https://www.uniprot.org/uniprotkb/Q9GZU1) |
| **Gene CDS** | 1740 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | CNS; retina |
| **Prevalence** | <1/1000000 |
| **OMIM** | [252650](https://omim.org/entry/252650) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — TRPML1 lysosomal membrane Ca2+ channel deficiency — cell-autonomous membrane protein NOT a secretable enzyme |
| **Gene-addition fit** | conditional |
| **Preferred modality** | direct_cns_aav_per_cell_delivery |
| **Mechanism evidence** | MCOLN1 encodes a lysosomal MEMBRANE CHANNEL (TRP family) not a soluble lysosomal enzyme. Cross-correction via M6P receptor uptake (the mechanism of Libmeldy/ARSA) is physically impossible for a membrane-anchored protein. Every target neuron must individually receive the vector. AAV-based CNS delivery is the appropriate strategy; HSC/LV programs are not transferable precedents for this protein class. |
| **Evidence source** | [OMIM MCOLN1 gene entry](https://omim.org/entry/605248) |
| **Evidence status** | source_linked_needs_review |

### Mucopolysaccharidosis type I (Hurler syndrome)

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:579](https://www.orpha.net/en/disease/detail/579) |
| **Gene** | [IDUA](https://www.uniprot.org/uniprotkb/P35475) |
| **Gene CDS** | 1962 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | CNS; liver |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [607014](https://omim.org/entry/607014) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Alpha-L-iduronidase lysosomal enzyme deficiency |
| **Gene-addition fit** | compatible |
| **Preferred modality** | gene_addition_or_cross_correction |
| **Mechanism evidence** | IDUA enzyme deficiency supports replacement and cross-correction biology |
| **Evidence source** | [OMIM MPS I 252800](https://omim.org/entry/252800) |
| **Evidence status** | source_linked_needs_review |

### Mucopolysaccharidosis type II (Hunter syndrome)

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:580](https://www.orpha.net/en/disease/detail/580) |
| **Gene** | [IDS](https://www.uniprot.org/uniprotkb/P22304) |
| **Gene CDS** | 1650 bp |
| **Inheritance** | X-linked recessive |
| **Primary tissues** | CNS; liver |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [309900](https://omim.org/entry/309900) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Iduronate-2-sulfatase lysosomal enzyme deficiency |
| **Gene-addition fit** | compatible |
| **Preferred modality** | gene_addition_or_cross_correction |
| **Mechanism evidence** | IDS enzyme deficiency supports replacement and cross-correction biology |
| **Evidence source** | [OMIM IDS gene entry](https://omim.org/entry/300823) |
| **Evidence status** | source_linked_needs_review |

### Mucopolysaccharidosis type IIIA (Sanfilippo A)

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:79269](https://www.orpha.net/en/disease/detail/79269) |
| **Gene** | [SGSH](https://www.uniprot.org/uniprotkb/P51688) |
| **Gene CDS** | 1674 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | CNS |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [252900](https://omim.org/entry/252900) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Heparan N-sulfatase lysosomal enzyme deficiency |
| **Gene-addition fit** | compatible |
| **Preferred modality** | cns_gene_addition_or_cross_correction |
| **Mechanism evidence** | SGSH enzyme deficiency supports replacement logic but CNS delivery is central for Sanfilippo A |
| **Evidence source** | [OMIM SGSH gene entry](https://omim.org/entry/605270) |
| **Evidence status** | source_linked_needs_review |

### Nephropathic cystinosis

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:213](https://www.orpha.net/en/disease/detail/213) |
| **Gene** | [CTNS](https://www.uniprot.org/uniprotkb/O60931) |
| **Gene CDS** | 1104 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | kidney; multisystem |
| **Prevalence** | <1/1000000 |
| **OMIM** | [219800](https://omim.org/entry/219800) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Cystinosin lysosomal cystine transporter deficiency — membrane protein; per-cell delivery required across kidney and multiple organs |
| **Gene-addition fit** | conditional |
| **Preferred modality** | kidney_or_systemic_gene_addition |
| **Mechanism evidence** | CTNS encodes a lysosomal membrane transporter; cross-correction via M6P uptake is not applicable — per-cell delivery needed in target tissues |
| **Evidence source** | [OMIM CTNS 219800](https://omim.org/entry/219800) |
| **Evidence status** | needs_user_fact_check |

### Niemann-Pick disease type C

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:646](https://www.orpha.net/en/disease/detail/646) |
| **Gene** | [NPC1](https://www.uniprot.org/uniprotkb/O15118) |
| **Gene CDS** | 3837 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | CNS; liver |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [257220](https://omim.org/entry/257220) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — NPC1 lysosomal cholesterol transporter deficiency — large membrane protein; per-cell delivery required |
| **Gene-addition fit** | conditional |
| **Preferred modality** | cns_gene_addition |
| **Mechanism evidence** | NPC1 is a large (~1.3 kb) lysosomal membrane protein; not secretable; CNS delivery is the primary challenge |
| **Evidence source** | [OMIM NPC1 257220](https://omim.org/entry/257220) |
| **Evidence status** | needs_user_fact_check |

### Ornithine transcarbamylase deficiency

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:664](https://www.orpha.net/en/disease/detail/664) |
| **Gene** | [OTC](https://www.uniprot.org/uniprotkb/P00480) |
| **Gene CDS** | 1065 bp |
| **Inheritance** | X-linked recessive |
| **Primary tissues** | liver; CNS |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [311250](https://omim.org/entry/311250) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Ornithine transcarbamylase urea-cycle enzyme deficiency |
| **Gene-addition fit** | compatible |
| **Preferred modality** | liver_gene_addition |
| **Mechanism evidence** | OTC deficiency is a liver metabolic enzyme loss compatible with hepatocyte gene addition |
| **Evidence source** | [OMIM OTC gene entry](https://omim.org/entry/300461) |
| **Evidence status** | source_linked_needs_review |

### Phenylketonuria

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:716](https://www.orpha.net/en/disease/detail/716) |
| **Gene** | [PAH](https://www.uniprot.org/uniprotkb/P00439) |
| **Gene CDS** | 1353 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | liver; CNS |
| **Prevalence** | 1-5/10000 |
| **OMIM** | [261600](https://omim.org/entry/261600) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Phenylalanine hydroxylase enzyme deficiency |
| **Gene-addition fit** | compatible |
| **Preferred modality** | liver_gene_addition |
| **Mechanism evidence** | PAH deficiency is a liver enzyme loss compatible with hepatocyte gene addition |
| **Evidence source** | [OMIM PAH gene entry](https://omim.org/entry/612349) |
| **Evidence status** | source_linked_needs_review |

### Pompe disease

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:365](https://www.orpha.net/en/disease/detail/365) |
| **Gene** | [GAA](https://www.uniprot.org/uniprotkb/P10253) |
| **Gene CDS** | 2856 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | muscle; heart |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [232300](https://omim.org/entry/232300) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Acid alpha-glucosidase lysosomal enzyme deficiency |
| **Gene-addition fit** | conditional |
| **Preferred modality** | gene_addition_or_secreted_enzyme_rescue |
| **Mechanism evidence** | GAA deficiency supports replacement logic but skeletal and cardiac delivery needs broad tissue correction |
| **Evidence source** | [OMIM GAA gene entry](https://omim.org/entry/606800) |
| **Evidence status** | source_linked_needs_review |

### Primary hyperoxaluria type 1

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:93598](https://www.orpha.net/en/disease/detail/93598) |
| **Gene** | [AGXT](https://www.uniprot.org/uniprotkb/P21549) |
| **Gene CDS** | 1179 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | liver; kidney |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [259900](https://omim.org/entry/259900) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Alanine-glyoxylate aminotransferase deficiency — nuclear-encoded peroxisomal enzyme requiring PTS1 signal for import |
| **Gene-addition fit** | conditional |
| **Preferred modality** | liver_gene_addition |
| **Mechanism evidence** | AGXT LOF supports liver-directed gene addition; peroxisomal targeting signal must be intact in the therapeutic construct |
| **Evidence source** | [OMIM AGXT 259900](https://omim.org/entry/259900) |
| **Evidence status** | needs_user_fact_check |

### Tay-Sachs disease

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:845](https://www.orpha.net/en/disease/detail/845) |
| **Gene** | [HEXA](https://www.uniprot.org/uniprotkb/P06865) |
| **Gene CDS** | 1590 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | CNS |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [272800](https://omim.org/entry/272800) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Beta-hexosaminidase alpha subunit deficiency causes GM2 ganglioside accumulation in neurons |
| **Gene-addition fit** | conditional |
| **Preferred modality** | cns_gene_addition_or_cross_correction |
| **Mechanism evidence** | HEXA LOF supports gene addition; CNS delivery and heterodimer assembly with HEXB subunit are key considerations |
| **Evidence source** | [OMIM HEXA 272800](https://omim.org/entry/272800) |
| **Evidence status** | needs_user_fact_check |

### Usher syndrome type 1B

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:886](https://www.orpha.net/en/disease/detail/886) |
| **Gene** | [MYO7A](https://www.uniprot.org/uniprotkb/Q13402) |
| **Gene CDS** | 6648 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | retina; cochlea |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [276900](https://omim.org/entry/276900) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — MYO7A myosin VIIA deficiency causing combined deafblindness; large CDS (~6.6 kb) exceeds single-AAV capacity |
| **Gene-addition fit** | conditional |
| **Preferred modality** | dual_aav_or_lv_retinal_cochlear_delivery |
| **Mechanism evidence** | MYO7A LOF supports gene addition logic but oversized CDS requires dual-AAV or lentiviral strategies for retinal and cochlear delivery |
| **Evidence source** | [OMIM MYO7A 276900](https://omim.org/entry/276900) |
| **Evidence status** | needs_user_fact_check |

### Vitamin B12-unresponsive methylmalonic acidemia

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:27](https://www.orpha.net/en/disease/detail/27) |
| **Gene** | [MMUT](https://www.uniprot.org/uniprotkb/P22033) |
| **Gene CDS** | 2250 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | liver; CNS |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [251000](https://omim.org/entry/251000) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Methylmalonyl-CoA mutase — nuclear-encoded mitochondrial MATRIX enzyme requiring post-translational import via intact N-terminal MTS |
| **Gene-addition fit** | conditional |
| **Preferred modality** | liver_aav_with_mts_validation |
| **Mechanism evidence** | MUT is a nuclear-encoded mitochondrial matrix enzyme. Nuclear AAV delivery is theoretically feasible but the N-terminal mitochondrial targeting sequence (MTS) must be intact in the therapeutic construct for correct post-translational import into the matrix. MTS functionality and import efficiency must be validated experimentally before vector precedent scores can be applied. Liver-directed AAV programs in development (e.g. NCT03721861) confirm the approach is viable but disease-specific construct validation is required. |
| **Evidence source** | [OMIM MUT gene entry](https://omim.org/entry/609058) |
| **Evidence status** | source_linked_needs_review |

### Wilson disease

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:905](https://www.orpha.net/en/disease/detail/905) |
| **Gene** | [ATP7B](https://www.uniprot.org/uniprotkb/P35670) |
| **Gene CDS** | 4398 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | liver; CNS |
| **Prevalence** | 1-5/10000 |
| **OMIM** | [277900](https://omim.org/entry/277900) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — ATP7B copper-transporting ATPase deficiency causes hepatic and CNS copper accumulation |
| **Gene-addition fit** | conditional |
| **Preferred modality** | liver_gene_addition |
| **Mechanism evidence** | ATP7B LOF supports liver-directed gene addition; large CDS (~4.3 kb) fits within AAV capacity |
| **Evidence source** | [OMIM ATP7B 277900](https://omim.org/entry/277900) |
| **Evidence status** | needs_user_fact_check |

### Wiskott-Aldrich syndrome

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:906](https://www.orpha.net/en/disease/detail/906) |
| **Gene** | [WAS](https://www.uniprot.org/uniprotkb/P42768) |
| **Gene CDS** | 1506 bp |
| **Inheritance** | X-linked recessive |
| **Primary tissues** | hematopoietic |
| **Prevalence** | 1-9/1000000 |
| **OMIM** | [301000](https://omim.org/entry/301000) |
| **Cohort notes** | ex vivo HSC/lentiviral precedent relevance |
| **Mechanism** | loss_of_function — WASP deficiency in hematopoietic cells |
| **Gene-addition fit** | compatible |
| **Preferred modality** | ex_vivo_hsc_gene_addition |
| **Mechanism evidence** | WAS loss of function is compatible with autologous hematopoietic stem-cell gene addition |
| **Evidence source** | [OMIM WAS gene entry](https://omim.org/entry/300392) |
| **Evidence status** | source_linked_needs_review |

### X-linked adrenoleukodystrophy

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:43](https://www.orpha.net/en/disease/detail/43) |
| **Gene** | [ABCD1](https://www.uniprot.org/uniprotkb/P33897) |
| **Gene CDS** | 2235 bp |
| **Inheritance** | X-linked dominant |
| **Primary tissues** | CNS |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [300100](https://omim.org/entry/300100) |
| **Cohort notes** | lentiviral HSC/CNS leukodystrophy precedent relevance |
| **Mechanism** | loss_of_function — Peroxisomal ABCD1 transporter deficiency |
| **Gene-addition fit** | conditional |
| **Preferred modality** | ex_vivo_hsc_gene_addition |
| **Mechanism evidence** | ABCD1 deficiency supports replacement logic but cerebral inflammatory disease relies on hematopoietic and CNS disease biology |
| **Evidence source** | [OMIM ABCD1 gene entry](https://omim.org/entry/300371) |
| **Evidence status** | source_linked_needs_review |

### X-linked centronuclear myopathy

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:596](https://www.orpha.net/en/disease/detail/596) |
| **Gene** | [MTM1](https://www.uniprot.org/uniprotkb/Q13496) |
| **Gene CDS** | 1878 bp |
| **Inheritance** | X-linked recessive |
| **Primary tissues** | muscle |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [310400](https://omim.org/entry/310400) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Myotubularin deficiency in skeletal muscle |
| **Gene-addition fit** | compatible |
| **Preferred modality** | muscle_gene_addition |
| **Mechanism evidence** | MTM1 loss of function is compatible with muscle-directed gene addition but dose toxicity must be reviewed |
| **Evidence source** | [OMIM MTM1 gene entry](https://omim.org/entry/300415) |
| **Evidence status** | source_linked_needs_review |

### X-linked retinoschisis

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:792](https://www.orpha.net/en/disease/detail/792) |
| **Gene** | [RS1](https://www.uniprot.org/uniprotkb/O15537) |
| **Gene CDS** | 672 bp |
| **Inheritance** | X-linked recessive |
| **Primary tissues** | retina |
| **Prevalence** | 1-5/10000 |
| **OMIM** | [312700](https://omim.org/entry/312700) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — Retinoschisin deficiency affecting retinal architecture |
| **Gene-addition fit** | compatible |
| **Preferred modality** | retinal_gene_addition |
| **Mechanism evidence** | RS1 deficiency supports retinal gene addition if target retinal structure remains treatable |
| **Evidence source** | [OMIM RS1 gene entry](https://omim.org/entry/300839) |
| **Evidence status** | source_linked_needs_review |

### Zellweger syndrome

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:912](https://www.orpha.net/en/disease/detail/912) |
| **Gene** | [PEX1](https://www.uniprot.org/uniprotkb/O43933) |
| **Gene CDS** | 3852 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | CNS; liver; kidney |
| **Prevalence** | <1/1000000 |
| **OMIM** | [214100](https://omim.org/entry/214100) |
| **Cohort notes** | selected to broaden tissue/pathway coverage of the monogenic GT matching cohort |
| **Mechanism** | loss_of_function — PEX1 peroxisome biogenesis factor deficiency; most severe peroxisome biogenesis disorder — multisystem |
| **Gene-addition fit** | conditional |
| **Preferred modality** | liver_cns_gene_addition |
| **Mechanism evidence** | PEX1 LOF supports gene addition but broad multisystem disease and neonatal severity limit treatment window |
| **Evidence source** | [OMIM PEX1 214100](https://omim.org/entry/214100) |
| **Evidence status** | needs_user_fact_check |

---

## Non-LOF — Haploinsufficiency (4 diseases)

### CHARGE syndrome

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:138](https://www.orpha.net/en/disease/detail/138) |
| **Gene** | [CHD7](https://www.uniprot.org/uniprotkb/Q9P2D1) |
| **Gene CDS** | 7950 bp |
| **Inheritance** | Autosomal dominant |
| **Primary tissues** | CNS; heart |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [214800](https://omim.org/entry/214800) |
| **Cohort notes** | haploinsufficiency; gene addition conditionally compatible; tests chromatin remodeller dosage sensitivity |
| **Mechanism** | haploinsufficiency — Loss of one functional CHD7 allele reduces chromatin remodeller dosage below the threshold needed for normal embryonic development; gene addition in principle restores dosage but CHD7 is large (7950bp) and developmental timing and cell-level expression requirements are complex |
| **Gene-addition fit** | conditional |
| **Preferred modality** | gene_addition_haploinsufficiency_rescue |
| **Mechanism evidence** | Vissers et al. (2004 Nat Genet PMID 15300250) identified de novo CHD7 mutations and deletions confirming haploinsufficiency as the pathogenic mechanism; conditional because CHD7 CDS approaches LV capacity limits and cell-level transgene dosage must be carefully controlled |
| **Evidence source** | [Vissers et al. 2004 Nat Genet PMID 15300250](https://pubmed.ncbi.nlm.nih.gov/15300250/) |
| **Evidence status** | source_checked |

### Neurofibromatosis type 1

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:636](https://www.orpha.net/en/disease/detail/636) |
| **Gene** | [NF1](https://www.uniprot.org/uniprotkb/P21359) |
| **Gene CDS** | 8451 bp |
| **Inheritance** | Autosomal dominant |
| **Primary tissues** | CNS; peripheral nerve |
| **Prevalence** | 1-5/1000 |
| **OMIM** | [162200](https://omim.org/entry/162200) |
| **Cohort notes** | haploinsufficiency tumour suppressor; gene addition conditionally compatible; somatic complexity |
| **Mechanism** | haploinsufficiency — Germline NF1 mutation reduces neurofibromin tumour suppressor dosage; subsequent somatic loss of the wild-type allele in individual cells initiates benign neurofibromas; gene addition cannot prevent independent somatic second-hit events across the lifetime of the patient |
| **Gene-addition fit** | conditional |
| **Preferred modality** | gene_addition_tumour_suppressor_rescue |
| **Mechanism evidence** | Serra et al. (1997 Am J Hum Genet PMID 9326316) confirmed biallelic NF1 inactivation in neurofibromas by LOH analysis demonstrating the two-hit mechanism; gene addition is conditional because somatic second hits in independent cells cannot be globally prevented by a single-dose systemic vector |
| **Evidence source** | [Serra et al. 1997 Am J Hum Genet PMID 9326316](https://pubmed.ncbi.nlm.nih.gov/9326316/) |
| **Evidence status** | source_checked |

### Rett syndrome

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:778](https://www.orpha.net/en/disease/detail/778) |
| **Gene** | [MECP2](https://www.uniprot.org/uniprotkb/P51608) |
| **Gene CDS** | 1461 bp |
| **Inheritance** | X-linked dominant |
| **Primary tissues** | CNS |
| **Prevalence** | 1-5/10000 |
| **OMIM** | [312750](https://omim.org/entry/312750) |
| **Cohort notes** | X-linked haploinsufficiency of MECP2; gene addition conditional (MECP2 duplication causes distinct disease — dosage window is narrow) |
| **Mechanism** | haploinsufficiency — X-linked haploinsufficiency of MECP2 methyl-CpG binding protein 2; gene addition is dosage-sensitive because MECP2 duplication (three copies) causes a distinct severe neurological disease in males — therapeutic window for expression is narrow |
| **Gene-addition fit** | conditional |
| **Preferred modality** | aav9_cns_gene_addition_with_dosage_control |
| **Mechanism evidence** | Amir RE et al. (1999 Nat Genet PMID 10508514) identified MECP2 as the causal gene; Van Esch H et al. (2005 Am J Hum Genet PMID 16080119) showed MECP2 duplication causes a separate severe disease — any AAV-MECP2 construct must use a regulated or low-expression promoter to stay within the narrow therapeutic dose window |
| **Evidence source** | [Amir RE et al. 1999 Nat Genet PMID 10508514; Van Esch H et al. 2005 Am J Hum Genet PMID 16080119](https://pubmed.ncbi.nlm.nih.gov/10508514/) |
| **Evidence status** | source_checked |

### Tuberous sclerosis complex

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:805](https://www.orpha.net/en/disease/detail/805) |
| **Gene** | [TSC1](https://www.uniprot.org/uniprotkb/Q92574) |
| **Gene CDS** | 3495 bp |
| **Inheritance** | Autosomal dominant |
| **Primary tissues** | CNS; kidney |
| **Prevalence** | 1-5/10000 |
| **OMIM** | [191100](https://omim.org/entry/191100) |
| **Cohort notes** | haploinsufficiency mTOR tumour suppressor; gene addition conditionally compatible; tests somatic second-hit complexity |
| **Mechanism** | haploinsufficiency — Germline TSC2 mutation plus somatic second-hit loss of the wild-type allele drives mTORC1 hyperactivation and hamartoma formation in multiple tissues; gene addition addresses the haploinsufficient state but cannot prevent independent somatic second-hit events in susceptible cells throughout the body |
| **Gene-addition fit** | conditional |
| **Preferred modality** | gene_addition_tumour_suppressor_rescue |
| **Mechanism evidence** | Henske et al. (1995 Genes Chromosomes Cancer PMID 7547639) demonstrated LOH at the TSC2 locus in angiomyolipomas confirming two-hit tumour suppressor mechanism; gene addition is conditional because systemic delivery cannot prevent the many independent somatic second-hit events that initiate individual hamartomas |
| **Evidence source** | [Henske et al. 1995 Genes Chromosomes Cancer PMID 7547639](https://pubmed.ncbi.nlm.nih.gov/7547639/) |
| **Evidence status** | source_checked |

---

## Non-LOF — Repeat Expansion / Silencing (2 diseases)

### Fragile X syndrome

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:908](https://www.orpha.net/en/disease/detail/908) |
| **Gene** | [FMR1](https://www.uniprot.org/uniprotkb/Q06787) |
| **Gene CDS** | 1899 bp |
| **Inheritance** | X-linked dominant |
| **Primary tissues** | CNS |
| **Prevalence** | 1-5/10000 |
| **OMIM** | [300624](https://omim.org/entry/300624) |
| **Cohort notes** | CGG repeat expansion silences FMR1 by methylation; cDNA addition bypasses silenced allele; FMR1 protein sequence is normal |
| **Mechanism** | repeat_expansion_silencing — CGG trinucleotide repeat expansion (>200 repeats) in the FMR1 5-prime UTR triggers de novo CpG methylation and transcriptional silencing; the FMR1 protein coding sequence is structurally normal when expressed |
| **Gene-addition fit** | conditional |
| **Preferred modality** | aav_cns_fmr1_cdna_addition |
| **Mechanism evidence** | Liu XS et al. (2018 Cell PMID 29456084) demonstrated methylation-dependent silencing of the FMR1 locus by the CGG repeat; FMR1 cDNA addition (lacking the expanded repeat-containing UTR) bypasses the silenced endogenous allele and is not subject to re-silencing — same logic as FXN in Friedreich ataxia |
| **Evidence source** | [Liu XS et al. 2018 Cell PMID 29456084](https://pubmed.ncbi.nlm.nih.gov/29456084/) |
| **Evidence status** | source_checked |

### Friedreich ataxia

| Field | Value |
|---|---|
| **ORPHA ID** | [ORPHA:95](https://www.orpha.net/en/disease/detail/95) |
| **Gene** | [FXN](https://www.uniprot.org/uniprotkb/Q16595) |
| **Gene CDS** | 633 bp |
| **Inheritance** | Autosomal recessive |
| **Primary tissues** | CNS; heart |
| **Prevalence** | 1-9/100000 |
| **OMIM** | [229300](https://omim.org/entry/229300) |
| **Cohort notes** | GAA repeat expansion silencing frataxin; gene addition conditionally compatible; tests epigenetic silencing scoring |
| **Mechanism** | repeat_expansion_silencing — GAA trinucleotide repeat expansion in FXN intron 1 induces heterochromatin formation with H3K9me3 and DNA hypermethylation silencing frataxin transcription; the FXN protein coding sequence is structurally normal so a transgenic cDNA (without the expanded intron) can restore frataxin expression |
| **Gene-addition fit** | conditional |
| **Preferred modality** | frataxin_gene_addition_or_epigenetic_derepression |
| **Mechanism evidence** | Campuzano et al. (1996 Science PMID 8596916) identified the intronic GAA expansion; Al-Mahdawi et al. (2008 Hum Mol Genet PMID 18045775) characterised the heterochromatin mechanism; FXN cDNA gene addition is actively pursued clinically because the normal frataxin protein sequence is preserved |
| **Evidence source** | [Campuzano et al. 1996 Science PMID 8596916; Al-Mahdawi et al. 2008 Hum Mol Genet PMID 18045775](https://pubmed.ncbi.nlm.nih.gov/8596916/) |
| **Evidence status** | source_checked |
