# report.py — Nano-rare GT Framework
"""Jinja2 report renderer."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from typing import Any, TypedDict

from jinja2 import Environment, FileSystemLoader, select_autoescape

from nanogt.models import (
    Disease,
    Gene,
    Match,
    Protein,
    Report,
    ScoreBreakdown,
    Vector,
)


class ScoreRow(TypedDict):
    label: str
    score: float


class ReportRenderer:
    """Renders framework reports from Jinja2 templates."""

    def __init__(self, templates_dir: Path | None = None) -> None:
        if templates_dir is None:
            templates_dir = Path(__file__).with_name("templates")
        self.env = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            autoescape=select_autoescape(["html", "xml"]),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )
        self.env.filters["score"] = self._format_score

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
            # ROGDI-specific rich data (for v0.2 source-audited deep-dive)
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

    def render_batch_report(self, report: Report, output_path: Path) -> Path:
        """Render a concise batch match report."""
        template = self.env.get_template("batch_report.md.j2")
        ctx = {
            "report": report,
            "score_rows": self._score_rows(report.top_match) if report.top_match else [],
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
    def _format_score(value: float | int | None, places: int = 3) -> str:
        """Format report scores without exposing floating-point representation noise."""
        if value is None:
            return "n/a"
        return f"{float(value):.{places}f}"

    @staticmethod
    def _score_rows(match: Match | None) -> list[ScoreRow]:
        if match is None:
            return []
        scores = match.scores
        return [
            {"label": "Gene size compatibility", "score": scores.size_compatibility},
            {"label": "Structural homology", "score": scores.structural_homology},
            {"label": "Sequence identity to surrogate", "score": scores.sequence_identity},
            {"label": "Domain similarity", "score": scores.domain_similarity},
            {"label": "Tissue tropism match", "score": scores.tissue_tropism},
            {"label": "Route-of-administration precedent", "score": scores.roa_precedent},
            {"label": "Promoter match", "score": scores.promoter_match},
            {"label": "Subcellular localization match", "score": scores.localization_match},
            {"label": "Immunogenicity", "score": scores.immunogenicity},
            {"label": "Therapeutic window", "score": scores.therapeutic_window},
            {"label": "Codon optimization", "score": scores.codon_optimization},
            {"label": "Platform depth", "score": scores.platform_depth},
        ]

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

    # ---- ROGDI-specific content loaders (v0.2 source-audited deep-dive) ----

    @staticmethod
    def _load_disease_description(disease: Disease) -> str:
        return (
            "Kohlschütter-Tönz syndrome (KTS), also described as "
            "amelocerebrohypohidrotic syndrome, is an ultra-rare autosomal recessive "
            "neuro-ectodermal disorder. The core clinical pattern is amelogenesis "
            "imperfecta, early-onset epilepsy, severe developmental delay or regression, "
            "spasticity, and variable hypohidrosis or nephrocalcinosis. Orphanet assigns "
            "KTS to ORPHA:1946; OMIM lists the phenotype as 226750 and the ROGDI gene as "
            "614574."
        )

    @staticmethod
    def _load_unmet_need(disease: Disease) -> str:
        return (
            "No disease-modifying therapy exists. Current care is supportive: antiseizure "
            "medicines, developmental support, dental restoration, nutrition support, and "
            "management of respiratory or aspiration complications. A gene-addition strategy "
            "is biologically plausible because KTS is recessive, published pathogenic "
            "variants are consistent with loss of ROGDI function, and the coding sequence is "
            "small enough for an AAV cassette. The unresolved problem is delivery: ROGDI is "
            "intracellular and non-secreted, so affected cells probably require direct "
            "transduction rather than cross-correction."
        )

    @staticmethod
    def _load_clinical_course(disease: Disease) -> str:
        return (
            "Seizures often begin in infancy or early childhood and may be refractory. Dental "
            "enamel defects become evident as teeth erupt. Neurodevelopmental impairment can "
            "be severe and may progress with loss of skills; spasticity and profound "
            "intellectual disability have been reported. Hypohidrosis can cause heat "
            "intolerance, and nephrocalcinosis has been reported in some patients. Because "
            "enamel is formed during a time-limited developmental window, established dental "
            "defects may not be reversible even if CNS disease is modified."
        )

    @staticmethod
    def _load_protein_function(gene: Gene) -> str:
        return (
            "ROGDI encodes Protein rogdi homolog (UniProt Q9GZN7), a 287 amino-acid, "
            "approximately 32.3 kDa intracellular protein. Structural and recent cell-biologic "
            "evidence support a non-enzymatic scaffolding or adaptor role. The solved human "
            "ROGDI structures (PDB 5XQH and 5XQI) show an atypical leucine-zipper-like fold, "
            "and a 2025 study identified ROGDI as a Rabconnectin-3-associated subunit linked "
            "to V-ATPase assembly or regulation in acidic organelle biology. This changes the "
            "potency strategy: assays should measure expression, localization, complex "
            "interaction, and V-ATPase/lysosomal rescue rather than catalytic activity."
        )

    @staticmethod
    def _load_localization(gene: Gene) -> str:
        return (
            "UniProt Q9GZN7 annotates ROGDI in the nuclear envelope and neuronal compartments "
            "including presynapse, axon, perikaryon, dendrite, and synaptic vesicle contexts. "
            "The KTS literature also links ROGDI to presynaptic biology. For gene therapy, "
            "this means that simply producing protein in the soma may not be enough; the "
            "construct and expression level must preserve endogenous intracellular "
            "localization and protein-complex stoichiometry."
        )

    @staticmethod
    def _load_expression(gene: Gene) -> str:
        return (
            "Human Protein Atlas and transcriptomic resources indicate broad ROGDI expression, "
            "including nervous system and other somatic tissues. The clinical phenotype shows "
            "that neurons and enamel-forming ameloblast-lineage cells are the high-priority "
            "therapeutic tissues. The broad expression pattern argues against assuming that "
            "one tissue-specific promoter can fully normalize every tissue, but CNS rescue is "
            "the clearest first therapeutic objective."
        )

    @staticmethod
    def _load_rationale(gene: Gene, disease: Disease) -> str:
        return (
            "Gene therapy is appropriate to investigate because: (1) the ROGDI amino-acid "
            "coding region is about 861 bp, leaving large AAV packaging margin; (2) KTS is "
            "autosomal recessive and consistent with loss of function, making gene addition "
            "conceptually suitable; (3) the most life-limiting manifestations are CNS-driven "
            "epileptic and neurodevelopmental features, where AAV9 and related CNS-directed "
            "AAV approaches have clinical precedent; and (4) no approved disease-modifying "
            "therapy exists. The main caveat is that ROGDI is intracellular, so adequate "
            "cell-autonomous transduction is probably required."
        )

    @staticmethod
    def _load_inheritance(gene: Gene, disease: Disease) -> str:
        return (
            "KTS follows autosomal recessive inheritance. Reported variants include nonsense, "
            "frameshift, and splice-site changes predicted to truncate or destabilize ROGDI. "
            "The Lee et al. crystal-structure paper mapped disease variants onto the protein "
            "fold and showed why truncations or exon loss would disrupt the four-helix/beta "
            "architecture. Supplying a wild-type ROGDI copy is therefore the correct first "
            "gene-therapy hypothesis, provided expression level and localization are controlled."
        )

    @staticmethod
    def _load_window(gene: Gene, disease: Disease) -> str:
        return (
            "The CNS therapeutic window is uncertain but likely earliest in infancy, before "
            "seizure networks and neurodevelopmental injury consolidate. Dental enamel is a "
            "separate timing problem: once enamel has formed abnormally, systemic CNS-directed "
            "gene therapy is unlikely to repair it. A first-in-program strategy should define "
            "CNS endpoints as primary and treat dental outcomes as residual morbidity or as a "
            "separate delivery program."
        )

    @staticmethod
    def _recommend_promoter(disease: Disease, gene: Gene) -> str:
        return (
            "Human synapsin-1 (hSYN1) promoter, approximately 470 bp, for the first CNS "
            "proof-of-concept. Rationale: hSYN1 restricts expression toward neurons, matching "
            "the epilepsy/neurodevelopmental objective and reducing unnecessary peripheral "
            "overexpression. A low-strength ubiquitous or endogenous-style promoter should "
            "only be considered after dose-response and stoichiometry studies show that broader "
            "expression is safe and necessary."
        )

    @staticmethod
    def _recommend_route(disease: Disease, gene: Gene, vector: Vector) -> str:
        return (
            "CNS-prioritized AAV9 delivery, either neonatal/early-infant systemic IV or an "
            "intrathecal route depending on safety and biodistribution data. IV AAV9 has SMA "
            "precedent, but intrathecal delivery may reduce peripheral exposure. The selected "
            "route should be justified around brain rescue, not dental rescue, because no "
            "single plausible route is expected to restore both CNS neurons and formed enamel."
        )

    @staticmethod
    def _recommend_age(disease: Disease) -> str:
        return (
            "As early as diagnosable, ideally neonatal or early infancy for CNS rescue. "
            "Earlier treatment is favored because seizures and neurodevelopmental injury may "
            "become self-reinforcing. Dental rescue would require an even earlier or separate "
            "ameloblast-targeted strategy and should not be assumed for the first CNS program."
        )

    @staticmethod
    def _vector_justification(vector: Vector, disease: Disease, gene: Gene) -> str:
        return (
            f"{vector.serotype} is recommended for initial CNS-focused feasibility because it "
            f"has clinical precedent for nervous-system gene delivery, a packaging limit of "
            f"about {vector.cargo_limit_bp} bp, and enough capacity for ROGDI cDNA plus a "
            f"compact neuronal promoter, ITRs, and polyadenylation signal. The cargo-size "
            f"gate is strong; the main risk is not packaging but achieving enough direct "
            f"transduction in the disease-relevant neurons while avoiding off-target "
            f"stoichiometric toxicity."
        )

    @staticmethod
    def _milestone_1() -> str:
        return (
            "Establish patient-derived iPSC neuronal models and, where possible, ameloblast- "
            "lineage or dental organoid assays. Confirm reduced or absent ROGDI protein, then "
            "measure baseline localization, Rabconnectin-3 interaction, acidic organelle/V-ATPase "
            "phenotypes, neuronal excitability, and synaptic-vesicle markers."
        )

    @staticmethod
    def _milestone_2() -> str:
        return (
            "Clone codon-optimized human ROGDI Q9GZN7 cDNA into an AAV9/hSYN1 backbone. Verify "
            "the vector genome by sequencing. Produce small-scale AAV9, titer by qPCR or ddPCR, "
            "and confirm protein expression, intracellular localization, complex interaction, "
            "and lysosomal/synaptic functional rescue in patient-derived neurons."
        )

    @staticmethod
    def _milestone_3() -> str:
        return (
            "Test AAV9-hSYN1-ROGDI in a Rogdi-deficient mouse model if available and validated. "
            "Assess vector biodistribution, brain ROGDI expression/localization, seizure burden "
            "by video-EEG, survival, behavior, and dental histology as an exploratory secondary "
            "endpoint. A meaningful go/no-go endpoint would be a reproducible reduction in "
            "seizure burden or neuronal functional phenotype versus untreated mutants."
        )

    @staticmethod
    def _milestone_4() -> str:
        return (
            "Run dose-ranging, biodistribution, and toxicology studies with special attention "
            "to liver exposure, dorsal-root-ganglion pathology, CNS inflammation, and abnormal "
            "ROGDI overexpression or mislocalization. Develop a release and potency package "
            "that includes vector genome integrity, expression, localization, protein-complex "
            "interaction, and cell-based rescue rather than enzyme activity."
        )

    @staticmethod
    def _regulatory_designation(disease: Disease) -> str:
        return (
            "Orphan Drug Designation is strongly plausible because KTS is ultra-rare, serious, "
            "and lacks approved disease-modifying therapy. A pre-IND meeting should focus on "
            "the potency assay challenge for a non-secreted intracellular scaffold, the choice "
            "of CNS endpoint, whether dental disease is primary or secondary, and the adequacy "
            "of the animal model for epileptic and developmental phenotypes."
        )

    @staticmethod
    def _precedent_programs() -> list[dict[str, Any]]:
        return [
            {
                "name": "Zolgensma (onasemnogene abeparvovec)",
                "indication": "Spinal muscular atrophy (SMA)",
                "relevance": "Single-dose systemic AAV9 gene replacement in infants; strongest precedent for an early-life CNS-prioritized AAV strategy.",
            },
            {
                "name": "Luxturna (voretigene neparvovec)",
                "indication": "RPE65-associated inherited retinal dystrophy",
                "relevance": "AAV gene-addition regulatory precedent and durability example; route and tissue are less relevant to ROGDI.",
            },
            {
                "name": "Resamirigene bilparvovec / AT132 precedent class",
                "indication": "X-linked myotubular myopathy programs",
                "relevance": "Illustrates risks and potency challenges for intracellular non-secreted proteins and the need for rigorous dose/tox controls.",
            },
        ]

    @staticmethod
    def _ind_timeline() -> str:
        return (
            "Estimated 4–6 years from corrected target validation to IND. Year 1: potency "
            "assay and patient-cell model development. Year 1–2: vector design, expression, "
            "localization, and cell rescue. Year 2–3: animal efficacy and dose selection. "
            "Year 3–5: GLP toxicology, biodistribution, CMC scale-up, and pre-IND engagement. "
            "Extra time may be needed because ROGDI lacks a simple catalytic potency assay."
        )

    @staticmethod
    def _build_risks(disease: Disease, gene: Gene, vector: Vector) -> list[dict[str, Any]]:
        return [
            {
                "name": "Cell-autonomous delivery failure",
                "likelihood": "High",
                "impact": "High",
                "mitigation": "Quantify direct neuronal transduction and ROGDI localization; do not assume cross-correction from neighboring cells.",
            },
            {
                "name": "Dental/CNS delivery mismatch",
                "likelihood": "High",
                "impact": "Moderate",
                "mitigation": "Define CNS rescue as the first primary objective; treat dental rescue as secondary, residual, or a separate local-delivery program.",
            },
            {
                "name": "Overexpression or stoichiometric toxicity",
                "likelihood": "Moderate",
                "impact": "Moderate",
                "mitigation": "Use a compact neuronal promoter, dose-ranging, localization assays, and protein-complex interaction assays before broad expression strategies.",
            },
            {
                "name": "Potency assay uncertainty",
                "likelihood": "High",
                "impact": "High",
                "mitigation": "Build orthogonal assays for expression, localization, Rabconnectin-3 interaction, acidic organelle function, and neuronal rescue.",
            },
            {
                "name": "Anti-capsid and systemic AAV toxicity",
                "likelihood": "Moderate",
                "impact": "High",
                "mitigation": "Screen neutralizing antibodies; monitor liver, DRG, and CNS inflammation; compare IV and intrathecal exposure before clinical route lock.",
            },
        ]

    @staticmethod
    def _build_scoring_dimensions(scores: ScoreBreakdown) -> list[dict[str, Any]]:
        return [
            {"name": "Structural Homology", "score": scores.structural_homology, "weight": 1.0, "notes": "Solved human ROGDI structures exist, but there is no close approved gene-therapy cargo surrogate."},
            {"name": "Sequence Identity", "score": scores.sequence_identity, "weight": 1.0, "notes": "No strong approved-cargo paralog; precedent should be based on platform and intracellular scaffold risk rather than paralog identity."},
            {"name": "Domain Similarity", "score": scores.domain_similarity, "weight": 1.0, "notes": "RAVE2/Rogdi and Rogdi_lz annotations support mechanism, but the domain family is not a mature therapeutic precedent class."},
            {"name": "Size Compatibility", "score": scores.size_compatibility, "weight": 2.0, "notes": "About 861 bp for the amino-acid coding region; excellent AAV margin. Hard gate."},
            {"name": "Tissue Tropism", "score": scores.tissue_tropism, "weight": 1.5, "notes": "AAV9 can support CNS strategy, but tooth/enamel biology creates a major mismatch."},
            {"name": "RoA Precedent", "score": scores.roa_precedent, "weight": 1.5, "notes": "Early-life AAV9 precedent is relevant for CNS rescue; route still needs disease-specific biodistribution."},
            {"name": "Promoter Match", "score": scores.promoter_match, "weight": 1.0, "notes": "hSYN1 is reasonable for neuronal proof-of-concept but may not address non-neuronal disease tissues."},
            {"name": "Localization Match", "score": scores.localization_match, "weight": 1.0, "notes": "Intracellular localization and complex stoichiometry must be empirically verified after transduction."},
            {"name": "Immunogenicity", "score": scores.immunogenicity, "weight": 1.0, "notes": "Self-protein reduces transgene concern, but AAV capsid immunity and codon-optimized epitopes remain risks."},
            {"name": "Therapeutic Window", "score": scores.therapeutic_window, "weight": 1.5, "notes": "CNS intervention is probably earliest-infant; dental disease may already be partly fixed by treatment time."},
            {"name": "Codon Optimization", "score": scores.codon_optimization, "weight": 0.5, "notes": "Short coding sequence makes optimization easy, but expression level should be tuned carefully."},
            {"name": "Platform Depth", "score": scores.platform_depth, "weight": 1.0, "notes": "AAV9 CNS programs provide platform precedent, not direct ROGDI-specific efficacy precedent."},
        ]

    @staticmethod
    def _go_no_go_items() -> list[str]:
        return [
            "Live source verification reconfirms ROGDI maps to UniProt Q9GZN7 and Orphanet ORPHA:1946",
            "AAV construct expresses 287 aa ROGDI protein at controlled levels in patient-derived neurons",
            "ROGDI localizes to expected intracellular neuronal compartments after transduction",
            "Rabconnectin-3/V-ATPase-linked cellular phenotype or neuronal functional phenotype is rescued",
            "Dose-response is demonstrated without mislocalization or overexpression toxicity",
            "Rogdi-deficient animal model shows meaningful CNS functional benefit",
            "Potency assay package is accepted in pre-IND discussion as relevant to the non-enzymatic mechanism",
        ]

    @staticmethod
    def _kill_criteria() -> str:
        return (
            "(1) Correctly mapped ROGDI protein cannot be expressed or localized in neurons; "
            "(2) functional assays show no rescue despite adequate expression; (3) therapeutic "
            "dose causes unacceptable liver, DRG, CNS, or overexpression toxicity; (4) CNS "
            "biodistribution is inadequate at a tolerable dose; (5) regulators reject the "
            "potency assay as unrelated to the disease mechanism."
        )

    @staticmethod
    def _green_light_criteria() -> str:
        return (
            "(1) Q9GZN7 identity and transcript/coding sequence are locked; (2) AAV-ROGDI "
            "restores expression, localization, and at least one mechanism-linked functional "
            "readout in patient neurons; (3) animal data show CNS benefit and tolerable safety; "
            "(4) CMC can produce a consistent small-cargo AAV product; (5) orphan and pre-IND "
            "interactions support a feasible first-in-human path."
        )

    @staticmethod
    def _conclusions(disease: Disease, gene: Gene, scores: ScoreBreakdown) -> str:
        return (
            "Corrected ROGDI biology makes the program still promising but more nuanced. The "
            "cargo-size gate is excellent, the inheritance model supports gene addition, and "
            "AAV9 provides a credible CNS-first route. However, ROGDI is a non-secreted "
            "intracellular scaffold/adaptor linked to Rabconnectin-3 and V-ATPase biology, so "
            "direct neuronal transduction and custom potency assays are the central bottlenecks. "
            "The recommended next step is a rigorous preclinical package centered on patient-"
            "derived neurons, localization and interaction assays, acidic organelle/synaptic "
            "functional rescue, and careful animal dose-response before any clinical claim."
        )
