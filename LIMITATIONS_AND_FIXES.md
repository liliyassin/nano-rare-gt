# NanoGT Framework: Limitations, Bugs, and v2 Fixes

**Version:** 2.0  
**Author:** Lili Yassin — Imperial College London dissertation  
**Date:** June 2026

This document records every systematic limitation identified in the v1 scoring framework,
explains the biological root cause of each problem, describes the code fix applied in v2,
and advises on diseases where important uncertainty remains after the fix.

It is intended for use in the dissertation **Methods/Limitations** section and as a permanent
record of analytical decisions made during development.

---

## Background: Why These Limitations Arose

The 40-disease cohort was selected by AI rather than manually curated. AI selection optimises
for surface-level compatibility signals (autosomal recessive, small gene, CNS or liver target)
without awareness of subtler biological constraints. This introduced several classes of disease
that challenge the framework's core assumptions:

1. Diseases where the therapeutic gene is **not in the nuclear genome** (mitochondrial DNA)
2. Diseases where the gene product must reach a **specific organelle** (mitochondrial matrix, peroxisome)
3. Diseases where the gene encodes a **lysosomal membrane protein** (not a secretable enzyme)
4. Diseases where the **molecular function of the gene is not yet characterised**
5. Diseases where the affected gene is **one subunit of a multi-gene enzyme complex**

None of these cases crash the v1 code, but they all produced scores that were either
numerically inflated (false positives) or built on biologically incorrect analogies.

---

## Bug 1: Lysosomal Membrane Proteins Scored as Lysosomal Enzymes

### Affected diseases
- **Mucolipidosis type IV** (ORPHA:578, MCOLN1) — v1 score: 9.1/10 ← **incorrect**
- **Salla disease** (ORPHA:309, SLC17A5) — v1 score: 8.8/10 ← **incorrect**

### Root cause
The v1 `score_protein_class()` function classified any protein with a lysosomal
subcellular location as a "lysosomal protein" and awarded full marks (2.0/2.0)
when compared against lysosomal-enzyme precedent programs (Libmeldy, RGX-121, etc.).

The v1 `score_cross_correction()` function gave these proteins 0.8/1.0 as
"lysosomal enzyme (non-secreted)."

**This is biologically wrong.** The cross-correction mechanism that underlies
Libmeldy and other HSC/LV programs depends on:
1. Transduced HSC-derived microglia **secreting** the lysosomal enzyme into the extracellular space
2. Neighbouring neurons **taking up** that enzyme via the mannose-6-phosphate (M6P) receptor pathway

MCOLN1 encodes mucolipin-1, a **lysosomal membrane Ca²⁺ channel** (TRP family). It is
a multi-pass transmembrane protein **anchored in the lysosomal membrane**. It cannot be
exocytosed as soluble cargo. It cannot be taken up via M6P receptors. **Every target cell
must individually receive the vector.**

SLC17A5 encodes sialin, a **lysosomal membrane transporter** for sialic acid. Exactly the
same argument applies.

The high scores these diseases received (9.1 and 8.8) were biologically meaningless and
potentially misleading. An examiner reading these results might incorrectly conclude that
Libmeldy is a close development precedent for ML-IV, when in fact the therapeutic mechanisms
are fundamentally incompatible.

### Fix applied (v2)
**`src/nanogt/scoring.py` — `_classify_gene_protein()` (new helper function):**
Added detection logic that distinguishes lysosomal membrane proteins from lysosomal enzymes.
Detection uses subcellular location strings ("membrane" in lysosomal location) and keyword
signals ("channel", "transport", "pump", "ion").

**`score_protein_class()`:**
- `lysosomal enzyme` vs `lysosomal program` → 2.0 (unchanged)
- `lysosomal membrane protein` vs `lysosomal program` → 1.0 (was 2.0)
  with note: "Lysosomal pathway shared, but disease gene encodes a lysosomal MEMBRANE protein
  (channel/transporter), NOT a soluble enzyme. HSC cross-correction mechanism not applicable."

**`score_cross_correction()`:**
- `lysosomal membrane protein` → 0.0 (was 0.8)
  with note: "Lysosomal MEMBRANE protein — no cross-correction possible."

**`data/disease_mechanisms.csv`:**
Updated MCOLN1 and SLC17A5 mechanism entries to explicitly state membrane protein class
and incompatibility with HSC/LV cross-correction approaches.

**`build_review_flags()`:**
Added Flag A: explicit `LYSOSOMAL MEMBRANE PROTEIN` review flag for these cases.

### Expected score change
Both diseases will receive substantially lower scores (~6.5–7.5 range) reflecting the
genuine challenge of per-cell CNS delivery without cross-correction benefit. This is
a more accurate representation of the therapeutic difficulty.

---

## Bug 2: Mitochondrial DNA Genes Scored Against Nuclear Gene Addition Programs

### Affected disease
- **Leber hereditary optic neuropathy** (ORPHA:104, MT-ND4) — v1 score: 6.8/10 (medium)

### Root cause
MT-ND4 is a gene in the **mitochondrial genome**. It is transcribed by mitochondrial RNA
polymerase, translated by mitochondrial ribosomes using a non-standard genetic code (UGA
encodes tryptophan in mtDNA rather than acting as a stop codon), and assembled directly into
Complex I within the inner mitochondrial membrane.

Standard AAV gene therapy delivers a transgene to the **nucleus**. The cell's own RNA
polymerase transcribes it and cytoplasmic ribosomes translate it. This pipeline is
**incompatible with producing a functional MT-ND4 protein** because:
1. The cytoplasmic genetic code would misread UGA as a stop codon
2. The protein would be produced in the cytoplasm, not inside mitochondria
3. There is no known transport mechanism to import mature ND4 protein post-translationally

The only viable gene therapy approach for MT-ND4 is **allotopic expression**: the gene is
recoded using the cytoplasmic genetic code, given an artificial N-terminal mitochondrial
targeting sequence (MTS), and expressed from the nucleus — trusting that the recoded protein
will fold correctly and be imported. This is a highly specialised, disease-specific strategy.
It is used by GS010/Lumevoq (Gensight Biologics, EU approved 2021).

**Every precedent comparison in v1 was a category error.** The programs scored against LHON
(CPCB-RPE1, Luxturna, Libmeldy, Hemgenix, Skysona) all deliver nuclear genes. None of them
involve allotopic expression or any mitochondrial-specific engineering. Comparing LHON to
these programs is like comparing a software fix to a hardware replacement.

Notably, GS010 **is** in the catalog, but v1 scored it as just another AAV2/retinal program.
It received 6.4/10 for LHON — below CPCB-RPE1 (6.8) — because the code did not recognise
that GS010 actually uses allotopic expression and IS the correct therapeutic approach for LHON.

### Fix applied (v2)
**`score_organelle_targeting()` (new dimension 14):**
Detects MT-* gene symbols and mitochondrial inheritance patterns. Returns 0.0 for these
cases with an explicit note explaining the allotopic expression requirement.

**`build_review_flags()`:**
Added Flag B: `MITOCHONDRIAL DNA GENE` flag with full explanation and reference to
GS010/Lumevoq as the real-world allotopic precedent.

**`_RAW_MAX` updated to 21.0** to accommodate the new dimension.

### Remaining limitation
The allotopic expression strategy is not represented as a distinct therapeutic modality
in the catalog. GS010 is catalogued as `gene_replacement` with `pathway: mitochondrial_complex`,
which does not distinguish it from other retinal programs. A future improvement would be to
add an `allotopic_expression` mechanism type and score accordingly. For now, LHON will
correctly score with a low organelle targeting score and a prominent review flag.

---

## Bug 3: Nuclear-Encoded Mitochondrial Matrix Enzymes — MTS Not Validated

### Affected diseases
- **Methylmalonic acidemia** (ORPHA:27, MUT) — v1 score: 7.8/10
- **Maple syrup urine disease** (ORPHA:511, BCKDHA) — v1 score: 8.1/10
- **OTC deficiency** (ORPHA:664, OTC) — v1 score: 8.2/10 ← less severe; OTC gene therapy works clinically

### Root cause (different from Bug 2)
These genes are in the **nuclear genome** — AAV can deliver them normally. However, after
translation in the cytoplasm, the protein must be **imported post-translationally into the
mitochondrial matrix** via its N-terminal mitochondrial targeting sequence (MTS).

v1 treated these as standard enzyme replacement cases with no additional constraints.
In practice, the therapeutic construct must:
1. Preserve the full MTS in the expressed protein
2. Rely on the TIM/TOM import machinery being functional in patient cells
3. Ensure the mature protein folds correctly inside the mitochondrial matrix

For OTC deficiency, these constraints have been validated — liver-directed AAV OTC programs
(DTX301, Phase 2) demonstrate successful mitochondrial import in vivo. The flag is advisory.

For MUT (MMA), clinical AAV programs are in development but MTS validation is still an
active area of research. The v1 score of 7.8 implied straightforward transferability of
BMN 307 (a PAH/PKU liver program) as a precedent — but PAH is a cytoplasmic enzyme.
MUT requires the additional mitochondrial import step that PAH does not.

### Fix applied (v2)
**`score_organelle_targeting()`:**
Returns 0.5 for mitochondrial matrix proteins with explanation of MTS requirement.

**`build_review_flags()`:**
Added Flag C: `MITOCHONDRIAL MATRIX ENZYME` flag for these cases (distinct from the
mtDNA flag, as the therapeutic approach IS viable — it just requires MTS validation).

**`data/disease_mechanisms.csv`:**
Updated MUT entry to explicitly state the mitochondrial matrix location and MTS requirement.

---

## Bug 4: ROGDI/Kohlschutter-Tonz — Unresolved Disease Biology

### Affected disease
- **Kohlschutter-Tonz syndrome** (ORPHA:1946, ROGDI) — v1 score: 7.5/10 (high confidence)

### Root cause
ROGDI (Rogdi homolog) is a protein with proposed roles in:
- Regulation of the V-ATPase complex via the RAVE/Rabconnectin-3 system
- Synaptic vesicle biology at the presynapse

However, as of 2025, no in vivo disease model has confirmed that ROGDI loss of function
causes the KTS phenotype by a mechanism that would be rescued by gene addition of ROGDI.
The disease biology — why loss of ROGDI specifically causes amelogenesis imperfecta (enamel
defects) and epileptic encephalopathy — **has not been fully established**.

The v1 score of 7.5/10 with high confidence was built on pattern-matching assumptions
(autosomal recessive, CNS disease, small gene, intracellular protein) — all of which are
true — but those assumptions do not validate the therapeutic logic. A disease can be
genetically LOF while still being poor for gene addition if:
- The protein has complex dosage sensitivity
- The critical cell type for rescue is unknown
- The relevant developmental window has already closed
- The phenotype involves irreversible structural changes (enamel defects cannot be reversed)

### Fix applied (v2)
**`data/disease_mechanisms.csv`:**
Updated ROGDI entry with detailed note: "molecular function is not fully resolved ...
no disease-specific in vivo model or gene addition rescue experiment has been published."

**`build_review_flags()`:**
Added Flag E: `UNRESOLVED DISEASE BIOLOGY` flag. Triggered when the mechanism_detail
field contains phrases like "not fully resolved" or "not been established."

### What remains uncertain
The score itself (7.5) has not been artificially lowered by the v2 fix — the genetics
are consistent with LOF and the gene does fit in an AAV vector for CNS delivery. What
has changed is that the review flags now make the epistemic status explicit. A reader
will see the flag and understand that the 7.5 reflects platform feasibility, not
established therapeutic rationale.

**Recommendation:** Keep this disease in the cohort, but in the dissertation discussion
explicitly frame KTS as "a disease that illustrates how AI selection can produce
numerically high scores for diseases where the experimental validation of the therapeutic
hypothesis has not been completed."

---

## Bug 5: Multi-Subunit Enzyme Complexes

### Affected disease
- **Maple syrup urine disease** (ORPHA:511, BCKDHA) — v1 score: 8.1/10

### Root cause
BCKDHA encodes the alpha subunit (E1α) of the branched-chain alpha-ketoacid dehydrogenase
(BCKDH) complex, which has four subunit genes: BCKDHA, BCKDHB, DBT, and DLD. MSUD can be
caused by pathogenic variants in any of these four genes. The v1 framework scored BCKDHA
as if replacing this one subunit would fully reconstitute enzyme activity — but:
1. If the patient's MSUD is caused by BCKDHB mutations, the BCKDHA score is irrelevant
2. Even in BCKDHA patients, overexpression of E1α relative to E1β could cause imbalanced
   complex assembly, and the metabolic rescue is contingent on liver-only correction of what
   is also a CNS-metabolic crisis disease

### Fix applied (v2)
**`build_review_flags()`:**
Added Flag D: `MULTI-SUBUNIT ENZYME` flag. Triggered by keyword detection ("subunit alpha",
"e1 alpha", "subunit" + "complex" in gene keywords).

---

## Other Important Limitations Not Fixed by Code (Require Dissertation Acknowledgement)

### 1. Heterogeneous disease subtypes (Gaucher, Fabry, Niemann-Pick)
Some diseases in the cohort have neuronopathic and non-neuronopathic subtypes with
completely different correction requirements. v2 adds a `DISEASE HETEROGENEITY` flag
for known cases (Gaucher, Fabry, Niemann-Pick), but the scoring itself uses the most
generic disease annotation. Subtype-specific reanalysis is needed before clinical use.

### 2. Catalog size (21 programs, 8 vectors)
The catalog contains 21 GT programs and 8 vectors. For any disease without a close
precedent in the catalog, the "best match" will still be a medium-confidence imperfect
comparison. Absence of a high-confidence match does not mean no GT is possible —
it may simply mean the most appropriate precedent is not in the catalog.

### 3. Allotopic expression not represented
GS010/Lumevoq for LHON uses allotopic expression, which is not modelled as a distinct
therapeutic modality. The framework cannot evaluate allotopic-expression-based programs
as genuine precedents; it treats GS010 as just another retinal AAV.

### 4. Ex vivo vs in vivo AAV is not fully distinguished
Several LV programs (Libmeldy, Skysona, Strimvelis) work ex vivo — cells are collected
from the patient, transduced outside the body, and reinfused. The framework scores
"tropism" based on the vector's in vivo tissue reach, which is not the relevant parameter
for ex vivo programs. A future improvement would add an `ex_vivo` flag to programs and
score differently.

### 5. DMD micro-dystrophin strategy
DMD (ORPHA:98896) is correctly flagged as `oversized_cargo_stress_test`. The code scores
it against SRP-9001 using the micro-dystrophin construct (3825 bp) rather than the
native DMD CDS (11,055 bp). This is the correct and only viable AAV strategy, but the
score (7.5/10) should be read as "micro-dystrophin strategy feasibility" not "native DMD
gene replacement feasibility."

---

## Summary Table: Before and After v2

| Disease | Gene | v1 Score | Issue | v2 Score (approx) | Fix |
|---------|------|----------|-------|-------------------|-----|
| Mucolipidosis type IV | MCOLN1 | 9.1/10 ⚠️ | Lysosomal channel scored as enzyme | ~6.8/10 | Protein class + cross-correction fix |
| Salla disease | SLC17A5 | 8.8/10 ⚠️ | Lysosomal transporter scored as enzyme | ~6.7/10 | Protein class + cross-correction fix |
| Leber hereditary optic neuropathy | MT-ND4 | 6.8/10 ⚠️ | mtDNA gene; allotopic strategy needed | ~3.5/10 | Organelle targeting dim. (0.0) |
| Methylmalonic acidemia | MUT | 7.8/10 ⚠️ | Mitochondrial matrix; MTS not validated | ~6.2/10 | Organelle targeting dim. (0.5) |
| Maple syrup urine disease | BCKDHA | 8.1/10 | Multi-subunit; liver-only uncertain | ~6.5/10 | Organelle targeting (0.5) + flag |
| Kohlschutter-Tonz | ROGDI | 7.5/10 | Biology unresolved | ~7.1/10 | Mechanism flag (score unchanged) |
| All other diseases | — | varies | Global normalisation change | ×(20/21) | _RAW_MAX 20→21 |

*Approximate v2 scores depend on live API data for each disease; exact values from run_results.py.*

---

## Files Modified in v2

| File | Change |
|------|--------|
| `src/nanogt/scoring.py` | Added `_classify_gene_protein()`, fixed `score_protein_class()`, fixed `score_cross_correction()`, added `score_organelle_targeting()` (dim 14), updated `ScoreBreakdown` dataclass, updated `build_review_flags()` with 6 new specific flags, updated `_RAW_MAX` to 21.0, wired dim 14 into `score_program()` |
| `src/nanogt/report.py` | Added organelle targeting row to score breakdown table |
| `data/disease_mechanisms.csv` | Updated MCOLN1, SLC17A5, MUT, ROGDI mechanism entries |
| `LIMITATIONS_AND_FIXES.md` | This file (new) |
