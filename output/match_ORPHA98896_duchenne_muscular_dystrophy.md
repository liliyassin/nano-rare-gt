# NanoGT Match Report: Duchenne muscular dystrophy

**Disease:** Duchenne muscular dystrophy (ORPHA:98896)  
**Primary gene:** DMD  
**Gene CDS:** 11055 bp  
**Inheritance:** X-linked recessive  
**Target tissues scored:** muscle, heart  

---

## Interpretation

- At least one high-confidence precedent was found, but this is still a precedent match rather than a clinical-trial recommendation.
- Main review flags: Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints; Cell-autonomous protein across multiple tissues; high transduction coverage may be required; Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy.

### Disease Mechanism Evidence

**Molecular mechanism:** loss of function oversized  
**Mechanistic detail:** Dystrophin loss with native DMD too large for single AAV  
**Gene-addition compatibility:** conditional  
**Preferred modality class:** engineered microgene or dual vector  
**Evidence level/status:** direct / source_linked_needs_review  
**Evidence summary:** DMD supports replacement logic but requires micro-dystrophin or other engineered strategies because full-length DMD exceeds AAV capacity  
**Evidence source:** [Chamberlain et al. 2023 microdystrophin review](https://pubmed.ncbi.nlm.nih.gov/36990339/)  

### Study-Level Limitations

- Catalog-relative ranking: current catalog contains 21 precedent programs and 8 vectors, so absence of a strong match is not proof that no therapy is possible.
- Modality coverage is limited mainly to AAV and integrating ex vivo HSC vector precedents; dual-AAV, LNP/mRNA, genome editing, ASO, and transplant-enabling strategies are not fully represented.
- Endpoint risk: muscle/cardiac diseases may need functional, respiratory, imaging, or cardiac endpoints that progress slowly and vary by age/stage.
- Endpoint risk: multi-system disease may need a hierarchy of primary and secondary endpoints; one tissue response may not equal whole-disease benefit.

---

## Top 1 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | SRP-9001 | AAV9 | 7.6/10 | 🟢 High | approved |

---

## Match #1: SRP-9001

**Precedent disease:** Duchenne muscular dystrophy  
**Vector:** AAV9  
**Tissue target:** muscle  
**Composite score:** 7.6 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Modality compatibility | 1.50 | 2.0 | Disease mechanism supports gene-addition precedent |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.60 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| Organelle targeting | 1.00 | 1.0 | Nuclear AAV delivery reaches correct subcellular compartment |
| **TOTAL (normalised)** | **7.62** | **10.0** | Raw sum / 21 × 10 (v2: 14 dimensions) |

### Rationale

- Native DMD CDS (11055bp) is oversized; scoring engineered DMD_micro construct (3825bp) as a micro/mini-transgene strategy, not full-length replacement
- Gene CDS 3825bp / cargo 4700bp (81% utilized)
- Vector tropism plus precedent target match: muscle
- Both membrane proteins
- Inheritance match (X-linked recessive <-> XL)
- Pathway match: myopathy
- Disease mechanism: loss of function oversized — Dystrophin loss with native DMD too large for single AAV
- Gene-addition modality compatibility: conditionally supports gene addition; review disease-specific constraints
- Mechanism evidence: DMD supports replacement logic but requires micro-dystrophin or other engineered strategies because full-length DMD exceeds AAV capacity
- Mechanism source: Chamberlain et al. 2023 microdystrophin review (https://pubmed.ncbi.nlm.nih.gov/36990339/)
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate immune surveillance — standard immunosuppression protocols typically sufficient
- Promoter availability: MHCK7, CK8, Desmin — validated in Elevidys (DMD) and SMA programs
- Route of administration: IV systemic or intramuscular injection — well established; used in SMA, DMD, Glybera
- ORGANELLE TARGETING: COMPATIBLE — DMD standard subcellular localisation; nuclear AAV delivery directly produces functional protein at the correct cellular compartment with no additional organelle-import steps required.

### Manual Review Flags

- Dual critical target tissues; confirm whether one route can plausibly address both clinical endpoints
- Cell-autonomous protein across multiple tissues; high transduction coverage may be required
- Native CDS exceeds standard single-AAV capacity; consider engineered, dual-vector, non-AAV, or editing strategy
- Engineered mini/micro-transgene strategy scored; not equivalent to full-length native gene replacement
- Mechanism evidence is conditionally compatible with gene addition; review the listed disease-specific constraints before treating vector precedent as transferable
- AAV tropism is species- and route-dependent; confirm human target-cell biodistribution rather than relying on animal tropism alone

---

## Excluded Programs (Packaging Failure)

| Program | Vector | Gene CDS Issue |
|---------|--------|----------------|
| ABO-101 | AAV9 | Gene CDS (11055bp) exceeds vector cargo (4700bp) — hard fail |
| AT132 | AAV8 | Gene CDS (11055bp) exceeds vector cargo (4700bp) — hard fail |
| AVR-RD-01 | LV | Gene CDS (11055bp) exceeds vector cargo (8000bp) — hard fail |
| BMN 307 | AAV5 | Gene CDS (11055bp) exceeds vector cargo (4700bp) — hard fail |
| CPCB-RPE1 | AAV8 | Gene CDS (11055bp) exceeds vector cargo (4700bp) — hard fail |
