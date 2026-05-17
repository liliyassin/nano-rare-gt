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

- [ ] Query UniProt Q9P2T1 programmatically — fetch full JSON, extract all fields
- [ ] Query OMIM 137260 (ROGDI gene) and OMIM 226750 (KTS phenotype)
- [ ] Research Kohlschütter-Tönz syndrome in depth:
  - [ ] Natural history and clinical course
  - [ ] Known pathophysiology (GMP reductase deficiency → purine imbalance)
  - [ ] All affected tissues: brain, teeth, kidney, retina?
  - [ ] Age of onset, progression, life expectancy
  - [ ] Current standard of care (none? supportive only?)
  - [ ] Why no gene therapy exists yet (what are the barriers?)
- [ ] Research ROGDI protein function:
  - [ ] IMPDH/GMP reductase enzyme — role in purine metabolism
  - [ ] Why intracellular/cytosolic localization matters for GT
  - [ ] Presynaptic terminal localization — why this matters for CNS rescue
  - [ ] Overexpression risk: enzyme activity vs. stoichiometry
- [ ] Research AAV delivery to ROGDI-relevant tissues:
  - [ ] CNS: AAV9 IV vs. ICV vs. intrathecal — what does LCA2/RPE65 tell us?
  - [ ] Dental/am eloblasts: has any AAV ever targeted enamel organ?
  - [ ] Kidney: AAV9 capsid engineering for renal targeting
- [ ] Structural homology search — what proteins are closest to ROGDI?
  - [ ] IMPDH1, IMPDH2 ( known GT targets? approved therapies?)
  - [ ] GMPR1 (the other GMP reductase isoform)
  - [ ] Any other IMPDH-domain proteins with clinical programs?

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
  3. **Therapeutic Rationale** — why GT is appropriate (AR, LoF, small gene, no cross-correction needed vs. reality)
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

- [ ] Wire `report.py` into `cli.py` so `nanogt match --disease ORPHA:916 --output rogdi_report.md` works
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

1. Run `nanogt match --disease ORPHA:916 --output rogdi_report.md` and get a **real file**
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
