# Codebase Inspection — pygount

Generated: Thursday 11 June 2026, BST.

## Command

```bash
uv run pygount --format=summary \
  --folders-to-skip=".git,node_modules,venv,.venv,__pycache__,.cache,dist,build,.next,.tox,.eggs,.pytest_cache,PDFs to Read,Trying_to_understand" \
  .
```

## Current result

| Language | Files | Code lines | Comment/documentation lines |
|---|---:|---:|---:|
| Python | 12 | 1,648 | 471 |
| HTML | 1 | 930 | 23 |
| Transact-SQL | 1 | 72 | 10 |
| JSON | 1 | 59 | 0 |
| TOML | 1 | 32 | 0 |
| Bash | 1 | 21 | 5 |
| Markdown | 71 | 0 | 11,255 |
| Other/generated/binary/empty/duplicate | 40 | 0 | 0 |
| **Total** | **127** | **2,762** | **11,764** |

## Interpretation

The repository is documentation-heavy, which is expected for a dissertation project. The executable core is small: approximately 1.6k Python code lines across 12 Python files. That is a strength for explainability, but it means the dissertation must not overclaim this as an industrial-scale platform.

## Maintenance note

`pygount>=3.2.0` has been added to the `dev` optional dependencies in `pyproject.toml`, so codebase inspection can be rerun with:

```bash
uv sync --extra dev
uv run pygount --format=summary --folders-to-skip=".git,node_modules,venv,.venv,__pycache__,.cache,dist,build,.next,.tox,.eggs,.pytest_cache,PDFs to Read,Trying_to_understand" .
```
