# NanoGT Match Report: Duchenne muscular dystrophy

**Disease:** Duchenne muscular dystrophy (ORPHA:98896)  
**Primary gene:** DMD  
**Gene CDS:** 11055 bp  
**Inheritance:** X-linked recessive  
**Target tissues:** muscle, heart  

---

## Top 1 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | SRP-9001 | AAV9 | 7.5/10 | 🟢 High | approved |

---

## Match #1: SRP-9001

**Precedent disease:** Duchenne muscular dystrophy  
**Vector:** AAV9  
**Tissue target:** muscle  
**Composite score:** 7.5 / 10  

### Score Breakdown

| Dimension | Score | Max | What it measures |
|-----------|-------|-----|-----------------|
| Packaging fit | 1.00 | 2.0 | Gene CDS size vs vector cargo capacity |
| Tissue tropism | 2.00 | 2.0 | Vector naturally reaches disease target tissue |
| Protein class | 1.50 | 2.0 | Same secreted/lysosomal/membrane/intracellular class |
| Pathway similarity | 2.00 | 2.0 | Same or related biological pathway |
| Inheritance compatibility | 1.00 | 1.0 | AR/XL loss-of-function pattern match |
| Approval precedent | 1.00 | 1.0 | Regulatory approval / trial stage |
| Immunogenicity | 1.00 | 2.0 | Pre-existing NAb seroprevalence for this vector |
| Therapeutic window | 1.50 | 2.0 | Can GT be given before irreversible damage? |
| Cross-correction | 0.20 | 1.0 | Can transduced cells rescue untransduced neighbours? |
| Immune privilege | 0.60 | 1.0 | Immunological protection of target tissue |
| Promoter availability | 0.80 | 1.0 | Validated tissue-specific promoters exist |
| Route of administration | 0.90 | 1.0 | Established delivery route to target tissue |
| **TOTAL (normalised)** | **7.50** | **10.0** | Raw sum / 18 × 10 |

### Rationale

- Native DMD CDS (11055bp) is oversized; scoring engineered DMD_micro construct (3825bp) as a micro/mini-transgene strategy, not full-length replacement
- Gene CDS 3825bp / cargo 4700bp (81% utilized)
- Vector tropism plus precedent target match: muscle
- Both membrane proteins
- Inheritance match (X-linked recessive <-> XL)
- Pathway match: myopathy
- Approval status: approved
- Vector immunogenicity (AAV9): high (~22%) — substantial patient exclusion expected; immunodepletion protocols may be needed
- Moderate therapeutic window — progressive disease with childhood onset; early intervention strongly recommended; newborn screening integration beneficial
- Intracellular or membrane-bound protein — no cross-correction possible; each target cell must individually receive the vector; requires high transduction efficiency and therefore a higher or more targeted dose
- Immune privilege: moderate immune surveillance — standard immunosuppression protocols typically sufficient
- Promoter availability: MHCK7, CK8, Desmin — validated in Elevidys (DMD) and SMA programs
- Route of administration: IV systemic or intramuscular injection — well established; used in SMA, DMD, Glybera

---

## Excluded Programs (Packaging Failure)

| Program | Vector | Gene CDS Issue |
|---------|--------|----------------|
| ABO-101 | AAV9 | Gene CDS (11055bp) exceeds vector cargo (4700bp) — hard fail |
| AT132 | AAV8 | Gene CDS (11055bp) exceeds vector cargo (4700bp) — hard fail |
| AVR-RD-01 | LV | Gene CDS (11055bp) exceeds vector cargo (8000bp) — hard fail |
| BMN 307 | AAV5 | Gene CDS (11055bp) exceeds vector cargo (4700bp) — hard fail |
| CPCB-RPE1 | AAV8 | Gene CDS (11055bp) exceeds vector cargo (4700bp) — hard fail |
