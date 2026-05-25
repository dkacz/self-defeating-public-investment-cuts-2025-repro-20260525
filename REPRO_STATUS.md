# Repro status

Current status: `PASS`.

The package includes the accepted 2025 granular notebook, its copied source data, current result ledgers, article source, article renders, Boox delivery evidence, annotation-accounting evidence and Pro R6 harvest summary.

Notebook execution QA is recorded in `qa/public_2025_notebook_execution_cells.csv`.

Public server QA passed on 2026-05-25: GitHub Pages is built from `main:/docs`, the landing page, JupyterLite shell, raw notebook, manifest and current annotation-accounting EPUB all return HTTP `200`, and downloaded notebook/accounting hashes match local hashes.

Boox QA passed on 2026-05-25: current R836 article files and `Annotation_Accounting_2025_Current_R836_20260525.epub` are present on the Boox Drive path with matching local hashes.
