# ROGDI / Kohlschütter-Tönz Syndrome — Corrected Deep-Dive Knowledge Base

Version: 0.2 source-audited
Date: 2026-05-19
Gene: ROGDI
HGNC: HGNC:29478
OMIM gene: 614574
OMIM phenotype: 226750
UniProt: Q9GZN7
Orphanet: ORPHA:1946
Disease name: Kohlschütter-Tönz syndrome / amelocerebrohypohidrotic syndrome

This document is the corrected ROGDI audit used by the nano-rare GT framework. Every mechanistic and vector-design conclusion below is built from the corrected ROGDI identity: UniProt Q9GZN7, Protein rogdi homolog, 287 amino acids, approximately 32.3 kDa, with PDB structures 5XQH and 5XQI.

Key source links used:
- UniProt Q9GZN7: https://www.uniprot.org/uniprotkb/Q9GZN7
- UniProt REST JSON used for live verification: https://rest.uniprot.org/uniprotkb/Q9GZN7.json
- Orphanet ORPHA:1946: https://www.orpha.net/en/disease/detail/1946
- OMIM phenotype 226750: https://omim.org/entry/226750
- OMIM gene 614574: https://omim.org/entry/614574
- PubMed: Schossig et al. 2012: https://pubmed.ncbi.nlm.nih.gov/22482807/
- PubMed: Lee et al. 2017 structure paper: https://pubmed.ncbi.nlm.nih.gov/28638151/
- RCSB PDB 5XQH: https://www.rcsb.org/structure/5XQH
- RCSB PDB 5XQI: https://www.rcsb.org/structure/5XQI
- PubMed: 2025 Rabconnectin-3 / V-ATPase study: https://pubmed.ncbi.nlm.nih.gov/40049412/
- PMC full text for 2025 study: https://pmc.ncbi.nlm.nih.gov/articles/PMC11997317/
- Human Protein Atlas ROGDI: https://www.proteinatlas.org/ENSG00000067836-ROGDI
- FDA Zolgensma approval announcement: https://www.fda.gov/news-events/press-announcements/fda-approves-novel-gene-therapy-treat-children-spinal-muscular-atrophy

Live verification performed in this repo:
- Query: https://rest.uniprot.org/uniprotkb/Q9GZN7.json
- HTTP status: 200
- primaryAccession: Q9GZN7
- recommended protein name: Protein rogdi homolog
- geneName: ROGDI
- sequence length: 287 aa
- molecular weight: 32,254 Da
- cross-references found: PDB 5XQH, PDB 5XQI, AlphaFoldDB Q9GZN7, InterPro IPR028241, Pfam PF10259

---

## 1. Keyword definitions

AAV: Adeno-associated virus. A small, non-replicating viral vector commonly used for in vivo gene delivery. Its practical packaging limit is usually treated as about 4.7 kb including the therapeutic cassette and regulatory elements.

AAV9: An AAV capsid with clinical precedent for systemic delivery and nervous-system exposure, especially in early-life contexts. It is relevant to ROGDI because the most severe disease features are neurological.

Ameloblast: A tooth-development cell responsible for enamel formation. Ameloblast biology matters in KTS because amelogenesis imperfecta is one of the defining features.

Amelogenesis imperfecta: Defective formation or mineralization of tooth enamel. In KTS it produces abnormal enamel and dental morbidity, but established enamel defects may not be reversible after tooth development.

Autosomal recessive: A mode of inheritance in which disease usually occurs when both gene copies are affected. This supports a gene-addition strategy because adding a functional copy can, in principle, replace missing activity.

Blood-brain barrier: A vascular barrier that limits entry of molecules and vectors into the brain. It is a major constraint for CNS gene therapy.

Cargo: The genetic payload packaged inside an AAV vector. For ROGDI this would include ROGDI cDNA, promoter, polyadenylation signal, and other regulatory elements.

cDNA: Complementary DNA. A DNA copy of the mature coding transcript used in many gene-addition vectors.

Cell-autonomous rescue: A therapeutic effect that requires correction inside the affected cell itself. ROGDI is intracellular and non-secreted, so cell-autonomous rescue is expected to be important.

Cross-correction: Rescue of neighboring untransduced cells by a secreted therapeutic protein. This is unlikely to be strong for ROGDI because ROGDI is not known to be secreted.

Epileptic encephalopathy: A severe neurological condition in which seizures and abnormal brain activity contribute to developmental impairment. KTS includes early-onset epilepsy and severe neurodevelopmental disease.

Gene addition: A gene-therapy strategy that supplies a working copy of a gene without editing the genome. It is most straightforward for recessive loss-of-function disorders.

hSYN1 promoter: A compact human synapsin-1 promoter used to drive neuron-biased transgene expression.

Intrathecal delivery: Delivery into cerebrospinal fluid, often by lumbar puncture. It can increase CNS exposure while reducing some peripheral exposure compared with systemic delivery.

Loss of function: A mutation mechanism in which protein function is reduced or absent. Published KTS variants and structural mapping support ROGDI loss of function.

Orphan Drug Designation: A regulatory status for rare-disease therapeutics that can provide development incentives.

Potency assay: A test that shows a therapeutic product has the expected biological activity. For ROGDI this cannot be a simple enzyme-activity assay; it should measure expression, localization, complex interaction, and cell-based rescue.

Rabconnectin-3: A protein complex linked to regulation of V-ATPase and acidic organelle function. Recent evidence places ROGDI in this biology.

V-ATPase: Vacuolar-type proton ATPase, a proton pump that acidifies intracellular organelles such as lysosomes and synaptic vesicles. This is relevant to neuronal and enamel biology.

Vector tropism: The tendency of a vector to enter certain tissues or cell types more efficiently than others.

---

## 2. Disease overview

Kohlschütter-Tönz syndrome is an ultra-rare autosomal recessive disorder. Orphanet lists ORPHA:1946 as amelocerebrohypohidrotic syndrome and describes the triad of amelogenesis imperfecta, infantile-onset epilepsy, and intellectual disability with or without regression and dementia.

Evidence:
- Orphanet ORPHA:1946 description: https://www.orpha.net/en/disease/detail/1946
- OMIM phenotype entry 226750: https://omim.org/entry/226750
- Schossig et al. 2012 identified pathogenic ROGDI variants in KTS: https://pubmed.ncbi.nlm.nih.gov/22482807/

Core clinical features:
1. Amelogenesis imperfecta: defective enamel formation.
2. Early-onset epilepsy: often infantile or early-childhood onset.
3. Severe developmental delay or intellectual disability: may include regression or dementia-like decline.
4. Spasticity and motor impairment.
5. Hypohidrosis and heat intolerance in some cases.
6. Nephrocalcinosis in some reported patients.

Therapeutic implication:
The CNS disease likely dominates morbidity and mortality. Dental disease is important but may be hard to rescue after enamel has already formed. Therefore, a first gene-therapy program should prioritize CNS rescue and treat dental rescue as a separate unresolved tissue-delivery and timing problem.

---

## 3. Correct gene and protein identity

Correct target:
- Gene symbol: ROGDI
- OMIM gene: 614574
- UniProt accession: Q9GZN7
- Protein name: Protein rogdi homolog
- Protein length: 287 amino acids
- Molecular weight: 32,254 Da
- Ensembl gene: ENSG00000067836
- Chromosome: 16p12.1
- Approximate amino-acid coding region: 861 bp, or 864 bp if the stop codon is included in a construct convention

Evidence:
- UniProt Q9GZN7 live REST response confirms accession, gene name, protein name, sequence length, mass, PDB links, AlphaFold link, InterPro, and Pfam: https://rest.uniprot.org/uniprotkb/Q9GZN7.json
- UniProt browser page: https://www.uniprot.org/uniprotkb/Q9GZN7
- OMIM gene 614574: https://omim.org/entry/614574
- Human Protein Atlas ROGDI: https://www.proteinatlas.org/ENSG00000067836-ROGDI

Why this matters:
A wrong protein identity would poison every downstream conclusion: cargo size, protein function, domain interpretation, structural homology, potency assay design, and gene-therapy risk assessment. The corrected identity makes ROGDI a small intracellular protein with structural and complex-biology questions, not a simple catalytic replacement program.

---

## 4. Protein structure and function

ROGDI is best treated as a non-secreted intracellular scaffold/adaptor protein. The strongest structural evidence comes from the 2017 crystal-structure study of human ROGDI.

Structural facts:
- PDB 5XQH: truncated human ROGDI structure.
- PDB 5XQI: full-length human ROGDI structure.
- UniProt Q9GZN7 links both PDB entries.
- Pfam: PF10259.
- InterPro: IPR028241.
- RCSB describes an elongated curved structure with an alpha-domain four-helix bundle and a beta-sheet domain.

Evidence:
- Lee et al. 2017 PubMed: https://pubmed.ncbi.nlm.nih.gov/28638151/
- RCSB PDB 5XQH: https://www.rcsb.org/structure/5XQH
- RCSB PDB 5XQI: https://www.rcsb.org/structure/5XQI
- UniProt Q9GZN7 cross-references: https://www.uniprot.org/uniprotkb/Q9GZN7

Functional interpretation:
The 2025 Rabconnectin-3 study connects ROGDI to Rabconnectin-3-associated V-ATPase biology. That is crucial for gene therapy because V-ATPase regulates acidification of organelles such as lysosomes and synaptic vesicles. This provides a biologically plausible bridge between neurological disease and enamel/mineralization phenotypes.

Evidence:
- PubMed 40049412: https://pubmed.ncbi.nlm.nih.gov/40049412/
- PMC full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC11997317/

Gene-therapy implication:
The potency assay should not be based on a generic catalytic readout. It should use orthogonal evidence:
1. Correct ROGDI protein expression.
2. Correct intracellular localization.
3. Rabconnectin-3 or relevant protein-complex interaction.
4. Rescue of lysosomal or synaptic-vesicle acidification phenotypes where measurable.
5. Rescue of neuronal excitability or synaptic phenotypes in patient-derived cells.

---

## 5. Cellular localization and affected tissues

Reported/annotated localization:
- Nuclear envelope.
- Neuronal processes: axon, dendrite, perikaryon, presynapse, synaptic vesicle contexts.
- Acidic organelle context through Rabconnectin-3 / V-ATPase biology.

Evidence:
- UniProt Q9GZN7: https://www.uniprot.org/uniprotkb/Q9GZN7
- 2017 ROGDI structure and KTS mechanism paper: https://pubmed.ncbi.nlm.nih.gov/28638151/
- 2025 Rabconnectin-3 / V-ATPase paper: https://pubmed.ncbi.nlm.nih.gov/40049412/

Affected therapeutic tissues:
1. CNS neurons: highest priority because of epilepsy and neurodevelopmental impairment.
2. Ameloblast-lineage tooth tissue: important but difficult to target and time-limited.
3. Kidney: lower priority but relevant because nephrocalcinosis is reported.
4. Sweat gland/ectodermal tissues: relevant to hypohidrosis, but not the first life-limiting endpoint.

Important constraint:
ROGDI is intracellular and non-secreted. Therefore, therapeutic benefit is likely cell-autonomous. AAV transduction must reach enough disease-relevant cells; neighboring corrected cells are unlikely to rescue uncorrected cells by secreting ROGDI.

---

## 6. Gene-therapy rationale

Why ROGDI remains a plausible GT target:

| Factor | Assessment | Evidence / reasoning |
|---|---|---|
| Genetic mechanism | Favorable | KTS is autosomal recessive; pathogenic variants are consistent with loss of function. |
| Cargo size | Very favorable | 287 aa protein = about 861 bp amino-acid coding region; excellent AAV margin. |
| Disease severity | Favorable | Severe epilepsy and neurodevelopmental impairment justify high-effort rare-disease development. |
| Unmet need | Favorable | No disease-modifying therapy exists. |
| CNS precedent | Moderate/favorable | AAV9 has clinical precedent in early-life CNS-directed gene replacement. |
| Potency assay | Challenging | ROGDI requires custom localization/complex/function assays. |
| Tissue reach | Challenging | CNS and enamel-forming tissues create a delivery mismatch. |
| Cross-correction | Challenging | Intracellular non-secreted protein; direct transduction likely needed. |

Overall conclusion:
ROGDI is not a simple program, but it is still a rational CNS-first gene-addition candidate if the preclinical plan is built around corrected biology.

---

## 7. AAV vector assessment

Cargo-size estimate:

| Component | Approximate size |
|---|---:|
| ROGDI amino-acid coding region | 861 bp |
| hSYN1 promoter | about 470 bp |
| polyA / regulatory sequence | about 100-300 bp depending design |
| AAV ITRs | about 290-300 bp total |
| Estimated compact cassette | about 1.7-2.0 kb |
| AAV practical limit | about 4.7 kb |

Verdict: PASS. ROGDI has excellent AAV cargo margin.

Recommended first-pass construct:
- Vector: AAV9 for CNS-first proof-of-concept.
- Promoter: hSYN1 for neuron-biased expression.
- Cargo: human ROGDI Q9GZN7 cDNA, sequence-verified.
- Route: systemic early-life IV or intrathecal, selected after biodistribution and toxicity comparison.
- Primary endpoint: CNS rescue, not dental rescue.

Evidence for AAV9 precedent:
- FDA approval announcement for Zolgensma: https://www.fda.gov/news-events/press-announcements/fda-approves-novel-gene-therapy-treat-children-spinal-muscular-atrophy

Caveat:
AAV9 precedent does not prove ROGDI efficacy. It only supports feasibility of an early-life CNS-directed AAV platform. ROGDI-specific success depends on direct neuronal transduction, correct localization, and a valid potency assay.

---

## 8. The dental paradox

Problem:
KTS affects both the brain and tooth enamel. Brain rescue requires CNS-directed delivery. Enamel defects arise from ameloblast biology during tooth development, and formed enamel does not remodel like bone.

Why this is hard:
- A CNS route is not expected to robustly correct ameloblasts.
- Dental-directed delivery is not expected to correct CNS neurons.
- Timing matters because enamel formation is developmentally limited.

Protocol decision:
Prioritize CNS rescue as the primary objective because epilepsy and neurodevelopmental disease drive severe morbidity. Dental outcomes should be explicitly framed as residual morbidity, a secondary/exploratory endpoint, or a future separate delivery program.

---

## 9. Preclinical strategy

Milestone 1: source-lock and construct design
- Reconfirm UniProt Q9GZN7 by live query.
- Lock the transcript/cDNA convention before vector design.
- Sequence-verify the cDNA.
- Avoid copying any stale scaffolded accession or protein annotation.

Milestone 2: patient-cell models
- Generate patient-derived iPSC neurons or use available disease-relevant cells.
- Confirm reduced or absent ROGDI protein.
- Define disease-relevant phenotypes: localization, acidic organelle function, synaptic vesicle markers, neuronal excitability.

Milestone 3: vector expression and potency
- Produce AAV9-hSYN1-ROGDI.
- Confirm protein expression and localization.
- Measure Rabconnectin-3-linked interaction or downstream V-ATPase/acidification readouts.
- Compare dose levels to avoid overexpression or mislocalization.

Milestone 4: animal proof-of-concept
- Use a validated Rogdi-deficient animal model if available.
- Assess CNS biodistribution, ROGDI protein expression, seizure burden, survival, behavior, and safety.
- Treat dental histology as secondary/exploratory.

Milestone 5: IND-enabling package
- Develop release assays: vector identity, genome integrity, titer, purity.
- Develop potency assays: expression, localization, complex interaction, cell-based rescue.
- Run GLP toxicology and biodistribution.
- Engage regulators early on potency assay relevance.

---

## 10. Risk assessment and mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Incorrect source identity | Low after correction, high if not checked | High | Re-run live UniProt/OMIM/Orphanet verification at every fixture refresh. |
| Cell-autonomous delivery failure | High | High | Quantify direct neuronal transduction; do not assume cross-correction. |
| Dental/CNS mismatch | High | Moderate | Make CNS rescue primary; treat dental rescue as secondary or separate. |
| Overexpression / stoichiometric toxicity | Moderate | Moderate | Use neuron-biased promoter, dose-ranging, localization assays, and protein-complex assays. |
| Potency assay uncertainty | High | High | Build orthogonal assays around expression, localization, Rabconnectin-3 interaction, V-ATPase biology, and neuronal rescue. |
| AAV toxicity or immune response | Moderate | High | Screen anti-AAV antibodies, monitor liver/CNS/DRG toxicity, compare IV vs intrathecal exposure. |
| Weak animal model translation | Moderate | High | Use both patient-cell and animal evidence before IND-enabling spend. |

---

## 11. Scoring summary for framework v0.2

| Dimension | Score | Rationale |
|---|---:|---|
| Structural homology | 0.50 | Human ROGDI structures exist, but no close approved GT cargo surrogate. |
| Sequence identity | 0.35 | No strong approved-cargo paralog precedent. |
| Domain similarity | 0.55 | RAVE2/Rogdi annotations support mechanism, but therapeutic precedent is immature. |
| Size compatibility | 0.98 | About 861 bp amino-acid coding region; excellent AAV margin. |
| Tissue tropism | 0.45 | AAV9 can support CNS strategy; enamel remains difficult. |
| Route-of-administration precedent | 0.80 | Early-life AAV9 CNS precedent exists. |
| Promoter match | 0.70 | hSYN1 is plausible for neuronal proof-of-concept. |
| Localization match | 0.45 | Intracellular localization and complex stoichiometry must be proven. |
| Immunogenicity | 0.60 | Self-protein helps; AAV capsid and optimized sequence risks remain. |
| Therapeutic window | 0.55 | CNS window likely early; dental window is more constrained. |
| Codon optimization | 0.85 | Short coding sequence makes construct design easy, but expression must be tuned. |
| Platform depth | 0.70 | AAV9 platform precedent exists; ROGDI-specific precedent does not. |

Composite score: approximately 0.62 using the current unweighted v0.2 implementation.
Gate status: PASS for size compatibility.
Interpretation: promising but technically demanding; proceed only with corrected biology and strong potency-assay development.

---

## 12. Go / no-go framework

Green-light criteria:
1. Live source verification still confirms Q9GZN7 / ROGDI / 287 aa.
2. Sequence-verified AAV-ROGDI expresses correctly in patient-derived neurons.
3. ROGDI localizes to relevant intracellular compartments.
4. At least one mechanism-linked cell phenotype is rescued.
5. Animal studies show CNS biodistribution and meaningful functional benefit at a tolerable dose.
6. Regulators accept the potency assay logic for a non-secreted intracellular scaffold/adaptor protein.

Kill criteria:
1. Correct ROGDI cannot be expressed or localized in disease-relevant cells.
2. Functional assays show no rescue despite adequate expression.
3. Therapeutic dose causes unacceptable toxicity.
4. CNS biodistribution is inadequate at tolerable exposure.
5. Potency assays cannot be linked convincingly to disease mechanism.

---

## 13. Final conclusion

The corrected audit changes the ROGDI program from a generic small-enzyme replacement concept into a much more specific intracellular scaffold/adaptor rescue problem. The good news is that the gene is very small and the inheritance model supports gene addition. The hard part is proving that AAV-delivered ROGDI reaches the right CNS cells, localizes correctly, restores Rabconnectin-3 / V-ATPase-linked biology, and produces a measurable neurological benefit without overexpression toxicity.

Recommended next action: keep ROGDI as the primary framework case study, but make the paper and protocol emphasize source verification, cell-autonomous delivery, custom potency assays, and the dental/CNS delivery mismatch. This is scientifically stronger than pretending the program is straightforward.
