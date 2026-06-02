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
    """Fetch gene/protein info from UniProt; fall back to static data."""
    if gene_symbol in _CACHE:
        return _CACHE[gene_symbol]  # ← already fetched → return cached

    data = _search_uniprot(gene_symbol)
    if data:
        info = _parse_uniprot(gene_symbol, data)   # ← parse the API response into a GeneInfo object
    else:
        info = _fallback_gene(gene_symbol)          # ← API failed → use hardcoded fallback

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
            "RPE65", "Q16518", "Retinal pigment epithelium 65",
            2646, 533, False, ["Cytoplasm", "ER membrane"], [], [], [],
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
    }
    return FALLBACKS.get(
        symbol,
        GeneInfo(symbol, None, None, None, None, False, [], [], [], []),
        # ← unknown gene → return empty GeneInfo (scoring will use neutral defaults)
    )
