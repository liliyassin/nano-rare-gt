"""Curated molecular-mechanism evidence for disease/modality matching.

The key distinction is deliberate: inheritance can suggest loss of function,
but it is not proof. This module loads source-linked mechanism evidence and
returns an explicit "unknown" record when a disease/gene pair has not been
curated.

SCOPE LIMITATION: curated records cover only the 46-disease dissertation cohort
(data/disease_mechanisms_46.csv). Any disease/gene pair outside this cohort
returns evidence_status="missing" and gene_addition_compatibility="uncertain",
which causes dimension 6 (modality_compatibility) to score 1.0/2.0 rather than
2.0/2.0. This is intentional: better to under-score an uncurated disease than to
assume LOF compatibility without source-linked evidence.

To extend coverage: add a row to disease_mechanisms_46.csv with the Orphanet ID,
gene symbol, mechanism_category, mechanism_detail, gene_addition_compatibility
(compatible / conditional / uncertain / incompatible), preferred_modality,
evidence_level, evidence_summary, evidence_url, and evidence_citation.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "disease_mechanisms_46.csv"


@dataclass(frozen=True)
class MechanismEvidence:
    orphanet_id: str
    disease_name: str
    gene: str
    mechanism_category: str
    mechanism_detail: str
    gene_addition_compatibility: str
    preferred_modality: str
    evidence_level: str
    evidence_summary: str
    evidence_url: str
    evidence_citation: str
    evidence_status: str

    @property
    def is_curated(self) -> bool:
        return self.evidence_status != "missing"

    @property
    def short_label(self) -> str:
        category = self.mechanism_category.replace("_", " ")
        compatibility = self.gene_addition_compatibility.replace("_", " ")
        return f"{category}; gene addition {compatibility}"


def _normalise_orpha(orphanet_id: str) -> str:
    return orphanet_id.replace("ORPHA:", "").strip()


def _normalise_gene(gene: str | None) -> str:
    return (gene or "").strip().upper()


def _unknown_evidence(orphanet_id: str, gene: str | None) -> MechanismEvidence:
    gene_label = gene or "unknown"
    return MechanismEvidence(
        orphanet_id=orphanet_id,
        disease_name="unknown",
        gene=gene_label,
        mechanism_category="unknown",
        mechanism_detail="No curated molecular mechanism evidence is available for this disease/gene pair.",
        gene_addition_compatibility="uncertain",
        preferred_modality="manual_review_required",
        evidence_level="missing",
        evidence_summary=(
            "Do not infer mechanism from inheritance alone. Add a source-linked "
            "mechanism row before treating this as gene-addition compatible."
        ),
        evidence_url="",
        evidence_citation="not curated",
        evidence_status="missing",
    )


@lru_cache(maxsize=1)
def load_mechanism_evidence() -> dict[tuple[str, str], MechanismEvidence]:
    """Load curated disease/gene mechanism records keyed by ORPHA number and gene."""
    records: dict[tuple[str, str], MechanismEvidence] = {}
    if not DATA_PATH.exists():
        return records

    with DATA_PATH.open(newline="") as f:
        for row in csv.DictReader(f):
            evidence = MechanismEvidence(**row)
            key = (_normalise_orpha(evidence.orphanet_id), _normalise_gene(evidence.gene))
            records[key] = evidence
    return records


def lookup_mechanism(orphanet_id: str, gene: str | None) -> MechanismEvidence:
    """Return curated mechanism evidence for a disease/gene pair if available."""
    records = load_mechanism_evidence()
    orpha_key = _normalise_orpha(orphanet_id)
    gene_key = _normalise_gene(gene)

    if (orpha_key, gene_key) in records:
        return records[(orpha_key, gene_key)]

    # If the caller has no selected gene yet, fall back to the single curated
    # record for that ORPHA ID when one exists. Multi-gene diseases should still
    # be scored per gene using --gene or --all-genes.
    matches = [record for (oid, _), record in records.items() if oid == orpha_key]
    if not gene_key and len(matches) == 1:
        return matches[0]

    return _unknown_evidence(orphanet_id, gene)


def score_gene_addition_compatibility(evidence: MechanismEvidence) -> tuple[float, list[str]]:
    """Score whether the curated mechanism supports a gene-addition precedent.

    This score is modality-level: it does not decide whether a specific vector
    reaches the right tissue. That remains the tissue-tropism score.
    """
    compatibility = evidence.gene_addition_compatibility.lower()

    if compatibility == "compatible":
        score = 2.0
        label = "supports gene addition"
    elif compatibility == "conditional":
        score = 1.5
        label = "conditionally supports gene addition; review disease-specific constraints"
    elif compatibility == "uncertain":
        score = 1.0
        label = "uncertain for ordinary gene addition"
    elif compatibility == "incompatible":
        score = 0.0
        label = "not compatible with simple gene addition"
    else:
        score = 1.0
        label = "unrecognised compatibility label; manual review required"

    notes = [
        "Disease mechanism: "
        f"{evidence.mechanism_category.replace('_', ' ')} — {evidence.mechanism_detail}",
        f"Gene-addition modality compatibility: {label}",
        f"Mechanism evidence: {evidence.evidence_summary}",
    ]
    if evidence.evidence_url:
        notes.append(f"Mechanism source: {evidence.evidence_citation} ({evidence.evidence_url})")
    else:
        notes.append("Mechanism source: none curated")

    return score, notes
