# Figure Captions and Notes

## Figure 1: Pipeline Schematic
<!-- Type: Flowchart / block diagram -->
<!-- Tool: draw.io, Excalidraw, or matplotlib -->
<!-- Elements: 9 stages as colored blocks; data inputs as document icons; decision diamonds for hard gates; final output as report stack -->
<!-- Color scheme: accessible palette (not red-green dependent) -->
<!-- Resolution: 300 DPI, width ~180mm -->

**Suggested caption:** "Overview of the 9-stage computational pipeline. Input is an Orphanet or OMIM identifier. Each stage queries public biological databases and applies scoring logic. Hard gates (orange diamonds) auto-reject or flag matches if critical thresholds are not met. Final output is a ranked list of surrogate-precedent gene therapy strategies with auto-generated protocols."

---

## Figure 2: Multi-Dimensional Scoring Radar Chart
<!-- Type: Radar / spider chart -->
<!-- Tool: matplotlib or seaborn -->
<!-- 11 axes: structural homology, sequence identity, domain similarity, size compatibility, tissue tropism, RoA precedent, promoter match, localization match, immunogenicity, therapeutic window, codon optimization, platform depth -->
<!-- Fill with one representative case study (e.g., top CNS match) -->

**Suggested caption:** "Multi-dimensional score profile for the top-matched prospective case study (CNS ultra-rare disease, Case Study 1). Each axis represents a normalized 0–1 score. The shaded area illustrates the composite area under the scoring profile. High platform depth and structural homology scores drive the top ranking despite moderate promoter match novelty."

---

## Figure 3: Retrospective Validation Summary
<!-- Type: Grouped bar chart -->
<!-- Tool: matplotlib -->
<!-- X-axis: Luxturna, Zolgensma, Negative Control -->
<!-- Y-axis: composite score -->
<!-- Dashed line: threshold for high-confidence recommendation -->

**Suggested caption:** "Retrospective validation of the scoring engine against two approved gene therapies and one clinically discontinued program. Luxturna and Zolgensma achieve composite scores above the high-confidence threshold (dashed line), while the negative control (discontinued due to immunogenicity) is correctly down-ranked. Individual dimension contributions are shown as stacked segments."

---

## Figure 4: Sensitivity Analysis Heatmap
<!-- Type: Heatmap -->
<!-- Tool: seaborn -->
<!-- X-axis: weight perturbation (-20%, baseline, +20%) per dimension -->
<!-- Y-axis: disease query cases -->
<!-- Color: rank of top match (stable = consistent color) -->

**Suggested caption:** "Sensitivity of top-match ranking to +/−20% perturbations in individual scoring dimension weights. Color stability across a row indicates that a disease’s top match is robust to weight variation. Structural homology and platform depth exert the strongest influence on rank stability for the tested retrospective and prospective cases."

---

## Figure 5: Prospective Protocol Comparison
<!-- Type: Side-by-side structured table + schematic -->
<!-- Tool: table in Markdown/Word + vector schematic -->
<!-- Left: CNS case (intrathecal AAV9) -->
<!-- Right: Hepatic case (IV AAV8/AAV9) -->

**Suggested caption:** "Auto-generated gene therapy protocols for the two prospective case studies. Left: CNS ultra-rare disease with intrathecal AAV9 delivery and ubiquitous promoter due to broad neuronal target requirement. Right: Metabolic hepatic disease with IV AAV8 delivery and liver-specific TBG promoter. Both protocols were generated in under two minutes and are consistent with clinical precedents for the respective tissues."

---

## Supplementary Table 1: Full Surrogate Database
<!-- CSV with columns: program_name, disease, target_gene, vector_serotype, promoter, target_tissue, cds_length_bp, approval_status, clinical_program_count, literature_DOI -->

## Supplementary Table 2: Complete Scoring Results
<!-- One row per disease query, columns = all ScoreBreakdown fields + composite + confidence -->

## Supplementary Note 1: Weight Selection Justification
<!-- Why each dimension included, weight rationale, sensitivity analysis protocol -->
