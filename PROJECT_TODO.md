# NanoGT Dissertation — Master To-Do List
*Generated from supervisor meeting 2026-06-22. Next meeting: Wednesday 2026-06-24 at 09:30.*

---

## 🔴 BEFORE WEDNESDAY (due 2026-06-24, 09:30)

- [ ] **Draw the decision flowchart** — literal diagram (paper or digital, e.g. Miro / draw.io / Figma). Nodes:
  1. Is it a loss-of-function disease?
  2. Is the gene ≤ ~4.7 kb (fits standard AAV)?
  3. If gene is too large — is a mini/micro-gene or split-AAV strategy feasible?
  4. Is the primary affected cell type known?
  5. Is that cell type accessible (CNS barrier, post-mitotic, etc.)?
  6. Does an AAV serotype with tropism for that tissue exist?
  7. Are there other biological barriers (immune privilege, dominant-negative mechanism, mosaic expression needs, etc.)?
  8. If all biology is OK — is a clinical trial already running?
  9. If no trial — is the reason economic/prevalence, or unknown?
- [ ] **Run your existing 5 diseases through the flowchart** and note where each one stops (or passes all the way through)
- [ ] **Write a 1-paragraph summary** of where each disease sits in the flowchart to bring to the meeting

---

## 🟠 DATASET EXPANSION

- [ ] **Identify the full universe of loss-of-function rare diseases**
  - Query Orphanet for diseases with LoF mechanism annotation (ORPHA disorder classification)
  - Cross-reference with OMIM (inheritance = AR/XL/AD-haploinsufficiency + LoF molecular mechanism)
  - Target: find every rare monogenic LoF disease with a named causative gene — aim for a curated list of **200+ diseases** (supervisor said "hundreds"; go to 200 minimum)
- [ ] **For each disease, record:**
  - ORPHA ID, OMIM ID
  - Gene name + Ensembl/UniProt ID
  - Inheritance pattern
  - Causative mechanism (LoF confirmed / LoF suspected / unknown / gain-of-function)
  - CDS length in kb (to test AAV fit)
  - Primary affected tissue(s)
  - Prevalence / number of patients worldwide
  - Whether a GT clinical trial exists (ClinicalTrials.gov NCT number)
  - If trial exists — phase, sponsor, vector used
- [ ] **Flag and separately document diseases that are NOT loss-of-function** — don't just delete them; record *why* they're excluded and what mechanism they do have (this strengthens the thesis narrative)
- [ ] **Verify your 5 existing diseases against the flowchart** as positive/negative controls

---

## 🟡 ALGORITHM / CODE

- [ ] **Encode the flowchart as a Python function** — `flowchart(disease_id) → FlowchartResult` that returns which node the disease fails at and why
- [ ] **Add gene size check to the pipeline**
  - Pull CDS length from Ensembl REST API or NCBI gene summary
  - Flag genes > 4.7 kb as "oversized for standard AAV"
  - Add a secondary field: "split-AAV or micro-gene strategy documented in literature? Y/N"
- [ ] **Add tissue accessibility classification**
  - For each primary tissue, encode accessibility tier: easy (liver, muscle), moderate (lung, eye, CNS via intrathecal), hard (CNS parenchyma systemic, bone marrow)
  - Map against known AAV serotype tropisms
- [ ] **Add AAV serotype lookup**
  - Expand the 8-vector catalog to cover all major serotypes (AAV1–AAV9, AAVrh10, AAV-PHP.B, AAV-PHP.eB, AAVAnc80, etc.) with their tropism profiles
  - Build a `tissue → best_serotypes[]` lookup
- [ ] **Add prevalence field**
  - Pull from Orphanet prevalence data
  - Flag diseases with < 1:1,000,000 prevalence as "ultra-rare / economic barrier likely"
- [ ] **Automate batch flowchart scoring** — `nanogt flowchart --batch diseases.csv` that runs all diseases through the decision tree and outputs a summary table
- [ ] **Validate on positive controls** — all diseases with approved GT therapies should pass all biological filters; document any that don't and explain why
- [ ] **Add a "gap" flag** — diseases that pass all biological filters but have no clinical trial → output as the key "gap list"

---

## 🟢 ANALYSIS

- [ ] **Compute the headline statistics for the thesis:**
  - Total rare LoF diseases identified (n = ?)
  - Of those: % with approved GT therapies
  - Of those: % with active/completed clinical trials (but not yet approved)
  - Of those: % with no trial at all
  - Of the "no trial" group: % that pass all biological filters → the gap
  - Of the "no trial" group: % that fail at gene size, tissue accessibility, biology, etc.
- [ ] **For every disease in your dataset with no existing trial:**
  - Run through the flowchart
  - If it passes all filters → write a 1–2 sentence "what the therapy would look like" proposal
  - If it fails a filter → document exactly which node and why
- [ ] **For diseases that fail gene-size filter:**
  - Document whether mini-gene / split-AAV / base editing / prime editing workarounds are theoretically applicable
  - Aim to cover at least 20 such diseases
- [ ] **For diseases that fail tissue-accessibility filter:**
  - Document whether route-of-administration innovations could overcome it (intrathecal, subretinal, direct injection, etc.)
- [ ] **Prevalence analysis:**
  - Plot number of patients worldwide vs. whether a GT trial exists
  - Test the hypothesis that low prevalence = no trial (Lili's instinct from seeing the data)
  - Quantify: what is the apparent "economic threshold" below which no trials are attempted?
- [ ] **Compare your gap diseases against orphan drug designations** — do they have orphan status? If not, flag that as an additional barrier
- [ ] **Literature check for each gap disease** — is anyone publishing preclinical work even if no trial exists? (PubMed search: gene name + "gene therapy" OR "AAV")

---

## 🔵 THESIS WRITING

- [ ] **Introduction:** Frame the core question — "sequence a genome → output a treatment; are we there yet?"
- [ ] **Methods section:**
  - Describe how the LoF disease list was compiled (sources, inclusion/exclusion criteria)
  - Describe the flowchart decision nodes and how each was operationalised
  - Describe the scoring algorithm (existing 6-dimension scorer) and how it maps onto flowchart nodes
  - Describe data sources: Orphanet, OMIM, UniProt, ClinicalTrials.gov, Ensembl
- [ ] **Results section:**
  - Section 1: Scope of LoF rare diseases (the numbers)
  - Section 2: Current state of GT trials coverage
  - Section 3: Flowchart analysis — where diseases fail and why
  - Section 4: The gap list — diseases with no biological barrier and no trial
  - Section 5: Validation — do positive-control diseases pass all flowchart filters?
- [ ] **Discussion:**
  - Biological barriers vs. economic/organisational barriers
  - What would it actually take to start a trial for a gap disease tomorrow?
  - Limitations of the analysis (data completeness, LoF annotation certainty)
  - Future directions: automation, LLM-assisted annotation, registry integration
- [ ] **Conclusion:** Restate the key finding — X diseases identified as biologically tractable but not being pursued; primary bottleneck is Y

---

## ⚪ VALIDATION & QUALITY CONTROL

- [ ] **Check that all LoF annotations are evidence-backed** — don't rely on single sources; cross-reference OMIM + Orphanet + at least one primary paper per disease
- [ ] **Re-run your existing 5 scored diseases through the new flowchart** to confirm consistency between old scoring and new framework
- [ ] **Have someone else (e.g. a labmate) try to run 3 diseases through the flowchart** — if they get the same answer as you, the flowchart is unambiguous enough
- [ ] **Sense-check your prevalence data** — Orphanet prevalence estimates can be outdated; cross-check against patient registries or recent epidemiology papers for your top gap diseases
- [ ] **Run the algorithm on at least 5 diseases where therapy exists but your algorithm wouldn't have predicted it** — document the discrepancy; these are interesting edge cases

---

## 📅 MILESTONES

| Date | Deliverable |
|------|-------------|
| 2026-06-24 (Wed 09:30) | Flowchart drawn; 5 diseases run through it; meeting with supervisor |
| ~2026-06-28 | LoF disease list compiled (target: 200+ diseases) |
| ~2026-07-05 | All diseases run through flowchart algorithmically; gap list identified |
| ~2026-07-12 | Gap disease proposals written; prevalence analysis done |
| ~2026-07-19 | Full results section drafted |
| ~2026-07-26 | Full thesis draft complete |

---

## 💡 AMBITIOUS EXTENSIONS (do these if time allows)

- [ ] **Build a web-facing version of the flowchart tool** so clinicians/researchers can input a disease and get an instant assessment
- [ ] **Cross-reference gap diseases against existing AAV manufacturing capacity** — some gaps may be manufacturing/CMC, not biology
- [ ] **Check whether gap diseases have patient advocacy groups** — these often drive trial initiation; their absence is itself a barrier
- [ ] **Quantify the "LoF certainty" spectrum** — diseases where LoF is definitively proven vs. inferred vs. unknown; your supervisor specifically asked about this
- [ ] **Add a "competitive landscape" column** — for each gap disease, are any biotech/pharma companies working in the space even without a registered trial?
- [ ] **Run a sensitivity analysis** — how does the gap list change if you relax the gene-size threshold from 4.7 kb to 6 kb (split-AAV) or 9 kb (large-capacity vectors)?
