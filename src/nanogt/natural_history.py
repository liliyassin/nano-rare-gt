"""Curated natural-history / therapeutic-window evidence for the cohort.

This module exists for the same reason as mechanism.py: a previously keyword-driven
score was producing clinically wrong values, so we replace it with curated,
source-linked, conservative-by-default data.

score_therapeutic_window() (scoring.py) consults this module FIRST and maps the
curated ``window_class`` to a 0–2 score. Diseases without a curated record fall back
to the legacy HPO-keyword heuristic and receive a review flag — better to flag an
uncurated disease than to assume a timing the keyword heuristic got wrong (it scored
PKU, the textbook wide-window disease, in the narrowest tier).

window_class vocabulary (mapped in scoring._WINDOW_CLASS_SCORES):
  wide        — adult/chronic onset, or effectively managed; broad timing latitude
  moderate    — childhood onset, progressive but screenable; early intervention helps
  narrow      — infantile/rapid onset; presymptomatic or very early dosing essential
  very_narrow — neonatal/congenital or rapidly fatal; in utero/immediate delivery

IMPORTANT: window_class assignments are curated from general clinical natural-history
knowledge and are marked ``curated_needs_review``. They MUST be verified against
disease-specific natural-history studies (and stratified by phenotype/subtype, e.g.
infantile vs late-onset Pompe) before use in clinical-development planning. Because
the therapeutic-window dimension contributes only to the disease-level tractability
score and NEVER to precedent ranking, an imperfect value cannot reorder precedents —
but it should still be confirmed before being reported as fact.

To extend coverage: add a row to data/disease_natural_history.csv with the Orphanet
ID, disease_name, onset_category, window_class, window_detail, evidence_summary,
evidence_url, evidence_citation, and evidence_status.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "disease_natural_history.csv"


@dataclass(frozen=True)
class NaturalHistory:
    orphanet_id: str
    disease_name: str
    onset_category: str
    window_class: str
    window_detail: str
    evidence_summary: str
    evidence_url: str
    evidence_citation: str
    evidence_status: str

    @property
    def is_curated(self) -> bool:
        return self.evidence_status not in ("", "missing")


def _normalise_orpha(orphanet_id: str) -> str:
    return orphanet_id.replace("ORPHA:", "").strip()


def _unknown(orphanet_id: str) -> NaturalHistory:
    return NaturalHistory(
        orphanet_id=orphanet_id,
        disease_name="unknown",
        onset_category="unknown",
        window_class="unknown",
        window_detail="No curated natural-history record for this disease.",
        evidence_summary=(
            "Therapeutic window falls back to the HPO-keyword heuristic. Verify the age "
            "of onset, progression rate, and reversibility against published natural history."
        ),
        evidence_url="",
        evidence_citation="not curated",
        evidence_status="missing",
    )


@lru_cache(maxsize=1)
def load_natural_history() -> dict[str, NaturalHistory]:
    """Load curated natural-history records keyed by ORPHA number."""
    records: dict[str, NaturalHistory] = {}
    if not DATA_PATH.exists():
        return records
    with DATA_PATH.open(newline="") as f:
        for row in csv.DictReader(f):
            nh = NaturalHistory(**row)
            records[_normalise_orpha(nh.orphanet_id)] = nh
    return records


def lookup_natural_history(orphanet_id: str) -> NaturalHistory:
    """Return curated natural-history evidence for a disease, or an 'unknown' record."""
    return load_natural_history().get(_normalise_orpha(orphanet_id), _unknown(orphanet_id))
