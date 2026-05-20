# Day 1 — Deep ROGDI Case Study + First Usable Output

**Goal:** Produce a publication-quality "Standardised Gene Therapy Protocol" for ROGDI / Kohlschütter-Tönz syndrome that serves as the framework's primary illustrative case study.

**Principle:** Depth over speed. Every claim must be traceable to a source. Every recommendation must justify why.

---

## Task 1: Understand the Existing Codebase (45 min)

- [ ] Read and annotate `src/nanogt/models.py` — understand the data model
- [ ] Read and annotate `src/nanogt/db.py` — understand how data flows into SQLite
- [ ] Read and annotate `src/nanogt/cli.py` — understand the CLI interface
- [ ] Read and annotate `src/nanogt/schema.sql` — understand the relational model
- [ ] Run `pytest` to confirm current tests pass
- [ ] Identify: what is the smallest change needed to produce a real report file?

**Deliverable:** Mental map of the codebase + gap analysis.

---

## Task 2: Deepen the ROGDI Knowledge Base (2 hours)

- [ ] Query UniProt by gene symbol (`gene:ROGDI AND organism_id:9606`) and verify Q9GZN7 programmatically — fetch full JSON, extract accession, protein name, gene name, sequence length, mass, PDB, InterPro, and Pfam fields
- [ ] Query OMIM 614574 (ROGDI gene) and OMIM 226750 (KTS phenotype)
- [ ] Research Kohlschütter-Tönz syndrome in depth:
  - [ ] Natural history and clinical course
  - [ ] Known pathophysiology: ROGDI loss/disruption → Rabconnectin-3 / V-ATPase-linked intracellular dysfunction → neuronal/endosomal/lysosomal or synaptic-vesicle biology → epilepsy/neurodevelopmental disease, plus enamel-development effects
  - [ ] All affected tissues: brain, teeth, kidney, retina?
  - [ ] Age of onset, progression, life expectancy
  - [ ] Current standard of care (none? supportive only?)
  - [ ] Why no gene therapy exists yet (what are the barriers?)
- [ ] Research ROGDI protein function:
  - [ ] Non-secreted intracellular scaffold/adaptor-like ROGDI/RAVE2 protein — do not treat it as a catalytic purine-metabolism protein
  - [ ] Why intracellular/cytosolic localization matters for GT
  - [ ] Presynaptic terminal localization — why this matters for CNS rescue
  - [ ] Overexpression risk: stoichiometry, mislocalization, and disrupted protein-complex assembly
- [ ] Research AAV delivery to ROGDI-relevant tissues:
  - [ ] CNS: AAV9 IV vs. ICV vs. intrathecal — use CNS-relevant precedent such as systemic AAV9 in SMA/Zolgensma and intrathecal CNS programs, not retinal-disease precedent as the main analogy
  - [ ] Dental/ameloblasts: has any AAV ever targeted enamel organ, and is the developmental timing realistic?
  - [ ] Kidney: assess whether renal involvement is consistent enough to justify a delivery endpoint; do not assume renal targeting is primary
- [ ] Structural homology search — what proteins/complexes are closest to corrected ROGDI biology?
  - [ ] ROGDI/RAVE2-like domain proteins and Rabconnectin-3 / V-ATPase-associated components
  - [ ] PDB 5XQH and 5XQI structural features and whether Foldseek finds meaningful non-enzyme structural neighbors
  - [ ] Non-catalytic GT precedent programs for scaffold/structural intracellular proteins, rather than forcing unrelated purine-metabolism surrogates

**Deliverable:** A comprehensive ROGDI knowledge document (`docs/ROGDI-deep-dive.md`) with citations, sufficient for a supervisor review.

---

## Task 3: Build the Report Template System (1 hour)

- [ ] Create `src/nanogt/templates/` directory
- [ ] Build base Markdown Jinja2 template (`base_report.md.j2`)
- [ ] Build ROGDI-specific section templates:
  - [ ] Disease overview section
  - [ ] Gene/protein analysis section
  - [ ] Vector assessment section
  - [ ] Therapeutic window / risk analysis section
  - [ ] Regulatory precedent section
  - [ ] Risk mitigation section
- [ ] Create `src/nanogt/report.py` — Jinja2 renderer that takes a `Report` model and writes Markdown
- [ ] Write unit tests for template rendering

**Deliverable:** A template system ready to produce structured reports.

---

## Task 4: Create the ROGDI Standardised Gene Therapy Protocol (2 hours)

- [ ] Draft the protocol using the template system
- [ ] Sections to include:
  1. **Indication Summary** — disease, prevalence, unmet need
  2. **Target Biology** — ROGDI gene, protein function, affected cell types
  3. **Therapeutic Rationale** — why GT is appropriate (AR, LoF-compatible, very small gene) and why it is hard (intracellular/non-secreted ROGDI means low cross-correction; direct transduction likely needed)
  4. **Vector Selection** — recommended serotype(s) with justification
  5. **Promoter Design** — tissue-specific vs. ubiquitous, why hSYN1 or CamKIIα or other
  6. **Delivery Route** — systemic IV vs. CNS-directed, age at dosing
  7. **Preclinical Milestones** — iPSC model, rodent KO, NHP (if needed)
  8. **CMC Strategy** — AAV manufacturing, plasmid design, cargo verification
  9. **Regulatory Pathway** — IND vs. RMAT, orphan drug designation eligibility
  10. **Risk Assessment** — immunogenicity, overexpression, delivery paradox (brain vs. teeth)
  11. **Surrogate Precedent Mapping** — closest approved/late-stage GT programs (even if for different genes)
  12. **Go/No-Go Decision Framework** — what data is needed to proceed to IND-enabling studies
- [ ] Include a **"Framework Scoring Breakdown"** section showing how the 9 dimensions apply to ROGDI
- [ ] Include **citations** for every major claim

**Deliverable:** A standalone Markdown document at `reports/ROGDI_Standardised_Gene_Therapy_Protocol.md`

---

## Task 5: Make It Usable from the CLI (30 min)

- [ ] Wire `report.py` into `cli.py` so `nanogt match --disease ORPHA:1946 --output rogdi_report.md` works
- [ ] The command should:
  1. Load the deep ROGDI data (from fixture + live APIs if available)
  2. Render the report through the template system
  3. Write a real Markdown file to disk
- [ ] Verify the output file opens cleanly in a Markdown viewer
- [ ] Add a `--deep-dive` flag that triggers the full protocol generation

**Deliverable:** A working CLI that produces a real file.

---

## Task 6: Review and Refine (30 min)

- [ ] Read the generated protocol aloud — does it make sense to a non-expert?
- [ ] Check for internal consistency (does vector choice match tissue targets?)
- [ ] Verify all numerical claims against sources
- [ ] Run `pytest` again — nothing broken
- [ ] Commit the report and all code changes

**Deliverable:** Clean git commit with Day 1 work.

---

## SUCCESS CRITERIA FOR DAY 1

At the end of today, a supervisor should be able to:

1. Run `nanogt match --disease ORPHA:1946 --output rogdi_report.md` and get a **real file**
2. Open that file and read a **comprehensive, citation-backed Standardised Gene Therapy Protocol** for ROGDI
3. See how every section maps to the framework's 9 scoring dimensions
4. Understand why ROGDI is a compelling (but challenging) GT candidate
5. Identify the exact Go/No-Go criteria for advancing to preclinical development

---

## NOTES

- Do NOT rush Task 2. The depth of the ROGDI analysis is the core value.
- Do NOT add new external APIs just to tick boxes. Static data + deep reasoning beats shallow automation.
- The first report does not need to be generated from a live pipeline. Hardcoded deep data rendered through templates is fine for v0.1.
- Focus on **why** ROGDI matters, not just **what** the gene does.
