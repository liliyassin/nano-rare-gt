# NanoGT Match Report: Mucolipidosis type IV

**Disease:** Mucolipidosis type IV (ORPHA:578)  
**Primary gene:** MCOLN1  
**Gene CDS:** 1740 bp  
**Inheritance:** Autosomal recessive  
**Target tissues:** CNS, retina  

---

## Top 5 GT Precedent Matches

| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
| 1 | ABO-101 | AAV9 | 9.0/10 | 🟢 High | phase1/2 |
| 2 | RGX-121 | AAV9 | 9.0/10 | 🟢 High | phase3 |
| 3 | CPCB-RPE1 | AAV8 | 7.2/10 | 🟡 Medium | phase2/3 |
| 4 | AVR-RD-01 | LV | 7.0/10 | 🟡 Medium | phase1/2 |
| 5 | OAV101-IT | AAV9 | 7.0/10 | 🟡 Medium | approved |

---

## Match #1: ABO-101

**Precedent disease:** Mucopolysaccharidosis type IIIB  
**Vector:** AAV9  
**Tissue target:** CNS  
**Composite score:** 9.0 / 10  

### Score Breakdown

| Dimension | Score | Max |
|-----------|-------|-----|
| Packaging fit | 1.5 | 2.0 |
| Tissue tropism | 2.0 | 2.0 |
| Protein class | 2.0 | 2.0 |
| Pathway similarity | 2.0 | 2.0 |
| Inheritance compatibility | 1.0 | 1.0 |
| Approval precedent | 0.5 | 1.0 |

### Rationale

- Gene CDS 1740bp / cargo 4700bp (37% utilized)
- Vector tropism plus precedent target match: cns
- Both lysosomal proteins — cross-correction likely
- Inheritance match (Autosomal recessive <-> AR)
- Pathway match: lysosomal_storage
- Approval status: phase1/2

## Match #2: RGX-121

**Precedent disease:** Mucopolysaccharidosis type II  
**Vector:** AAV9  
**Tissue target:** CNS/liver  
**Composite score:** 9.0 / 10  

### Score Breakdown

| Dimension | Score | Max |
|-----------|-------|-----|
| Packaging fit | 1.5 | 2.0 |
| Tissue tropism | 2.0 | 2.0 |
| Protein class | 2.0 | 2.0 |
| Pathway similarity | 2.0 | 2.0 |
| Inheritance compatibility | 0.7 | 1.0 |
| Approval precedent | 0.8 | 1.0 |

### Rationale

- Gene CDS 1740bp / cargo 4700bp (37% utilized)
- Vector tropism plus precedent target match: cns
- Both lysosomal proteins — cross-correction likely
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Approval status: phase3

## Match #3: CPCB-RPE1

**Precedent disease:** Achromatopsia  
**Vector:** AAV8  
**Tissue target:** retina/photoreceptor  
**Composite score:** 7.2 / 10  

### Score Breakdown

| Dimension | Score | Max |
|-----------|-------|-----|
| Packaging fit | 1.5 | 2.0 |
| Tissue tropism | 2.0 | 2.0 |
| Protein class | 1.5 | 2.0 |
| Pathway similarity | 0.5 | 2.0 |
| Inheritance compatibility | 1.0 | 1.0 |
| Approval precedent | 0.7 | 1.0 |

### Rationale

- Gene CDS 1740bp / cargo 4700bp (37% utilized)
- Vector tropism plus precedent target match: retina
- Both membrane proteins
- Inheritance match (Autosomal recessive <-> AR)
- Different pathway (lysosomal_storage vs retinal_phototransduction)
- Approval status: phase2/3

## Match #4: AVR-RD-01

**Precedent disease:** Fabry disease  
**Vector:** LV  
**Tissue target:** hematopoietic  
**Composite score:** 7.0 / 10  

### Score Breakdown

| Dimension | Score | Max |
|-----------|-------|-----|
| Packaging fit | 1.5 | 2.0 |
| Tissue tropism | 0.3 | 2.0 |
| Protein class | 2.0 | 2.0 |
| Pathway similarity | 2.0 | 2.0 |
| Inheritance compatibility | 0.7 | 1.0 |
| Approval precedent | 0.5 | 1.0 |

### Rationale

- Gene CDS 1740bp / cargo 4700bp (37% utilized)
- No tissue overlap (disease: ['CNS', 'retina'], vector: [])
- Both lysosomal proteins — cross-correction likely
- LOF inheritance — compatible for gene replacement
- Pathway match: lysosomal_storage
- Approval status: phase1/2

## Match #5: OAV101-IT

**Precedent disease:** Spinal Muscular Atrophy  
**Vector:** AAV9  
**Tissue target:** CNS/spinal cord  
**Composite score:** 7.0 / 10  

### Score Breakdown

| Dimension | Score | Max |
|-----------|-------|-----|
| Packaging fit | 1.5 | 2.0 |
| Tissue tropism | 2.0 | 2.0 |
| Protein class | 1.0 | 2.0 |
| Pathway similarity | 0.5 | 2.0 |
| Inheritance compatibility | 1.0 | 1.0 |
| Approval precedent | 1.0 | 1.0 |

### Rationale

- Gene CDS 1740bp / cargo 4700bp (37% utilized)
- Vector tropism plus precedent target match: cns
- Partial match: extracellular/secreted component present
- Inheritance match (Autosomal recessive <-> AR)
- Different pathway (lysosomal_storage vs motor_neuron)
- Approval status: approved
