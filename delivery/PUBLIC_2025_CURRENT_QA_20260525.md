# Public and Boox QA for the current 2025 release

Date: 2026-05-25

Status: `PASS` for public server and Boox refresh; final external review still pending.

## Public server

- Repository: `https://github.com/dkacz/self-defeating-public-investment-cuts-2025-repro-20260525`
- Latest public commit checked: `7bed821`
- GitHub Pages source: `main:/docs`
- GitHub Pages status: `built`
- Latest checked Pages run: `26397873267`, success
- Landing page: HTTP `200`, SHA-256 `eadf32d9fb0194065163350c8870fea2f122383fab13b988a04d06119f102953`
- Raw notebook: HTTP `200`, SHA-256 `23e688351dab68a5c836c0cc2ac7ae8e59f5146eb2e864ec576369b258d60d6e`
- Old audit-framed notebook URL: HTTP `404`
- Full public package ZIP checksum: stored only in `docs/downloads/full_public_2025_repro_package.zip.sha256` and verified after publication; no inline ZIP hash is stored in package reports.
- Release manifest: HTTP `200`; exact checksum verified after publication, not embedded inside package reports.

## Notebook QA

- Total cells: `589`
- Code cells: `273`
- Markdown cells: `316`
- Maximum nonblank code lines in a code cell: `10`
- Paper-number consistency checks: `6/6 pass`
- Maximum absolute paper-reference difference: `1.4210854715202004e-14`

## Boox

Current annotation-accounting files are present in `gdrive:onyx/NoteAir2/Read/fiscal` and downloaded hashes match local files. The active accounting file is `Annotation_Accounting_2025_Current_20260525.epub`.

## Strategic meaning

The accepted 2025 article, public notebook and Boox accounting now point to the same current object. The numbers in the step-by-step notebook match the paper reference tables up to machine rounding.
