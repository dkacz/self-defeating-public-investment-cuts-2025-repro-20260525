# Repro status

Current status: `PUBLIC_READER_NOTEBOOK_REFRESH_PASS_PENDING_BOOX_AND_FINAL_REVIEW`.

The package includes the accepted 2025 granular notebook, its copied source data, current result ledgers, article source, article renders, Boox delivery evidence, annotation-accounting evidence and Pro R6 harvest summary.

Update 2026-05-25: after the public-notebook remediation verdict and operator review, the reader-facing notebook has been rebuilt as `docs/notebooks/self_defeating_public_investment_cuts_2025_reproducibility.ipynb` and rendered to `docs/index.html`. Local execution passes with `320` cells, `150` code cells, maximum `20` nonblank code lines per code cell, `150/150` adjacent `Econometric sense.` explanations and no execution errors. The public repository was refreshed at commit `469de94`; the landing page and raw notebook return HTTP `200`, and the old audit-framed notebook URL returns `404`. Boox/current annotation accounting, wiki state and final public-delivery review still need refresh before delivery closure.

Notebook execution QA is recorded in `qa/public_2025_notebook_execution_cells.csv`.

Public server QA passed on 2026-05-25: GitHub Pages is built from `main:/docs`, the landing page, JupyterLite shell, raw notebook, manifest and current annotation-accounting EPUB all return HTTP `200`, and downloaded notebook/accounting hashes match local hashes.

Boox QA passed on 2026-05-25: current R836 article files and `Annotation_Accounting_2025_Current_R836_20260525.epub` are present on the Boox Drive path with matching local hashes.
