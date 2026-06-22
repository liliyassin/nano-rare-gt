"""UniProt gene/protein client."""

# ── What this file is ──────────────────────────────────────────────────────
# Fetches gene and protein information from the UniProt database.
# UniProt = the main public database for protein sequences and annotations.
#
# Same two-tier pattern as disease.py:
#   1. Try the live UniProt API (internet required)
#   2. Fall back to hardcoded data for all known genes in this project

import time
from dataclasses import dataclass
from typing import Optional
import requests

UNIPROT_BASE = "https://rest.uniprot.org/uniprotkb"   # ← UniProt REST API endpoint
_SESSION = requests.Session()
_SESSION.headers["Accept"] = "application/json"
_CACHE: dict = {}   # ← in-memory cache: same gene won't be fetched twice in one run


@dataclass
class GeneInfo:
    # ← data container for one gene's properties; used by scoring.py
    symbol: str                          # ← gene name, e.g. "SMN1", "GLA"
    uniprot_id: Optional[str]            # ← UniProt accession code, e.g. "P06280"
    protein_name: Optional[str]          # ← full protein name, e.g. "Alpha-galactosidase A"
    cds_length_bp: Optional[int]         # ← coding sequence length (base pairs) → used in packaging score
    aa_length: Optional[int]             # ← protein length (amino acids); cds_bp ÷ 3 = aa_length
    is_secreted: bool                    # ← True if protein is released outside the cell
    subcellular_location: list[str]      # ← where in the cell it lives, e.g. ["Lysosome", "Nucleus"]
    go_terms: list[str]                  # ← Gene Ontology IDs describing biological function
    keywords: list[str]                  # ← UniProt keyword tags, e.g. ["Lysosome", "Secreted"]
    domains: list[str]                   # ← protein domain names, e.g. ["Tudor", "Kinase"]


def _search_uniprot(gene_symbol: str, organism: str = "human") -> Optional[dict]:
    """Search UniProt for a human gene by symbol."""
    # ← builds a search query and fetches the top result from UniProt
    query = f"gene_exact:{gene_symbol} AND organism_id:9606 AND reviewed:true"
    # ← organism_id:9606 = human; reviewed:true = only manually verified "Swiss-Prot" entries
    try:
        r = _SESSION.get(
            f"{UNIPROT_BASE}/search",
            params={
                "query": query,
                "fields": "accession,gene_names,protein_name,sequence,cc_subcellular_location,go,keyword,ft_domain,organism_name",
                # ← which fields to return (accession=ID, sequence, subcellular location, GO terms, etc.)
                "size": 1,        # ← only want the top result
                "format": "json",
            },
            timeout=15,
        )
        if r.status_code == 200:
            results = r.json().get("results", [])
            return results[0] if results else None  # ← return first result, or None if nothing found
    except Exception:
        pass
    return None


def fetch_gene(gene_symbol: str) -> GeneInfo:
    """Fetch gene/protein info from UniProt; fall back to static data.

    Known poster-cohort genes use the curated local record first so generated
    results are reproducible and are not changed by UniProt search ranking,
    isoform choice, or network availability. Unknown genes still use UniProt,
    which is what lets the same code path run on arbitrary monogenic diseases.
    """
    if gene_symbol in _CACHE:
        return _CACHE[gene_symbol]  # ← already fetched → return cached

    fallback = _fallback_gene(gene_symbol)
    if fallback.uniprot_id is not None:
        info = fallback
    else:
        data = _search_uniprot(gene_symbol)
        if data:
            info = _parse_uniprot(gene_symbol, data)   # ← parse the API response into a GeneInfo object
        else:
            info = fallback          # ← API failed → use empty hardcoded fallback

    _CACHE[gene_symbol] = info
    return info


def _parse_uniprot(symbol: str, data: dict) -> GeneInfo:
    # ← extracts the relevant fields from the raw UniProt JSON response
    acc = data.get("primaryAccession", "")   # ← the UniProt ID, e.g. "P00740"
    seq = data.get("sequence", {})
    aa_len = seq.get("length", 0)            # ← protein length in amino acids
    cds_bp = aa_len * 3 if aa_len else None  # ← coding sequence = 3 base pairs per amino acid (codon)

    # ── Subcellular location ───────────────────────────────────────────────
    sub_locs = []
    for comment in data.get("comments", []):
        if comment.get("commentType") == "SUBCELLULAR LOCATION":
            for loc in comment.get("subcellularLocations", []):
                loc_val = loc.get("location", {}).get("value", "")
                if loc_val:
                    sub_locs.append(loc_val)
    # ← digs through nested JSON to find where the protein lives in the cell

    is_secreted = any("secret" in loc.lower() or "extracell" in loc.lower() for loc in sub_locs)
    # ← True if any location mentions "secreted" or "extracellular"

    # ── GO terms (first 10 only) ───────────────────────────────────────────
    go_terms = [
        go.get("id", "")
        for go in data.get("uniProtKBCrossReferences", [])
        if go.get("database") == "GO"
    ][:10]  # ← limit to 10 to avoid overloading the scoring text matching

    # ── Keywords ─────────────────────────────────────────────────────────
    keywords = [kw.get("name", "") for kw in data.get("keywords", [])]
    # ← e.g. ["Lysosome", "Glycoprotein", "Secreted"]

    # ── Protein name ──────────────────────────────────────────────────────
    prot_name = (
        data.get("proteinDescription", {})
        .get("recommendedName", {})
        .get("fullName", {})
        .get("value", "")
    )  # ← navigates nested JSON: proteinDescription → recommendedName → fullName → value

    # ── Protein domains ───────────────────────────────────────────────────
    domains = [
        feat.get("description", "")
        for feat in data.get("features", [])
        if feat.get("type") == "Domain"
    ]  # ← extracts named domain features from the UniProt feature annotations

    return GeneInfo(
        symbol=symbol,
        uniprot_id=acc,
        protein_name=prot_name,
        cds_length_bp=cds_bp,
        aa_length=aa_len,
        is_secreted=is_secreted,
        subcellular_location=sub_locs,
        go_terms=go_terms,
        keywords=keywords,
        domains=domains,
    )


# ══════════════════════════════════════════════════════════════════════════════
# STATIC FALLBACK DATA
# Hardcoded GeneInfo for all genes in this project.
# Used when UniProt API is unavailable or gene not found.
# Data sourced manually from UniProt and literature.
# ══════════════════════════════════════════════════════════════════════════════
def _fallback_gene(symbol: str) -> GeneInfo:
    """Static fallback for known genes."""
    FALLBACKS = {
        "SMN1": GeneInfo(
            "SMN1", "Q16637", "Survival motor neuron protein",
            891, 294, False, ["Intracellular", "Nucleus"], [], ["SMN"], ["Tudor"],
            # ← tiny 891bp gene, lives in nucleus, intracellular → high packaging score
        ),
        "F9": GeneInfo(
            "F9", "P00740", "Coagulation factor IX",
            1383, 461, True, ["Secreted", "Extracellular"], [], ["Coagulation"], [],
            # ← secreted into bloodstream → systemic delivery possible
        ),
        "GLA": GeneInfo(
            "GLA", "P06280", "Alpha-galactosidase A",
            1290, 429, True, ["Lysosome", "Secreted"], [], ["Lysosome"], [],
            # ← both lysosomal AND secreted → cross-correction possible; Fabry disease gene
        ),
        "SGSH": GeneInfo(
            "SGSH", "P51688", "N-sulphoglucosamine sulphohydrolase",
            1674, 557, True, ["Lysosome"], [], ["Lysosome"], [],
            # ← lysosomal enzyme; Sanfilippo A gene
        ),
        "UGT1A1": GeneInfo(
            "UGT1A1", "P22309", "UDP-glucuronosyltransferase 1-1",
            1596, 531, False, ["ER membrane", "Microsome"], [], [], [],
            # ← lives in ER membrane, NOT lysosomal/secreted → different class from most precedents
            # ← this explains Crigler-Najjar's lower score: fewer close protein-class matches
        ),
        "ROGDI": GeneInfo(
            "ROGDI", "Q9GZN7", "Protein rogdi homolog",
            861, 287, False,
            ["Nuclear envelope", "Presynapse", "Synaptic vesicle"],
            ["Rabconnectin-3 complex interaction", "V-ATPase assembly/regulation"],
            ["Synapse", "Rabconnectin-3", "V-ATPase"],
            ["RAVE2/Rogdi", "Rogdi_lz"],
            # ← Kohlschutter-Tonz gene; synapse protein; unusual biology → no perfect pathway match
        ),
        "RPE65": GeneInfo(
            "RPE65", "Q16518", "Retinal pigment epithelium-specific 65 kDa protein",
            1599, 533, False, ["Cytoplasm", "ER membrane"], [], ["Retinoid-binding", "Visual cycle"], [],
        ),
        "F8": GeneInfo(
            "F8", "P00451", "Coagulation factor VIII",
            4374, 2351, True, ["Secreted"], [], ["Coagulation"], [],
            # ← HUGE gene (4374bp); fills 93% of AAV5 capacity → tight packaging score
        ),
        "PAH": GeneInfo(
            "PAH", "P00439", "Phenylalanine-4-hydroxylase",
            1353, 451, False, ["Cytoplasm"], [], [], [],
        ),
        "OTC": GeneInfo(
            "OTC", "P00480", "Ornithine carbamoyltransferase",
            1065, 354, False, ["Mitochondrial matrix"], [], [], [],
        ),
        "NAGLU": GeneInfo(
            "NAGLU", "P54802", "Alpha-N-acetylglucosaminidase",
            2238, 743, True, ["Lysosome"], [], ["Lysosome"], [],
        ),
        "MTM1": GeneInfo(
            "MTM1", "Q13496", "Myotubularin",
            1878, 625, False, ["Cytoplasm"], [], [], [],
        ),
        "DMD_micro": GeneInfo(
            "DMD_micro", None, "Micro-dystrophin (synthetic)",
            3825, 1275, False, ["Sarcolemma", "Cytoplasm"], [], [], [],
            # ← synthetic gene; truncated version of full dystrophin (10,000bp+ → wouldn't fit in AAV)
        ),
        # ── No-trial target disease genes (added for extended analysis) ───────
        "MCOLN1": GeneInfo(
            "MCOLN1", "Q9GZU1", "Mucolipin-1",
            1740, 580, False, ["Lysosome membrane", "Late endosome membrane"],
            [], ["Lysosome", "Ion channel"], ["TRP channel"],
            # ← Mucolipidosis type IV; ion channel in lysosome membrane
        ),
        "MAN2B1": GeneInfo(
            "MAN2B1", "O00754", "Lysosomal alpha-mannosidase",
            3033, 1011, True, ["Lysosome"], [], ["Lysosome"], ["Alpha-mannosidase"],
            # ← Alpha-mannosidosis; large lysosomal enzyme (3033bp → ~65% of AAV capacity)
        ),
        "BCKDHA": GeneInfo(
            "BCKDHA", "P12694", "2-oxoisovalerate dehydrogenase subunit alpha",
            1335, 445, False, ["Mitochondrial matrix"], [], [], [],
            # ← Maple syrup urine disease; mitochondrial enzyme
        ),
        "SLC17A5": GeneInfo(
            "SLC17A5", "Q9NRA2", "Sialin",
            1485, 495, False, ["Lysosome membrane"], [], ["Lysosome", "Transport"], [],
            # ← Salla disease; lysosomal transporter for sialic acid
        ),

        # ── Extended cohort genes (40-disease dissertation cohort) ──────────
        "MT-ND4": GeneInfo(
            "MT-ND4", "P03905", "NADH dehydrogenase subunit 4",
            1377, 459, False, ["Mitochondrial inner membrane"], ["mitochondrial complex I"], ["Mitochondrion", "Membrane"], [],
        ),
        "CNGB3": GeneInfo(
            "CNGB3", "Q9NQW8", "Cyclic nucleotide-gated cation channel beta-3",
            2427, 809, False, ["Photoreceptor outer segment membrane"], ["phototransduction"], ["Membrane", "Ion channel"], [],
        ),
        "CNGA3": GeneInfo(
            "CNGA3", "Q16281", "Cyclic nucleotide-gated cation channel alpha-3",
            2085, 694, False, ["Photoreceptor outer segment membrane"], ["phototransduction"], ["Membrane", "Ion channel"], [],
        ),
        "GNAT2": GeneInfo(
            "GNAT2", "P19087", "Guanine nucleotide-binding protein G(t) subunit alpha-2",
            1065, 354, False, ["Photoreceptor outer segment", "Cytoplasm"], ["phototransduction"], ["G-protein", "Photoreceptor"], [],
        ),
        "PDE6C": GeneInfo(
            "PDE6C", "P51160", "Cone cGMP-specific 3',5'-cyclic phosphodiesterase subunit alpha'",
            2577, 858, False, ["Photoreceptor outer segment", "Cytoplasm"], ["phototransduction"], ["Hydrolase", "Photoreceptor"], [],
        ),
        "PDE6H": GeneInfo(
            "PDE6H", "Q13956", "Retinal cone rhodopsin-sensitive cGMP 3',5'-cyclic phosphodiesterase subunit gamma",
            252, 83, False, ["Photoreceptor outer segment", "Cytoplasm"], ["phototransduction"], ["Photoreceptor"], [],
        ),
        "ATF6": GeneInfo(
            "ATF6", "P18850", "Cyclic AMP-dependent transcription factor ATF-6 alpha",
            2013, 670, False, ["Endoplasmic reticulum membrane", "Nucleus"], ["unfolded protein response"], ["Transcription", "Membrane"], [],
        ),
        "RS1": GeneInfo(
            "RS1", "O15537", "Retinoschisin",
            672, 224, True, ["Secreted", "Extracellular matrix"], ["retina development"], ["Secreted"], ["Discoidin"],
        ),
        "CHM": GeneInfo(
            "CHM", "P24386", "Rab proteins geranylgeranyltransferase component A 1",
            1962, 653, False, ["Cytoplasm"], ["protein prenylation"], [], [],
        ),
        "G6PC": GeneInfo(
            "G6PC", "P35575", "Glucose-6-phosphatase",
            1071, 357, False, ["Endoplasmic reticulum membrane"], ["glucose homeostasis", "glycogen metabolism"], ["Membrane"], [],
        ),
        "MUT": GeneInfo(
            "MUT", "P22033", "Methylmalonyl-CoA mutase",
            2250, 750, False, ["Mitochondrial matrix"], ["amino acid catabolism"], ["Mitochondrion"], [],
        ),
        "GAA": GeneInfo(
            "GAA", "P10253", "Lysosomal alpha-glucosidase",
            2856, 952, True, ["Lysosome", "Secreted"], ["glycogen catabolism"], ["Lysosome"], [],
        ),
        "GBA": GeneInfo(
            "GBA", "P04062", "Glucosylceramidase",
            1491, 497, True, ["Lysosome"], ["glycosphingolipid metabolism"], ["Lysosome"], [],
        ),
        "ARSA": GeneInfo(
            "ARSA", "P15289", "Arylsulfatase A",
            1521, 507, True, ["Lysosome", "Secreted"], ["sphingolipid metabolism"], ["Lysosome"], [],
        ),
        "GALC": GeneInfo(
            "GALC", "P54803", "Galactocerebrosidase",
            2055, 685, True, ["Lysosome", "Secreted"], ["sphingolipid metabolism"], ["Lysosome"], [],
        ),
        "IDUA": GeneInfo(
            "IDUA", "P35475", "Alpha-L-iduronidase",
            1962, 653, True, ["Lysosome", "Secreted"], ["glycosaminoglycan catabolism"], ["Lysosome"], [],
        ),
        "IDS": GeneInfo(
            "IDS", "P22304", "Iduronate 2-sulfatase",
            1650, 550, True, ["Lysosome", "Secreted"], ["glycosaminoglycan catabolism"], ["Lysosome"], [],
        ),
        "DMD": GeneInfo(
            "DMD", "P11532", "Dystrophin",
            11055, 3685, False, ["Sarcolemma", "Cytoskeleton"], ["muscle structure"], ["Membrane", "Cytoskeleton"], [],
        ),
        "WAS": GeneInfo(
            "WAS", "P42768", "Wiskott-Aldrich syndrome protein",
            1506, 502, False, ["Cytoplasm", "Cytoskeleton"], ["actin cytoskeleton organization", "immune synapse"], [], [],
        ),
        "ADA": GeneInfo(
            "ADA", "P00813", "Adenosine deaminase",
            1092, 363, False, ["Cytoplasm"], ["purine metabolism", "lymphocyte development"], [], [],
        ),
        "ABCD1": GeneInfo(
            "ABCD1", "P33897", "ATP-binding cassette sub-family D member 1",
            2235, 745, False, ["Peroxisome membrane"], ["very-long-chain fatty acid transport"], ["Membrane", "Transport"], [],
        ),
        # ── Non-LOF stress-test genes ─────────────────────────────────────────
        "CHD7": GeneInfo(
            "CHD7", "Q9P2D1", "Chromodomain-helicase-DNA-binding protein 7",
            # ← very large chromatin remodeller; haploinsufficiency; complex dosage sensitivity
            7950, 2997, False, ["Nucleus"], ["chromatin remodelling", "embryonic development"], ["Nucleus", "Helicase", "Disease mutation"], ["Chromo", "Helicase", "BRK"],
        ),
        "NF1": GeneInfo(
            "NF1", "P21359", "Neurofibromin",
            # ← tumour suppressor; haploinsufficiency plus somatic second-hit
            8451, 2818, False, ["Cytoplasm", "Nucleus"], ["RAS-GAP activity", "tumour suppressor", "mTOR regulation"], ["Disease mutation"], ["RasGAP"],
        ),
        "FXN": GeneInfo(
            "FXN", "Q16595", "Frataxin",
            # ← small mitochondrial iron chaperone; silenced by GAA repeat expansion;
            #   adding a transgene can restore levels (conditional compatibility)
            633, 210, False, ["Mitochondrial matrix"], ["iron-sulfur cluster assembly", "GAA repeat silencing"], ["Mitochondrion", "Disease mutation"], [],
        ),
        "TSC2": GeneInfo(
            "TSC2", "P49815", "Tuberin",
            # ← tumour suppressor; haploinsufficiency; mTORC1 pathway regulator
            5694, 1898, False, ["Cytoplasm", "Nucleus"], ["mTOR signalling", "GTPase activation", "tumour suppressor"], ["Disease mutation"], ["GAP"],
        ),

        # ── Conditional non-LOF replacement genes ────────────────────────────
        "MECP2": GeneInfo(
            "MECP2", "P51608", "Methyl-CpG-binding protein 2",
            # ← small nuclear protein; X-linked; 1461bp fits all AAVs comfortably
            # ← haploinsufficiency causes Rett; duplication also pathogenic (dosage-sensitive)
            1461, 486, False, ["Nucleus", "Chromatin"], ["chromatin remodelling", "gene silencing"],
            ["Nucleus", "Disease mutation"], [],
        ),
        "SCN1A": GeneInfo(
            "SCN1A", "P35498", "Sodium channel protein type 1 subunit alpha",
            # ← very large voltage-gated sodium channel (6027bp); exceeds AAV capacity
            # ← fits LV (8000bp); only LV-based programs can deliver
            # ← haploinsufficiency in inhibitory interneurons causes Dravet syndrome
            6027, 2009, False, ["Cell membrane"], ["sodium channel", "inhibitory interneuron", "action potential"],
            ["Membrane", "Ion channel", "Disease mutation"], ["Voltage-gated sodium channel"],
        ),
        "FMR1": GeneInfo(
            "FMR1", "Q06787", "Fragile X mental retardation protein 1",
            # ← RNA-binding protein; 1899bp fits AAV; expressed in neurons
            # ← CGG repeat expansion silences the locus; protein sequence is normal when expressed
            1899, 632, False, ["Nucleus", "Cytoplasm", "Dendrites"],
            ["mRNA transport", "synaptic plasticity", "CGG repeat silencing"],
            ["RNA-binding", "Disease mutation"], ["KH", "Agenet"],
        ),
        "UBE3A": GeneInfo(
            "UBE3A", "Q05086", "Ubiquitin-protein ligase E3A",
            # ← E3 ubiquitin ligase; 2598bp fits AAV; maternal allele lost in Angelman
            # ← paternal allele silenced by antisense RNA in neurons
            2598, 865, False, ["Nucleus", "Cytoplasm", "Synapse"],
            ["ubiquitin-proteasome", "synaptic protein degradation", "imprinting"],
            ["Ubiquitin ligase", "Disease mutation"], ["HECT"],
        ),
        "CDKL5": GeneInfo(
            "CDKL5", "O76039", "Cyclin-dependent kinase-like 5",
            # ← serine/threonine kinase; 3093bp fits AAV; X-linked
            # ← haploinsufficiency disrupts neuronal cytoskeletal and synaptic signalling
            3093, 1030, False, ["Nucleus", "Cytoplasm", "Dendrites"],
            ["neuronal kinase", "synaptic signalling", "MECP2 phosphorylation"],
            ["Kinase", "Disease mutation"], ["Protein kinase"],
        ),
        "GATA2": GeneInfo(
            "GATA2", "P23769", "Endothelial transcription factor GATA-2",
            # ← zinc-finger transcription factor; 1443bp fits all AAVs
            # ← haploinsufficiency depletes HSC and lymphatic endothelial progenitors
            1443, 480, False, ["Nucleus"],
            ["hematopoiesis", "HSC maintenance", "lymphatic development"],
            ["Transcription factor", "Zinc-finger", "Disease mutation"], ["GATA zinc finger"],
        ),

        # ── 46-disease cohort new additions ──────────────────────────────────
        # UniProt CDS = (protein_length_aa × 3) + 3 (stop codon)
        "CFTR": GeneInfo(
            "CFTR", "P13569", "Cystic fibrosis transmembrane conductance regulator",
            # ← ABC-family Cl⁻ channel; 4443bp fills ~95% of AAV5 capacity → very tight packaging
            # ← transmembrane channel; not secreted; apical surface of epithelial cells
            # ← UniProt P13569: 1480 aa → CDS 4443 bp
            4443, 1480, False, ["Cell membrane", "Apical membrane"],
            ["chloride channel", "epithelial ion transport", "CFTR pathway"],
            ["Ion channel", "Membrane", "Disease mutation"], ["ABC transporter"],
        ),
        "ASPA": GeneInfo(
            "ASPA", "P45381", "Aspartoacylase",
            # ← cytoplasmic enzyme in oligodendrocytes; hydrolyses N-acetyl-aspartate
            # ← 942bp fits all AAVs easily; CNS target
            # ← UniProt P45381: 313 aa → CDS 942 bp
            942, 313, False, ["Cytoplasm"],
            ["N-acetyl-aspartate catabolism", "myelin synthesis", "oligodendrocyte"],
            ["Hydrolase", "Disease mutation"], [],
        ),
        "BTD": GeneInfo(
            "BTD", "P43251", "Biotinidase",
            # ← secreted glycoprotein; recycles biotin from biotinylated proteins in plasma
            # ← 1632bp; ubiquitous expression; liver is the main source
            # ← UniProt P43251: 543 aa → CDS 1632 bp
            1632, 543, True, ["Secreted", "Extracellular"],
            ["biotin recycling", "coenzyme metabolism"],
            ["Hydrolase", "Disease mutation"], [],
        ),
        "HEXA": GeneInfo(
            "HEXA", "P06865", "Beta-hexosaminidase subunit alpha",
            # ← lysosomal enzyme; alpha subunit of hexosaminidase A (HEXA/HEXB heterodimer)
            # ← secreted form exists; cross-correction plausible
            # ← UniProt P06865: 529 aa → CDS 1590 bp
            1590, 529, True, ["Lysosome", "Secreted"],
            ["GM2 ganglioside catabolism", "glycolipid metabolism"],
            ["Lysosome", "Hydrolase", "Disease mutation"], ["Glycosyl hydrolase"],
        ),
        "ATP7B": GeneInfo(
            "ATP7B", "P35670", "Copper-transporting ATPase 2",
            # ← P-type ATPase; trans-Golgi network in hepatocytes; excretes copper into bile
            # ← 4398bp; large transmembrane pump; important to check packaging capacity
            # ← UniProt P35670: 1465 aa → CDS 4398 bp
            4398, 1465, False, ["Trans-Golgi network", "Membrane"],
            ["copper transport", "bile secretion", "copper homeostasis"],
            ["ATPase", "Membrane", "Metal-binding", "Disease mutation"], ["Cation transport ATPase"],
        ),
        "CTNS": GeneInfo(
            "CTNS", "O60931", "Cystinosin",
            # ← lysosomal membrane protein; cystine/H+ co-transporter (7-transmembrane)
            # ← NOT a soluble enzyme; cannot be secreted; no cross-correction possible
            # ← same class as MCOLN1 (ML-IV): membrane-anchored transporter
            # ← UniProt O60931: 367 aa → CDS 1104 bp
            1104, 367, False, ["Lysosome membrane", "Late endosome membrane"],
            ["cystine transport", "lysosomal cystine export"],
            ["Lysosome", "Transport", "Membrane", "Disease mutation"], ["Cystinosin"],
        ),
        "SMPD1": GeneInfo(
            "SMPD1", "P17405", "Sphingomyelin phosphodiesterase 1",
            # ← lysosomal enzyme with a secreted form; hydrolyses sphingomyelin → ceramide
            # ← 1890bp fits AAV; liver/spleen are primary sites; CNS involvement in type A
            # ← UniProt P17405: 629 aa → CDS 1890 bp
            1890, 629, True, ["Lysosome", "Secreted"],
            ["sphingomyelin catabolism", "sphingolipid metabolism"],
            ["Lysosome", "Hydrolase", "Disease mutation"], [],
        ),
        "NPC1": GeneInfo(
            "NPC1", "O15118", "NPC intracellular cholesterol transporter 1",
            # ← large lysosomal membrane protein; 13-transmembrane cholesterol transporter
            # ← 3837bp; transmembrane; NOT secreted; no cross-correction possible
            # ← UniProt O15118: 1278 aa → CDS 3837 bp
            3837, 1278, False, ["Lysosome membrane", "Late endosome membrane"],
            ["cholesterol transport", "intracellular lipid trafficking"],
            ["Lysosome", "Membrane", "Transport", "Disease mutation"], ["NPC1"],
        ),
        "PEX1": GeneInfo(
            "PEX1", "O43933", "Peroxisome biogenesis factor 1",
            # ← AAA-ATPase; cytoplasmic; peroxisome import receptor recycling
            # ← 3852bp fits AAV; peroxisome target → peroxisomal import machinery required
            # ← UniProt O43933: 1283 aa → CDS 3852 bp
            3852, 1283, False, ["Cytoplasm", "Peroxisome membrane"],
            ["peroxisome biogenesis", "peroxin import", "AAA ATPase"],
            ["ATPase", "Peroxisome", "Disease mutation"], ["AAA ATPase"],
        ),
        "AGXT": GeneInfo(
            "AGXT", "P21549", "Alanine-glyoxylate aminotransferase",
            # ← peroxisomal enzyme; converts glyoxylate → glycine in hepatocytes
            # ← 1179bp; small gene; but peroxisomal targeting signal must be preserved
            # ← UniProt P21549: 392 aa → CDS 1179 bp
            1179, 392, False, ["Peroxisome"],
            ["glyoxylate metabolism", "oxalate prevention", "peroxisomal aminotransferase"],
            ["Aminotransferase", "Peroxisome", "Disease mutation"], ["Aminotransferase"],
        ),
        "MYO7A": GeneInfo(
            "MYO7A", "Q13402", "Unconventional myosin-VIIa",
            # ← large actin-based motor protein; expressed in retinal pigment epithelium and hair cells
            # ← 6648bp > AAV capacity (~4.7kb); dual-vector or LV delivery likely required
            # ← UniProt Q13402: 2215 aa → CDS 6648 bp
            6648, 2215, False, ["Cytoplasm", "Cytoskeleton", "Stereocilia"],
            ["actin motor", "retinal pigment epithelium", "hair cell stereocilia"],
            ["Motor protein", "Cytoskeleton", "Disease mutation"], ["Myosin head", "IQ motif", "FERM"],
        ),
        "TSC1": GeneInfo(
            "TSC1", "Q92574", "Hamartin",
            # ← tumour suppressor; haploinsufficiency; forms TSC1/TSC2 complex (GAP for Rheb)
            # ← 3495bp fits most AAVs; mTORC1 pathway regulation
            # ← UniProt Q92574: 1164 aa → CDS 3495 bp
            3495, 1164, False, ["Cytoplasm", "Nucleus"],
            ["mTOR signalling", "GTPase activation", "tumour suppressor", "Rheb-GAP"],
            ["Disease mutation"], ["HEAT repeat"],
        ),
        # Approved HGNC aliases — same protein as GBA/G6PC/MUT static entries above
        "GBA1": GeneInfo(
            "GBA1", "P04062", "Glucosylceramidase beta 1",
            1491, 497, True, ["Lysosome"], ["glycosphingolipid metabolism"], ["Lysosome"], [],
        ),
        "G6PC1": GeneInfo(
            "G6PC1", "P35575", "Glucose-6-phosphatase catalytic subunit 1",
            1071, 357, False, ["Endoplasmic reticulum membrane"], ["glucose homeostasis", "glycogen metabolism"], ["Membrane"], [],
        ),
        "MMUT": GeneInfo(
            "MMUT", "P22033", "Methylmalonyl-CoA mutase",
            2250, 750, False, ["Mitochondrial matrix"], ["amino acid catabolism"], ["Mitochondrion"], [],
        ),
    }
    return FALLBACKS.get(
        symbol,
        GeneInfo(symbol, None, None, None, None, False, [], [], [], []),
        # ← unknown gene → return empty GeneInfo (scoring will use neutral defaults)
    )
