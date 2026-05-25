# Public 2025 current notebook release

Date: 2026-05-25T05:48:24Z
Updated locally: 2026-05-25T11:09:39Z after granular notebook and paper-number consistency repair

Status: `PUBLIC_READER_NOTEBOOK_GRANULAR_REBUILD_PASS_PENDING_PUBLIC_REFRESH_AND_FINAL_REVIEW`.

This package originally exposed the current accepted 2025 notebook and article layer after strict Pro R6. After the later Pro remediation verdict and operator review, the public notebook layer has been rebuilt as a reader-facing executed notebook. After the operator's further granularity instruction, it was rebuilt again so that every code cell is small and the notebook explicitly compares its central numbers with the paper reference tables. The accepted numbers do not change. Public GitHub Pages, Boox/current annotation accounting, wiki state and final public-delivery review still need to be refreshed before the broader delivery goal can be treated as closed.

## 2026-05-25 reader-notebook rebuild

- New local notebook: `docs/notebooks/self_defeating_public_investment_cuts_2025_reproducibility.ipynb`
- New local root page: `docs/index.html`
- Old public audit-framed notebook removed locally from `docs/notebooks/`
- Notebook cells: `589`
- Code cells: `273`
- Markdown cells: `316`
- Maximum nonblank code lines per code cell: `10`
- Code cells with adjacent explicit `Econometric sense.` explanations: `273/273`
- Paper-number consistency checks: `6/6 pass`
- Maximum absolute paper-reference difference: `1.4210854715202004e-14`
- Execution errors: `0`
- Visible internal round labels / `audit` / `QA` hits in the notebook and root page: `0`
- Full local rebuild report: `artifacts/action_tasks/manuscript_imrad_20260427/public_notebook_remediation_pro_20260525/LOCAL_READER_NOTEBOOK_REBUILD_REPORT_20260525.md`
- Public repository was refreshed on `main` after the reader-notebook rebuild.
- Public landing page HTTP: `200`, bytes `284074`, SHA-256 `1feae9906eb13f576ef4e6987d61fc0c065cec0597a9309d3f88f7ffe590f520`
- Public raw notebook HTTP: `200`, bytes `283808`, SHA-256 `0f89505b103934992b325e4510b588fb2c13afc077d2464a77681cd4bc3c8a5f`
- Old audit-framed public notebook URL: `404`
- Full public package ZIP checksum is published in `docs/downloads/full_public_2025_repro_package.zip.sha256`.
- Current Boox/accounting update: `Annotation_Accounting_2025_Current_R840_20260525.epub`, SHA-256 `9ca0d4daf59263b53dc0846ff770669dcd99357f9a2ec4f65892fb0af5718b00`

## Public URLs

- Landing page: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/`
- Notebook: rendered directly at the landing page above.
- Raw notebook: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/notebooks/self_defeating_public_investment_cuts_2025_reproducibility.ipynb`
- Current annotation-accounting EPUB: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/annotation_accounting_current_r840_20260525/Annotation_Accounting_2025_Current_R840_20260525.epub`

## Key hashes

- Notebook SHA-256: `23e688351dab68a5c836c0cc2ac7ae8e59f5146eb2e864ec576369b258d60d6e`
- Rendered public notebook HTML SHA-256: `eadf32d9fb0194065163350c8870fea2f122383fab13b988a04d06119f102953`
- PDF SHA-256: `fda5ab3de8af7f6a21aed3e7adb0fb7137670d7e9e2ea3546f071354d238b150`
- EPUB SHA-256: `fe5bfa51bd615019514cc300e5e1854897ba31af8ce476ff490426f8184074c5`
- Current annotation-accounting EPUB SHA-256: `41df20b5eb926d61b4e493d6826b244483da61073fc071a4e90530b8cd6dc41f`
- Full public package ZIP SHA-256: stored only in `docs/downloads/full_public_2025_repro_package.zip.sha256` to avoid self-referential archive hashes.

## Publication QA

- GitHub repository: `https://github.com/dkacz/self-defeating-public-investment-cuts-2025-repro-20260525`
- Public repository commits: initial publication `e989445e0c78c903baaf533d00f8e8cdabe68733`; current Boox/accounting refresh `2289f87c315c6ecae23fce3ce4c21d76d23bade0`.
- GitHub Pages source: `main:/docs`
- GitHub Pages status: `built`
- Landing page HTTP: `200`
- JupyterLite notebook URL HTTP: `200`
- Raw notebook HTTP: `200`, bytes `271445`, hash matches local notebook.
- Current annotation-accounting EPUB HTTP: `200`, bytes `23558`, hash matches local EPUB.
- Manifest HTTP: `200`, bytes `90061`.

## Boox QA

Boox now has current R836 files for the article and annotation accounting:

- `Annotation_Accounting_2025_Current_R836_20260525.epub`
- `Annotation_Accounting_2025_Current_R836_20260525.html`
- `Annotation_Accounting_2025_Current_R836_20260525.md`
- `Self_Defeating_Public_Investment_Cuts_2025_Current_R836_20260525.pdf`
- `Self_Defeating_Public_Investment_Cuts_2025_Current_R836_20260525.epub`
- `Self_Defeating_Public_Investment_Cuts_2025_Current_R836_20260525.html`

Local-to-Boox hash checks are `PASS` for all current files. The current readable delivery layer no longer presents the accepted 2025 version as a pre-R6 review object.

## Strategic meaning

The public audit layer and Boox now follow the paper-truth state: the 2025 version is the current paper version, and neither the server entrypoint nor the active Boox accounting is stuck on the older 2026-05-21 or pre-R6 delivery layer.
