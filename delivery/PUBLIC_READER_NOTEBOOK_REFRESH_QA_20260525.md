# Public reader-notebook refresh QA

Date: 2026-05-25

Status: `PASS` for public deployment; final external review still pending.

Public repository: `https://github.com/dkacz/self-defeating-public-investment-cuts-2025-repro-20260525`

## Public URLs checked

- Landing page: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/`
- Raw notebook: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/notebooks/self_defeating_public_investment_cuts_2025_reproducibility.ipynb`
- Old audit-framed notebook URL: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/notebooks/self_defeating_public_investment_cuts_2025_granular_audit.ipynb`
- Current annotation accounting EPUB: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/annotation_accounting_current_20260525/Annotation_Accounting_2025_Current_20260525.epub`
- Full package checksum sidecar: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/downloads/full_public_2025_repro_package.zip.sha256`

## HTTP and hash checks

- Landing page HTTP: `200`, bytes `363746`, SHA-256 `eadf32d9fb0194065163350c8870fea2f122383fab13b988a04d06119f102953`
- Raw notebook HTTP: `200`, bytes `363638`, SHA-256 `23e688351dab68a5c836c0cc2ac7ae8e59f5146eb2e864ec576369b258d60d6e`
- Old audit-framed notebook HTTP: `404`
- Full public package ZIP checksum: stored only in `docs/downloads/full_public_2025_repro_package.zip.sha256` and verified after publication; no inline ZIP hash is stored in package reports.
- Full package ZIP SHA-256: stored only in `docs/downloads/full_public_2025_repro_package.zip.sha256` to avoid self-referential archive hashes.
- GitHub Pages source: `main:/docs`, status `built`, latest checked Pages run `26397873267` completed successfully.

## Notebook QA

- Total cells: `589`
- Code cells: `273`
- Markdown cells: `316`
- Maximum nonblank code lines in a code cell: `10`
- Rendered econometric explanations on public landing page: `273`
- Rendered code cells on public landing page: `273`
- Paper-number consistency checks: `6/6 pass`
- Maximum absolute paper-reference difference: `1.4210854715202004e-14`
- Old notebook filename present in public landing page: `false`

## Strategic meaning

This refresh does not change any accepted empirical number. It repairs the public-delivery failure identified by Pro and the operator: the public first screen is now the executed reader notebook itself, each code step is small, and the notebook visibly checks that central notebook numbers match the paper reference tables.
