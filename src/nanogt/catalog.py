"""Static catalog data: vectors and GT programs."""

# Dataset has two hand-curated lists:
#   VECTORS     → 8 AAV/LV vectors with their properties
# AAV1, AAV2, AAV5, AAV8, AAV9, AAVrh10, AAV2/6, LV
# each vector has properties like tropism, cargo limit, clinical precedents, whether it's freely available, etc.
#   GT_PROGRAMS → 18 real gene therapy programs used as precedents
# e.g. Zolgensma for SMA, Hemgenix for haemophilia B, Luxturna for retinal disease, etc.
# each program has properties like disease, gene, vector used, tissue target, approval status, mechanism, protein class, inheritance, pathway, etc.
#
# This is static data (hardcoded here) that gets loaded into the SQLite
# database the first time you run `nanogt init`. Nothing here is fetched
# from the internet — it was all researched and entered manually.


# ══════════════════════════════════════════════════════════════════════════════
# VECTORS — the delivery vehicles
# ══════════════════════════════════════════════════════════════════════════════
# cargo_limit_bp  → how many base pairs of gene the vector can carry (~4700 for most AAVs)
# tissue_tropism  → which tissues the vector naturally infects
# cns_tropic      → 1 = crosses blood-brain barrier and reaches CNS
# hepatic_tropic  → 1 = reaches the liver
# muscle_tropic   → 1 = reaches muscle
# clinical_precedents → how many clinical programs have used this vector (more = more trust)
# freely_available    → 0 = patent-restricted (needs a licence to use)

VECTORS = [
    {
        "serotype": "AAV1",  # ← first AAV type developed; mainly muscle and CNS
        "cargo_limit_bp": 4700,
        "tissue_tropism": ["muscle", "CNS"],
        "cns_tropic": 1,
        "retinal_tropic": 0,
        "hepatic_tropic": 0,
        "muscle_tropic": 1,
        "clinical_precedents": 8,
        "freely_available": 1,
    },
    {
        "serotype": "AAV2",  # ← most studied AAV; retina, liver, CNS; used in Luxturna (blindness)
        "cargo_limit_bp": 4700,
        "tissue_tropism": ["retina", "liver", "CNS"],
        "cns_tropic": 1,
        "retinal_tropic": 1,
        "hepatic_tropic": 1,
        "muscle_tropic": 0,
        "clinical_precedents": 15,
        "freely_available": 1,
    },
    {
        "serotype": "AAV5",  # ← liver and CNS; used in Hemgenix (haemophilia B) and Roctavian
        "cargo_limit_bp": 4700,
        "tissue_tropism": ["liver", "lung", "CNS"],
        "cns_tropic": 1,
        "retinal_tropic": 0,
        "hepatic_tropic": 1,
        "muscle_tropic": 0,
        "clinical_precedents": 12,
        "freely_available": 0,  # ← patent-restricted
    },
    {
        "serotype": "AAV8",  # ← liver-tropic workhorse; high transduction efficiency in liver
        "cargo_limit_bp": 4700,
        "tissue_tropism": ["liver", "muscle"],
        "cns_tropic": 0,
        "retinal_tropic": 0,
        "hepatic_tropic": 1,
        "muscle_tropic": 1,
        "clinical_precedents": 10,
        "freely_available": 0,  # ← patent-restricted
    },
    {
        "serotype": "AAV9",  # ← broadest tropism; used in Zolgensma (SMA); crosses blood-brain barrier
        "cargo_limit_bp": 4700,
        "tissue_tropism": ["CNS", "muscle", "liver", "heart"],
        "cns_tropic": 1,
        "retinal_tropic": 0,
        "hepatic_tropic": 1,
        "muscle_tropic": 1,
        "clinical_precedents": 18,  # ← most clinical experience of any AAV
        "freely_available": 1,
    },
    {
        "serotype": "AAVrh10",  # ← rhesus macaque-derived; strong CNS penetration, less immune response
        "cargo_limit_bp": 4700,
        "tissue_tropism": ["CNS", "liver"],
        "cns_tropic": 1,
        "retinal_tropic": 0,
        "hepatic_tropic": 1,
        "muscle_tropic": 0,
        "clinical_precedents": 5,
        "freely_available": 0,
    },
    {
        "serotype": "AAV2/6",  # ← hybrid of AAV2 and AAV6 capsid; efficient in liver and muscle
        "cargo_limit_bp": 4700,
        "tissue_tropism": ["liver", "muscle"],
        "cns_tropic": 0,
        "retinal_tropic": 0,
        "hepatic_tropic": 1,
        "muscle_tropic": 1,
        "clinical_precedents": 6,
        "freely_available": 0,
    },
    {
        "serotype": "LV",  # ← Integrating ex vivo HSC vector class; most entries are lentiviral, Strimvelis is gammaretroviral
        "cargo_limit_bp": 8000,  # ← can carry much larger genes than AAV; used as a coarse HSC-vector capacity bucket
        "tissue_tropism": [
            "hematopoietic",
        ],  # ← mainly used for blood stem cells (ex vivo); tissue benefit comes from cell engraftment/cross-correction, not direct in vivo tropism
        "cns_tropic": 0,
        "retinal_tropic": 0,
        "hepatic_tropic": 0,
        "muscle_tropic": 0,
        "clinical_precedents": 20,  # ← most clinical experience of all vector classes (ADA-SCID, beta-thal, etc.)
        "freely_available": 1,
    },
]


# ══════════════════════════════════════════════════════════════════════════════
# GT_PROGRAMS — the 18 precedent gene therapy programs
# ══════════════════════════════════════════════════════════════════════════════
# name             → brand/trial name
# disease          → what disease it treats
# gene_symbol      → which gene is replaced/delivered
# vector           → which vector serotype is used
# tissue_target    → where in the body the gene is delivered
# cds_bp           → coding sequence size in base pairs (used in packaging check)
# approval_status  → "approved", "phase2", "phase3", etc.
# approval_year    → year of approval (None = not yet approved)
# mechanism        → always "gene_replacement" in this catalog
# protein_class    → "secreted", "lysosomal", "intracellular", "membrane", "secreted_lysosomal"
# inheritance      → "AR" (autosomal recessive) or "XL" (X-linked)
# pathway          → biological pathway label (must match keys in scoring._PATHWAY_GROUPS)

GT_PROGRAMS = [
    {
        "name": "Zolgensma",  # ← onasemnogene abeparvovec; approved 2019 (US)
        "disease": "Spinal Muscular Atrophy",  # ← SMA type 1; most severe form
        "gene_symbol": "SMN1",  # ← survival motor neuron 1; tiny gene (891bp)
        "vector": "AAV9",  # ← AAV9 chosen for CNS penetration
        "tissue_target": "CNS/motor neuron",
        "cds_bp": 891,  # ← very small gene → perfect packaging score
        "approval_status": "approved",
        "approval_year": 2019,
        "mechanism": "gene_replacement",
        "protein_class": "intracellular",  # ← SMN1 protein stays inside the cell (nucleus)
        "inheritance": "AR",  # ← autosomal recessive
        "pathway": "motor_neuron",
        "notes": None,
    },
    {
        "name": "Hemgenix",  # ← etranacogene dezaparvovec; approved 2022 (US/EU)
        "disease": "Hemophilia B",  # ← Factor IX deficiency
        "gene_symbol": "FIX",  # ← Factor 9 coagulation gene
        "vector": "AAV5",
        "tissue_target": "liver",  # ← liver makes and secretes clotting factors
        "cds_bp": 1383,
        "approval_status": "approved",
        "approval_year": 2022,
        "mechanism": "gene_replacement",
        "protein_class": "secreted",  # ← FIX is secreted into bloodstream → works body-wide
        "inheritance": "XL",  # ← X-linked recessive
        "pathway": "coagulation",
        "notes": None,
    },
    {
        "name": "Roctavian",  # ← valoctocogene roxaparvovec; approved 2023 (EU)
        "disease": "Hemophilia A",  # ← Factor VIII deficiency (more severe than B)
        "gene_symbol": "F8",
        "vector": "AAV5",
        "tissue_target": "liver",
        "cds_bp": 4374,  # ← large gene → fills almost 93% of AAV5 capacity
        "approval_status": "approved",
        "approval_year": 2023,
        "mechanism": "gene_replacement",
        "protein_class": "secreted",
        "inheritance": "XL",
        "pathway": "coagulation",
        "notes": None,
    },
    {
        "name": "Luxturna",  # ← voretigene neparvovec; approved 2017 (US/EU); FIRST AAV approval
        "disease": "Leber congenital amaurosis type 2",
        "gene_symbol": "RPE65",
        "vector": "AAV2",  # ← AAV2 has strong retinal tropism
        "tissue_target": "retina/RPE",  # ← injected directly into the eye (subretinal)
        "cds_bp": 2646,
        "approval_status": "approved",
        "approval_year": 2017,
        "mechanism": "gene_replacement",
        "protein_class": "intracellular",
        "inheritance": "AR",
        "pathway": "retinal_visual_cycle",
        "notes": None,
    },
    {
        "name": "Glybera",  # ← alipogene tiparvovec; approved EU 2012, withdrawn 2017 (no demand)
        "disease": "Lipoprotein lipase deficiency",
        "gene_symbol": "LPL",
        "vector": "AAV1",
        "tissue_target": "muscle",  # ← injected into muscle; LPL acts locally
        "cds_bp": 1527,
        "approval_status": "withdrawn",  # ← first gene therapy approved in West; withdrawn due to price/demand
        "approval_year": 2012,
        "mechanism": "gene_replacement",
        "protein_class": "secreted",
        "inheritance": "AR",
        "pathway": "lipid_metabolism",
        "notes": None,
    },
    {
        "name": "AT132",  # ← also known as resamirigene bilparvovec; Phase 3
        "disease": "X-linked myotubular myopathy",
        "gene_symbol": "MTM1",
        "vector": "AAV8",
        "tissue_target": "muscle",
        "cds_bp": 1878,
        "approval_status": "phase3",
        "approval_year": None,
        "mechanism": "gene_replacement",
        "protein_class": "intracellular",
        "inheritance": "XL",
        "pathway": "myopathy",
        "notes": None,
    },
    {
        "name": "SRP-9001",  # ← delandistrogene moxeparvovec (Elevidys); approved 2023 (US)
        "disease": "Duchenne muscular dystrophy",
        "gene_symbol": "DMD_micro",  # ← "micro-dystrophin": synthetic shortened version that fits in AAV
        "vector": "AAV9",
        "tissue_target": "muscle",
        "cds_bp": 3825,
        "approval_status": "approved",
        "approval_year": 2023,
        "mechanism": "gene_replacement",
        "protein_class": "membrane",  # ← dystrophin anchors to the muscle cell membrane
        "inheritance": "XL",
        "pathway": "myopathy",
        "notes": None,
    },
    {
        "name": "BMN 307",  # ← pegvaliase gene therapy; Phase 2 for PKU
        "disease": "Phenylketonuria",  # ← PAH enzyme deficiency → can't break down phenylalanine
        "gene_symbol": "PAH",
        "vector": "AAV5",
        "tissue_target": "liver",
        "cds_bp": 1353,
        "approval_status": "phase2",
        "approval_year": None,
        "mechanism": "gene_replacement",
        "protein_class": "intracellular",  # ← PAH enzyme works inside liver cells
        "inheritance": "AR",
        "pathway": "amino_acid_metabolism",  # ← same pathway as Crigler-Najjar (liver enzyme deficiency)
        "notes": None,
    },
    {
        "name": "GS010",  # ← lenadogene nolparvovec; Phase 3 completed; EMA MAA withdrawn April 2023 (no efficacy significance vs sham); early-access programmes active in France/Israel
        "disease": "Leber hereditary optic neuropathy",
        "gene_symbol": "ND4",  # ← mitochondrial gene; unusual — normally impossible to deliver
        "vector": "AAV2",
        "tissue_target": "retina/RGC",  # ← retinal ganglion cells
        "cds_bp": 1378,
        "approval_status": "phase3",
        "approval_year": None,
        "mechanism": "gene_replacement",
        "protein_class": "intracellular",
        "inheritance": "mitochondrial",  # ← only inheritance type that isn't AR or XL
        "pathway": "mitochondrial_complex",
        "notes": None,
    },
    {
        "name": "OAV101-IT",  # ← onasemnogene abeparvovec-brve (Itvisma); intrathecal version of Zolgensma; FDA approved Nov 2025
        "disease": "Spinal Muscular Atrophy",
        "gene_symbol": "SMN1",
        "vector": "AAV9",
        "tissue_target": "CNS/spinal cord",  # ← injected into spinal fluid (intrathecal) rather than IV
        "cds_bp": 891,
        "approval_status": "approved",
        "approval_year": 2025,
        "mechanism": "gene_replacement",
        "protein_class": "intracellular",
        "inheritance": "AR",
        "pathway": "motor_neuron",
        "notes": None,
    },
    {
        "name": "RGX-121",  # ← intrathecal AAV9 for MPS II (Hunter syndrome); Phase 3
        "disease": "Mucopolysaccharidosis type II",
        "gene_symbol": "IDS",  # ← iduronate-2-sulfatase; lysosomal enzyme
        "vector": "AAV9",
        "tissue_target": "CNS/liver",
        "cds_bp": 1659,
        "approval_status": "phase3",
        "approval_year": None,
        "mechanism": "gene_replacement",
        "protein_class": "secreted_lysosomal",  # ← IDS is both secreted AND works in lysosomes → cross-correction possible
        "inheritance": "XL",
        "pathway": "lysosomal_storage",
        "notes": None,
    },
    {
        "name": "ABO-101",  # ← AAV9 for MPS IIIB (Sanfilippo B); Phase 1/2
        "disease": "Mucopolysaccharidosis type IIIB",
        "gene_symbol": "NAGLU",
        "vector": "AAV9",
        "tissue_target": "CNS",  # ← CNS is the main target for Sanfilippo
        "cds_bp": 2238,
        "approval_status": "phase1/2",
        "approval_year": None,
        "mechanism": "gene_replacement",
        "protein_class": "secreted_lysosomal",
        "inheritance": "AR",
        "pathway": "lysosomal_storage",
        "notes": None,
    },
    {
        "name": "AVR-RD-01",  # ← lentiviral ex vivo approach for Fabry; Phase 1/2
        "disease": "Fabry disease",  # ← GLA enzyme deficiency; lysosomal storage
        "gene_symbol": "GLA",
        "vector": "LV",  # ← lentiviral, not AAV; modifies blood stem cells outside body then reinfuses
        "tissue_target": "hematopoietic",  # ← stem cells in bone marrow
        "cds_bp": 1290,
        "approval_status": "phase1/2",
        "approval_year": None,
        "mechanism": "gene_replacement",
        "protein_class": "secreted_lysosomal",
        "inheritance": "XL",
        "pathway": "lysosomal_storage",
        "notes": None,
    },
    {
        "name": "ST-920",  # ← AAV2/6 liver-targeted approach for Fabry; Phase 1/2
        "disease": "Fabry disease",
        "gene_symbol": "GLA",
        "vector": "AAV2/6",  # ← hybrid AAV; good liver transduction
        "tissue_target": "liver",
        "cds_bp": 1290,
        "approval_status": "phase1/2",
        "approval_year": None,
        "mechanism": "gene_replacement",
        "protein_class": "secreted_lysosomal",
        "inheritance": "XL",
        "pathway": "lysosomal_storage",
        "notes": None,
    },
    {
        "name": "DTX301",  # ← AAV8 for OTC deficiency (urea cycle); Phase 2
        "disease": "Ornithine transcarbamylase deficiency",
        "gene_symbol": "OTC",
        "vector": "AAV8",
        "tissue_target": "liver",
        "cds_bp": 1065,
        "approval_status": "phase2",
        "approval_year": None,
        "mechanism": "gene_replacement",
        "protein_class": "intracellular",
        "inheritance": "XL",
        "pathway": "urea_cycle",  # ← urea cycle = same pathway group as amino_acid_metabolism
        "notes": None,
    },
    {
        "name": "CPCB-RPE1",  # ← for achromatopsia (colour blindness); Phase 2/3
        "disease": "Achromatopsia",
        "gene_symbol": "CNGB3",
        "vector": "AAV8",
        "tissue_target": "retina/photoreceptor",  # ← photoreceptors (rods/cones)
        "cds_bp": 2499,
        "approval_status": "phase2/3",
        "approval_year": None,
        "mechanism": "gene_replacement",
        "protein_class": "membrane",  # ← CNGB3 is an ion channel in the photoreceptor membrane
        "inheritance": "AR",
        "pathway": "retinal_phototransduction",
        "notes": None,
    },
    {
        "name": "SPK-8011",  # ← AAVrh10 for Haemophilia A; Phase 3
        "disease": "Hemophilia A",
        "gene_symbol": "F8",
        "vector": "AAVrh10",
        "tissue_target": "liver",
        "cds_bp": 4374,  # ← F8 is huge; fills 93% of AAVrh10 capacity
        "approval_status": "phase3",
        "approval_year": None,
        "mechanism": "gene_replacement",
        "protein_class": "secreted",
        "inheritance": "XL",
        "pathway": "coagulation",
        "notes": None,
    },
    {
        "name": "DTX201",  # ← AAV8 for Haemophilia A; Phase 2
        "disease": "Hemophilia A",
        "gene_symbol": "F8",
        "vector": "AAV8",
        "tissue_target": "liver",
        "cds_bp": 4374,
        "approval_status": "phase2",
        "approval_year": None,
        "mechanism": "gene_replacement",
        "protein_class": "secreted",
        "inheritance": "XL",
        "pathway": "coagulation",
        "notes": None,
    },
    {
        "name": "Strimvelis",  # ← ex vivo autologous CD34+ gammaretroviral ADA gene therapy; grouped in the LV/integrating-HSC bucket for v0.1 scoring
        "disease": "ADA-SCID",
        "gene_symbol": "ADA",
        "vector": "LV",
        "tissue_target": "hematopoietic",
        "cds_bp": 1092,
        "approval_status": "approved",
        "approval_year": 2016,
        "mechanism": "gene_replacement",
        "protein_class": "intracellular",
        "inheritance": "AR",
        "pathway": "immune_hematopoietic",
        "notes": "Ex vivo autologous CD34+ ADA gene-addition precedent; original product uses a gammaretroviral vector, grouped with integrating HSC vectors for v0.1 scoring.",
    },
    {
        "name": "Libmeldy",  # ← atidarsagene autotemcel; approved ex vivo LV for MLD
        "disease": "Metachromatic leukodystrophy",
        "gene_symbol": "ARSA",
        "vector": "LV",
        "tissue_target": "hematopoietic/CNS",
        "cds_bp": 1521,
        "approval_status": "approved",
        "approval_year": 2020,
        "mechanism": "gene_replacement",
        "protein_class": "secreted_lysosomal",
        "inheritance": "AR",
        "pathway": "leukodystrophy",
        "notes": "Ex vivo HSC approach intended to deliver enzyme to CNS through myeloid engraftment/cross-correction.",
    },
    {
        "name": "Skysona",  # ← elivaldogene autotemcel; approved ex vivo LV for cerebral ALD
        "disease": "Cerebral adrenoleukodystrophy",
        "gene_symbol": "ABCD1",
        "vector": "LV",
        "tissue_target": "hematopoietic/CNS",
        "cds_bp": 2235,
        "approval_status": "approved",
        "approval_year": 2022,
        "mechanism": "gene_replacement",
        "protein_class": "membrane",
        "inheritance": "XL",
        "pathway": "peroxisomal",
        "notes": "Ex vivo lentiviral HSC precedent for CNS/peroxisomal disease.",
    },
]
