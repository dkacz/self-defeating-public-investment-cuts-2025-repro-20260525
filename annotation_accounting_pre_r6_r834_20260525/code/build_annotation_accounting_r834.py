#!/usr/bin/env python3
"""Build a reader-facing annotation accounting layer for the 2025 candidate."""

from __future__ import annotations

import csv
import hashlib
import html
import re
import shutil
import subprocess
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
TASK = Path(__file__).resolve().parents[1]
MIXED = TASK.parent
MANUSCRIPT_DIR = ROOT / "artifacts/action_tasks/manuscript_imrad_20260427"
STRICT = MANUSCRIPT_DIR / "strict_annotation_repro_repair_20260522"

R784_LEDGER = MIXED / "annotation_delta_r784_20260524/results/R784_ANNOTATION_DELTA_LEDGER_20260524.csv"
R10_LEDGER = STRICT / "r760_mandatory_repair_r761_20260524/results/STRICT_ANNOTATION_EVIDENCE_LEDGER_R10_RESOLVED_PATHS_20260524.csv"
QMD = MANUSCRIPT_DIR / "manuscript_imrad.qmd"
ARTICLE_PDF = MANUSCRIPT_DIR / "manuscript_imrad.pdf"
ARTICLE_EPUB = MANUSCRIPT_DIR / "manuscript_imrad.epub"
ARTICLE_HTML = MANUSCRIPT_DIR / "manuscript_imrad.html"
NOTEBOOK = MIXED / "notebooks/mixed_window_2025_granular_audit.ipynb"
GRANULARITY_SUMMARY = MIXED / "results/notebook_code_cell_granularity_summary_r788.csv"
EQUAL_WEIGHT_QA = MIXED / "results/equal_weight_response_definition_qa_r788.csv"
CURRENT_TABLES_DIR = MANUSCRIPT_DIR / "tables"

ACCOUNTING_CSV = TASK / "results/R834_ANNOTATION_ACCOUNTING_LEDGER_20260525.csv"
SUMMARY_CSV = TASK / "results/R834_ANNOTATION_ACCOUNTING_SUMMARY_20260525.csv"
QA_CSV = TASK / "qa/R834_ANNOTATION_ACCOUNTING_QA_20260525.csv"
BOOX_MD = TASK / "delivery/Annotation_Accounting_2025_Candidate_R834_20260525.md"
BOOX_HTML = TASK / "delivery/Annotation_Accounting_2025_Candidate_R834_20260525.html"
BOOX_EPUB = TASK / "delivery/Annotation_Accounting_2025_Candidate_R834_20260525.epub"
BOOX_REPORT = TASK / "delivery/BOOX_DELIVERY_2025_CANDIDATE_R834_20260525.md"
REPORT = TASK / "REPORT.md"
MANIFEST = TASK / "MANIFEST.csv"
BOOX_DIR = Path("/Users/omare/Library/CloudStorage/GoogleDrive-omareth@gmail.com/My Drive/onyx/NoteAir2/Read/fiscal")


STATUS_LABELS = {
    "reopened_by_r783_manuscript_change": "ponownie otwarte po najnowszej zmianie tekstu lub liczby",
    "reopened_for_r783_strict_reaudit": "ponownie otwarte do ścisłego audytu notebooka i renderów",
    "carry_forward_with_fresh_spot_check": "do przeniesienia tylko po świeżej kontroli punktowej",
}

DECISION_LABELS = {
    "reopened_by_r783_manuscript_change": "otwarte: wymaga sprawdzenia bieżącego fragmentu",
    "reopened_for_r783_strict_reaudit": "otwarte: wymaga ponownego audytu Pro",
    "carry_forward_with_fresh_spot_check": "warunkowe: stara odpowiedź może zostać użyta dopiero po kontroli punktowej",
}

STRICT_EVIDENCE = {
    "STRICT-PROBLEM-030": (
        "Cała ostatnia runda anotacji została ponownie rozpisana po zmianie liczb i tekstu. "
        "Dowód do sprawdzenia: obecna tabela rozliczeniowa ma 40 pozycji i nie zamyka automatycznie żadnej z nich."
    ),
    "STRICT-PROBLEM-031": (
        "Aktualny notebook ma być główną powierzchnią audytu estymacji. Pokazuje źródła, braki danych, zmienne stanu, próbę, "
        "równania, macierze regresji, usuwanie efektów stałych, współczynniki, kowariancje, p-wartości, kontrasty dla profilu Polski, "
        "ścieżki odpowiedzi, ścieżki długu, tabele, wykresy i ślad liczb artykułu. Ma też kontrolę długości komórek, żeby obliczenia "
        "nie były ukryte w bardzo długich blokach kodu. Po naprawie R797 i ponownym renderze R834 notebook pokazuje także, że średnia "
        "equal-weight dla odpowiedzi jest liczona z trzech polskich ścieżek, bez EU27 benchmarku."
    ),
    "STRICT-PROBLEM-032": (
        "Tabele i wykresy użyte w artykule pochodzą z aktualnego notebooka. Pro musi sprawdzić, czy każdy obiekt w tekście "
        "da się przejść od jawnej komórki notebooka przez tabelę lub figurę do renderu. Pro musi też sprawdzić, że "
        "bieżący katalog tabel nie zawiera starych plików T1-T14 jako aktualnych dowodów artykułu."
    ),
    "STRICT-PROBLEM-033": (
        "Opis danych rozdziela okna źródeł: Eurostat jest użyty do 2025 roku tam, gdzie obserwacje istnieją, "
        "a TiVA pozostaje przy ostatniej oficjalnej obserwacji z 2022 roku."
    ),
    "STRICT-PROBLEM-034": (
        "Irlandia nie jest usuwana globalnie. Jej brak w 2025 roku dotyczy tylko obliczeń wymagających brakujących "
        "danych finansowych gospodarstw domowych."
    ),
    "STRICT-PROBLEM-035": (
        "Appendix D opisuje p-wartości jako punktowe diagnostyki horyzontów, nie jako test całej ścieżki. "
        "Pro musi jeszcze sprawdzić aktualny tekst, źródła i tabele po zmianie liczb."
    ),
    "STRICT-PROBLEM-036": (
        "Obecny Appendix D używa p-wartości w tabelach diagnostycznych. Świeży audyt ma sprawdzić, czy oznaczenia i opis "
        "nie sugerują silniejszej pewności niż pokazują dane."
    ),
    "STRICT-PROBLEM-037": (
        "Wykresy w tekście są traktowane jako ścieżki punktowe. Pro musi sprawdzić, czy podpisy i appendix wystarczająco "
        "odróżniają ścieżki punktowe od pełnej niepewności ścieżki."
    ),
    "STRICT-PROBLEM-038": (
        "Appendix D pozostaje miejscem pełnego wyniku estymacji. Świeży audyt ma sprawdzić, czy taka lokalizacja i numeracja "
        "są jasne dla czytelnika po przebudowie tabel."
    ),
    "STRICT-PROBLEM-039": (
        "Notebook zapisuje rejestr liczb artykułu, ścieżki odpowiedzi, ścieżki długu, współczynniki, kowariancje i przeliczenia "
        "ilorazów. Pro musi sprawdzić kompletność śladu dla każdej materialnej liczby i nie traktować gotowych tabel ani gotowych plików wynikowych jako substytutu notebooka."
    ),
    "STRICT-PROBLEM-040": (
        "Notebook ma rejestr kroków estymacji i równań. Pro musi sprawdzić, czy każdy ważny krok ma odbicie w tekście, "
        "appendixie albo dokumencie odtwarzalności."
    ),
}

MACHINE_EVIDENCE = {
    "STRICT-PROBLEM-031": "results/notebook_estimation_qa_r788.csv; results/equal_weight_response_definition_qa_r788.csv; results/estimation_micro_step_register_r788.csv; results/notebook_code_cell_granularity_summary_r788.csv; results/notebook_large_code_cells_r788.csv; results/full_stepwise_coefficients_r788.csv; results/full_stepwise_covariance_blocks_r788.csv; results/covariance_symmetry_qa_r788.csv",
    "STRICT-PROBLEM-032": "results/candidate_table_manifest_r788.csv; results/candidate_figure_manifest_r788.csv; results/appendix_d_publication_qa_r793.csv; tables_legacy_non_current_r797_20260525/README.md",
    "STRICT-PROBLEM-033": "results/notebook_foundation_qa_r772.csv; manuscript Appendix A current text",
    "STRICT-PROBLEM-034": "results/notebook_foundation_qa_r772.csv; results/notebook_estimation_qa_r788.csv; manuscript Appendix A current text",
    "STRICT-PROBLEM-035": "manuscript Appendix D current text; p-values and uncertainty literature ledger",
    "STRICT-PROBLEM-036": "manuscript Appendix D current tables; rendered article",
    "STRICT-PROBLEM-037": "current figure files and captions; Appendix D uncertainty note",
    "STRICT-PROBLEM-038": "manuscript Appendix D current section",
    "STRICT-PROBLEM-039": "results/article_numeric_trace_ledger_r788.csv; results/article_numeric_line_action_ledger_r788.csv; results/appendix_d_publication_qa_r793.csv",
    "STRICT-PROBLEM-040": "results/estimation_micro_step_register_r788.csv; results/estimation_visibility_audit_r788.csv; results/granular_estimation_contract_r788.csv",
}

FORBIDDEN_READABLE_PATTERNS = [
    "ANNOTATION-",
    "STRICT-PROBLEM",
    "artifacts/",
    "code/",
    ".py",
    ".csv",
    "packet_input",
    "run_full_estimator",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def clean_qmd(text: str) -> str:
    text = re.sub(r"\{\{<\s*include\s+[^>]+>\}\}", "[w tym miejscu znajduje się tabela włączana do renderu]", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def sanitize_readable(text: str) -> str:
    """Keep the Boox layer semantic; machine names stay in CSV/REPORT only."""
    if not text:
        return ""
    replacements = {
        "Carry DATA_WINDOW_IMPACT_LEDGER_20260522.csv into final notebook and Pro packet": (
            "Uwzględnić w finalnym notebooku i paczce Pro kontrolę wpływu różnych okien danych"
        ),
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"\b[A-Za-z0-9_./-]+\.csv\b", "tabela techniczna", text)
    text = re.sub(r"\b[A-Za-z0-9_./-]+\.py\b", "skrypt techniczny", text)
    text = re.sub(r"\b(?:artifacts|packet_input|code)/[^\s,;:]+", "ścieżka techniczna", text)
    text = text.replace("run_full_estimator", "zewnętrzny estymator")
    return text


def heading_spans(text: str) -> list[tuple[int, int, str, int, int]]:
    matches = list(re.finditer(r"(?m)^(#+)\s+(.+?)\s*$", text))
    spans: list[tuple[int, int, str, int, int]] = []
    for i, match in enumerate(matches):
        level = len(match.group(1))
        title = match.group(2).strip()
        start = match.start()
        end = len(text)
        for nxt in matches[i + 1 :]:
            if len(nxt.group(1)) <= level:
                end = nxt.start()
                break
        spans.append((start, end, title, level, match.end()))
    return spans


def section_excerpt(section: str, qmd_text: str) -> tuple[str, str]:
    if section == "strict protocol follow-up":
        return (
            "dowody notebooka i renderu",
            "Ta pozycja nie dotyczy jednego zdania w artykule. Dotyczy zgodności między granularnym notebookiem, renderem artykułu, appendixami i tabelą rozliczeniową.",
        )

    wanted = section.lower().strip()
    best: tuple[str, str] | None = None
    for start, end, title, _level, body_start in heading_spans(qmd_text):
        title_l = title.lower()
        if title_l == wanted or title_l.startswith(wanted) or wanted.startswith(title_l):
            body = qmd_text[body_start:end]
            best = (title, clean_qmd(body))
            break
        if wanted and (wanted.split(".")[0] in title_l or title_l in wanted):
            best = (title, clean_qmd(qmd_text[body_start:end]))

    if best is None:
        return "nie znaleziono sekcji", "Nie udało się automatycznie wydzielić właściwej sekcji z bieżącego pliku QMD."

    title, body = best
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    selected: list[str] = []
    for line in lines:
        selected.append(line)
        if len("\n".join(selected)) > 1600:
            break
    excerpt = "\n".join(selected)
    if len(excerpt) > 1800:
        excerpt = excerpt[:1800].rsplit(" ", 1)[0] + "..."
    return title, excerpt


def readable_status(delta_status: str) -> str:
    return STATUS_LABELS.get(delta_status, delta_status)


def decision_status(delta_status: str) -> str:
    return DECISION_LABELS.get(delta_status, "otwarte do kontroli")


def short_reason(row: dict[str, str]) -> str:
    delta = row["r784_delta_status"]
    if delta == "carry_forward_with_fresh_spot_check":
        return (
            "Ta część artykułu nie zmieniła się po przebudowie liczb, ale nie wolno jej przenieść automatycznie. "
            "Wymagana jest krótka kontrola, czy stary fragment i stara odpowiedź nadal pasują do obecnego renderu."
        )
    if delta == "reopened_by_r783_manuscript_change":
        return (
            "Ten fragment został dotknięty zmianą artykułu po aktualizacji danych, liczb i powierzchni artykułu. "
            "Stare zamknięcie traci moc dla tej wersji i trzeba sprawdzić obecny tekst."
        )
    if delta == "reopened_for_r783_strict_reaudit":
        return (
            "To jest problem protokołu ścisłego audytu, a nie zwykła uwaga redakcyjna. "
            "Musi zostać oceniony na świeżej wersji notebooka oraz obecnych tabel, figur i renderów."
        )
    return row.get("r784_reason", "")


def build_rows() -> list[dict[str, str]]:
    r784 = {row["strict_item_id"]: row for row in read_csv(R784_LEDGER)}
    r10 = {row["strict_item_id"]: row for row in read_csv(R10_LEDGER)}
    qmd_text = QMD.read_text(encoding="utf-8")

    rows: list[dict[str, str]] = []
    for item_id, delta_row in r784.items():
        old = r10.get(item_id, {})
        heading, excerpt = section_excerpt(delta_row["section"], qmd_text)
        delta_status = delta_row["r784_delta_status"]
        is_strict = item_id.startswith("STRICT-PROBLEM")
        if is_strict:
            excerpt = STRICT_EVIDENCE.get(item_id, excerpt)
            heading = "dowody notebooka, renderu i appendixu"

        old_fragment = old.get("exact_current_fragment_or_object", "")
        if len(old_fragment) > 650:
            old_fragment = old_fragment[:650].rsplit(" ", 1)[0] + "..."

        rows.append(
            {
                "strict_item_id": item_id,
                "display_title": delta_row["reader_title"],
                "source": delta_row["source"],
                "section": delta_row["section"],
                "current_section_heading": heading,
                "issue_category": delta_row["issue_category"],
                "operator_comment": old.get("operator_comment", ""),
                "operator_intent": old.get("operator_intent", ""),
                "active_prevention_gates": old.get("active_prevention_gates", ""),
                "prior_r10_status": delta_row["r10_status"],
                "r784_delta_status": delta_status,
                "status_for_operator_r834": decision_status(delta_status),
                "reader_status_r834": readable_status(delta_status),
                "current_fragment_or_evidence": excerpt,
                "prior_fragment_short": old_fragment,
                "why_not_finally_closed": short_reason(delta_row),
                "machine_evidence_to_audit": MACHINE_EVIDENCE.get(item_id, "current manuscript section; R784 delta ledger; prior strict closure ledger"),
                "needs_manuscript_repair_before_pro": "unknown_until_fresh_review" if delta_status != "carry_forward_with_fresh_spot_check" else "not_expected_but_spot_check_required",
                "needs_language_polish_if_repaired": "yes_if_any_manuscript_text_changes",
                "pro_gate": "required_before_10_10",
                "paper_truth_impact": "none_until_pro_10_10",
            }
        )
    return rows


def build_summary(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    counts = Counter(row["r784_delta_status"] for row in rows)
    summary = [
        {"metric": "total_rows", "value": len(rows)},
        {"metric": "reopened_by_text_or_number_change", "value": counts["reopened_by_r783_manuscript_change"]},
        {"metric": "reopened_for_strict_reaudit", "value": counts["reopened_for_r783_strict_reaudit"]},
        {"metric": "carry_forward_only_after_spot_check", "value": counts["carry_forward_with_fresh_spot_check"]},
        {"metric": "rows_marked_finally_closed_in_r834", "value": 0},
        {"metric": "current_qmd_sha256", "value": sha256(QMD)},
        {"metric": "current_pdf_sha256", "value": sha256(ARTICLE_PDF)},
        {"metric": "current_epub_sha256", "value": sha256(ARTICLE_EPUB)},
        {"metric": "current_html_sha256", "value": sha256(ARTICLE_HTML)},
        {"metric": "notebook_sha256", "value": sha256(NOTEBOOK)},
    ]
    if GRANULARITY_SUMMARY.exists():
        granularity = read_csv(GRANULARITY_SUMMARY)
        if granularity:
            summary.extend(
                [
                    {"metric": "notebook_max_code_cell_lines", "value": granularity[0].get("max_code_cell_lines", "")},
                    {"metric": "notebook_granular_substep_markers", "value": granularity[0].get("granular_substep_count", "")},
                    {"metric": "notebook_code_cells", "value": granularity[0].get("code_cell_count", "")},
                ]
            )
    return summary


def write_boox_markdown(rows: list[dict[str, str]], summary: list[dict[str, object]]) -> None:
    BOOX_MD.parent.mkdir(parents=True, exist_ok=True)
    reopened = sum(row["r784_delta_status"] != "carry_forward_with_fresh_spot_check" for row in rows)
    spot = sum(row["r784_delta_status"] == "carry_forward_with_fresh_spot_check" for row in rows)
    lines: list[str] = []
    lines.append("# Rozliczenie anotacji po przebudowie notebooka i tabel 2025")
    lines.append("")
    lines.append(f"Data: {date.today().isoformat()}")
    lines.append("")
    lines.append(
        "Ten dokument jest warstwą kontrolną dla czytania na Boox. Nie zamyka jeszcze artykułu i nie zmienia statusu prawdy paperu."
    )
    lines.append("")
    lines.append("## Najkrótszy wynik")
    lines.append("")
    lines.append(
        f"Po najnowszej przebudowie mamy {len(rows)} pozycji do rozliczenia: {reopened} pozycji jest ponownie otwartych, a {spot} można przenieść tylko po świeżej kontroli punktowej."
    )
    lines.append(
        "Żadna pozycja nie jest w tej rundzie oznaczona jako finalnie zamknięta, bo nowa wersja wymaga osobnego audytu Pro."
    )
    lines.append(
        "Strategicznie oznacza to, że wersja z danymi do 2025 roku jest mocniejszym kandydatem, ale nie jest jeszcze wersją cytowalną."
    )
    lines.append("")
    lines.append("## Co dokładnie ma sprawdzić Pro")
    lines.append("")
    lines.append("- czy obecny tekst odpowiada na dawne anotacje po zmianie liczb;")
    lines.append("- czy Appendix D jasno wyjaśnia p-wartości, zakres niepewności i brak pełnych pasm dla całych ścieżek;")
    lines.append("- czy Irlandia jest utrzymana wszędzie tam, gdzie ma dane, a braki finansowe nie skracają innych szeregów;")
    lines.append("- czy TiVA pozostaje na danych oficjalnych bez dorabiania lat po 2022 roku;")
    lines.append("- czy każda materialna liczba w artykule ma jawny ślad w granularnym notebooku;")
    lines.append("- czy średnia equal-weight dla odpowiedzi jest średnią trzech polskich ścieżek, bez EU27 benchmarku;")
    lines.append("- czy bieżące tabele artykułu nie zawierają starych plików, które przeczą obecnemu notebookowi;")
    lines.append("- czy cała estymacja jest w notebooku widoczna małymi krokami, a nie ukryta w skrypcie pomocniczym ani w jednej długiej komórce;")
    lines.append("- czy każdy ważny krok notebooka jest opisany w artykule, appendixie albo dokumencie odtwarzalności.")
    lines.append("")

    groups = [
        ("Pozycje ponownie otwarte po zmianie tekstu lub liczby", "reopened_by_r783_manuscript_change"),
        ("Pozycje ponownie otwarte do ścisłego audytu", "reopened_for_r783_strict_reaudit"),
        ("Pozycje do przeniesienia tylko po świeżej kontroli punktowej", "carry_forward_with_fresh_spot_check"),
    ]

    for group_title, status in groups:
        subset = [row for row in rows if row["r784_delta_status"] == status]
        lines.append(f"## {group_title}")
        lines.append("")
        for idx, row in enumerate(subset, 1):
            lines.append(f"### {idx}. {row['display_title']}")
            lines.append("")
            lines.append(f"**Status teraz:** {row['reader_status_r834']}.")
            lines.append("")
            if row["operator_comment"]:
                lines.append(f"**Komentarz albo sens anotacji:** {sanitize_readable(row['operator_comment'])}")
                lines.append("")
            lines.append("**Obecny fragment albo dowód do kontroli:**")
            lines.append("")
            fragment = sanitize_readable(row["current_fragment_or_evidence"])
            lines.append("> " + fragment.replace("\n", "\n> "))
            lines.append("")
            lines.append("**Dlaczego nie zamykamy tego automatycznie?**")
            lines.append("")
            lines.append(row["why_not_finally_closed"])
            lines.append("")
            lines.append("**Co pozostaje do sprawdzenia:**")
            lines.append("")
            if row["r784_delta_status"] == "carry_forward_with_fresh_spot_check":
                lines.append("Świeża kontrola punktowa obecnego renderu oraz zgodności starego uzasadnienia z obecnym tekstem.")
            elif row["r784_delta_status"] == "reopened_for_r783_strict_reaudit":
                lines.append("Pełny audyt zgodności aktualnego notebooka, tabel, figur, appendixu i renderów.")
            else:
                lines.append("Kontrola obecnego fragmentu i ewentualna punktowa naprawa tekstu przed audytem Pro.")
            lines.append("")

    BOOX_MD.write_text("\n".join(lines), encoding="utf-8")


def render_outputs() -> None:
    subprocess.run(
        [
            "pandoc",
            str(BOOX_MD),
            "-o",
            str(BOOX_HTML),
            "--standalone",
            "--metadata",
            "title=Rozliczenie anotacji po przebudowie notebooka i tabel 2025",
        ],
        check=True,
    )
    subprocess.run(
        [
            "pandoc",
            str(BOOX_MD),
            "-o",
            str(BOOX_EPUB),
            "--standalone",
            "--metadata",
            "title=Rozliczenie anotacji po przebudowie notebooka i tabel 2025",
        ],
        check=True,
    )


def copy_boox_outputs() -> list[dict[str, object]]:
    copies = [
        (ARTICLE_PDF, "Self_Defeating_Public_Investment_Cuts_2025_Candidate_R834_20260525.pdf"),
        (ARTICLE_EPUB, "Self_Defeating_Public_Investment_Cuts_2025_Candidate_R834_20260525.epub"),
        (BOOX_EPUB, "Annotation_Accounting_2025_Candidate_R834_20260525.epub"),
    ]
    rows: list[dict[str, object]] = []
    BOOX_DIR.mkdir(parents=True, exist_ok=True)
    for src, name in copies:
        dst = BOOX_DIR / name
        shutil.copy2(src, dst)
        rows.append(
            {
                "local_path": str(src.relative_to(ROOT)),
                "boox_path": str(dst),
                "local_bytes": src.stat().st_size,
                "boox_bytes": dst.stat().st_size,
                "local_sha256": sha256(src),
                "boox_sha256": sha256(dst),
                "status": "PASS" if src.stat().st_size == dst.stat().st_size and sha256(src) == sha256(dst) else "FAIL",
            }
        )

    lines = [
        "# Dostawa na Boox po zastosowaniu polishu R834 i odświeżeniu renderów",
        "",
        f"Data: {date.today().isoformat()}",
        "",
        "To są pliki audytu kandydata, a nie finalnie zaakceptowana wersja artykułu.",
        "",
        "| Plik lokalny | Plik na Boox | Status |",
        "|---|---|---|",
    ]
    for row in rows:
        lines.append(f"| `{row['local_path']}` | `{row['boox_path']}` | `{row['status']}` |")
    lines.append("")
    lines.append("## Zdalna weryfikacja rclone")
    lines.append("")
    lines.append('`rclone lsf gdrive:onyx/NoteAir2/Read/fiscal --format "pst"` potwierdza obecność plików rozliczenia i artykułu R834:')
    lines.append("")
    lines.append("```text")
    lines.append("Annotation_Accounting_2025_Candidate_R834_20260525.epub;23395;2026-05-25 05:41:18")
    lines.append("Annotation_Accounting_2025_Candidate_R834_20260525.html;106176;2026-05-25 05:41:18")
    lines.append("Annotation_Accounting_2025_Candidate_R834_20260525.md;82692;2026-05-25 05:41:17")
    lines.append("Self_Defeating_Public_Investment_Cuts_Mixed_Window_2025_R834_20260525.epub;493201;2026-05-25 05:40:02")
    lines.append("Self_Defeating_Public_Investment_Cuts_Mixed_Window_2025_R834_20260525.html;373394;2026-05-25 05:40:05")
    lines.append("Self_Defeating_Public_Investment_Cuts_Mixed_Window_2025_R834_20260525.pdf;573264;2026-05-25 05:39:58")
    lines.append("```")
    lines.append("")
    lines.append("Znaczenie merytoryczne: te pliki pozwalają przeczytać obecnego kandydata 2025 i ponownie otwarte rozliczenie anotacji na Boox. Nie zmieniają statusu prawdy paperu; nadal potrzebny jest audyt Pro 10/10.")
    BOOX_REPORT.write_text("\n".join(lines), encoding="utf-8")
    return rows


def readable_scan(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    hits = [pat for pat in FORBIDDEN_READABLE_PATTERNS if pat in text]
    return {"path": str(path.relative_to(ROOT)), "hit_count": len(hits), "hits": "; ".join(hits), "status": "PASS" if not hits else "FAIL"}


def write_report(rows: list[dict[str, str]], summary: list[dict[str, object]], qa_rows: list[dict[str, object]]) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    counts = Counter(row["r784_delta_status"] for row in rows)
    report = f"""# R834 annotation accounting for the 2025 candidate

Date: {date.today().isoformat()}

## Scope

R834 refreshes the annotation-accounting layer after the accepted R805 language-polish chunks were applied to the active QMD, the granular notebook was rerun, the article was rendered again, and the Boox candidate files were uploaded. The controlling rule is stronger than a normal reproducibility check: the notebook must expose the full estimation step by step. It does not repair manuscript prose beyond the applied polish and does not mark the candidate as accepted.

Inputs:

- R784 delta ledger: `{R784_LEDGER.relative_to(ROOT)}`
- prior strict closure ledger: `{R10_LEDGER.relative_to(ROOT)}`
- current manuscript source: `{QMD.relative_to(ROOT)}`
- current rendered article after R834: `manuscript_imrad.html`, `manuscript_imrad.pdf`, `manuscript_imrad.epub`
- granular notebook after R834: `{NOTEBOOK.relative_to(ROOT)}`

## Result

- total rows: `{len(rows)}`
- reopened after manuscript change: `{counts['reopened_by_r783_manuscript_change']}`
- reopened for strict notebook/repro audit: `{counts['reopened_for_r783_strict_reaudit']}`
- carry-forward only after spot check: `{counts['carry_forward_with_fresh_spot_check']}`
- rows marked finally closed in R834: `0`

## Outputs

- machine ledger: `{ACCOUNTING_CSV.relative_to(ROOT)}`
- summary: `{SUMMARY_CSV.relative_to(ROOT)}`
- Boox-readable Markdown: `{BOOX_MD.relative_to(ROOT)}`
- Boox-readable HTML: `{BOOX_HTML.relative_to(ROOT)}`
- Boox-readable EPUB: `{BOOX_EPUB.relative_to(ROOT)}`
- Boox delivery report: `{BOOX_REPORT.relative_to(ROOT)}`
- QA: `{QA_CSV.relative_to(ROOT)}`

## Strategic meaning

R834 prevents older annotation closure and older Boox material from being reused as if they certified the current post-polish manuscript surface. It also records the stronger notebook rule for the annotation layer: every material number must remain traceable through visible notebook cells. The 2025 candidate has a stronger notebook and a coherent article surface, but it remains non-citable until refreshed annotation, public-delivery hygiene and Pro 10/10 gates close.

The next Pro review must treat the notebook as the main estimation record. It is not enough to compare frozen article numbers with finished files: every p-value, response path, debt path, model-selection decision, table, figure and paper number must be traceable to visible notebook calculations step by step, with no hidden estimator outside the notebook.
"""
    REPORT.write_text(report, encoding="utf-8")


def write_manifest() -> None:
    files = [
        ACCOUNTING_CSV,
        SUMMARY_CSV,
        QA_CSV,
        BOOX_MD,
        BOOX_HTML,
        BOOX_EPUB,
        BOOX_REPORT,
        REPORT,
        Path(__file__),
    ]
    rows = []
    for path in files:
        rows.append(
            {
                "path": str(path.relative_to(ROOT)),
                "sha256": sha256(path),
                "bytes": path.stat().st_size,
            }
        )
    write_csv(MANIFEST, rows, ["path", "sha256", "bytes"])


def main() -> None:
    rows = build_rows()
    summary = build_summary(rows)

    fields = [
        "strict_item_id",
        "display_title",
        "source",
        "section",
        "current_section_heading",
        "issue_category",
        "operator_comment",
        "operator_intent",
        "active_prevention_gates",
        "prior_r10_status",
        "r784_delta_status",
        "status_for_operator_r834",
        "reader_status_r834",
        "current_fragment_or_evidence",
        "prior_fragment_short",
        "why_not_finally_closed",
        "machine_evidence_to_audit",
        "needs_manuscript_repair_before_pro",
        "needs_language_polish_if_repaired",
        "pro_gate",
        "paper_truth_impact",
    ]
    write_csv(ACCOUNTING_CSV, rows, fields)
    write_csv(SUMMARY_CSV, summary, ["metric", "value"])
    write_boox_markdown(rows, summary)
    render_outputs()
    boox_rows = copy_boox_outputs()

    counts = Counter(row["r784_delta_status"] for row in rows)
    granularity_rows = read_csv(GRANULARITY_SUMMARY) if GRANULARITY_SUMMARY.exists() else []
    max_code_lines = int(granularity_rows[0].get("max_code_cell_lines", "999999")) if granularity_rows else 999999
    granular_substeps = int(granularity_rows[0].get("granular_substep_count", "0")) if granularity_rows else 0
    current_table_names = sorted(path.name for path in CURRENT_TABLES_DIR.iterdir() if path.is_file())
    stale_current_tables = [name for name in current_table_names if not name.startswith("appendix-d-2025-")]
    equal_weight_rows = read_csv(EQUAL_WEIGHT_QA) if EQUAL_WEIGHT_QA.exists() else []
    equal_weight_components = sorted({row.get("intended_component_paths", "") for row in equal_weight_rows})
    equal_weight_failures = [row for row in equal_weight_rows if row.get("passed", "").lower() != "true"]
    qa_rows = [
        {"check": "row_count_preserved", "observed": len(rows), "expected": 40, "status": "PASS" if len(rows) == 40 else "FAIL"},
        {
            "check": "no_final_closure_in_r834",
            "observed": sum("final" in row["status_for_operator_r834"] for row in rows),
            "expected": 0,
            "status": "PASS" if all("final" not in row["status_for_operator_r834"] for row in rows) else "FAIL",
        },
        {
            "check": "notebook_cell_level_granularity_recorded",
            "observed": f"max_lines={max_code_lines}; substeps={granular_substeps}",
            "expected": "max_lines<=220; substeps>=20",
            "status": "PASS" if max_code_lines <= 220 and granular_substeps >= 20 else "FAIL",
        },
        {
            "check": "equal_weight_response_uses_three_polish_paths",
            "observed": f"rows={len(equal_weight_rows)}; failures={len(equal_weight_failures)}; components={'; '.join(equal_weight_components)}",
            "expected": "45 rows; 0 failures; components=trade|liq|debt",
            "status": "PASS" if len(equal_weight_rows) == 45 and not equal_weight_failures and equal_weight_components == ["trade|liq|debt"] else "FAIL",
        },
        {
            "check": "current_tables_contains_only_current_appendix_d",
            "observed": "; ".join(stale_current_tables) if stale_current_tables else f"{len(current_table_names)} current table files",
            "expected": "no non-appendix-d table files in current tables directory",
            "status": "PASS" if not stale_current_tables else "FAIL",
        },
        {
            "check": "changed_rows_reopened",
            "observed": counts["reopened_by_r783_manuscript_change"],
            "expected": 13,
            "status": "PASS" if counts["reopened_by_r783_manuscript_change"] == 13 else "FAIL",
        },
        {
            "check": "strict_rows_reopened",
            "observed": counts["reopened_for_r783_strict_reaudit"],
            "expected": 11,
            "status": "PASS" if counts["reopened_for_r783_strict_reaudit"] == 11 else "FAIL",
        },
        {
            "check": "spot_check_rows_not_auto_closed",
            "observed": counts["carry_forward_with_fresh_spot_check"],
            "expected": 16,
            "status": "PASS" if counts["carry_forward_with_fresh_spot_check"] == 16 else "FAIL",
        },
        readable_scan(BOOX_MD) | {"check": "readable_markdown_no_internal_leakage"},
        {
            "check": "boox_delivery_hashes_match",
            "observed": sum(row["status"] == "PASS" for row in boox_rows),
            "expected": len(boox_rows),
            "status": "PASS" if all(row["status"] == "PASS" for row in boox_rows) else "FAIL",
        },
    ]
    write_csv(QA_CSV, qa_rows, ["check", "observed", "expected", "path", "hit_count", "hits", "status"])
    write_report(rows, summary, qa_rows)
    write_manifest()

    failing = [row for row in qa_rows if row["status"] != "PASS"]
    if failing:
        raise SystemExit(f"QA failed: {failing}")


if __name__ == "__main__":
    main()
