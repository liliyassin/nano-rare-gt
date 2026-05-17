# Nano-Rare Gene Therapy Matching Framework

A systematic multi-parameter computational framework that matches untreated nano-rare monogenic diseases with approved or late-stage gene therapies, dramatically de-risking and accelerating development using surrogate precedents.

## Primary Case Study: ROGDI / Kohlschütter-Tönz Syndrome

The framework is being validated first on **ROGDI** (GMPR2), the gene responsible for Kohlschütter-Tönz syndrome — a nano-rare autosomal recessive disorder causing amelogenesis imperfecta, psychomotor regression, and epilepsy. ROGDI was selected as the primary deep-dive case by project supervision.

## Quick Start

```bash
pip install nanogt
nanogt init
nanogt match --disease ORPHA:916 --output rogdi_report.md
```

## Architecture

See `docs/ADR-001-architecture.md` for design decisions.

## License

MIT
