# report.py — Nano-rare GT Framework
"""Jinja2 report renderer."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from nanogt.models import Disease, Gene, Protein, ScoreBreakdown, Vector


class ReportRenderer:
    """Renders framework reports from Jinja2 templates."""

    def __init__(self, templates_dir: Path | None = None) -> None:
        if templates_dir is None:
            templates_dir = Path(__file__).with_name("templates")
        self.env = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            autoescape=select_autoescape(["html", "xml"]),
        )

    def render_protocol(
        self,
        disease: Disease,
        gene: Gene,
        protein: Protein,
        vector: Vector,
        scores: ScoreBreakdown,
        output_path: Path,
    ) -> Path:
        """Render the Standardised Gene Therapy Protocol for a single match."""
        template = self.env.get_template("protocol.md.j2")

        # Build composite score
        composite = self._calculate_composite(scores)

        # Build context
        ctx = {
            "disease": disease,
            "gene": gene,
            "protein": protein,
            "vector": vector,
            "scores": scores,
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "overall_assessment": self._assess_overall(scores, gene),
            "composite_score": composite,
            "confidence": self._confidence_label(composite),
            "gate_status": "PASS" if all(scores.must_pass_gates.values()) else "FAIL",
            # ROGDI-specific rich data (for v0.1 deep-dive)
            "disease_description": self._load_disease_description(disease),
            "unmet_need": self._load_unmet_need(disease),
            "clinical_course": self._load_clinical_course(disease),
            "protein_function": self._load_protein_function(gene),
            "cellular_localization": self._load_localization(gene),
            "expression_pattern": self._load_expression(gene),
            "therapeutic_rationale": self._load_rationale(gene, disease),
            "inheritance_mechanism": self._load_inheritance(gene, disease),
            "therapeutic_window": self._load_window(gene, disease),
            "estimated_total_cargo": gene.cds_length_bp + 1500 if gene.cds_length_bp else 3000,
            "cargo_status": "PASS ✅" if (gene.cds_length_bp or 9999) <= vector.cargo_limit_bp else "FAIL ❌",
            "promoter": self._recommend_promoter(disease, gene),
            "delivery_route": self._recommend_route(disease, gene, vector),
            "dosing_age": self._recommend_age(disease),
            "vector_justification": self._vector_justification(vector, disease, gene),
            "milestone_1": self._milestone_1(),
            "milestone_2": self._milestone_2(),
            "milestone_3": self._milestone_3(),
            "milestone_4": self._milestone_4(),
            "regulatory_designation": self._regulatory_designation(disease),
            "precedent_programs": self._precedent_programs(),
            "ind_timeline": self._ind_timeline(),
            "risks": self._build_risks(disease, gene, vector),
            "scoring_dimensions": self._build_scoring_dimensions(scores),
            "go_no_go_items": self._go_no_go_items(),
            "kill_criteria": self._kill_criteria(),
            "green_light_criteria": self._green_light_criteria(),
            "conclusions": self._conclusions(disease, gene, scores),
        }

        rendered = template.render(ctx)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered)
        return output_path

    @staticmethod
    def _calculate_composite(scores: ScoreBreakdown) -> float:
        # Simple average for v0.1; weighted in future versions
        vals = [
            scores.structural_homology,
            scores.sequence_identity,
            scores.domain_similarity,
            scores.size_compatibility,
            scores.tissue_tropism,
            scores.roa_precedent,
            scores.promoter_match,
            scores.localization_match,
            scores.immunogenicity,
            scores.therapeutic_window,
            scores.codon_optimization,
            scores.platform_depth,
        ]
        return sum(vals) / len(vals)

    @staticmethod
    def _assess_overall(scores: ScoreBreakdown, gene: Gene) -> str:
        if not all(scores.must_pass_gates.values()):
            return "REJECTED — Fails must-pass cargo gate"
        return "PROMISING CANDIDATE with manageable risks"

    @staticmethod
    def _confidence_label(score: float) -> str:
        if score >= 0.75:
            return "high"
        if score >= 0.5:
            return "medium"
        return "low"

    # ---- ROGDI-specific content loaders (v0.1 hardcoded deep-dive) ----

    @staticmethod
    def _load_disease_description(disease: Disease) -> str:
        return (
            "Kohlschütter-Tönz syndrome (KTS) is a rare autosomal recessive disorder "
            "characterized by the triad of amelogenesis imperfecta (defective enamel), "
            "early-onset epilepsy, and progressive psychomotor regression. First described "
            "in 1974, it belongs to the ectodermal dysplasias. Affected children develop "
            "yellow-brown, hypoplastic teeth and experience severe intellectual disability, "
            "often accompanied by spasticity and autistic features. Survival into adulthood "
            "is uncommon; most patients die from status epilepticus or aspiration pneumonia."
        )

    @staticmethod
    def _load_unmet_need(disease: Disease) -> str:
        return (
            "No disease-modifying therapy exists. Current management is entirely supportive: "
            "multiple antiepileptic drugs, physical therapy, dental restoration, and "
            "nutritional support. The underlying genetic defect has never been addressed "
            "therapeutically. Gene therapy offers a rational path to disease modification "
            "because the gene is small, the inheritance is autosomal recessive with loss-of-function "
            "mutations, and the most disabling manifestations (CNS) are potentially "
            "rescuable with a single systemic vector dose."
        )

    @staticmethod
    def _load_clinical_course(disease: Disease) -> str:
        return (
            "Seizures typically begin in infancy (often within the first year). Dental "
            "abnormalities become visible in early childhood. Psychomotor delay is progressive; "
            "many patients lose previously acquired skills. Nephrocalcinosis has been reported "
            "in some cases. Hypohidrosis (reduced sweating) may cause heat intolerance. "
            "Life expectancy is significantly shortened."
        )

    @staticmethod
    def _load_protein_function(gene: Gene) -> str:
        return (
            "ROGDI encodes GMP reductase 2, an enzyme that catalyzes the NADPH-dependent "
            "deamination of GMP to IMP. It functions in purine nucleotide interconversion. "
            "Recent evidence (2025) reveals that ROGDI is also a Rabconnectin-3 subunit "
            "(Rav2 homolog), regulating V-ATPase assembly in lysosomes and synaptic vesicles. "
            "This dual function may explain the multi-system phenotype: GMP reductase loss "
            "causes metabolic imbalance, while V-ATPase dysregulation affects enamel acid handling "
            "and synaptic vesicle acidification."
        )

    @staticmethod
    def _load_localization(gene: Gene) -> str:
        return (
            "Primarily cytosolic (GO:0005829). Critically, ROGDI is presynaptically localized "
            "in neurons — a 2017 study showed GFP-tagged recombinant ROGDI enriches at "
            "presynaptic boutons. This means therapeutic transgene expression must achieve "
            "sufficient levels in presynaptic terminals, not just neuronal soma."
        )

    @staticmethod
    def _load_expression(gene: Gene) -> str:
        return (
            "Highly expressed in brain (hippocampus, cortex), heart, skeletal muscle, "
            "kidney, liver, and testis. Low expression in colon, thymus, and peripheral "
            "blood. The broad expression pattern is consistent with its metabolic housekeeping "
            "function but complicates tissue-specific targeting."
        )

    @staticmethod
    def _load_rationale(gene: Gene, disease: Disease) -> str:
        return (
            "Gene therapy is appropriate because: (1) ROGDI is a small gene (≈1044 bp) that "
            "fits comfortably within AAV packaging limits; (2) KTS results from autosomal "
            "recessive loss-of-function mutations, making simple gene addition theoretically "
            "curative; (3) the most disabling manifestations (epilepsy, neurodevelopmental delay) "
            "occur in tissues accessible to systemically administered AAV9; (4) there is no "
            "known dominant-negative mechanism; (5) a Rogdi knockout mouse exists, providing "
            "a preclinical model."
        )

    @staticmethod
    def _load_inheritance(gene: Gene, disease: Disease) -> str:
        return (
            "KTS follows autosomal recessive inheritance. Pathogenic variants include "
            "nonsense mutations, splice-site disruptions, and frameshift deletions. "
            "Compound heterozygosity is common. The protein is truncated or absent in "
            "affected individuals, consistent with a loss-of-function mechanism. "
            "Gene replacement therapy (supplying a wild-type copy) is the canonical approach "
            "for AR LoF disorders and has succeeded in SMA (SMN1), LCA2 (RPE65), and MLD (ARSA)."
        )

    @staticmethod
    def _load_window(gene: Gene, disease: Disease) -> str:
        return (
            "The therapeutic window is uncertain but likely exists. In SMA (Zolgensma), "
            "neonatal treatment produces the best outcomes, but treatment in infants up to "
            "6 months still yields meaningful benefit. For KTS, early intervention before "
            "irreversible neurodegeneration is likely critical—ideally in the first weeks of "
            "life, though pre-symptomatic newborn screening does not yet exist. "
            "Dental enamel defects may be irreversible once formed, suggesting that even "
            "perfect CNS rescue would leave residual dental morbidity."
        )

    @staticmethod
    def _recommend_promoter(disease: Disease, gene: Gene) -> str:
        return (
            "Human synapsin-1 (hSYN1) promoter, ~470 bp. Rationale: neuron-specific expression "
            "minimizes off-target expression in liver and muscle; hSYN1 is the most widely "
            "used neuronal promoter in AAV GT programs (including CNS clinical trials); "
            "it drives expression in both excitatory and inhibitory neurons, essential for "
            "epilepsy control. Alternative: CamKIIα if forebrain bias is desired."
        )

    @staticmethod
    def _recommend_route(disease: Disease, gene: Gene, vector: Vector) -> str:
        return (
            "Systemic intravenous (IV) infusion, preferably in the neonatal or early infant "
            "period. Rationale: AAV9 efficiently crosses the blood-brain barrier in young "
            "patients (Zolgensma precedent); provides brain-wide distribution; minimally invasive; "
            "avoids neurosurgical risks of intracranial injection. Backup: intrathecal delivery "
            "if systemic dosing is limited by liver toxicity concerns."
        )

    @staticmethod
    def _recommend_age(disease: Disease) -> str:
        return (
            "Neonatal (birth to 14 days) or early infancy (<3 months). Rationale: BBB "
            "permeability to AAV9 is highest in neonates; neuronal circuitry is still plastic; "
            "seizure threshold may be modifiable before hyperexcitable networks consolidate."
        )

    @staticmethod
    def _vector_justification(vector: Vector, disease: Disease, gene: Gene) -> str:
        return (
            f"{vector.serotype} is recommended based on: (1) proven CNS tropism with "
            f"{vector.clinical_precedents} clinical programs providing safety and regulatory precedent; "
            f"(2) efficient BBB crossing in infants (Zolgensma model); (3) non-replicative, "
            f"non-pathogenic profile well-established in >1000 treated patients; (4) cargo limit "
            f"({vector.cargo_limit_bp} bp) comfortably exceeds ROGDI CDS + promoter + regulatory elements."
        )

    @staticmethod
    def _milestone_1() -> str:
        return (
            "Establish patient-derived iPSC lines from KTS probands (available from "
            "dent pulp or skin fibroblasts). Differentiate to cortical and hippocampal "
            "neurons. Confirm ROGDI protein absence by Western blot and immunofluorescence. "
            "Verify presynaptic targeting deficit and V-ATPase dysfunction (LysoTracker assays)."
        )

    @staticmethod
    def _milestone_2() -> str:
        return (
            "Clone codon-optimized human ROGDI cDNA into AAV9/hSYN1 backbone. Verify vector "
            "genome integrity by restriction digest and Sanger sequencing. Produce small-scale "
            "AAV9 vector using triple-transfection in HEK293. Titrate by qPCR (vg/mL). "
            "Confirm ROGDI expression and presynaptic trafficking in iPSC-neurons."
        )

    @staticmethod
    def _milestone_3() -> str:
        return (
            "Inject Rogdi knockout mice (available from JAX or literature) with AAV9-hSYN1-ROGDI "
            "via IV (neonatal) or intracerebroventricular (ICV). Assess: (a) survival and "
            "seizure frequency (video-EEG), (b) dental enamel histology, (c) brain ROGDI protein "
            "levels by WB/IF, (d) behavioral tests (rotarod, open field). Primary endpoint: "
            "≥50% reduction in seizure burden vs. untreated KO at 8 weeks."
        )

    @staticmethod
    def _milestone_4() -> str:
        return (
            "Biodistribution study in immunocompetent mice: qPCR vector genome in brain, "
            "liver, spleen, heart, kidney. Toxicology in rats: single ascending dose with "
            "28-day observation. Assess: liver enzymes (ALT/AST), histopathology, anti-capsid "
            "antibody titers. Dose-finding: bracket around proposed clinical dose scaled by "
            "brain:body weight ratio."
        )

    @staticmethod
    def _regulatory_designation(disease: Disease) -> str:
        return (
            "Orphan Drug Designation (ODD) is strongly recommended and likely achievable: "
            "prevalence <200,000 in US; no approved therapy; serious/life-threatening. "
            "RMAT (Regenerative Medicine Advanced Therapy) may be sought if preclinical data "
            "shows substantial improvement over existing care. Pediatric Investigation Plan (PIP) "
            "will be required in EU. Fast Track and Breakthrough Therapy are feasible if "
            "clinical data shows dramatic efficacy in a small open-label study."
        )

    @staticmethod
    def _precedent_programs() -> list[dict[str, Any]]:
        return [
            {
                "name": "Zolgensma (onasemnogene abeparvovec)",
                "indication": "Spinal muscular atrophy (SMA)",
                "relevance": "Single-dose IV AAV9 gene replacement in infants. Proves BBB crossing, CNS rescue, and neonatal dosing safety. Regulatory pathway (ODD, priority review) is directly applicable.",
            },
            {
                "name": "Luxturna (voretigene neparvovec)",
                "indication": "RPE65-associated retinal dystrophy",
                "relevance": "First FDA-approved in vivo GT. Less relevant for CNS but demonstrates AAV gene replacement regulatory precedent and long-term durability data.",
            },
            {
                "name": "Elevidys (delandistrogene moxeparvovec)",
                "indication": "Duchenne muscular dystrophy",
                "relevance": "AAVrh74 capsid with micro-dystrophin. Demonstrates systemic IV delivery to muscle + CNS and accelerated approval pathway under subpart H.",
            },
        ]

    @staticmethod
    def _ind_timeline() -> str:
        return (
            "Estimated 4–5 years from target validation to IND: Year 1–2: vector design, "
            "iPSC validation, small-scale AAV production. Year 2–3: rodent efficacy, "
            "dose-finding, GLP tox. Year 3–4: NHP biodistribution (if required for CNS). "
            "Year 4–5: CMC scale-up, regulatory pre-submission meeting, IND filing."
        )

    @staticmethod
    def _build_risks(disease: Disease, gene: Gene, vector: Vector) -> list[dict[str, Any]]:
        return [
            {
                "name": "Immunogenicity (anti-capsid)",
                "likelihood": "High",
                "impact": "Moderate",
                "mitigation": "Pre-screen for AAV9 NABs; corticosteroid prophylaxis (as in Zolgensma program); transient immunosuppression if needed.",
            },
            {
                "name": "Overexpression toxicity",
                "likelihood": "Moderate",
                "impact": "Moderate",
                "mitigation": "Use neuron-specific promoter (hSYN1) to restrict expression; scAAV for lower expression; incorporate miRNA de-targeting of liver.",
            },
            {
                "name": "Delivery failure (dental paradox)",
                "likelihood": "High",
                "impact": "Moderate",
                "mitigation": "Accept dental morbidity as secondary; focus CNS rescue as primary endpoint; consider dual-vector approach for ameloblasts.",
            },
            {
                "name": "Preclinical model failure",
                "likelihood": "Moderate",
                "impact": "High",
                "mitigation": "Use both Rogdi KO mouse AND patient-derived iPSC neurons; validate rescue in both systems before IND.",
            },
            {
                "name": "Regulatory uncertainty (novel mechanism)",
                "likelihood": "Moderate",
                "impact": "Moderate",
                "mitigation": "Engage FDA CBER early (pre-IND Type B meeting); frame as GT for epileptic encephalopathy, a well-understood indication class.",
            },
        ]

    @staticmethod
    def _build_scoring_dimensions(scores: ScoreBreakdown) -> list[dict[str, Any]]:
        return [
            {"name": "Structural Homology", "score": scores.structural_homology, "weight": 1.0, "notes": "IMPDH/GMPR family has extensive structural precedent but exact ROGDI 3D fold is rare."},
            {"name": "Sequence Identity", "score": scores.sequence_identity, "weight": 1.0, "notes": "GMPR1 ~65% identity provides partial functional redundancy evidence."},
            {"name": "Domain Similarity", "score": scores.domain_similarity, "weight": 1.0, "notes": "Single IMPDH/GMPR domain — well-characterized catalytic fold."},
            {"name": "Size Compatibility", "score": scores.size_compatibility, "weight": 2.0, "notes": "~1044 bp is excellent; leaves margin for regulatory elements. Hard gate."},
            {"name": "Tissue Tropism", "score": scores.tissue_tropism, "weight": 1.5, "notes": "AAV9 reaches CNS but not ameloblasts. Partial tissue match."},
            {"name": "RoA Precedent", "score": scores.roa_precedent, "weight": 1.5, "notes": "IV neonatal AAV9 precedent established by Zolgensma."},
            {"name": "Promoter Match", "score": scores.promoter_match, "weight": 1.0, "notes": "hSYN1 is well-validated for CNS neurons."},
            {"name": "Localization Match", "score": scores.localization_match, "weight": 1.0, "notes": "Presynaptic trafficking may require endogenous localization signals in transgene."},
            {"name": "Immunogenicity", "score": scores.immunogenicity, "weight": 1.0, "notes": "Self-protein but codon-optimization may expose new epitopes."},
            {"name": "Therapeutic Window", "score": scores.therapeutic_window, "weight": 1.5, "notes": "Likely exists in infancy before neurodegeneration consolidates."},
            {"name": "Codon Optimization", "score": scores.codon_optimization, "weight": 0.5, "notes": "Standard practice; minimal risk."},
            {"name": "Platform Depth", "score": scores.platform_depth, "weight": 1.0, "notes": "AAV9 + hSYN1 combination has 8+ clinical programs."},
        ]

    @staticmethod
    def _go_no_go_items() -> list[str]:
        return [
            "ROGDI protein expression confirmed in presynaptic terminals of transduced iPSC-neurons",
            "Seizure burden reduction ≥50% in Rogdi KO mouse after AAV9-hSYN1-ROGDI",
            "No unacceptable toxicity in GLP rodent study ( Grade ≤2 )",
            "CMC: scalable AAV9 production meeting ≥1e15 vg/dose in Sf9 or HEK system",
            "Regulatory: pre-IND Type B meeting minutes from FDA CBER",
            "Anti-AAV9 NAB prevalence established in target population",
            "Natural history data published (at least 20-patient cohort)",
        ]

    @staticmethod
    def _kill_criteria() -> str:
        return (
            "(1) No measurable ROGDI protein in brain after systemic AAV9 at tolerated dose; "
            "(2) Seizure burden worsens or mortality increases in treated vs. untreated KO mice; "
            "(3) Severe hepatotoxicity (ALT >10× ULN) at therapeutic dose in NHP or rodent; "
            "(4) Immunogenicity prevents redosing and initial dose shows <6-month durability; "
            "(5) Regulatory pathway requires >5-year pivotal trial (not feasible for ultra-rare disease)."
        )

    @staticmethod
    def _green_light_criteria() -> str:
        return (
            "(1) Robust presynaptic ROGDI expression in brain at ≥1% of WT levels; "
            "(2) ≥50% seizure reduction + improved survival in rodent model; "
            "(3) Dose-response relationship confirming efficacy in at least two species; "
            "(4) GLP tox package clean with NOAEL ≥5× projected clinical dose; "
            "(5) ODD granted; FDA CBER agreeable to accelerated approval based on biomarker + functional endpoint."
        )

    @staticmethod
    def _conclusions(disease: Disease, gene: Gene, scores: ScoreBreakdown) -> str:
        return (
            "ROGDI is a compelling but challenging gene therapy candidate for Kohlschütter-Tönz "
            "syndrome. The gene is small, the inheritance is straightforward AR LoF, and AAV9 "
            "systemic delivery has precedent for CNS rescue in infants. However, the multi-system "
            "nature (brain + teeth + kidney), the intracellular presynaptic localization, and the "
            "lack of any GT clinical data for ROGDI make this a high-risk, high-reward program. "
            "The recommended path forward is a focused preclinical program centered on iPSC-neuron "
            "and Rogdi KO mouse rescue, with a clear go/no-go decision at 18 months based on "
            "efficacy and safety in the rodent model."
        )
