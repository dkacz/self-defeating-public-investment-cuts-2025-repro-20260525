# R834 annotation accounting for the 2025 candidate

Date: 2026-05-25

## Scope

R834 refreshes the annotation-accounting layer after the accepted R805 language-polish chunks were applied to the active QMD, the granular notebook was rerun, the article was rendered again, and the Boox candidate files were uploaded. The controlling rule is stronger than a normal reproducibility check: the notebook must expose the full estimation step by step. It does not repair manuscript prose beyond the applied polish and does not mark the candidate as accepted.

Inputs:

- R784 delta ledger: `artifacts/action_tasks/manuscript_imrad_20260427/mixed_window_2025_granular_notebook_20260524/annotation_delta_r784_20260524/results/R784_ANNOTATION_DELTA_LEDGER_20260524.csv`
- prior strict closure ledger: `artifacts/action_tasks/manuscript_imrad_20260427/strict_annotation_repro_repair_20260522/r760_mandatory_repair_r761_20260524/results/STRICT_ANNOTATION_EVIDENCE_LEDGER_R10_RESOLVED_PATHS_20260524.csv`
- current manuscript source: `artifacts/action_tasks/manuscript_imrad_20260427/manuscript_imrad.qmd`
- current rendered article after R834: `manuscript_imrad.html`, `manuscript_imrad.pdf`, `manuscript_imrad.epub`
- granular notebook after R834: `artifacts/action_tasks/manuscript_imrad_20260427/mixed_window_2025_granular_notebook_20260524/notebooks/mixed_window_2025_granular_audit.ipynb`

## Result

- total rows: `40`
- reopened after manuscript change: `13`
- reopened for strict notebook/repro audit: `11`
- carry-forward only after spot check: `16`
- rows marked finally closed in R834: `0`

## Outputs

- machine ledger: `artifacts/action_tasks/manuscript_imrad_20260427/mixed_window_2025_granular_notebook_20260524/annotation_accounting_r834_20260525/results/R834_ANNOTATION_ACCOUNTING_LEDGER_20260525.csv`
- summary: `artifacts/action_tasks/manuscript_imrad_20260427/mixed_window_2025_granular_notebook_20260524/annotation_accounting_r834_20260525/results/R834_ANNOTATION_ACCOUNTING_SUMMARY_20260525.csv`
- Boox-readable Markdown: `artifacts/action_tasks/manuscript_imrad_20260427/mixed_window_2025_granular_notebook_20260524/annotation_accounting_r834_20260525/delivery/Annotation_Accounting_2025_Candidate_R834_20260525.md`
- Boox-readable HTML: `artifacts/action_tasks/manuscript_imrad_20260427/mixed_window_2025_granular_notebook_20260524/annotation_accounting_r834_20260525/delivery/Annotation_Accounting_2025_Candidate_R834_20260525.html`
- Boox-readable EPUB: `artifacts/action_tasks/manuscript_imrad_20260427/mixed_window_2025_granular_notebook_20260524/annotation_accounting_r834_20260525/delivery/Annotation_Accounting_2025_Candidate_R834_20260525.epub`
- Boox delivery report: `artifacts/action_tasks/manuscript_imrad_20260427/mixed_window_2025_granular_notebook_20260524/annotation_accounting_r834_20260525/delivery/BOOX_DELIVERY_2025_CANDIDATE_R834_20260525.md`
- QA: `artifacts/action_tasks/manuscript_imrad_20260427/mixed_window_2025_granular_notebook_20260524/annotation_accounting_r834_20260525/qa/R834_ANNOTATION_ACCOUNTING_QA_20260525.csv`

## Strategic meaning

R834 prevents older annotation closure and older Boox material from being reused as if they certified the current post-polish manuscript surface. It also records the stronger notebook rule for the annotation layer: every material number must remain traceable through visible notebook cells. The 2025 candidate has a stronger notebook and a coherent article surface, but it remains non-citable until refreshed annotation, public-delivery hygiene and Pro 10/10 gates close.

The next Pro review must treat the notebook as the main estimation record. It is not enough to compare frozen article numbers with finished files: every p-value, response path, debt path, model-selection decision, table, figure and paper number must be traceable to visible notebook calculations step by step, with no hidden estimator outside the notebook.
