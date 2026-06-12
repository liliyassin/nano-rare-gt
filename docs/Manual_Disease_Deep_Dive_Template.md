# NanoGT Manual Scoring Sheet

> **How to use:** Fill in Parts A–C from Orphanet, OMIM, and UniProt. Then for each precedent program you want to evaluate, fill in Part D (one copy per program). Compare your scores to the code output.

---

## PART A — Disease Identity

| Field | Your Answer |
|---|---|
| Disease name | |
| Orphanet ID | ORPHA: |
| OMIM phenotype ID | |
| Prevalence | |
| **Inheritance** — circle one | AR / XL-recessive / XL-dominant / AD / Mitochondrial / Unknown |

**Source:** [orpha.net](https://www.orpha.net) → search disease name → Orphanet summary page

---

## PART B — Gene & Protein

| Field | Your Answer |
|---|---|
| Gene symbol | |
| CDS length (bp) | bp &nbsp;&nbsp; *(= amino acid length × 3)* |
| Amino acid (aa) length | aa |
| UniProt accession | |
| **Protein class** — circle one | Secreted / Lysosomal / Membrane / Intracellular |
| Subcellular location (from UniProt) | |
| Is secreted? | Y / N |
| UniProt keywords (paste relevant ones) | |
| GO terms (paste relevant ones) | |

**Source:** [uniprot.org](https://www.uniprot.org) → search gene symbol, filter Human (reviewed) → Subcellular location + Keywords + Sequences tab (length)

---

## PART C — Tissues, HPO & Onset

| Field | Your Answer |
|---|---|
| **Primary affected tissue(s)** — circle all that apply | Liver / CNS / Retina / Muscle / Haematopoietic / Heart / Kidney |
| Key HPO terms | |
| **Onset timing** — circle one | Congenital/neonatal / Early childhood / Childhood / Adolescent / Adult / Chronic-episodic |
| Progressive neurodegeneration? | Y / N |
| **Inferred pathway** — circle one | Lysosomal storage / Coagulation / Motor neuron / Myopathy / Retinal / Amino acid metabolism / Urea cycle / Mitochondrial / **Unknown** |

**Source:** Orphanet disease page → Clinical signs & phenotypes → HPO terms. Onset from OMIM clinical synopsis.

> **Note — which dimensions are fixed vs vary per program:**
> Dimensions 8, 9, 10, 11, 12 depend only on *your disease/gene* — score them once here.
> Dimensions 1, 2, 3, 4, 5, 6, 7 depend on the *precedent program* you are comparing against — fill in Part D once per program.

---

## PART C (continued) — Disease-Fixed Dimension Pre-scores

Fill these in once, before looking at any precedent program.

| Dim | Name | Max | Scoring Rule | **Your Score** |
|---|---|---|---|---|
| 8 | Therapeutic Window | 2.0 | Adult/chronic onset (not irreversible) → **2.0** · Progressive childhood (not neonatal) → **1.5** · Early childhood (not neonatal) → **1.2** · Neonatal → **0.8** · Congenital/rapidly fatal → **0.5** | /2.0 |
| 9 | Cross-Correction | 1.0 | Secreted lysosomal enzyme → **1.0** · Secreted protein → **1.0** · Non-secreted lysosomal → **0.8** · Intracellular or membrane-bound → **0.2** | /1.0 |
| 10 | Immune Privilege | 1.0 | Retina → **1.0** · CNS → **0.9** · Liver → **0.8** · Muscle/Heart → **0.6** · Kidney → **0.5** · Haematopoietic → **0.3** · (uses best tissue if multi-tissue) | /1.0 |
| 11 | Promoter Availability | 1.0 | Liver → **1.0** (ApoE/hAAT, TBG) · Retina → **1.0** (VMD2, GRK1) · CNS → **0.8** (Syn1, CaMKII) · Muscle → **0.8** (MHCK7) · Haem → **0.7** · Heart → **0.6** · Kidney → **0.4** | /1.0 |
| 12 | RoA Feasibility | 1.0 | Liver (IV) → **1.0** · Muscle (IV/IM) → **0.9** · Haem (ex vivo HSC) → **0.9** · Retina (subretinal/intravitreal) → **0.8** · CNS (intrathecal/ICV) → **0.7** · Heart → **0.6** · Kidney → **0.4** | /1.0 |

---

## PART D — Per-Program Scoring

*Duplicate this section for each precedent program you evaluate.*

**Precedent program name:** ___________________________

**Vector:** ___________ &nbsp;&nbsp; **Approval status:** ___________ &nbsp;&nbsp; **Disease it was designed for:** ___________________________

**Vector cargo limit (bp):** ___________ &nbsp;&nbsp; **Program CDS (bp):** ___________ &nbsp;&nbsp; **Program protein class:** ___________

**Program tissue target:** ___________ &nbsp;&nbsp; **Program inheritance:** AR / XL / Other &nbsp;&nbsp; **Program pathway:** ___________________________

---

| Dim | Name | Max | Scoring Rule | **Your Score** | Notes |
|---|---|---|---|---|---|
| 1 | Packaging Fit | 2.0 | *Your disease gene CDS ÷ vector cargo limit = utilisation %* · >100% → **FAIL (0.0)** stop here · ≤30% → **2.0** · 31–60% → **1.5** · 61–85% → **1.0** · 86–100% → **0.5** | /2.0 | _%_ utilisation |
| 2 | Tissue Tropism | 2.0 | Vector tropism **AND** program target both match disease tissue → **2.0** · Program target matches (or vector covers 2+ disease tissues) → **1.5** · Vector covers 1 disease tissue → **1.0** · No overlap → **0.3** · No tissue data → **1.0** | /2.0 | |
| 3 | Protein Class | 2.0 | Both lysosomal → **2.0** · Both secreted → **2.0** · Both intracellular → **1.5** · Both membrane → **1.5** · Partial extracellular component → **1.0** · Class mismatch → **0.5** | /2.0 | |
| 4 | Inheritance | 1.0 | Exact match (AR↔AR or XL↔XL) → **1.0** · Any LOF ↔ any LOF → **0.7** · Dominant or mito vs recessive → **0.3** · Unknown → **0.5** | /1.0 | |
| 5 | Pathway Similarity | 2.0 | Exact pathway match → **2.0** · Related pathway group → **1.5** · Different pathway → **0.5** · Unknown disease pathway → **1.0** (neutral) · Groups: lysosomal_storage · coagulation · motor_neuron~myopathy · retinal · amino_acid~urea_cycle · mitochondrial | /2.0 | |
| 6 | Approval Weight | 1.0 | Approved → **1.0** · Phase 3 → **0.8** · Phase 2/3 or Withdrawn → **0.7** · Phase 2 → **0.6** · Phase 1/2 → **0.5** · Phase 1 → **0.4** | /1.0 | |
| 7 | Immunogenicity | 2.0 | Seroprevalence of **vector**: <10% → **2.0** · 10–19% → **1.5** · 20–39% → **1.0** · ≥40% → **0.5** · AAV2=55% · AAV8=30% · AAV9=22% · AAV1=20% · AAV2/6=17% · AAVrh10=10% · AAV5=9% · LV=2% | /2.0 | |
| 8 | Therapeutic Window | 2.0 | *(Copy from Part C)* | /2.0 | |
| 9 | Cross-Correction | 1.0 | *(Copy from Part C)* | /1.0 | |
| 10 | Immune Privilege | 1.0 | *(Copy from Part C)* | /1.0 | |
| 11 | Promoter Availability | 1.0 | *(Copy from Part C)* | /1.0 | |
| 12 | RoA Feasibility | 1.0 | *(Copy from Part C)* | /1.0 | |

---

### Score Calculation

| | |
|---|---|
| **Raw total** (sum dims 1–12) | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 18.0 |
| **Composite score** (raw ÷ 18 × 10) | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 10.0 |
| **Confidence** — circle one | High (≥7.5) / Medium (5.0–7.4) / Low (<5.0) / FAIL (pkg=0) |

---

### My Interpretation

What surprised me about this score? What dimension drove it highest / lowest?

```
_______________________________________________________________________________

_______________________________________________________________________________
```

Does the code output match? If not, which dimension differs and why?

```
_______________________________________________________________________________

_______________________________________________________________________________
```
