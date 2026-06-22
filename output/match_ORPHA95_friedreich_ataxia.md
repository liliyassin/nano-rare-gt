# NanoGT Match Report: Friedreich ataxia

**Disease:** Friedreich ataxia (ORPHA:95)  
**Primary gene:** FXN  
**Gene CDS:** 633 bp  
**Inheritance:** Autosomal recessive  
**Target tissues scored:** CNS, heart  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: MITOCHONDRIAL MATRIX ENZYME (FXN): nuclear-encoded but the protein must be imported into the mitochondrial matrix post-translation via its N-terminal mitochondrial targeting sequence (MTS). Nuclear AAV delivery is theoretically feasible, but the therapeutic construct must preserve the intact MTS. MTS functionality is not captured by any other scoring dimension — this is an additional disease-specific development step requiring experimental validation.; Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints; Cell-autonomous protein across multiple tissues; high transduction coverage may be required.

### Disease Mechanism Evidence

**Molecular mechanism:** repeat expansion silencing  
**Mechanistic detail:** GAA trinucleotide repeat expansion in FXN intron 1 induces heterochromatin formation with H3K9me3 and DNA hypermethylation silencing frataxin transcription; the FXN protein coding sequence is structurally normal so a transgenic cDNA (without the expanded intron) can restore frataxin expression  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** frataxin gene addition or epigenetic derepression  
**Evidence level/status:** direct / source_checked  
**Evidence summary:** Campuzano et al. (1996 Science PMID 8596916) identified the intronic GAA expansion; Al-Mahdawi et al. (2008 Hum Mol Genet PMID 18045775) characterised the heterochromatin mechanism; FXN cDNA gene addition is actively pursued clinically because the normal frataxin protein sequence is preserved  
**Evidence source:** [Campuzano et al. 1996 Science PMID 8596916; Al-Mahdawi et al. 2008 Hum Mol Genet PMID 18045775](https://pubmed.ncbi.nlm.nih.gov/8596916/)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and integrating ex vivo HSC vector precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint risk: CNS/neurodevelopmental outcomes may require natural-history data, age-stratified endpoints, and long follow-up because short-term clinical change can be hard to interpret.
- Endpoint risk: muscle/cardiac diseases may need functional, respiratory, imaging, or cardiac endpoints that progress slowly and vary by age/stage.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | OAV101-IT | AAV9 | 7.9/10 | 🟢 High | approved |
| 2 | Zolgensma | AAV9 | 7.9/10 | 🟢 High | approved |
| 3 | SRP-9001 | AAV9 | 7.0/10 | 🟡 Medium | approved |
| 4 | BMN 307 | AAV5 | 7.0/10 | 🟡 Medium | phase2 |
| 5 | Libmeldy | LV | 7.0/10 | 🟡 Medium | approved |

---

## Match #1: OAV101-IT

**Precedent disease:** Spinal Muscular Atrophy  
**Vector:** AAV9  
**Tissue target:** CNS/spinal cord  
**Composite score:** 7.9 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.50 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.90** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 633bp / cargo 4700bp (13% utilized)
- Vector tropism plus precedent target match: cns
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: motor_neuron
- Disease mechanism: repeat expansion silencing — GAA trinucleotide repeat expansion in FXN intron 1 induces heterochromatin formation with H3K9me3 and DNA hypermethylation silencing frataxin transcription; the FXN protein coding sequence is structurally normal so a transgenic cDNA (without the expanded intron) can restore frataxin expression
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Campuzano et al. (1996 Science PMID 8596916) identified the intronic GAA expansion; Al-Mahdawi et al. (2008 Hum Mol Genet PMID 18045775) characterised the heterochromatin mechanism; FXN cDNA gene addition is actively pursued clinically because the normal frataxin protein sequence is preserved
- Mechanism source: Campuzano et al. 1996 Science PMID 8596916; Al-Mahdawi et al. 2008 Hum Mol Genet PMID 18045775 (https://pubmed.ncbi.nlm.nih.gov/8596916/)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: CONDITIONAL — FXN is a nuclear-encoded mitochondrial matrix protein. Nuclear AAV delivery is theoretically feasible (the gene is in the nuclear genome) but the N-terminal mitochondrial targeting sequence (MTS) must be preserved intact in the therapeutic construct for correct post-translational import into the mitochondrial matrix. MTS functionality is not validated by any other dimension in this framework. Confirm import efficiency with disease-specific in vitro/in vivo data before treating vector precedent scores as directly transferable.

### Manual Review Flags

- MITOCHONDRIAL MATRIX ENZYME (FXN): nuclear-encoded but the protein must be imported into the mitochondrial matrix post-translation via its N-terminal mitochondrial targeting sequence (MTS). Nuclear AAV delivery is theoretically feasible, but the therapeutic construct must preserve the intact MTS. MTS functionality is not captured by any other scoring dimension — this is an additional disease-specific development step requiring experimental validation.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #2: Zolgensma

**Precedent disease:** Spinal Muscular Atrophy  
**Vector:** AAV9  
**Tissue target:** CNS/motor neuron  
**Composite score:** 7.9 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.50 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.90** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 633bp / cargo 4700bp (13% utilized)
- Vector tropism plus precedent target match: cns
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: motor_neuron
- Disease mechanism: repeat expansion silencing — GAA trinucleotide repeat expansion in FXN intron 1 induces heterochromatin formation with H3K9me3 and DNA hypermethylation silencing frataxin transcription; the FXN protein coding sequence is structurally normal so a transgenic cDNA (without the expanded intron) can restore frataxin expression
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Campuzano et al. (1996 Science PMID 8596916) identified the intronic GAA expansion; Al-Mahdawi et al. (2008 Hum Mol Genet PMID 18045775) characterised the heterochromatin mechanism; FXN cDNA gene addition is actively pursued clinically because the normal frataxin protein sequence is preserved
- Mechanism source: Campuzano et al. 1996 Science PMID 8596916; Al-Mahdawi et al. 2008 Hum Mol Genet PMID 18045775 (https://pubmed.ncbi.nlm.nih.gov/8596916/)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: CONDITIONAL — FXN is a nuclear-encoded mitochondrial matrix protein. Nuclear AAV delivery is theoretically feasible (the gene is in the nuclear genome) but the N-terminal mitochondrial targeting sequence (MTS) must be preserved intact in the therapeutic construct for correct post-translational import into the mitochondrial matrix. MTS functionality is not validated by any other dimension in this framework. Confirm import efficiency with disease-specific in vitro/in vivo data before treating vector precedent scores as directly transferable.

### Manual Review Flags

- MITOCHONDRIAL MATRIX ENZYME (FXN): nuclear-encoded but the protein must be imported into the mitochondrial matrix post-translation via its N-terminal mitochondrial targeting sequence (MTS). Nuclear AAV delivery is theoretically feasible, but the therapeutic construct must preserve the intact MTS. MTS functionality is not captured by any other scoring dimension — this is an additional disease-specific development step requiring experimental validation.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #3: SRP-9001

**Precedent disease:** Duchenne muscular dystrophy  
**Vector:** AAV9  
**Tissue target:** muscle  
**Composite score:** 7.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 0.70 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.50 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.05** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 633bp / cargo 4700bp (13% utilized)
- Vector tropism overlap: cns, heart
- Protein class mismatch
- LOF inheritance — compatible for gene replacement
- Pathway match: myopathy
- Disease mechanism: repeat expansion silencing — GAA trinucleotide repeat expansion in FXN intron 1 induces heterochromatin formation with H3K9me3 and DNA hypermethylation silencing frataxin transcription; the FXN protein coding sequence is structurally normal so a transgenic cDNA (without the expanded intron) can restore frataxin expression
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Campuzano et al. (1996 Science PMID 8596916) identified the intronic GAA expansion; Al-Mahdawi et al. (2008 Hum Mol Genet PMID 18045775) characterised the heterochromatin mechanism; FXN cDNA gene addition is actively pursued clinically because the normal frataxin protein sequence is preserved
- Mechanism source: Campuzano et al. 1996 Science PMID 8596916; Al-Mahdawi et al. 2008 Hum Mol Genet PMID 18045775 (https://pubmed.ncbi.nlm.nih.gov/8596916/)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: CONDITIONAL — FXN is a nuclear-encoded mitochondrial matrix protein. Nuclear AAV delivery is theoretically feasible (the gene is in the nuclear genome) but the N-terminal mitochondrial targeting sequence (MTS) must be preserved intact in the therapeutic construct for correct post-translational import into the mitochondrial matrix. MTS functionality is not validated by any other dimension in this framework. Confirm import efficiency with disease-specific in vitro/in vivo data before treating vector precedent scores as directly transferable.

### Manual Review Flags

- MITOCHONDRIAL MATRIX ENZYME (FXN): nuclear-encoded but the protein must be imported into the mitochondrial matrix post-translation via its N-terminal mitochondrial targeting sequence (MTS). Nuclear AAV delivery is theoretically feasible, but the therapeutic construct must preserve the intact MTS. MTS functionality is not captured by any other scoring dimension — this is an additional disease-specific development step requiring experimental validation.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #4: BMN 307

**Precedent disease:** Phenylketonuria  
**Vector:** AAV5  
**Tissue target:** liver  
**Composite score:** 7.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 0.60 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.50 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.00** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 633bp / cargo 4700bp (13% utilized)
- Vector tropism overlaps cns, but precedent target is liver
- Both intracellular proteins
- Inheritance match (Autosomal recessive <-> AR)
- Different pathway (myopathy vs amino_acid_metabolism)
- Disease mechanism: repeat expansion silencing — GAA trinucleotide repeat expansion in FXN intron 1 induces heterochromatin formation with H3K9me3 and DNA hypermethylation silencing frataxin transcription; the FXN protein coding sequence is structurally normal so a transgenic cDNA (without the expanded intron) can restore frataxin expression
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Campuzano et al. (1996 Science PMID 8596916) identified the intronic GAA expansion; Al-Mahdawi et al. (2008 Hum Mol Genet PMID 18045775) characterised the heterochromatin mechanism; FXN cDNA gene addition is actively pursued clinically because the normal frataxin protein sequence is preserved
- Mechanism source: Campuzano et al. 1996 Science PMID 8596916; Al-Mahdawi et al. 2008 Hum Mol Genet PMID 18045775 (https://pubmed.ncbi.nlm.nih.gov/8596916/)
- Approval status: phase2
- Vector immunogenicity (AAV5): low (~9%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: CONDITIONAL — FXN is a nuclear-encoded mitochondrial matrix protein. Nuclear AAV delivery is theoretically feasible (the gene is in the nuclear genome) but the N-terminal mitochondrial targeting sequence (MTS) must be preserved intact in the therapeutic construct for correct post-translational import into the mitochondrial matrix. MTS functionality is not validated by any other dimension in this framework. Confirm import efficiency with disease-specific in vitro/in vivo data before treating vector precedent scores as directly transferable.

### Manual Review Flags

- MITOCHONDRIAL MATRIX ENZYME (FXN): nuclear-encoded but the protein must be imported into the mitochondrial matrix post-translation via its N-terminal mitochondrial targeting sequence (MTS). Nuclear AAV delivery is theoretically feasible, but the therapeutic construct must preserve the intact MTS. MTS functionality is not captured by any other scoring dimension — this is an additional disease-specific development step requiring experimental validation.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: heart
- Only partial tissue match; verify target-cell transduction and delivery route manually
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

## Match #5: Libmeldy

**Precedent disease:** Metachromatic leukodystrophy  
**Vector:** LV  
**Tissue target:** hematopoietic/CNS  
**Composite score:** 7.0 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 2.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 1.50 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 0.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 0.50 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 2.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.90 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.70 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 0.50 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **6.95** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Gene CDS 633bp / cargo 8000bp (8% utilized)
- Precedent target match: cns
- Protein class mismatch
- Inheritance match (Autosomal recessive <-> AR)
- Different pathway (myopathy vs leukodystrophy)
- Disease mechanism: repeat expansion silencing — GAA trinucleotide repeat expansion in FXN intron 1 induces heterochromatin formation with H3K9me3 and DNA hypermethylation silencing frataxin transcription; the FXN protein coding sequence is structurally normal so a transgenic cDNA (without the expanded intron) can restore frataxin expression
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: Campuzano et al. (1996 Science PMID 8596916) identified the intronic GAA expansion; Al-Mahdawi et al. (2008 Hum Mol Genet PMID 18045775) characterised the heterochromatin mechanism; FXN cDNA gene addition is actively pursued clinically because the normal frataxin protein sequence is preserved
- Mechanism source: Campuzano et al. 1996 Science PMID 8596916; Al-Mahdawi et al. 2008 Hum Mol Genet PMID 18045775 (https://pubmed.ncbi.nlm.nih.gov/8596916/)
- Approval status: approved
- Vector immunogenicity (LV): low (~2%) — most patients eligible; minimal screening burden
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: high privilege — blood-brain barrier severely limits T-cell access; durable expression expected
- Promoter availability: Synapsin-1 (pan-neuronal), CaMKII (excitatory neurons), GFAP (astrocytes) — validated but cell-type specificity varies
- Route of administration: Intrathecal or ICV delivery — more invasive than IV; established in OAV101-IT and RGX-121 but higher procedural risk
- ORGANELLE TARGETING: CONDITIONAL — FXN is a nuclear-encoded mitochondrial matrix protein. Nuclear AAV delivery is theoretically feasible (the gene is in the nuclear genome) but the N-terminal mitochondrial targeting sequence (MTS) must be preserved intact in the therapeutic construct for correct post-translational import into the mitochondrial matrix. MTS functionality is not validated by any other dimension in this framework. Confirm import efficiency with disease-specific in vitro/in vivo data before treating vector precedent scores as directly transferable.

### Manual Review Flags

- MITOCHONDRIAL MATRIX ENZYME (FXN): nuclear-encoded but the protein must be imported into the mitochondrial matrix post-translation via its N-terminal mitochondrial targeting sequence (MTS). Nuclear AAV delivery is theoretically feasible, but the therapeutic construct must preserve the intact MTS. MTS functionality is not captured by any other scoring dimension — this is an additional disease-specific development step requiring experimental validation.
- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Vector does not naturally cover all annotated disease tissues: cns, heart
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
