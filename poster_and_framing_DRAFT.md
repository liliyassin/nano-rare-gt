# NanoGT — Project Framing & Poster Content (working draft)

*Drafted 2026-06-23 from your own project materials: the **final 35-disease list** (`New 35 Table of Diseases.pdf`), the decision-flowchart direction your supervisor set on 22 June, your achromatopsia trial analysis, and your reference library. Everything below is a **draft for you to edit, verify and make your own** — the wording is deliberately defensible against your actual disease set, but you should be able to explain every line in a viva, so read it critically and change anything you'd phrase differently.*

> **Status of the two open items:**
> 1. **Disease list — now settled.** 35 monogenic loss-of-function rare diseases (your final table). All 24 earlier diseases retained; 11 added (Friedreich ataxia, classic galactosemia, argininosuccinic aciduria, citrin deficiency/NICCD, fucosidosis, aspartylglucosaminuria, CLN3/Batten, gyrate atrophy, congenital erythropoietic porphyria, DOCK8 deficiency, Sjögren-Larsson). Full classification in **Appendix A**.
> 2. **Framing** — keep "NanoGT the tool" central, or present this as a literature-based decision framework? The text below works for both; I've flagged the one or two places it matters.

---

## 1. Thesis statement

*(One sentence is the spine of the whole poster and report. Draft:)*

> **A rare monogenic diagnosis is necessary but not sufficient for AAV gene therapy: whether a loss-of-function disease is curable with an AAV vector is decided by a small, definable set of molecular criteria — and where every criterion is met but no therapy exists, the limiting factor is economic and not biological.**

Alternative, tool-flavoured phrasing if you keep NanoGT central:

> *Using a reproducible decision framework applied to 35 curated loss-of-function rare diseases, AAV curability can be predicted from molecular first principles; the framework recovers every approved precedent and isolates a set of "biologically solved, commercially unfunded" diseases.*

**Why this is defensible:** it is exactly what your 35-disease set shows — positive controls (Hemophilia B, SMA) pass; only two diseases (MECP2/Rett, CLN3) fail on fundamental biology; and Crigler-Najjar is biologically tractable but has no approved therapy.

---

## 2. Aim(s)

*(Aim = the high-level purpose. Keep it to 1 primary aim + 2–3 sub-aims.)*

**Primary aim.** To determine, from molecular first principles, which loss-of-function rare diseases are curable with an AAV gene-addition vector, and to explain why some are not.

**Sub-aims.**
- Build an explicit, reproducible decision framework (flowchart) that encodes the molecular requirements for successful AAV gene addition.
- Apply it systematically to a curated set of 35 monogenic loss-of-function rare diseases spanning liver, CNS, retina, muscle and haematopoietic targets.
- Distinguish diseases blocked by **biology** (gene too large, inaccessible tissue, no cross-correction, dosage sensitivity, wrong subcellular compartment) from those blocked only by **economics/prevalence**.

---

## 3. Objectives

*(Objectives = the concrete, checkable steps that deliver the aims. These map onto what you've actually done — good for "what did you do?" questions.)*

1. Define the molecular decision nodes that gate AAV curability (see flowchart, §5) from the gene-therapy literature.
2. Curate the 35-disease set and record, per disease: causative gene, inheritance, molecular mechanism (LoF confirmed/conditional/other), CDS length (bp), primary affected cell type/tissue, and existing trial status (NCT).
3. Run each disease through the framework and record the node at which it stops (or that it passes all nodes).
4. Validate the framework on positive controls — diseases with approved AAV therapies should pass every node.
5. For each disease, write a structured AAV-curability analysis (achromatopsia-style; template in §7).
6. Classify the gaps: for diseases that pass all biological nodes but have no therapy, assess whether the barrier is prevalence/economics.

---

## 4. Hypotheses

*(State them so they can be supported or falsified by your own data.)*

- **H1 (tractability).** Small-gene (<~4.7 kb CDS) loss-of-function diseases affecting an AAV-accessible, ideally immune-privileged tissue are biologically tractable for AAV gene addition.
- **H2 (the gap = economics).** Among diseases that satisfy every biological criterion, the diseases without an approved therapy are predominantly the rarest — i.e. the dominant barrier is prevalence/commercial incentive, not biology.
- **H3 (validation).** The framework recovers known precedents: every positive-control disease with an approved AAV therapy passes all biological nodes.
- **H4 (predictable failure modes).** Diseases fail at *specific, nameable* molecular nodes — oversized CDS (e.g. DMD, *MYO7A*, *DOCK8*), absent cross-correction for membrane proteins (e.g. *ATP7B*, *CLN3*, *SLC25A13*), wrong subcellular compartment (mitochondrial genes; matrix-import enzymes), or dosage sensitivity/haploinsufficiency (e.g. *MECP2*) — rather than failing diffusely.

---

## 5. Decision flowchart — every molecular step from "gene" to "cure"

The figure `flowchart_aav_molecular.svg` (in your project folder) renders this. The logic, node by node, with the molecular reason each one matters and a worked example from your set:

1. **Monogenic loss-of-function?** Gene addition restores a missing/non-functional protein. Gain-of-function, dominant-negative and toxic-RNA mechanisms need silencing/editing instead → out of simple-addition scope.
2. **Dosage-sensitive / haploinsufficient?** If too much protein is also harmful, unregulated gene addition is unsafe. → *MECP2* (Rett): *MECP2* duplication is itself a disease, so expression must be tightly regulated.
3. **CDS ≤ ~4.7 kb (single-AAV packaging limit)?** If no → micro/mini-gene, dual/split-AAV, or a different modality. → DMD (11 kb → micro-dystrophin), Usher 1B *MYO7A* (6.6 kb → dual-AAV), *DOCK8* (6.3 kb). Borderline: *F8* (4.4 kb), *ATP7B* (4.4 kb).
4. **Cell-autonomous, or can it cross-correct?** Secreted/secretable lysosomal enzymes spread to untransduced cells via the M6P receptor → lower dose, wider reach. Membrane channels/transporters cannot → every target cell must be hit. → cross-correcting: *ARSA*, *IDUA*, *SGSH*, *GLA*, *GALC*, *FUCA1*, *AGA*; cell-autonomous: *ATP7B*, *MECP2*, *CLN3*, *SLC25A13*.
5. **Is the primary target cell type known and defined?** You can't engineer tropism/promoter without it.
6. **Is that tissue AAV-accessible, and does a serotype with the right tropism exist?** Liver (IV) and retina (subretinal) are easy and the retina is immune-privileged; CNS needs intrathecal/ICV; **bone marrow is not an AAV target** → ex-vivo HSC lentiviral route instead (ADA-SCID, Wiskott-Aldrich, DOCK8, congenital erythropoietic porphyria).
7. **Correct subcellular compartment reachable?** mtDNA-encoded genes need allotopic expression (not standard AAV); nuclear-encoded mitochondrial enzymes/carriers need an intact targeting sequence. → *OTC* (urea-cycle matrix import), *OAT* (gyrate atrophy), *SLC25A13* (citrin, mito inner membrane).
8. **Validated tissue-specific promoter available?** Needed to restrict and tune expression (liver: TBG/hAAT; retina: GRK1/CRX; CNS: synapsin).
9. **Immune barriers manageable?** Pre-existing anti-capsid neutralising antibodies exclude patients; T-cell responses limit durability; tissue immune privilege helps.
10. **Therapeutic window?** Can you treat before irreversible damage (lost motor neurons in SMA; lost cones in achromatopsia; neurodegeneration in Tay-Sachs/Krabbe/Canavan)?
11. **Measurable biomarker/endpoint?** e.g. FIX activity (Hem B), serum bilirubin (Crigler-Najjar), enzyme activity (LSDs), retinal function (IRDs).
12. **Does a trial already exist? If not — is the only remaining barrier prevalence/economics?** → **key finding node:** Crigler-Najjar passes all biology, measurable endpoint, but is ultra-rare → economic gap, not a scientific one.

---

## 6. Poster content (poster-ready draft)

*Built to your stated poster spec: A1 landscape, 3-column, Imperial branding, **no abstract**, **no acknowledgements box**, 3–12 references **with no numbering**, a short catchy title, and a mix of prose and occasional bullets. Edit freely — keep word counts roughly as-is so it fits.*

### Title (pick one)
- **NanoGT: Why AAV Cures Some Rare Diseases — But Not Others**
- **From Genome to Cure? A Molecular Decision Framework for AAV in Rare Disease**

### Introduction
Around 7,000 rare diseases are known and most are monogenic, yet only a small minority have an approved disease-modifying therapy. AAV gene therapy can correct loss-of-function disease at its root — Luxturna, Zolgensma and Hemgenix are proof — but a rare monogenic diagnosis alone does **not** guarantee an AAV is feasible. This project asks a deceptively simple question: *if we can sequence a child's genome, can we read off whether an AAV could treat them — and if not, why not?* I define the molecular criteria that decide AAV curability and apply them systematically across 35 loss-of-function rare diseases.

### Methods
A literature-based decision framework was built encoding the molecular requirements for AAV gene addition (mechanism, packaging fit, cross-correction, tissue accessibility and tropism, subcellular targeting, expression control, immune barriers, therapeutic window, biomarker). The 35 monogenic loss-of-function rare diseases were verified against Orphanet/OMIM/UniProt, recording for each: causative gene, inheritance, molecular mechanism, CDS length, primary tissue, and clinical-trial status (ClinicalTrials.gov). Each disease was run through the framework; the node at which it stops was recorded. Diseases with approved AAV therapies were used as positive controls.

### Results & Discussion
*(Pair this with your coloured bar chart of AAV-suitability across a representative subset, plus the table below. Full 35-disease classification is in Appendix A.)*

- **The framework validates on positive controls.** Hemophilia B (*F9*, 1.4 kb, liver, measurable FIX) and SMA (*SMN1*, 0.9 kb, AAV9-accessible motor neurons) pass every node — matching their approved therapies.
- **Across all 35, fundamental biological dead-ends are rare.** Only two diseases are genuinely hard for simple AAV addition — *MECP2*/Rett (dosage-sensitive) and *CLN3*/Batten (a non-secreted membrane protein that cannot cross-correct). The rest are tractable or need a *named* workaround.
- **Failures occur at specific, nameable nodes, not diffusely.** Oversized genes (DMD 11 kb, *MYO7A* 6.6 kb, *DOCK8* 6.3 kb) → micro-gene/dual-AAV. Bone-marrow diseases (ADA-SCID, Wiskott-Aldrich, DOCK8, congenital erythropoietic porphyria) → ex-vivo HSC route. Mitochondrial-compartment enzymes (*OTC*, *OAT*, citrin) → targeting-sequence constraints.
- **Tissue and protein biology drive feasibility.** Secreted lysosomal enzymes (MLD, MPS I, Sanfilippo A, Fabry, fucosidosis, aspartylglucosaminuria) cross-correct neighbouring cells and cluster as the strongest soluble-enzyme candidates; membrane proteins (Wilson *ATP7B*, CLN3, citrin) cannot cross-correct and are harder.
- **The headline finding — biology solved, therapy absent.** Crigler-Najjar type I is small-gene, liver-directed, with a clean biomarker (bilirubin), yet has no approved therapy. Where biology is satisfied but no therapy exists, the barrier is **prevalence/economics, not science**.

| Disease | Gene (CDS) | Target | AAV verdict | Limiting node |
|---|---|---|---|---|
| Hemophilia B | *F9* (1.4 kb) | Liver | Strong ✓ | none (approved) |
| Spinal muscular atrophy | *SMN1* (0.9 kb) | Motor neuron | Strong ✓ | treatment window |
| Metachromatic leukodystrophy | *ARSA* (1.5 kb) | CNS (secreted enzyme) | Strong ✓ | CNS delivery |
| Achromatopsia | *CNGB3* (2.4 kb) | Cone photoreceptor | Feasible ◐ | window / cone viability |
| Crigler-Najjar type I | *UGT1A1* (1.6 kb) | Liver | Feasible ◐ | **economics (gap)** |
| Duchenne | *DMD* (11 kb) | Muscle | Conditional △ | packaging → micro-gene |
| Rett syndrome | *MECP2* (1.5 kb) | CNS neuron | Hard ✕ | dosage sensitivity |
| CLN3 (Batten) | *CLN3* (1.3 kb) | CNS + retina | Hard ✕ | membrane protein — no cross-correction |

### Conclusion
AAV curability is decided by molecular fit — small gene, accessible and ideally immune-privileged tissue, cross-correcting or reachable protein, controllable expression, an open treatment window and a clear biomarker. Across 35 loss-of-function rare diseases the framework reproduces every approved precedent and shows that genuine biological dead-ends are the exception (2 of 35): most untreated diseases stall at a *named* engineering node — delivery route, packaging, or treatment window — or at no biological barrier at all. The most actionable result is this last group: diseases that clear every biological hurdle yet remain untreated, where the bottleneck is prevalence and commercial incentive — addressable by policy and platform approaches, not new biology.

### References (no numbering; trim to 5–8)
- Wang J-H, Gessler DJ, Zhan W, Gallagher TL, Gao G. Adeno-associated virus as a delivery vector for gene therapy of human diseases. *Signal Transduct Target Ther.* 2024.
- Nguengang Wakap S, et al. Estimating cumulative point prevalence of rare diseases: analysis of the Orphanet database. *Eur J Hum Genet.* 2020.
- Grieger JC, Samulski RJ. Packaging capacity of adeno-associated virus serotypes. *J Virol.* 2005.
- Russell S, et al. Voretigene neparvovec (AAV2-hRPE65v2) for RPE65-mediated retinal dystrophy: phase 3. *Lancet.* 2017.
- Mendell JR, et al. Single-dose gene-replacement therapy for spinal muscular atrophy. *N Engl J Med.* 2017.
- Pipe SW, et al. Gene therapy with etranacogene dezaparvovec for hemophilia B. *N Engl J Med.* 2023.
- Chamberlain JS, et al. Microdystrophin expression as a surrogate endpoint for DMD clinical trials. *Hum Gene Ther.* 2023.
- *(optional 8th)* Brooks PJ, et al. The Platform Vector Gene Therapies Project. *Hum Gene Ther.* 2020.

---

## 7. Per-disease analysis template (the achromatopsia depth, applied to every disease)

Use this for each of your 35 diseases so the depth is consistent. Fill it yourself — I'll check each against the literature.

```
DISEASE / ORPHA / OMIM:
Gene + protein + UniProt:  | Inheritance:  | CDS length (bp):
1. Mechanism — is it loss-of-function? (confirmed / conditional / other). Evidence + source.
2. Dosage sensitivity — is overexpression harmful? (y/n + why)
3. Packaging — CDS vs ~4.7 kb. If oversized: workaround (micro-gene / dual-AAV / other)?
4. Protein class & cross-correction — secreted / lysosomal-secretable / membrane / intracellular?
5. Target cell type & tissue — defined?
6. Tissue accessibility + AAV serotype/route (IV liver / subretinal / intrathecal / ex-vivo HSC)
7. Subcellular compartment — cytosol/secreted OK; mitochondrial/peroxisomal caveats?
8. Promoter — validated tissue-specific promoter available?
9. Immune barriers — capsid seroprevalence, immune privilege of tissue
10. Therapeutic window — when is damage irreversible?
11. Biomarker / endpoint — what would you measure?
12. Trial status — NCT(s), sponsor, phase, outcome
VERDICT: curable with AAV? where does it stop in the flowchart? if biology is fine, is the gap economic?
KEY REFERENCES (read + annotated):
```

---

## Appendix A — the framework applied to all 35 diseases

*This is a first-pass classification you can check and correct, not a finished result. Verdict key: ✓ strong · ◐ feasible (real caveat) · △ conditional (needs a workaround or non-AAV route) · ✕ hard (fundamental barrier for simple AAV addition). CDS = canonical protein length × 3 (approximate — source-check before quoting; entries from your existing cohort are verified). "Limiting node" is the flowchart step where the disease first runs into difficulty.*

**First-pass distribution:** of 35 — **6 strong ✓, 15 feasible ◐, 12 conditional △, 2 hard ✕.** Only 2/35 hit a fundamental biological dead-end; everything else is tractable or has a named workaround. (Confirm these counts yourself once you've filled the §7 templates.)

| # | Disease | Gene · CDS | Primary tissue | Cross-corrects? | Verdict | Limiting node / note |
|--:|---|---|---|---|:--:|---|
| 1 | Hemophilia A | *F8* · 4.4 kb | Liver | Yes (secreted) | ✓ | near packaging limit; approved (Roctavian) |
| 2 | Hemophilia B | *F9* · 1.4 kb | Liver | Yes (secreted) | ✓ | none — approved (Hemgenix) |
| 3 | ADA-SCID | *ADA* · 1.1 kb | Haematopoietic | Systemic enzyme | △ | bone marrow → ex-vivo HSC route |
| 4 | Spinal muscular atrophy 1 | *SMN1* · 0.9 kb | Motor neuron | No | ✓ | treat pre-symptomatically (window) |
| 5 | Duchenne MD | *DMD* · 11 kb | Skeletal/cardiac muscle | No | △ | oversized → micro-dystrophin |
| 6 | Achromatopsia | *CNGB3* · 2.4 kb | Cone photoreceptor | No | ◐ | window / cone viability |
| 7 | Alpha-mannosidosis | *MAN2B1* · 3.0 kb | CNS + viscera | Yes (secreted enzyme) | ◐ | CNS delivery |
| 8 | Choroideremia | *CHM* · 2.0 kb | Retina / RPE | No | ◐ | endpoint sensitivity (Ph3 missed) |
| 9 | Crigler-Najjar I | *UGT1A1* · 1.6 kb | Liver | No | ◐ | ★ economics (gap disease) |
| 10 | Fabry | *GLA* · 1.3 kb | Viscera, kidney, heart | Yes (secreted enzyme) | ◐ | kidney/heart reach |
| 11 | Gaucher type 1 | *GBA1* · 1.5 kb | Macrophages / viscera | Yes (secreted enzyme) | ✓ | non-neuronopathic subtype only |
| 12 | Krabbe | *GALC* · 2.1 kb | CNS + PNS | Yes (secreted enzyme) | ◐ | dual CNS+PNS + early window |
| 13 | Metachromatic leukodystrophy | *ARSA* · 1.5 kb | CNS | Yes (secreted enzyme) | ✓ | CNS delivery (HSC precedent) |
| 14 | MPS I (Hurler) | *IDUA* · 2.0 kb | CNS + viscera | Yes (secreted enzyme) | ✓ | CNS + window |
| 15 | Sanfilippo A (MPS IIIA) | *SGSH* · 1.7 kb | CNS | Yes (secreted enzyme) | ◐ | CNS delivery + window |
| 16 | OTC deficiency | *OTC* · 1.1 kb | Liver (mito matrix) | No | ◐ | mito import (MTS) + neonatal window |
| 17 | Wiskott-Aldrich | *WAS* · 1.5 kb | Haematopoietic | No | △ | bone marrow → ex-vivo HSC |
| 18 | X-linked centronuclear myopathy | *MTM1* · 1.9 kb | Skeletal muscle | No | ◐ | high-dose AAV safety (AT132 deaths) |
| 19 | X-linked retinoschisis | *RS1* · 0.7 kb | Retina (Müller/bipolar) | Partial (secreted) | ◐ | intravitreal efficacy/endpoint |
| 20 | Friedreich ataxia | *FXN* · 0.6 kb | DRG, heart, CNS | No (mito) | △ | DRG/heart delivery + dosage + organelle |
| 21 | Rett syndrome | *MECP2* · 1.5 kb | CNS neurons | No (nuclear) | ✕ | dosage sensitivity (overexpression toxic) |
| 22 | Canavan | *ASPA* · 0.9 kb | CNS (oligo/neuron) | No | ◐ | CNS delivery + window |
| 23 | Tay-Sachs | *HEXA* · 1.6 kb | CNS | Partial (secreted enzyme) | ◐ | CNS + HexA needs α+β subunits + window |
| 24 | Wilson | *ATP7B* · 4.4 kb | Liver | No (membrane transporter) | △ | large cargo + no cross-correction |
| 25 | Usher syndrome 1B | *MYO7A* · 6.6 kb | Retina + inner ear | No | △ | oversized → dual-AAV; dual tissue |
| 26 | Classic galactosemia | *GALT* · 1.1 kb | Liver, brain, ovary | No (cytosolic) | △ | multi-system + cell-autonomous + neonatal |
| 27 | Argininosuccinic aciduria | *ASL* · 1.4 kb | Liver + CNS | Partial | △ | dual liver+brain correction |
| 28 | NICCD (citrin) | *SLC25A13* · 2.0 kb | Liver (mito membrane) | No (membrane carrier) | △ | mito-membrane + cell-autonomous |
| 29 | Fucosidosis | *FUCA1* · 1.4 kb | CNS + viscera | Yes (secreted enzyme) | ◐ | CNS delivery |
| 30 | Aspartylglucosaminuria | *AGA* · 1.0 kb | CNS | Yes (secreted enzyme) | ◐ | CNS delivery + window |
| 31 | CLN3 disease (Batten) | *CLN3* · 1.3 kb | CNS + retina | No (membrane protein) | ✕ | membrane protein — no cross-correction; dual CNS/retina |
| 32 | Gyrate atrophy | *OAT* · 1.3 kb | Retina (+ systemic) | No (mito matrix) | ◐ | mito import (MTS); retina accessible |
| 33 | Congenital erythropoietic porphyria | *UROS* · 0.8 kb | Erythroid / marrow | No | △ | haematopoietic → ex-vivo HSC |
| 34 | DOCK8 deficiency | *DOCK8* · 6.3 kb | Haematopoietic | No | △ | oversized + bone marrow → HSC LV |
| 35 | Sjögren-Larsson | *ALDH3A2* · 1.5 kb | Skin + CNS | No (ER membrane enzyme) | △ | multi-tissue (skin + CNS) + cell-autonomous |

---

## 8. What's still yours to do
- Fill the §7 template for each of the 35 diseases — I'll fact-check each, especially the Appendix A verdicts and the CDS values I marked approximate.
- Decide the title and trim references to your 5–8 favourites.
- Draw/sign off the flowchart as your own (your supervisor wanted *you* to own it) — the SVG is a starting point to redraw or annotate.
- Pressure-test H2 (the economics claim) with prevalence numbers for your gap diseases (e.g. Crigler-Najjar) — that's the part most worth being able to defend, and the distribution stat in Appendix A is only as strong as those numbers.
