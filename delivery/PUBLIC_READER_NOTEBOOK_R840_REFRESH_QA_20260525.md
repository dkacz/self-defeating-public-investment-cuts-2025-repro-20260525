# Public reader-notebook refresh QA

Date: 2026-05-25

Status: `PASS`.

Public repository: `https://github.com/dkacz/self-defeating-public-investment-cuts-2025-repro-20260525`

Public commits:

- `469de94` (`Rebuild public notebook as reader-facing walkthrough`)
- `b1ce13f` (`Record public reader notebook deployment status`)
- `b756838` (`Remove self-referential deployment hashes`)
- `71a5740` (`Publish current annotation accounting after notebook rebuild`)

## Public URLs checked

- Landing page: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/`
- Raw notebook: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/notebooks/self_defeating_public_investment_cuts_2025_reproducibility.ipynb`
- Old audit-framed notebook URL: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/notebooks/self_defeating_public_investment_cuts_2025_granular_audit.ipynb`
- Current annotation accounting EPUB: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/annotation_accounting_current_r840_20260525/Annotation_Accounting_2025_Current_R840_20260525.epub`
- Full package checksum sidecar: `https://dkacz.github.io/self-defeating-public-investment-cuts-2025-repro-20260525/downloads/full_public_2025_repro_package.zip.sha256`

## HTTP and hash checks

- Landing page HTTP: `200`, bytes `284074`, SHA-256 `1feae9906eb13f576ef4e6987d61fc0c065cec0597a9309d3f88f7ffe590f520`
- Raw notebook HTTP: `200`, bytes `283808`, SHA-256 `0f89505b103934992b325e4510b588fb2c13afc077d2464a77681cd4bc3c8a5f`
- Old audit-framed notebook HTTP: `404`
- Current annotation accounting EPUB HTTP: `200`, bytes `24134`, SHA-256 `9ca0d4daf59263b53dc0846ff770669dcd99357f9a2ec4f65892fb0af5718b00`
- Full package ZIP SHA-256: `06ef8d51bdb87d9d191fb44ec809054fe8d90a8ba82cea5592661e9542bd3f23`

## Notebook QA

- Total cells: `320`
- Code cells: `150`
- Markdown cells: `170`
- Maximum nonblank code lines in a code cell: `20`
- Rendered `Econometric sense.` explanations on public landing page: `150`
- Rendered code cells on public landing page: `150`
- Old notebook filename present in public landing page: `false`

## Strategic meaning

This refresh does not change any accepted empirical number. It repairs the public-delivery failure identified by Pro and the operator: the public first screen is now the executed reader notebook itself, the old audit-framed notebook is gone from public notebook URLs, and each code step carries an explicit econometric explanation.
