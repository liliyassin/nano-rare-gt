"""UniProt gene/protein client."""
import time
from dataclasses import dataclass
from typing import Optional
import requests

UNIPROT_BASE = "https://rest.uniprot.org/uniprotkb"
_SESSION = requests.Session()
_SESSION.headers["Accept"] = "application/json"
_CACHE: dict = {}


@dataclass
class GeneInfo:
    symbol: str
    uniprot_id: Optional[str]
    protein_name: Optional[str]
    cds_length_bp: Optional[int]
    aa_length: Optional[int]
    is_secreted: bool
    subcellular_location: list[str]
    go_terms: list[str]
    keywords: list[str]
    domains: list[str]


def _search_uniprot(gene_symbol: str, organism: str = "human") -> Optional[dict]:
    """Search UniProt for a human gene by symbol."""
    query = f"gene_exact:{gene_symbol} AND organism_id:9606 AND reviewed:true"
    try:
        r = _SESSION.get(
            f"{UNIPROT_BASE}/search",
            params={
                "query": query,
                "fields": "accession,gene_names,protein_name,sequence,cc_subcellular_location,go,keyword,ft_domain,organism_name",
                "size": 1,
                "format": "json",
            },
            timeout=15,
        )
        if r.status_code == 200:
            results = r.json().get("results", [])
            return results[0] if results else None
    except Exception:
        pass
    return None


def fetch_gene(gene_symbol: str) -> GeneInfo:
    """Fetch gene/protein info from UniProt; fall back to static data."""
    if gene_symbol in _CACHE:
        return _CACHE[gene_symbol]

    data = _search_uniprot(gene_symbol)
    if data:
        info = _parse_uniprot(gene_symbol, data)
    else:
        info = _fallback_gene(gene_symbol)

    _CACHE[gene_symbol] = info
    return info


def _parse_uniprot(symbol: str, data: dict) -> GeneInfo:
    acc = data.get("primaryAccession", "")
    seq = data.get("sequence", {})
    aa_len = seq.get("length", 0)
    cds_bp = aa_len * 3 if aa_len else None

    # Subcellular location
    sub_locs = []
    for comment in data.get("comments", []):
        if comment.get("commentType") == "SUBCELLULAR LOCATION":
            for loc in comment.get("subcellularLocations", []):
                loc_val = loc.get("location", {}).get("value", "")
                if loc_val:
                    sub_locs.append(loc_val)

    is_secreted = any("secret" in loc.lower() or "extracell" in loc.lower() for loc in sub_locs)

    # GO terms
    go_terms = [
        go.get("id", "")
        for go in data.get("uniProtKBCrossReferences", [])
        if go.get("database") == "GO"
    ][:10]

    # Keywords
    keywords = [kw.get("name", "") for kw in data.get("keywords", [])]

    # Protein name
    prot_name = (
        data.get("proteinDescription", {})
        .get("recommendedName", {})
        .get("fullName", {})
        .get("value", "")
    )

    # Domains
    domains = [
        feat.get("description", "")
        for feat in data.get("features", [])
        if feat.get("type") == "Domain"
    ]

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


def _fallback_gene(symbol: str) -> GeneInfo:
    """Static fallback for known genes."""
    FALLBACKS = {
        "SMN1": GeneInfo(
            "SMN1", "Q16637", "Survival motor neuron protein",
            891, 294, False, ["Intracellular", "Nucleus"], [], ["SMN"], ["Tudor"],
        ),
        "F9": GeneInfo(
            "F9", "P00740", "Coagulation factor IX",
            1383, 461, True, ["Secreted", "Extracellular"], [], ["Coagulation"], [],
        ),
        "GLA": GeneInfo(
            "GLA", "P06280", "Alpha-galactosidase A",
            1290, 429, True, ["Lysosome", "Secreted"], [], ["Lysosome"], [],
        ),
        "SGSH": GeneInfo(
            "SGSH", "P51688", "N-sulphoglucosamine sulphohydrolase",
            1674, 557, True, ["Lysosome"], [], ["Lysosome"], [],
        ),
        "UGT1A1": GeneInfo(
            "UGT1A1", "P22309", "UDP-glucuronosyltransferase 1-1",
            1596, 531, False, ["ER membrane", "Microsome"], [], [], [],
        ),
        "ROGDI": GeneInfo(
            "ROGDI", "Q9GZN7", "Protein rogdi homolog",
            861, 287, False,
            ["Nuclear envelope", "Presynapse", "Synaptic vesicle"],
            ["Rabconnectin-3 complex interaction", "V-ATPase assembly/regulation"],
            ["Synapse", "Rabconnectin-3", "V-ATPase"],
            ["RAVE2/Rogdi", "Rogdi_lz"],
        ),
        "RPE65": GeneInfo(
            "RPE65", "Q16518", "Retinal pigment epithelium 65",
            2646, 533, False, ["Cytoplasm", "ER membrane"], [], [], [],
        ),
        "F8": GeneInfo(
            "F8", "P00451", "Coagulation factor VIII",
            4374, 2351, True, ["Secreted"], [], ["Coagulation"], [],
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
        ),
        # ── No-trial target disease genes ────────────────────────────────────
        "MCOLN1": GeneInfo(
            "MCOLN1", "Q9GZU1", "Mucolipin-1",
            1740, 580, False, ["Lysosome membrane", "Late endosome membrane"],
            [], ["Lysosome", "Ion channel"], ["TRP channel"],
        ),
        "MAN2B1": GeneInfo(
            "MAN2B1", "O00754", "Lysosomal alpha-mannosidase",
            3033, 1011, True, ["Lysosome"], [], ["Lysosome"], ["Alpha-mannosidase"],
        ),
        "BCKDHA": GeneInfo(
            "BCKDHA", "P12694", "2-oxoisovalerate dehydrogenase subunit alpha",
            1335, 445, False, ["Mitochondrial matrix"], [], [], [],
        ),
        "SLC17A5": GeneInfo(
            "SLC17A5", "Q9NRA2", "Sialin",
            1485, 495, False, ["Lysosome membrane"], [], ["Lysosome", "Transport"], [],
        ),
    }
    return FALLBACKS.get(
        symbol,
        GeneInfo(symbol, None, None, None, None, False, [], [], [], []),
    )
