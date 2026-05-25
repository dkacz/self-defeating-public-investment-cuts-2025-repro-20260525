# Repro status

Current status: `PUBLIC_READER_NOTEBOOK_GRANULAR_REBUILD_PASS_PENDING_PUBLIC_REFRESH_AND_FINAL_REVIEW`.

The package includes the accepted 2025 granular notebook, its copied source data, current result ledgers, article source, article renders, Boox delivery evidence, annotation-accounting evidence and Pro R6 harvest summary.

Update 2026-05-25: after the public-notebook remediation verdict and operator review, the reader-facing notebook has been rebuilt as `docs/notebooks/self_defeating_public_investment_cuts_2025_reproducibility.ipynb` and rendered to `docs/index.html`. After the operator's further instruction, it was rebuilt again into smaller steps. Local execution passes with `589` cells, `273` code cells, maximum `10` nonblank code lines per code cell, `273/273` adjacent `Econometric sense.` explanations and no execution errors. The notebook now includes a visible paper-number consistency table: `6/6` reference tables pass, covering retained response paths, debt endpoints, model admission, the p-value appendix table and uncertainty summaries. Public repository refresh, Boox/current annotation accounting, wiki state and final public-delivery review still need refresh before delivery closure.

Notebook execution QA is recorded in `qa/public_2025_notebook_execution_cells.csv`.

Public server QA passed on 2026-05-25: GitHub Pages is built from `main:/docs`, the landing page, JupyterLite shell, raw notebook, manifest and current annotation-accounting EPUB all return HTTP `200`, and downloaded notebook/accounting hashes match local hashes.

Boox QA passed on 2026-05-25: current R836 article files and `Annotation_Accounting_2025_Current_R836_20260525.epub` are present on the Boox Drive path with matching local hashes.
