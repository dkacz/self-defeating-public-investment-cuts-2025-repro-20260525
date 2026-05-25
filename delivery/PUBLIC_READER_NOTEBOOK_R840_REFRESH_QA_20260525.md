# Public reader-notebook refresh QA

Date: 2026-05-25

Status: `PASS`.

Public repository: `https://github.com/dkacz/self-defeating-public-investment-cuts-2025-repro-20260525`

Public commits:

- `469de94` (`Rebuild public notebook as reader-facing walkthrough`)
- `b1ce13f` (`Record public reader notebook deployment status`)
- `b756838` (`Remove self-referential deployment hashes`)
- `71a5740` (`Publish current annotation accounting after notebook rebuild`)
- `0f01bfc` (`Make public notebook granular and paper-consistent`)

## Public URLs checked

- Landing page: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/`
- Raw notebook: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/notebooks/self_defeating_public_investment_cuts_2025_reproducibility.ipynb`
- Old audit-framed notebook URL: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/notebooks/self_defeating_public_investment_cuts_2025_granular_audit.ipynb`
- Current annotation accounting EPUB: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/annotation_accounting_current_r840_20260525/Annotation_Accounting_2025_Current_R840_20260525.epub`
- Full package checksum sidecar: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/downloads/full_public_2025_repro_package.zip.sha256`

## HTTP and hash checks

- Landing page HTTP: `200`, bytes `363746`, SHA-256 `eadf32d9fb0194065163350c8870fea2f122383fab13b988a04d06119f102953`
- Raw notebook HTTP: `200`, bytes `363638`, SHA-256 `23e688351dab68a5c836c0cc2ac7ae8e59f5146eb2e864ec576369b258d60d6e`
- Old audit-framed notebook HTTP: `404`
- Current annotation accounting EPUB HTTP: `200`, bytes `24134`, SHA-256 `9ca0d4daf59263b53dc0846ff770669dcd99357f9a2ec4f65892fb0af5718b00`
- Full package ZIP SHA-256: `1133dd11ae4aba1a6feb9338a6bf9e4c34502bda42ef7632812c7dc8abec563b`
- GitHub Pages source: `main:/docs`, status `built`, latest Pages run `26397553225` completed successfully.

## Notebook QA

- Total cells: `589`
- Code cells: `273`
- Markdown cells: `316`
- Maximum nonblank code lines in a code cell: `10`
- Rendered `Econometric sense.` explanations on public landing page: `273`
- Rendered code cells on public landing page: `273`
- Paper-number consistency checks: `6/6 pass`
- Maximum absolute paper-reference difference: `1.4210854715202004e-14`
- Old notebook filename present in public landing page: `false`

## Strategic meaning

This refresh does not change any accepted empirical number. It repairs the public-delivery failure identified by Pro and the operator, and the later operator finding that the cells were still too large: the public first screen is now the executed reader notebook itself, the old audit-framed notebook is gone from public notebook URLs, each code step is small, and the notebook visibly checks that central notebook numbers match the paper reference tables.
