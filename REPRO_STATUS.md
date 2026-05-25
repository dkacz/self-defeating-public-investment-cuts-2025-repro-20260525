# Repro status

Current status: `PUBLIC_READER_NOTEBOOK_GRANULAR_REBUILD_PASS_PENDING_FINAL_PRO_REVIEW`.

The package includes the accepted 2025 granular notebook, copied source data, current result ledgers, article source, article renders, Boox delivery evidence, annotation-accounting evidence and final Pro harvest summary.

Update 2026-05-25: after the public-notebook remediation verdict and operator review, the reader-facing notebook has been rebuilt as `docs/notebooks/self_defeating_public_investment_cuts_2025_reproducibility.ipynb` and rendered to `docs/index.html`. Local execution passes with `589` cells, `273` code cells, maximum `10` nonblank code lines per code cell, `273/273` adjacent econometric explanations and no execution errors. The notebook includes a visible paper-number consistency table: `6/6` reference tables pass, covering retained response paths, debt endpoints, model admission, the p-value appendix table and uncertainty summaries.

Public server QA passed on 2026-05-25: GitHub Pages is built from `main:/docs`; the landing page, raw notebook, full package ZIP, checksum sidecar and manifest return HTTP `200`; the old audit-framed notebook returns HTTP `404`; public hashes match local hashes.

Boox QA passed on 2026-05-25: clean current annotation-accounting Markdown, HTML, EPUB and checksum sidecar are present on the Boox Drive path with matching downloaded hashes. The Boox accounting now reports the same notebook facts as the public server.
