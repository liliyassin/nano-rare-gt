# 49-Day War Plan: Nano-Rare Gene Therapy Framework

**Objective:** Build a publishable, generalizable computational framework that matches untreated nano-rare monogenic diseases to gene therapy development strategies via multi-parameter structural homology and clinical surrogate matching.

**Final Deliverable:** An 8000-word manuscript with validated pipeline, retrospective controls, prospective case studies, and 70 references.

**Timeline:** 49 days (7 weeks), 10-14 hours/day, no weekends off.

**Working Directory:** `/Users/suzie/nano-rare-gt/` (primary repo)  
**This Plan Location:** `/Users/suzie/Desktop/GitHub/nano-rare-gt/`

---

## 1. THE ALGORITHMIC PIPELINE

INPUT: Orphanet ID / OMIM ID / Gene Symbol of untreated nano-rare monogenic disease  
OUTPUT: Ranked GT development strategies with feasibility scores, risk flags, auto-generated protocols

### Stage 1 — Disease Characterization
- Orphanet API: prevalence, inheritance, phenotypes, severity
- OMIM cross-ref: gene mapping, allelic disorders
- ClinicalTrials.gov: active GT trial count (exclusion gate: >0 active trials deprioritized unless no approved therapy)
- Inheritance flag: homozygous LOF, dominant negative, GOF (determines knockdown vs cDNA vs editing strategy)

### Stage 2 — Gene & Protein Annotation
- UniProt API: sequence, domains, GO terms, MW, subcellular location
- AlphaFold DB: structure availability, pLDDT confidence (<50 = low-confidence flag)
- Secreted vs intracellular classifier (secreted = higher cross-correction potential = easier target)

### Stage 3 — Structural Homology & Surrogate Matching
- BLASTp / Foldseek vs all proteins with approved/phase-3 gene therapies
- Scores: global sequence identity, domain architecture similarity (Pfam/InterPro overlap), structure alignment RMSD (if both have AF models)
- Surrogate selection: approved GT with highest structural homology + shared tissue tropism

### Stage 4 — Vector Compatibility
- CDS length vs AAV packaging limit (4.7 kb hard gate)
- If >4.7 kb: flag oversized, suggest dual-AAV, lentivirus, or mini-gene design
- Serotype matching: target tissue to optimal serotype (CNS -> AAV9/PHP.eB, retina -> AAV2/AAV8, liver -> AAV8/AAV9, muscle -> AAVrh74/AAV9)
- Patent/freedom-to-operate flag on serotypes

### Stage 5 — Expression & Regulatory Matching
- GTEx: target tissue TPM (>1.0 on-target, <0.1 off-target avoidance)
- Promoter selection: ubiquitous (CMV/CBA) vs tissue-specific (RHO retina, MHCK7 muscle, TBG liver, GfaABC1D astrocytes)
- TiProD or literature for regulatory element precedents

### Stage 6 — Immunogenicity Risk
- IEDB-based MHC-I epitope prediction for transgene vs common HLA alleles (A*02:01, A*01:01, B*07:02, DRB1*04:01)
- Flag high epitope density (>20 predicted binders)
- Compare to human ortholog similarity (self-like = lower risk)

### Stage 7 — Therapeutic Window & Codon Optimization
- Codon Adaptation Index (CAI) for target organism
- Overexpression toxicity flag (check OMIM/ClinVar for WT overexpression toxicity)
- Therapeutic index: rescue expression needed vs toxicity threshold

### Stage 8 — Multi-Parameter Scoring Engine
- 11 dimensions, each 0-1 normalized
- Weights: structural homology (0.20), size compatibility (0.15, hard gate), tissue tropism (0.15), platform depth (0.15), immunogenicity (0.10), promoter match (0.10), therapeutic window (0.10), codon opt (0.05)
- Confidence tiers: high (all primary data), medium (1-2 gaps), low (major gaps)
- Auto-reject if size gate fails AND no dual-AAV/lenti workaround selected

### Stage 9 — Protocol Synthesis
- Jinja2 template: cargo cDNA, vector serotype, promoter, RoA, dosing, risks, mitigations
- Output: JSONL for downstream + Markdown report for human review

---

## 2. THE 49-DAY BATTLE PLAN

---

### WEEK 1: FOUNDATION & DATA LAYER (Days 1-7)

**Day 1 — Environment Lock**
- Purge R artifacts from primary repo (.Rhistory, .Rproj)
- Finalize VS Code workspace: .venv, black, ruff, mypy
- Run full test suite; fix any breakage
- Write ADR-001: "Why SQLite for v1, PostgreSQL for v2"
- Set up requests-cache with 7-day TTL for all external APIs
- Git commit: "w1d1: env locked, caching configured"

**Day 2 — Schema Hardening**
- Review existing models.py; add missing fields if needed
- Finalize SQLite schema in db.py; ensure clean serialization
- Add Alembic migration baseline
- Test: roundtrip Disease -> DB -> Pydantic -> dict
- Git commit: "w1d2: schema hardened"

**Day 3 — Orphanet Pipeline**
- Build orphanet.py client: query by ID, parse prevalence/severity/inheritance
- Graceful API failure handling (cached fallback + error logging)
- Map phenotypes to HPO terms if possible
- Test with mocked response
- Git commit: "w1d3: orphanet client"

**Day 4 — OMIM & ClinicalTrials.gov**
- Build omim.py: gene mapping, allelic disorders
- Build trials.py: count active GT trials by disease/gene query
- Implement exclusion gate: active trial count > 0 -> flag "existing development"
- Integration test: Orphanet ID -> OMIM gene -> trial count
- Git commit: "w1d4: omim + trials linkage"

**Day 5 — UniProt Integration**
- Build uniprot.py: fetch sequence, domains, GO, MW, subcellular location
- Cache raw XML/JSON in data/cache/
- Implement Protein model population
- Build secreted/intracellular classifier from go_terms and keywords
- Git commit: "w1d5: uniprot pipeline"

**Day 6 — AlphaFold DB Linkage**
- Build alphafold.py: map UniProt ID -> AFDB ID -> structure URL
- Download PDB/CIF for validation cases to data/structures/
- Implement pLDDT confidence extraction
- Flag avg pLDDT < 50 as low-confidence
- Git commit: "w1d6: alphafold linkage"

**Day 7 — Week 1 Integration**
- E2E test: ORPHA:324 -> full disease/gene/protein/structure record in <30 seconds
- Profile API call times; optimize slow paths
- ruff + mypy: zero warnings
- Update README with Week 1 progress
- Git commit: "w1d7: disease characterization pipeline complete"

---

### WEEK 2: HOMOLOGY, VECTOR, EXPRESSION (Days 8-14)

**Day 8 — Surrogate Database Construction**
- Manually curate JSON/CSV of approved + phase-3 gene therapies
- Fields: program_name, target_gene, vector_serotype, promoter, target_tissue, cds_length_bp, disease_orphanet_id
- Target: 20-30 entries minimum (Luxturna, Zolgensma, Hemgenix, Roctavian, Elevidys, etc.)
- Store in data/surrogate_db.jsonl
- Git commit: "w2d8: surrogate db v1"

**Day 9 — Sequence Homology Module**
- Build homology.py: BLASTp wrapper or EBI NCBIblast API client
- BLAST query protein against all surrogate_db sequences
- Score: % identity, % similarity, alignment coverage
- Unit tests with known homologs
- Git commit: "w2d9: sequence homology"

**Day 10 — Structural Homology & Domain Matching**
- Build structure.py: compute domain overlap (Pfam/InterPro intersection/union)
- If both have AF models: use Foldseek/TM-align if installable; else use domain architecture score
- Weight: sequence identity 0.6, domain similarity 0.4 for structural score
- Git commit: "w2d10: domain + structural scoring"

**Day 11 — Vector Sizing & Serotype Matching**
- Build vector.py: gate on cds_length_bp vs cargo_limit_bp (4700 bp hard)
- If >4700 bp: flag oversized, suggest dual-AAV/lenti/minigene
- Match tissue to serotype from data/serotype_map.json
- Score tissue_tropism: exact=1.0, related=0.5, no match=0.0
- Git commit: "w2d11: vector compatibility engine"

**Day 12 — Tissue Expression (GTEx)**
- Build expression.py: GTEx API or local GTEx median TPM parsing
- Fetch expression across 50+ tissues for query gene
- Map primary target tissue from disease phenotype terms
- Score: high target-tissue + low off-target = high score
- Git commit: "w2d12: gtex expression matching"

**Day 13 — Promoter & Regulatory Matching**
- Build promoter.py: static knowledge base tissue -> recommended promoters
- Sources: literature, TiProD, GTEx co-expression
- Score promoter match: exact tissue-specific=1.0, ubiquitous=0.6, mismatched=0.2
- Git commit: "w2d13: promoter selection"

**Day 14 — Week 2 Integration**
- Pipeline test: query gene -> structural homology -> vector match -> expression -> promoter
- Benchmark: 5 diseases in <5 minutes
- Zero lint warnings
- Git commit: "w2d14: matching engine v1"

---

### WEEK 3: IMMUNOGENICITY, SCORING, CLI, REPORTS (Days 15-21)

**Day 15 — Immunogenicity Module**
- Build immuno.py: IEDB API or local MHC-I binding prediction
- If installable: mhcflurry or netMHCpan; else use sequence heuristics
- Flag high epitope count; compare to human self-similarity
- Git commit: "w3d15: immunogenicity risk"

**Day 16 — Codon Optimization & Therapeutic Window**
- Build codon.py: calculate CAI using standard human codon usage table
- Build therapeutics.py: check OMIM/ClinVar for WT overexpression toxicity
- Score therapeutic window: 1.0 no toxicity, 0.5 uncertain, 0.0 known toxicity
- Git commit: "w3d16: codon + toxicity"

**Day 17 — Scoring Engine v1**
- Build scoring.py: implement ScoreBreakdown population from all modules
- Normalization: raw score -> 0-1 scale with disease-aware percentiles
- Hard gates and composite weighting (ADR-002)
- Unit test: known match scores higher than random pair
- Git commit: "w3d17: scoring engine"

**Day 18 — Ranking & Confidence**
- Build ranking.py: sort by composite score, break ties by platform depth
- Confidence tiers: high/all primary data, medium/1-2 gaps, low/>2 gaps
- Top match selection with justification extraction
- Git commit: "w3d18: ranking + confidence"

**Day 19 — Report Generation**
- Build/refine report.py: Jinja2 templates for Markdown output
- Sections: Executive Summary, Disease Profile, Surrogate Rationale, Protocol Recommendation, Risk Assessment, Development Roadmap
- Every score dimension gets 1-2 sentences justification
- Git commit: "w3d19: report templates"

**Day 20 — CLI Wiring**
- Wire all modules into cli.py: nanogt match --disease ORPHA:XXX --output report.md
- Add --format json, --top-n
- Rich progress bars for long queries
- Git commit: "w3d20: CLI wired"

**Day 21 — End-to-End Pole Test**
- Run full pipeline on 5 diverse diseases (CNS, retina, liver, muscle, metabolic)
- Verify reports are coherent and scientifically defensible
- Fix all bugs. Zero mypy warnings.
- Git tag: v0.2-alpha
- Git commit: "w3d21: e2e validated"

---

### WEEK 4: VALIDATION & CASE STUDIES (Days 22-28)

**Day 22 — Retrospective Positive Control #1: Luxturna (RPE65)**
- Input: RPE65-related retinal dystrophy
- Expected: high match to itself, AAV2, subretinal, CMV/CBA
- Validate algorithm. Fix discrepancies.
- Git commit: "w4d22: luxturna validation"

**Day 23 — Retrospective Positive Control #2: Zolgensma (SMN1)**
- Input: Spinal muscular atrophy
- Expected: AAV9, intrathecal/IV, scAAV-CB
- Test gene duplication edge case handling
- Git commit: "w4d23: zolgensma validation"

**Day 24 — Retrospective Negative Control**
- Research one discontinued GT program (e.g., early CNS failures, certain hemophilia AAV5 programs with immunogenicity issues)
- Input target gene/disease. Algorithm should flag immunogenicity risk or tissue mismatch matching known failure mode.
- Git commit: "w4d24: negative control validation"

**Day 25 — Prospective Case Study #1: CNS Ultra-Rare**
- Select untreated ultra-rare CNS monogenic disease with homozygous LOF
- Run full pipeline. Generate protocol. Manually verify against literature.
- Write 800-word case study narrative.
- Git commit: "w4d25: prospective cns case"

**Day 26 — Prospective Case Study #2: Metabolic/Hepatic**
- Select untreated metabolic liver disease
- Run pipeline. Focus on AAV8/9 liver targeting, TBG promoter.
- Verify CDS fit and GTEx liver expression.
- Write 800-word case study narrative.
- Git commit: "w4d26: prospective hepatic case"

**Day 27 — Sensitivity Analysis**
- Systematically vary scoring weights +/- 20% and re-run retrospective cases
- Measure rank stability. Report which dimensions are most influential.
- Generate weight sensitivity heatmap data for paper figures.
- Git commit: "w4d27: sensitivity analysis"

**Day 28 — Case Study Documentation**
- Compile all validation into docs/validation.md
- Include expected vs observed, algorithm fixes, limitations
- Generate first draft schematics
- Git commit: "w4d28: validation complete"

---

### WEEK 5: PAPER WRITING — CORE SECTIONS (Days 29-35)

**Day 29 — Introduction & Background (target 1200 words)**
- Nano-rare disease definition and prevalence statistics
- Gap: thousands of monogenic diseases, <50 approved GTs
- Solution: computational framework leveraging structural homology + clinical surrogates
- Prior art and hypothesis
- File: paper/introduction.md

**Day 30 — Methods — System Overview (target 600 words)**
- Architecture diagram description
- Data sources and APIs
- Software stack: Python, Pydantic, SQLite, Typer
- Ethical/data statement: all public data, no patient data
- File: paper/methods_system.md

**Day 31 — Methods — Disease & Gene Module (target 400 words)**
- Orphanet + OMIM + ClinicalTrials.gov integration
- Disease severity scoring, trial-status exclusion
- File: paper/methods_disease.md

**Day 32 — Methods — Homology & Vector (target 500 words)**
- BLASTp parameters, domain similarity metric, surrogate DB construction
- AAV sizing gate, serotype selection, packaging limit handling
- File: paper/methods_homology.md

**Day 33 — Methods — Expression & Immunogenicity (target 500 words)**
- GTEx thresholds, promoter selection rules
- MHC-I epitope prediction approach, self-similarity correction
- Codon optimization (CAI), therapeutic window assessment
- File: paper/methods_expression.md

**Day 34 — Methods — Scoring & Output (target 400 words)**
- Weighted composite formula, normalization, confidence tiers
- Protocol synthesis via template generation
- File: paper/methods_scoring.md

**Day 35 — Assemble Methods**
- Combine all methods into paper/methods_full.md
- Cross-references, consistent notation
- Internal word count check
- Git commit: "w5d35: methods draft complete"

---

### WEEK 6: RESULTS, DISCUSSION, FIGURES (Days 36-42)

**Day 36 — Results — Pipeline Performance (target 800 words)**
- Database coverage statistics
- Query speed benchmarks (median, 95th percentile)
- Data completeness per dimension
- File: paper/results_performance.md

**Day 37 — Results — Retrospective Validation (target 700 words)**
- Luxturna, Zolgensma results with scores
- Negative control discrimination
- Accuracy metrics: top-k retrieval, rank correlation
- File: paper/results_validation.md

**Day 38 — Results — Prospective Case Studies (target 800 words)**
- CNS and hepatic cases with full protocols
- Score breakdown tables
- File: paper/results_cases.md

**Day 39 — Figures**
- Figure 1: Pipeline schematic (SVG/PNG, high-res)
- Figure 2: Scoring radar chart for top case study
- Figure 3: Sensitivity analysis heatmap (weight perturbation vs rank)
- Figure 4: Composite score distribution across tested diseases
- Figure 5: Prospective case study comparison table + schematic
- All at 300 DPI, journal-ready
- Git commit: "w6d39: figures finalized"

**Day 40 — Discussion — Strengths & Limitations (target 1000 words)**
- Generalizability across monogenic disease classes
- Limitations: AlphaFold confidence, incomplete surrogate DB, immunogenicity prediction accuracy, lack of patient-specific HLA data
- Comparison to manual GT development timelines
- File: paper/discussion_strengths.md

**Day 41 — Discussion — Regulatory, CMC, IP & Future (target 1000 words)**
- Regulatory pathway acceleration via surrogate precedent
- CMC: platform manufacturing vs novel cargo
- IP: freedom-to-operate for serotypes, promoters, transgenes
- Future work: CRISPR expansion, non-viral delivery, ML refinement
- File: paper/discussion_future.md

**Day 42 — First Full Draft Assembly**
- Combine all sections into paper/manuscript_v1.md
- Add Abstract (250 words), Keywords, Title
- Target total: 7500-8000 words excluding references
- Read aloud, fix logic gaps, check transitions
- Git commit: "w6d42: manuscript v1 complete"

---

### WEEK 7: REFINEMENT, POLISH, SUBMISSION PREP (Days 43-49)

**Day 43 — Citation Audit**
- Ensure every claim has a citation
- Add 60-80 references: OMIM/Orphanet methods, GT reviews, AAV engineering, AlphaFold, GTEx, IEDB, prior approvals
- Decide target journal: Molecular Therapy (Methods & Clinical Development) for methods focus, or Nature Communications for broader scope
- Consistent formatting (Vancouver for MolTher; APA for Nature)
- File: paper/references.bib or formatted text
- Git commit: "w7d43: citations complete"

**Day 44 — Code Reproducibility Audit**
- Re-run all analyses from fresh clone / fresh venv
- Document exact dependency versions (pip freeze > requirements.txt)
- Ensure README has installation + usage instructions
- Create docs/reproducibility.md with expected runtimes and outputs
- Git commit: "w7d44: reproducibility verified"

**Day 45 — Language Edit**
- Reduce jargon where possible
- Replace passive voice where active is stronger
- Frame: "generalizable framework applicable across the full spectrum of monogenic disease" (scientifically defensible)
- Check word count exactly on target (7500-8500)
- Git commit: "w7d45: language edit"

**Day 46 — Journal Formatting & Supplementary**
- Format per chosen journal guidelines (font, headings, refs)
- Supplementary tables: full scoring tables, surrogate DB as Supp Table 1, weight justification as Supp Note 1
- Git commit: "w7d46: supplementary complete"

**Day 47 — Peer Pre-Review (Self-Critique)**
- Read as Reviewer #2. Anticipate:
  - "Is the surrogate database large enough?"
  - "How do you handle genes >4.7kb?"
  - "What about gene editing approaches?"
- Write responses in paper/anticipated_reviews.md
- Adjust manuscript to address top 3 criticisms preemptively
- Git commit: "w7d47: pre-review pass"

**Day 48 — Final Figures & Accessibility**
- All figures meet journal resolution requirements
- Alt-text for accessibility
- Generate final PDF from Markdown (pandoc or preferred tool)
- Generate code archive zip for supplemental software
- Git commit: "w7d48: final outputs"

**Day 49 — Final Read-Through & Submission Prep**
- Read entire paper start-to-finish without editing
- Write cover letter: novelty, significance, audience
- Check supplementary package completeness
- Submit to target journal OR post to bioRxiv
- Final git tag: v1.0-submission
- Git commit: "w7d49: SUBMISSION READY"

---

## 3. DAILY SCHEDULE (Mad Scientist Mode)

| Time | Activity |
|------|----------|
| 0600 | Wake, coffee, 30 min paper reading (Nature / Molecular Therapy / GT news) |
| 0630 | 3-hour deep work block (no Slack, no email, no phone) |
| 0930 | Break, walk, snack |
| 1000 | 3-hour deep work block |
| 1300 | Lunch + 30 min break (walk outside, no screens) |
| 1400 | 2-hour coding/writing block |
| 1600 | Coffee + 30 min break |
| 1630 | 2-hour integration/testing/writing block |
| 1830 | Dinner break |
| 1930 | 2-hour lighter work: documentation, tests, reading, citations |
| 2130 | Git commit, write tomorrow's 3 specific objectives |
| 2200 | Stop. Sleep is non-negotiable for cognitive performance. |

**Total:** ~12 hours focused work daily. Sustainable for 7 weeks if sleep and exercise are protected.

---

## 4. CONTINGENCY PROTOCOLS

| Problem | Response |
|---------|----------|
| **API outage** (Orphanet/UniProt/CT.gov down) | Use local cached data (requests-cache 7-day TTL). If >2 days, build static JSON from cache and document limitation in Methods. |
| **No AlphaFold structure** | Fallback to domain architecture-only scoring. Document lower confidence tier. |
| **Gene > 4.7kb (AAV limit)** | Do not discard. Branch: suggest dual AAV, AAV-ITR minigene, or lentivirus. Document as "oversized cargo pathway." |
| **Immunogenicity prediction too slow** | Simplify to epitope count threshold rather than full MHC binding for v1. Document in limitations. |
| **Writer's block** | Switch to figure-making or test-writing for 1 day. Return to prose after. |
| **Mypy/ruff refuses to pass** | Spend max 2 hours; if stuck, document the type ignore in an ADR and move on. |
| **Surrogate DB <20 entries by Day 9** | Lower threshold to 15 + document as v1 limitation. Expand to 30+ in Week 4 as background task. |

---

## 5. SUCCESS CRITERIA (Day 49)

- [ ] Repository: 2000+ lines of tested Python, 80%+ coverage
- [ ] Paper: 8000 words, 5 figures, 2 tables, 70 references, formatted for target journal
- [ ] Validation: 2 retrospective positive controls, 1 negative control, 2 prospective cases
- [ ] Deliverable: Complete GT protocol for untreated ultra-rare disease in <2 minutes via `nanogt match --disease ORPHA:XXX`
- [ ] Reproducibility: fresh install + run produces identical results in <30 minutes setup

---

## 6. TARGET JOURNAL OPTIONS

1. **Molecular Therapy — Methods & Clinical Development** (methods-focused, rapid review)
2. **Nature Communications** (broad reach, high impact)
3. **Human Gene Therapy** (specialist audience)
4. **bioRxiv** (immediate preprint if journal submission feels premature)

Decide on **Day 43** after reading recent issues of each.

---

## 7. FILES TO CREATE NOW

After reading this plan, create these files in your repo TODAY:

```bash
cd /Users/suzie/nano-rare-gt
mkdir -p paper docs/figures data/structures data/cache tests/fixtures
```

This plan was generated on 17 May 2026. The clock starts when you say go.
