"""Orphanet disease client — fetches disease metadata and gene associations."""

# ── What this file is ──────────────────────────────────────────────────────
# Fetches disease information when you give it an Orphanet ID.
# Two-tier system:
#   1. First tries the live Orphanet API (internet required)
#   2. If that fails (API down, no internet, disease not found), uses hardcoded fallback data
#
# The fallback data covers all the diseases in this project so the tool
# always works even without internet access.

import json
import time
from dataclasses import dataclass, field
from typing import Optional
import requests

ORPHANET_BASE = "https://api.orphacode.org/EN/ClinicalEntity"     # ← main Orphanet API endpoint
ORPHADATA_BASE = "https://www.orphadata.com/cgi-bin/ORPHAnomenclature.php"  # ← backup (not currently used)

_CACHE: dict = {}                      # ← in-memory cache: avoids re-fetching the same disease twice in one run
_SESSION = requests.Session()          # ← reusable HTTP session (more efficient than new connection each time)
_SESSION.headers["accept"] = "application/json"  # ← tells the API to send data as JSON


@dataclass
class DiseaseInfo:
    # ← the data container for one disease; populated by fetch_disease()
    orphanet_id: str         # ← e.g. "ORPHA:70"
    name: str                # ← e.g. "Spinal Muscular Atrophy"
    omim_ids: list[str]      # ← OMIM database cross-references
    prevalence: Optional[str]      # ← e.g. "1-5/10000"
    inheritance: list[str]         # ← e.g. ["Autosomal recessive"]
    gene_symbols: list[str]        # ← causal genes, e.g. ["SMN1", "SMN2"]
    hpo_terms: list[str]           # ← HPO symptom names, e.g. ["Muscle weakness", "Seizures"]
    affected_tissues: list[str]    # ← derived from HPO terms; used in tropism scoring


def _orpha_num(orpha_id: str) -> str:
    """Extract numeric part from 'ORPHA:70' or '70'."""
    # ← strips the "ORPHA:" prefix so we get just the number for API calls
    return orpha_id.replace("ORPHA:", "").strip()


def _tissues_from_hpo(hpo_terms: list[str]) -> list[str]:
    """Crude tissue mapping from HPO term names."""
    # ← converts HPO symptom names into tissue labels used by the scoring engine
    # Why crude? HPO terms are plain-text descriptions; we search for keywords within them.
    # e.g. "Hepatomegaly" contains "hepat" → maps to "liver"

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
    found = set()  # ← set = no duplicates
    for term in hpo_terms:
        tl = term.lower()
        for tissue, keywords in tissue_map.items():
            if any(kw in tl for kw in keywords):  # ← if any keyword appears in the HPO term
                found.add(tissue)
    return list(found)


def fetch_disease(orpha_id: str) -> Optional[DiseaseInfo]:
    """Fetch disease info from Orphanet API."""
    num = _orpha_num(orpha_id)
    cache_key = f"disease:{num}"
    if cache_key in _CACHE:
        return _CACHE[cache_key]  # ← already fetched this session → return cached result

    result = _fetch_from_orphanet(num)
    _CACHE[cache_key] = result  # ← store in cache for reuse
    return result


def _fetch_from_orphanet(orpha_num: str) -> Optional[DiseaseInfo]:
    """Try the Orphanet REST API (api.orphacode.org)."""
    try:
        # ── Request 1: basic disease info ─────────────────────────────────
        r = _SESSION.get(f"{ORPHANET_BASE}/orphacode/{orpha_num}", timeout=10)
        # ← GET request to Orphanet; timeout=10 means give up after 10 seconds
        if r.status_code != 200:
            return _fallback_disease(orpha_num)  # ← API error → use hardcoded fallback
        data = r.json()  # ← parse the JSON response into a Python dictionary
        name = data.get("Preferred term", f"ORPHA:{orpha_num}")  # ← get disease name

        # ── Request 2: gene associations ──────────────────────────────────
        time.sleep(0.2)  # ← polite pause: don't hammer the API with rapid requests
        r2 = _SESSION.get(f"{ORPHANET_BASE}/orphacode/{orpha_num}/Gene", timeout=10)
        gene_symbols = []
        if r2.status_code == 200:
            genes_data = r2.json()
            for assoc in genes_data.get("Genes", []):
                sym = assoc.get("Gene symbol") or assoc.get("Symbol", "")
                if sym:
                    gene_symbols.append(sym)

        # ── Request 3: inheritance pattern ────────────────────────────────
        time.sleep(0.2)
        r3 = _SESSION.get(f"{ORPHANET_BASE}/orphacode/{orpha_num}/inheritance", timeout=10)
        inheritance = []
        if r3.status_code == 200:
            inh_data = r3.json()
            for inh in inh_data.get("Inheritance", []):
                val = inh.get("Inheritance value", "")
                if val:
                    inheritance.append(val)

        # ── Extract OMIM cross-references ─────────────────────────────────
        omim_ids = []
        for xref in data.get("References", []):
            if xref.get("Source") == "OMIM":
                omim_ids.append(xref.get("Reference", ""))

        hpo_terms: list[str] = []  # ← Orphanet API doesn't return HPO terms in this endpoint
        info = DiseaseInfo(
            orphanet_id=f"ORPHA:{orpha_num}",
            name=name,
            omim_ids=omim_ids,
            prevalence=data.get("Prevalence", {}).get("Prevalence class", None) if isinstance(data.get("Prevalence"), dict) else None,
            inheritance=inheritance,
            gene_symbols=gene_symbols,
            hpo_terms=hpo_terms,
            affected_tissues=_tissues_from_hpo(hpo_terms),
            # ← affected_tissues derived from HPO; empty here since API doesn't return HPO
        )
        return info

    except Exception:
        return _fallback_disease(orpha_num)  # ← any error (timeout, bad JSON, etc.) → use fallback


# ══════════════════════════════════════════════════════════════════════════════
# STATIC FALLBACK DATA
# All 5 target diseases (+ extras) hardcoded so tool works without internet.
# HPO terms here are manually curated → better tissue mapping than API version.
# ══════════════════════════════════════════════════════════════════════════════
_FALLBACK: dict[str, DiseaseInfo] = {}


def _build_fallbacks() -> None:
    global _FALLBACK
    _FALLBACK = {
        "70": DiseaseInfo(                             # ← SMA (positive control)
            orphanet_id="ORPHA:70", name="Spinal Muscular Atrophy",
            omim_ids=["253300"], prevalence="1-5/10000",
            inheritance=["Autosomal recessive"],
            gene_symbols=["SMN1", "SMN2"],
            hpo_terms=["Muscle weakness", "Spinal cord degeneration", "Motor neuron loss"],
            affected_tissues=["CNS", "muscle"],
        ),
        "306": DiseaseInfo(                            # ← Haemophilia B (positive control)
            orphanet_id="ORPHA:306", name="Hemophilia B",
            omim_ids=["306900"], prevalence="1-5/100000",
            inheritance=["X-linked recessive"],
            gene_symbols=["F9"],
            hpo_terms=["Prolonged bleeding", "Joint hemorrhage", "Liver coagulation"],
            affected_tissues=["liver"],
        ),
        "324": DiseaseInfo(                            # ← Fabry disease (novel result)
            orphanet_id="ORPHA:324", name="Fabry disease",
            omim_ids=["301500"], prevalence="1-5/10000",
            inheritance=["X-linked dominant"],
            gene_symbols=["GLA"],
            hpo_terms=["Neuropathic pain", "Cardiomyopathy", "Renal failure",
                       "Angiokeratoma", "Lysosomal storage"],
            affected_tissues=["liver", "kidney", "heart", "CNS"],
        ),
        "79269": DiseaseInfo(                          # ← Sanfilippo A (MPS IIIA)
            orphanet_id="ORPHA:79269", name="Mucopolysaccharidosis type IIIA (Sanfilippo A)",
            omim_ids=["252900"], prevalence="1-9/100000",
            inheritance=["Autosomal recessive"],
            gene_symbols=["SGSH"],
            hpo_terms=["Intellectual disability", "Neurodegeneration", "Brain atrophy",
                       "Lysosomal storage", "Behavioural problems"],
            affected_tissues=["CNS"],
        ),
        "1060": DiseaseInfo(                           # ← Crigler-Najjar type I (unmet need)
            orphanet_id="ORPHA:1060", name="Crigler-Najjar syndrome type I",
            omim_ids=["218800"], prevalence="<1/1000000",
            inheritance=["Autosomal recessive"],
            gene_symbols=["UGT1A1"],
            hpo_terms=["Jaundice", "Hepatic dysfunction", "Bilirubin encephalopathy",
                       "Liver enzyme deficiency"],
            affected_tissues=["liver"],
        ),
        "1946": DiseaseInfo(                           # ← Kohlschutter-Tonz syndrome (ROGDI gene)
            orphanet_id="ORPHA:1946",
            name="Kohlschutter-Tonz syndrome",
            omim_ids=["226750"],
            prevalence="<1/1000000",
            inheritance=["Autosomal recessive"],
            gene_symbols=["ROGDI"],
            hpo_terms=[
                "Amelogenesis imperfecta",     # ← abnormal tooth enamel development
                "Early-onset epilepsy",
                "Severe developmental delay",
                "Intellectual disability",
                "Spasticity",
                "Neurodegeneration",
            ],
            affected_tissues=["CNS"],
        ),
        "578": DiseaseInfo(                            # ← Mucolipidosis type IV
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
        "61": DiseaseInfo(                             # ← Alpha-mannosidosis
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
        "511": DiseaseInfo(                            # ← Maple syrup urine disease (MSUD)
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
        "309": DiseaseInfo(                            # ← Salla disease (lysosomal sialic acid transport)
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


_build_fallbacks()  # ← runs immediately when this file is imported; populates _FALLBACK dictionary


def _fallback_disease(orpha_num: str) -> Optional[DiseaseInfo]:
    return _FALLBACK.get(orpha_num)  # ← returns the hardcoded entry, or None if not in list


def cache_disease_to_db(conn, info: DiseaseInfo) -> None:
    """Persist a DiseaseInfo to the diseases table."""
    # ← saves disease info to SQLite database so it doesn't need refetching next run
    import json as _json
    conn.execute("""
        INSERT OR REPLACE INTO diseases
        (orphanet_id, name, omim_id, prevalence, inheritance,
         phenotype_terms)
        VALUES (?,?,?,?,?,?)
    """, (
        info.orphanet_id, info.name,
        info.omim_ids[0] if info.omim_ids else None,  # ← take only the first OMIM ID
        info.prevalence,
        info.inheritance[0] if info.inheritance else None,
        _json.dumps(info.hpo_terms),  # ← store list as JSON string in the database
    ))
    conn.commit()  # ← save changes to disk
