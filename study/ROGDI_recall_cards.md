# ROGDI Recall Cards

These cards are based on `docs/ROGDI-deep-dive.md` and focus on reusable gene-therapy framework knowledge.

## 1. Core identity

**Question:** What disease is the ROGDI case study about?

**Answer:** Kohlschutter-Tonz syndrome, also called amelocerebrohypohidrotic syndrome.

## 2. Core identity

**Question:** What is the Orphanet ID for the ROGDI/KTS disease case?

**Answer:** ORPHA:1946.

## 3. Core identity

**Question:** What are the two OMIM identifiers used in the ROGDI audit?

**Answer:** OMIM phenotype 226750 and OMIM gene 614574.

## 4. Core identity

**Question:** What is the correct gene symbol for the case study?

**Answer:** ROGDI.

## 5. Core identity

**Question:** What is the correct UniProt accession for human ROGDI?

**Answer:** Q9GZN7.

## 6. Core identity

**Question:** What is the recommended protein name for UniProt Q9GZN7?

**Answer:** Protein rogdi homolog.

## 7. Core identity

**Question:** What are three aliases for ROGDI?

**Answer:** KIAA0267, FLJ22386, and RAV2.

## 8. Core identity

**Question:** What chromosome location is listed for ROGDI?

**Answer:** 16p12.1.

## 9. Core identity

**Question:** What is the protein length of ROGDI?

**Answer:** 287 amino acids.

## 10. Core identity

**Question:** What is the approximate molecular weight of ROGDI?

**Answer:** About 32.3 kDa, or 32,254 Da.

## 11. Core identity

**Question:** What is the approximate ROGDI amino-acid coding region length?

**Answer:** About 861 bp, or 864 bp if the stop codon is included by convention.

## 12. Source verification

**Question:** Why is source verification the first step before scoring a gene therapy target?

**Answer:** Because a wrong disease, gene, or protein identity poisons every downstream conclusion: cargo size, mechanism, potency assay, vector fit, and risk assessment.

## 13. Source verification

**Question:** Which source is used to confirm protein identity and sequence facts?

**Answer:** UniProt. For ROGDI, the key accession is Q9GZN7.

## 14. Source verification

**Question:** Which source is used to anchor rare disease identity?

**Answer:** Orphanet. For this case, the disease is ORPHA:1946.

## 15. Source verification

**Question:** Which source is used for disease and gene OMIM entries?

**Answer:** OMIM. For ROGDI/KTS, phenotype 226750 and gene 614574 are used.

## 16. Source verification

**Question:** What live UniProt facts were checked for Q9GZN7?

**Answer:** Primary accession, protein name, gene name, sequence length, molecular weight, and cross-references such as PDB, AlphaFoldDB, InterPro, and Pfam.

## 17. Disease biology

**Question:** What is the inheritance pattern of Kohlschutter-Tonz syndrome?

**Answer:** Autosomal recessive.

## 18. Disease biology

**Question:** Why does autosomal recessive loss of function support gene addition?

**Answer:** Because adding a working copy of the gene can, in principle, replace missing or reduced function.

## 19. Disease biology

**Question:** What are the three classic features of KTS described in the audit?

**Answer:** Amelogenesis imperfecta, infantile or early-onset epilepsy, and intellectual disability or severe neurodevelopmental impairment.

## 20. Disease biology

**Question:** Name three additional clinical features reported in KTS.

**Answer:** Spasticity, hypohidrosis or heat intolerance, and nephrocalcinosis in some patients.

## 21. Disease biology

**Question:** Why does the audit prioritize CNS rescue?

**Answer:** Because epilepsy and neurodevelopmental impairment likely dominate morbidity and mortality.

## 22. Disease biology

**Question:** Why might dental disease be hard to reverse in KTS?

**Answer:** Enamel is formed during a limited developmental window and does not remodel like bone once formed.

## 23. Protein function

**Question:** How should ROGDI be treated functionally for gene therapy planning?

**Answer:** As a non-secreted intracellular scaffold or adaptor protein, not as a simple enzyme replacement target.

## 24. Protein function

**Question:** What two PDB structures are linked to human ROGDI?

**Answer:** 5XQH and 5XQI.

## 25. Protein function

**Question:** What domain or family annotations are listed for ROGDI?

**Answer:** RAVE2/Rogdi, Rogdi_lz, InterPro IPR028241, and Pfam PF10259.

## 26. Protein function

**Question:** What 2025 biology connection is important for ROGDI?

**Answer:** ROGDI is connected to Rabconnectin-3-associated V-ATPase biology.

## 27. Protein function

**Question:** Why does the Rabconnectin-3/V-ATPase link matter?

**Answer:** It gives a plausible mechanism involving acidic organelles, lysosomes, synaptic vesicles, neurons, and enamel/mineralization biology.

## 28. Localization

**Question:** Is ROGDI secreted?

**Answer:** No. ROGDI is treated as intracellular and non-secreted.

## 29. Localization

**Question:** Why does non-secreted localization make gene therapy harder?

**Answer:** Because neighboring corrected cells are unlikely to rescue uncorrected cells by secreting the protein. The affected cells probably need direct transduction.

## 30. Localization

**Question:** What is cell-autonomous rescue?

**Answer:** A therapeutic effect that requires correction inside the affected cell itself.

## 31. Localization

**Question:** What is cross-correction?

**Answer:** Rescue of neighboring untransduced cells by a secreted therapeutic protein.

## 32. Localization

**Question:** Why is cross-correction expected to be low for ROGDI?

**Answer:** Because ROGDI is not known to be secreted.

## 33. Localization

**Question:** Name three reported or annotated ROGDI localization contexts.

**Answer:** Nuclear envelope, axon/dendrite/perikaryon, presynapse, synaptic vesicle context, or acidic organelle context.

## 34. Target tissues

**Question:** What is the highest-priority therapeutic tissue for the first ROGDI program?

**Answer:** CNS neurons.

## 35. Target tissues

**Question:** Which tooth-development cell type matters for KTS dental disease?

**Answer:** Ameloblasts, the cells responsible for enamel formation.

## 36. Target tissues

**Question:** Why is there a brain/teeth delivery mismatch?

**Answer:** A CNS-directed route is not expected to robustly correct ameloblasts, and dental-directed delivery will not rescue CNS neurons.

## 37. AAV and cargo

**Question:** What is AAV?

**Answer:** Adeno-associated virus, a small non-replicating viral vector commonly used for in vivo gene delivery.

## 38. AAV and cargo

**Question:** What practical AAV packaging limit is used in the audit?

**Answer:** About 4.7 kb.

## 39. AAV and cargo

**Question:** Why does ROGDI pass the AAV cargo-size gate?

**Answer:** Its coding sequence is about 861 bp, leaving large room for promoter, polyA, ITRs, and other regulatory elements within the AAV limit.

## 40. AAV and cargo

**Question:** What first-pass vector is recommended for the ROGDI CNS proof of concept?

**Answer:** AAV9.

## 41. AAV and cargo

**Question:** Why is AAV9 considered relevant to ROGDI?

**Answer:** It has clinical precedent for nervous-system exposure, especially early-life CNS-directed gene replacement.

## 42. AAV and cargo

**Question:** Does AAV9 precedent prove ROGDI efficacy?

**Answer:** No. It only supports platform feasibility. ROGDI-specific success still requires direct neuronal transduction, correct localization, and valid potency assays.

## 43. Construct design

**Question:** What promoter is recommended for the first ROGDI CNS proof of concept?

**Answer:** hSYN1, a compact human synapsin-1 promoter for neuron-biased expression.

## 44. Construct design

**Question:** Why use a neuron-biased promoter like hSYN1 first?

**Answer:** It matches the CNS objective and may reduce unnecessary peripheral overexpression.

## 45. Construct design

**Question:** What cargo would the first-pass ROGDI construct carry?

**Answer:** Sequence-verified human ROGDI Q9GZN7 cDNA.

## 46. Construct design

**Question:** What routes are considered for CNS-prioritized ROGDI delivery?

**Answer:** Early-life systemic IV or intrathecal delivery, selected after biodistribution and toxicity comparison.

## 47. Potency assays

**Question:** Why is a simple enzyme activity assay not enough for ROGDI?

**Answer:** ROGDI is not being treated as a simple catalytic enzyme. It likely works through localization, complex interaction, and organelle/synaptic biology.

## 48. Potency assays

**Question:** What should a ROGDI potency assay package measure?

**Answer:** Expression, intracellular localization, Rabconnectin-3 or complex interaction, V-ATPase/acidification readouts, and cell-based rescue.

## 49. Potency assays

**Question:** What patient-cell model is proposed for early ROGDI testing?

**Answer:** Patient-derived iPSC neurons, with ameloblast-lineage or dental organoid assays where possible.

## 50. Preclinical plan

**Question:** What is milestone 1 in the ROGDI preclinical strategy?

**Answer:** Source-lock and construct design: reconfirm Q9GZN7, lock transcript/cDNA convention, sequence-verify cDNA, and avoid stale annotations.

## 51. Preclinical plan

**Question:** What is milestone 2 in the ROGDI preclinical strategy?

**Answer:** Patient-cell models: generate disease-relevant cells, confirm reduced or absent ROGDI, and define disease phenotypes.

## 52. Preclinical plan

**Question:** What is milestone 3 in the ROGDI preclinical strategy?

**Answer:** Vector expression and potency: produce AAV9-hSYN1-ROGDI, confirm expression/localization, measure mechanism-linked rescue, and compare doses.

## 53. Preclinical plan

**Question:** What is milestone 4 in the ROGDI preclinical strategy?

**Answer:** Animal proof of concept: use a validated Rogdi-deficient model if available and assess biodistribution, expression, seizure burden, survival, behavior, and safety.

## 54. Preclinical plan

**Question:** What is milestone 5 in the ROGDI preclinical strategy?

**Answer:** IND-enabling package: release assays, potency assays, GLP toxicology, biodistribution, and early regulator engagement.

## 55. Risks

**Question:** What is the risk called when AAV does not reach enough affected cells?

**Answer:** Cell-autonomous delivery failure.

## 56. Risks

**Question:** How should cell-autonomous delivery failure be mitigated?

**Answer:** Quantify direct neuronal transduction and do not assume cross-correction.

## 57. Risks

**Question:** What is the dental/CNS mismatch risk?

**Answer:** A brain-focused therapy may not fix tooth enamel disease, and a dental-focused therapy will not rescue the brain.

## 58. Risks

**Question:** What is the main overexpression concern for ROGDI?

**Answer:** Stoichiometric imbalance, mislocalization, or disrupted protein-complex assembly.

## 59. Risks

**Question:** What AAV safety issues should be monitored?

**Answer:** Anti-AAV immunity, liver toxicity, CNS inflammation, and dorsal root ganglion toxicity.

## 60. Scoring

**Question:** Which ROGDI score is the strongest in the framework and why?

**Answer:** Size compatibility, because the ROGDI coding sequence is very small compared with the AAV packaging limit.

## 61. Scoring

**Question:** What composite score does the deep-dive give ROGDI approximately?

**Answer:** About 0.62 in the current unweighted v0.2 implementation.

## 62. Scoring

**Question:** What is the ROGDI gate status?

**Answer:** PASS for size compatibility.

## 63. Scoring

**Question:** Why is tissue tropism not scored as very high for ROGDI?

**Answer:** AAV9 can support a CNS strategy, but enamel-forming tissues remain hard to reach and timing-limited.

## 64. Go/no-go

**Question:** Name three green-light criteria for ROGDI.

**Answer:** Confirmed Q9GZN7/ROGDI identity, correct expression/localization in patient neurons, mechanism-linked cell rescue, animal CNS benefit at tolerable dose, and regulatory acceptance of potency logic.

## 65. Go/no-go

**Question:** Name three kill criteria for ROGDI.

**Answer:** Failure to express or localize ROGDI, no functional rescue despite expression, unacceptable toxicity, inadequate CNS biodistribution, or potency assays that cannot be linked to disease mechanism.

## 66. Reusable workflow

**Question:** What is the first reusable step when applying this framework to another disease?

**Answer:** Lock the disease, gene, and protein identity using trusted source IDs before scoring or designing a vector.

## 67. Reusable workflow

**Question:** What key facts should be collected for any new disease?

**Answer:** Disease ID, gene ID, protein ID, inheritance, mechanism, clinical features, target tissues, protein size, localization, secretion status, existing treatments, and source links.

## 68. Reusable workflow

**Question:** What is the main lesson of the corrected ROGDI audit?

**Answer:** A small gene can still be technically demanding if the protein is intracellular, non-secreted, localization-sensitive, and affects hard-to-reach tissues.
