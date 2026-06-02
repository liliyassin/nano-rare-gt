"""Orphanet disease client — fetches disease metadata and gene associations."""
import json
import time
from dataclasses import dataclass, field
from typing import Optional
import requests

ORPHANET_BASE = "https://api.orphacode.org/EN/ClinicalEntity"
# Fallback: use Orphadata REST API
ORPHADATA_BASE = "https://www.orphadata.com/cgi-bin/ORPHAnomenclature.php"

_CACHE: dict = {}
_SESSION = requests.Session()
_SESSION.headers["accept"] = "application/json"


@dataclass
class DiseaseInfo:
    orphanet_id: str        # e.g. "ORPHA:70"
    name: str
    omim_ids: list[str]
    prevalence: Optional[str]
    inheritance: list[str]
    gene_symbols: list[str]   # causal genes
    hpo_terms: list[str]
    affected_tissues: list[str]  # derived from HPO


def _orpha_num(orpha_id: str) -> str:
    """Extract numeric part from 'ORPHA:70' or '70'."""
    return orpha_id.replace("ORPHA:", "").strip()


def _tissues_from_hpo(hpo_terms: list[str]) -> list[str]:
    """Crude tissue mapping from HPO term names."""
    tissue_map = {
        "liver": ["hepat", "liver", "cirrhosis", "jaundice"],
        "CNS": ["brain", "cerebr", "spinal", "neurolog", "intellectual", "seizure",
                "dementia", "ataxia", "cognitive", "neurodegen"],
        "muscle": ["muscul", "myopathy", "dystrophi", "myotonia", "weakness"],
        "retina": ["retina", "visual", "optic", "blindness", "macular"],
        "hematopoietic": ["anemia", "hematolog", "platelet", "leukocyte", "bone marrow"],
        "heart": ["cardiac", "cardiomyopathy", "heart"],
        "kidney": ["renal", "kidney", "nephro"],
    }
    found = set()
    for term in hpo_terms:
        tl = term.lower()
        for tissue, keywords in tissue_map.items():
            if any(kw in tl for kw in keywords):
                found.add(tissue)
    return list(found)


def fetch_disease(orpha_id: str) -> Optional[DiseaseInfo]:
    """Fetch disease info from Orphanet API."""
    num = _orpha_num(orpha_id)
    cache_key = f"disease:{num}"
    if cache_key in _CACHE:
        return _CACHE[cache_key]

    # Try Orphanet API
    result = _fetch_from_orphanet(num)
    _CACHE[cache_key] = result
    return result


def _fetch_from_orphanet(orpha_num: str) -> Optional[DiseaseInfo]:
    """Try the Orphanet REST API (api.orphacode.org)."""
    try:
        # Get basic disease info
        r = _SESSION.get(f"{ORPHANET_BASE}/orphacode/{orpha_num}", timeout=10)
        if r.status_code != 200:
            return _fallback_disease(orpha_num)
        data = r.json()
        name = data.get("Preferred term", f"ORPHA:{orpha_num}")

        # Get gene associations
        time.sleep(0.2)
        r2 = _SESSION.get(f"{ORPHANET_BASE}/orphacode/{orpha_num}/Gene", timeout=10)
        gene_symbols = []
        if r2.status_code == 200:
            genes_data = r2.json()
            for assoc in genes_data.get("Genes", []):
                sym = assoc.get("Gene symbol") or assoc.get("Symbol", "")
                if sym:
                    gene_symbols.append(sym)

        # Get inheritance
        time.sleep(0.2)
        r3 = _SESSION.get(f"{ORPHANET_BASE}/orphacode/{orpha_num}/inheritance", timeout=10)
        inheritance = []
        if r3.status_code == 200:
            inh_data = r3.json()
            for inh in inh_data.get("Inheritance", []):
                val = inh.get("Inheritance value", "")
                if val:
                    inheritance.append(val)

        # Extract OMIM cross-refs from base data
        omim_ids = []
        for xref in data.get("References", []):
            if xref.get("Source") == "OMIM":
                omim_ids.append(xref.get("Reference", ""))

        hpo_terms: list[str] = []
        info = DiseaseInfo(
            orphanet_id=f"ORPHA:{orpha_num}",
            name=name,
            omim_ids=omim_ids,
            prevalence=data.get("Prevalence", {}).get("Prevalence class", None) if isinstance(data.get("Prevalence"), dict) else None,
            inheritance=inheritance,
            gene_symbols=gene_symbols,
            hpo_terms=hpo_terms,
            affected_tissues=_tissues_from_hpo(hpo_terms),
        )
        return info

    except Exception:
        return _fallback_disease(orpha_num)


# ── Static fallback data for the 5 target diseases ──────────────────────────
_FALLBACK: dict[str, DiseaseInfo] = {}


def _build_fallbacks() -> None:
    global _FALLBACK
    _FALLBACK = {
        "70": DiseaseInfo(
            orphanet_id="ORPHA:70", name="Spinal Muscular Atrophy",
            omim_ids=["253300"], prevalence="1-5/10000",
            inheritance=["Autosomal recessive"],
            gene_symbols=["SMN1", "SMN2"],
            hpo_terms=["Muscle weakness", "Spinal cord degeneration", "Motor neuron loss"],
            affected_tissues=["CNS", "muscle"],
        ),
        "306": DiseaseInfo(
            orphanet_id="ORPHA:306", name="Hemophilia B",
            omim_ids=["306900"], prevalence="1-5/100000",
            inheritance=["X-linked recessive"],
            gene_symbols=["F9"],
            hpo_terms=["Prolonged bleeding", "Joint hemorrhage", "Liver coagulation"],
            affected_tissues=["liver"],
        ),
        "324": DiseaseInfo(
            orphanet_id="ORPHA:324", name="Fabry disease",
            omim_ids=["301500"], prevalence="1-5/10000",
            inheritance=["X-linked dominant"],
            gene_symbols=["GLA"],
            hpo_terms=["Neuropathic pain", "Cardiomyopathy", "Renal failure",
                       "Angiokeratoma", "Lysosomal storage"],
            affected_tissues=["liver", "kidney", "heart", "CNS"],
        ),
        "79269": DiseaseInfo(
            orphanet_id="ORPHA:79269", name="Mucopolysaccharidosis type IIIA (Sanfilippo A)",
            omim_ids=["252900"], prevalence="1-9/100000",
            inheritance=["Autosomal recessive"],
            gene_symbols=["SGSH"],
            hpo_terms=["Intellectual disability", "Neurodegeneration", "Brain atrophy",
                       "Lysosomal storage", "Behavioural problems"],
            affected_tissues=["CNS"],
        ),
        "1060": DiseaseInfo(
            orphanet_id="ORPHA:1060", name="Crigler-Najjar syndrome type I",
            omim_ids=["218800"], prevalence="<1/1000000",
            inheritance=["Autosomal recessive"],
            gene_symbols=["UGT1A1"],
            hpo_terms=["Jaundice", "Hepatic dysfunction", "Bilirubin encephalopathy",
                       "Liver enzyme deficiency"],
            affected_tissues=["liver"],
        ),
        "1946": DiseaseInfo(
            orphanet_id="ORPHA:1946",
            name="Kohlschutter-Tonz syndrome",
            omim_ids=["226750"],
            prevalence="<1/1000000",
            inheritance=["Autosomal recessive"],
            gene_symbols=["ROGDI"],
            hpo_terms=[
                "Amelogenesis imperfecta",
                "Early-onset epilepsy",
                "Severe developmental delay",
                "Intellectual disability",
                "Spasticity",
                "Neurodegeneration",
            ],
            affected_tissues=["CNS"],
        ),
        "578": DiseaseInfo(
            orphanet_id="ORPHA:578",
            name="Mucolipidosis type IV",
            omim_ids=["252650"],
            prevalence="<1/1000000",
            inheritance=["Autosomal recessive"],
            gene_symbols=["MCOLN1"],
            hpo_terms=[
                "Psychomotor delay",
                "Corneal opacity",
                "Retinal degeneration",
                "Intellectual disability",
                "Lysosomal storage",
                "Brain white matter abnormality",
            ],
            affected_tissues=["CNS", "retina"],
        ),
        "61": DiseaseInfo(
            orphanet_id="ORPHA:61",
            name="Alpha-mannosidosis",
            omim_ids=["248500"],
            prevalence="1-9/1000000",
            inheritance=["Autosomal recessive"],
            gene_symbols=["MAN2B1"],
            hpo_terms=[
                "Intellectual disability",
                "Coarse facies",
                "Hearing impairment",
                "Recurrent infections",
                "Lysosomal storage",
                "Hepatomegaly",
            ],
            affected_tissues=["CNS", "liver"],
        ),
        "511": DiseaseInfo(
            orphanet_id="ORPHA:511",
            name="Maple syrup urine disease",
            omim_ids=["248600"],
            prevalence="1-9/100000",
            inheritance=["Autosomal recessive"],
            gene_symbols=["BCKDHA"],
            hpo_terms=[
                "Maple syrup odor",
                "Metabolic encephalopathy",
                "Intellectual disability",
                "Liver dysfunction",
                "Neonatal metabolic crisis",
            ],
            affected_tissues=["liver", "CNS"],
        ),
        "309": DiseaseInfo(
            orphanet_id="ORPHA:309",
            name="Salla disease",
            omim_ids=["604369"],
            prevalence="<1/1000000",
            inheritance=["Autosomal recessive"],
            gene_symbols=["SLC17A5"],
            hpo_terms=[
                "Intellectual disability",
                "Cerebellar ataxia",
                "Nystagmus",
                "Hypotonia",
                "White matter abnormality",
                "Neurodegeneration",
            ],
            affected_tissues=["CNS"],
        ),
    }


_build_fallbacks()


def _fallback_disease(orpha_num: str) -> Optional[DiseaseInfo]:
    return _FALLBACK.get(orpha_num)


def cache_disease_to_db(conn, info: DiseaseInfo) -> None:
    """Persist a DiseaseInfo to the diseases table."""
    import json as _json
    conn.execute("""
        INSERT OR REPLACE INTO diseases
        (orphanet_id, name, omim_id, prevalence, inheritance,
         phenotype_terms)
        VALUES (?,?,?,?,?,?)
    """, (
        info.orphanet_id, info.name,
        info.omim_ids[0] if info.omim_ids else None,
        info.prevalence,
        info.inheritance[0] if info.inheritance else None,
        _json.dumps(info.hpo_terms),
    ))
    conn.commit()
