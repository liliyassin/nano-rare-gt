# NanoGT Match Report: Leber hereditary optic neuropathy

**Disease:** Leber hereditary optic neuropathy (ORPHA:104)  
**Primary gene:** MT-ND4  
**Gene CDS:** 1377 bp  
**Inheritance:** Mitochondrial inheritance  
**Target tissues scored:** retina, CNS  

---

## Interpretation

- No high-confidence vector precedent was found; the best result is medium-confidence and should be treated as manual-review territory.
- Main review flags: MITOCHONDRIAL DNA GENE (MT-ND4): this gene is encoded in the mitochondrial genome, translated by mitochondrial ribosomes using a non-standard genetic code. Standard nuclear AAV gene addition CANNOT produce this protein. Treatment requires allotopic expression: the gene must be recoded for cytoplasmic translation and given an artificial MTS — a strategy fundamentally different from every program in this catalog. All precedent scores are cross-paradigm comparisons. See: GS010/Lumevoq (Gensight Biologics) as a real-world allotopic precedent.; Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints; Vector does not naturally cover all annotated disease tissues: cns, retina.

### Disease Mechanism Evidence

**Molecular mechanism:** mitochondrial loss of function  
**Mechanistic detail:** Mitochondrial complex I dysfunction from MT-ND4 variant  
**Gene-addition compatibility:** uncertain  
**Preferred modality class:** specialized allotopic expression or mitochondrial strategy  
**Evidence level/status:** direct / needs_manual_review  
**Evidence summary:** Mitochondrial DNA disease is not ordinary nuclear gene addition; allotopic AAV approaches are specialized and disease-specific  
**Evidence source:** [OMIM MT-ND4 gene entry](https://omim.org/entry/516003)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and lentiviral precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint readiness: retinal diseases often have measurable endpoints such as OCT, ERG, visual acuity, visual fields, or mobility testing, but genotype-specific progression still needs confirmation.
- Endpoint risk: CNS/neurodevelopmental outcomes may require natural-history data, age-stratified endpoints, and long follow-up because short-term clinical change can be hard to interpret.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | CPCB-RPE1 | AAV8 | 6.4/10 | 🟡 Medium | phase2/3 |
| 2 | Skysona | LV | 6.3/10 | 🟡 Medium | approved |
| 3 | Luxturna | AAV2 | 6.1/10 | 🟡 Medium | approved |
| 4 | Libmeldy | LV | 5.9/10 | 🟡 Medium | approved |
| 5 | Hemgenix | AAV5 | 5.6/10 | 🟡 Medium | approved |

---

## Match #1: CPCB-RPE1

**Precedent disease:** Achromatopsia  
**Vector:** AAV8  
**Tissue target:** retina/photoreceptor  
**Composite score:** 6.4 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.70 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.43** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1377bp / cargo 4700bp (29% utilized)
- Precedent target match: retina
- Both membrane proteins
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Pathway match: retinal_phototransduction
- Disease mechanism: mitochondrial loss of function — Mitochondrial complex I dysfunction from MT-ND4 variant
- Gene-addition modality compatibility: uncertain for ordinary gene addition
- Mechanism evidence: Mitochondrial DNA disease is not ordinary nuclear gene addition; allotopic AAV approaches are specialized and disease-specific
- Mechanism source: OMIM MT-ND4 gene entry (https://omim.org/entry/516003)
- Approval status: phase2/3
- Vector immunogenicity (AAV8): high (~30%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010
- ORGANELLE TARGETING: INCOMPATIBLE — MT-ND4 is a mitochondrial DNA-encoded gene. Standard nuclear AAV delivery cannot produce a functional protein at the mitochondrial target site. Treatment requires allotopic expression: cytoplasmic recoding of the gene using the standard genetic code plus an artificial mitochondrial targeting sequence (MTS). This strategy is disease-specific and fundamentally different from the nuclear gene-addition programs in this catalog. All precedent scores for this disease should be treated as cross-paradigm comparisons only, not direct development templates. (Real-world precedent: GS010/Lumevoq for MT-ND4/LHON; Phase 3 completed, EMA MAA withdrawn April 2023.)

### Manual Review Flags

- MITOCHONDRIAL DNA GENE (MT-ND4): this gene is encoded in the mitochondrial genome, translated by mitochondrial ribosomes using a non-standard genetic code. Standard nuclear AAV gene addition CANNOT produce this protein. Treatment requires allotopic expression: the gene must be recoded for cytoplasmic translation and given an artificial MTS — a strategy fundamentally different from every program in this catalog. All precedent scores are cross-paradigm comparisons. See: GS010/Lumevoq (Gensight Biologics) as a real-world allotopic precedent.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: cns, retina
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence does not cleanly support simple gene addition; consider RNA, editing, silencing, mitochondrial, or other non-catalog modalities
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #2: Skysona

**Precedent disease:** Cerebral adrenoleukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 6.3 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.33** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1377bp / cargo 8000bp (17% utilized)
- Precedent target match: cns
- Both membrane proteins
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Different pathway (retinal_phototransduction vs peroxisomal)
- Disease mechanism: mitochondrial loss of function — Mitochondrial complex I dysfunction from MT-ND4 variant
- Gene-addition modality compatibility: uncertain for ordinary gene addition
- Mechanism evidence: Mitochondrial DNA disease is not ordinary nuclear gene addition; allotopic AAV approaches are specialized and disease-specific
- Mechanism source: OMIM MT-ND4 gene entry (https://omim.org/entry/516003)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010
- ORGANELLE TARGETING: INCOMPATIBLE — MT-ND4 is a mitochondrial DNA-encoded gene. Standard nuclear AAV delivery cannot produce a functional protein at the mitochondrial target site. Treatment requires allotopic expression: cytoplasmic recoding of the gene using the standard genetic code plus an artificial mitochondrial targeting sequence (MTS). This strategy is disease-specific and fundamentally different from the nuclear gene-addition programs in this catalog. All precedent scores for this disease should be treated as cross-paradigm comparisons only, not direct development templates. (Real-world precedent: GS010/Lumevoq for MT-ND4/LHON; Phase 3 completed, EMA MAA withdrawn April 2023.)

### Manual Review Flags

- MITOCHONDRIAL DNA GENE (MT-ND4): this gene is encoded in the mitochondrial genome, translated by mitochondrial ribosomes using a non-standard genetic code. Standard nuclear AAV gene addition CANNOT produce this protein. Treatment requires allotopic expression: the gene must be recoded for cytoplasmic translation and given an artificial MTS — a strategy fundamentally different from every program in this catalog. All precedent scores are cross-paradigm comparisons. See: GS010/Lumevoq (Gensight Biologics) as a real-world allotopic precedent.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: cns, retina
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence does not cleanly support simple gene addition; consider RNA, editing, silencing, mitochondrial, or other non-catalog modalities

## Match #3: Luxturna

**Precedent disease:** Leber congenital amaurosis type 2  
**Vector:** AAV2  
**Tissue target:** retina/RPE  
**Composite score:** 6.1 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 0.50 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.10** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1377bp / cargo 4700bp (29% utilized)
- Vector tropism plus precedent target match: retina
- Protein class mismatch
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Pathway match: retinal_visual_cycle
- Disease mechanism: mitochondrial loss of function — Mitochondrial complex I dysfunction from MT-ND4 variant
- Gene-addition modality compatibility: uncertain for ordinary gene addition
- Mechanism evidence: Mitochondrial DNA disease is not ordinary nuclear gene addition; allotopic AAV approaches are specialized and disease-specific
- Mechanism source: OMIM MT-ND4 gene entry (https://omim.org/entry/516003)
- Approval status: approved
- Vector immunogenicity (AAV2): very high (~55%) — majority of patients may be ineligible; major trial design challenge
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010
- ORGANELLE TARGETING: INCOMPATIBLE — MT-ND4 is a mitochondrial DNA-encoded gene. Standard nuclear AAV delivery cannot produce a functional protein at the mitochondrial target site. Treatment requires allotopic expression: cytoplasmic recoding of the gene using the standard genetic code plus an artificial mitochondrial targeting sequence (MTS). This strategy is disease-specific and fundamentally different from the nuclear gene-addition programs in this catalog. All precedent scores for this disease should be treated as cross-paradigm comparisons only, not direct development templates. (Real-world precedent: GS010/Lumevoq for MT-ND4/LHON; Phase 3 completed, EMA MAA withdrawn April 2023.)

### Manual Review Flags

- MITOCHONDRIAL DNA GENE (MT-ND4): this gene is encoded in the mitochondrial genome, translated by mitochondrial ribosomes using a non-standard genetic code. Standard nuclear AAV gene addition CANNOT produce this protein. Treatment requires allotopic expression: the gene must be recoded for cytoplasmic translation and given an artificial MTS — a strategy fundamentally different from every program in this catalog. All precedent scores are cross-paradigm comparisons. See: GS010/Lumevoq (Gensight Biologics) as a real-world allotopic precedent.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence does not cleanly support simple gene addition; consider RNA, editing, silencing, mitochondrial, or other non-catalog modalities
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 5.9 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **5.86** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1377bp / cargo 8000bp (17% utilized)
- Precedent target match: cns
- Protein class mismatch
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Different pathway (retinal_phototransduction vs leukodystrophy)
- Disease mechanism: mitochondrial loss of function — Mitochondrial complex I dysfunction from MT-ND4 variant
- Gene-addition modality compatibility: uncertain for ordinary gene addition
- Mechanism evidence: Mitochondrial DNA disease is not ordinary nuclear gene addition; allotopic AAV approaches are specialized and disease-specific
- Mechanism source: OMIM MT-ND4 gene entry (https://omim.org/entry/516003)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010
- ORGANELLE TARGETING: INCOMPATIBLE — MT-ND4 is a mitochondrial DNA-encoded gene. Standard nuclear AAV delivery cannot produce a functional protein at the mitochondrial target site. Treatment requires allotopic expression: cytoplasmic recoding of the gene using the standard genetic code plus an artificial mitochondrial targeting sequence (MTS). This strategy is disease-specific and fundamentally different from the nuclear gene-addition programs in this catalog. All precedent scores for this disease should be treated as cross-paradigm comparisons only, not direct development templates. (Real-world precedent: GS010/Lumevoq for MT-ND4/LHON; Phase 3 completed, EMA MAA withdrawn April 2023.)

### Manual Review Flags

- MITOCHONDRIAL DNA GENE (MT-ND4): this gene is encoded in the mitochondrial genome, translated by mitochondrial ribosomes using a non-standard genetic code. Standard nuclear AAV gene addition CANNOT produce this protein. Treatment requires allotopic expression: the gene must be recoded for cytoplasmic translation and given an artificial MTS — a strategy fundamentally different from every program in this catalog. All precedent scores are cross-paradigm comparisons. See: GS010/Lumevoq (Gensight Biologics) as a real-world allotopic precedent.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: cns, retina
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence does not cleanly support simple gene addition; consider RNA, editing, silencing, mitochondrial, or other non-catalog modalities

## Match #5: Hemgenix

**Precedent disease:** Hemophilia B  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 5.6 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.00 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.30 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 0.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 1.00 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 1.00 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.80 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **5.62** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 1377bp / cargo 4700bp (29% utilized)
- Vector tropism overlaps cns, but precedent target is liver
- Protein class mismatch
- Inheritance mismatch (dominant/mitochondrial — higher complexity)
- Different pathway (retinal_phototransduction vs coagulation)
- Disease mechanism: mitochondrial loss of function — Mitochondrial complex I dysfunction from MT-ND4 variant
- Gene-addition modality compatibility: uncertain for ordinary gene addition
- Mechanism evidence: Mitochondrial DNA disease is not ordinary nuclear gene addition; allotopic AAV approaches are specialized and disease-specific
- Mechanism source: OMIM MT-ND4 gene entry (https://omim.org/entry/516003)
- Approval status: approved
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Very narrow therapeutic window — congenital or rapidly fatal early onset; in utero or immediate neonatal GT required; substantially increases trial complexity
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: highest immune privilege — blood-retinal barrier + FasL + TGF-β2; minimal T-cell clearance risk
- Promoter availability: VMD2, RPGR, GRK1, CRX, IRBP — multiple validated retinal promoters used in Luxturna, GS010, CPCB-RPE1
- Route of administration: Subretinal/intravitreal injection — specialist ophthalmic procedure; established in Luxturna and GS010
- ORGANELLE TARGETING: INCOMPATIBLE — MT-ND4 is a mitochondrial DNA-encoded gene. Standard nuclear AAV delivery cannot produce a functional protein at the mitochondrial target site. Treatment requires allotopic expression: cytoplasmic recoding of the gene using the standard genetic code plus an artificial mitochondrial targeting sequence (MTS). This strategy is disease-specific and fundamentally different from the nuclear gene-addition programs in this catalog. All precedent scores for this disease should be treated as cross-paradigm comparisons only, not direct development templates. (Real-world precedent: GS010/Lumevoq for MT-ND4/LHON; Phase 3 completed, EMA MAA withdrawn April 2023.)

### Manual Review Flags

- MITOCHONDRIAL DNA GENE (MT-ND4): this gene is encoded in the mitochondrial genome, translated by mitochondrial ribosomes using a non-standard genetic code. Standard nuclear AAV gene addition CANNOT produce this protein. Treatment requires allotopic expression: the gene must be recoded for cytoplasmic translation and given an artificial MTS — a strategy fundamentally different from every program in this catalog. All precedent scores are cross-paradigm comparisons. See: GS010/Lumevoq (Gensight Biologics) as a real-world allotopic precedent.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: retina
- Only partial tissue match; verify target-cell transduction and delivery route manually
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Narrow therapeutic window; evaluate newborn screening, presymptomatic diagnosis, or very early dosing feasibility
- Inheritance/mechanism may not be simple loss-of-function replacement; check dominant-negative, gain-of-function, or mitochondrial biology
- Mechanism evidence does not cleanly support simple gene addition; consider RNA, editing, silencing, mitochondrial, or other non-catalog modalities
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone
