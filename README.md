# Nano-Rare Gene Therapy Matching Framework

A systematic multi-parameter computational framework that matches untreated nano-rare monogenic diseases with approved or late-stage gene therapy precedents, with explicit source verification before target scoring.

## Primary Case Study: ROGDI / Kohlschütter-Tönz Syndrome

The framework is being validated first on **ROGDI**, the gene associated with Kohlschütter-Tönz syndrome / amelocerebrohypohidrotic syndrome — a nano-rare autosomal recessive disorder involving amelogenesis imperfecta, early-onset epilepsy, and severe neurodevelopmental impairment. The corrected source-audited identifiers are:

- Orphanet: ORPHA:1946
- OMIM phenotype: 226750
- OMIM gene: 614574
- UniProt: Q9GZN7
- Protein: Protein rogdi homolog, 287 aa

See `docs/ROGDI-deep-dive.md` for the corrected audit, definitions, evidence links, and gene-therapy assessment.

## Quick Start

```bash
pip install nanogt
nanogt init
nanogt match --disease ORPHA:1946 --deep-dive --output rogdi_report.md
```

## Architecture

See `docs/ADR-001-architecture.md` for design decisions.

## License

MIT
