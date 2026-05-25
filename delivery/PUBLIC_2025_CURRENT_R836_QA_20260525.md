# Public and Boox QA for the current R836 2025 release

Date: 2026-05-25

## Status

`PASS`.

## Public server

- Repository: `https://github.com/dkacz/self-defeating-public-investment-cuts-2025-repro-20260525`
- Commit: `e989445e0c78c903baaf533d00f8e8cdabe68733`
- GitHub Pages source: `main:/docs`
- GitHub Pages status: `built`
- Landing page: HTTP `200`
- JupyterLite notebook shell: HTTP `200`
- Raw notebook: HTTP `200`, bytes `271445`, SHA-256 `005969a60454f803816f527e9618cdaacd3cb79a2aea060c6fbfa0dbe081d2b3`
- Current annotation-accounting EPUB: HTTP `200`, bytes `23558`, SHA-256 `41df20b5eb926d61b4e493d6826b244483da61073fc071a4e90530b8cd6dc41f`
- Manifest: HTTP `200`, bytes `90061`

## Boox

Current R836 files are present in `gdrive:onyx/NoteAir2/Read/fiscal` and in the local Google Drive mirror. Hash checks passed for all current article and annotation-accounting files.

The active accounting file is `Annotation_Accounting_2025_Current_R836_20260525.epub`. It reflects Pro R6 `PASS 10/10` and no longer labels the accepted 2025 paper as a pre-R6 review object.

## Strategic meaning

The accepted 2025 article, public notebook and Boox accounting now point to the same current object. This closes the delivery gap that remained after R6: Pro had accepted the paper, but the operator-facing and public layers still needed to be brought into line.
