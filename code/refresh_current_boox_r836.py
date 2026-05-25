#!/usr/bin/env python3
"""Refresh Boox-facing current files after the R6 10/10 verdict."""

from __future__ import annotations

import csv
import hashlib
import shutil
import subprocess
import zipfile
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
MANUSCRIPT_DIR = ROOT / "artifacts/action_tasks/manuscript_imrad_20260427"
MIXED_DIR = MANUSCRIPT_DIR / "mixed_window_2025_granular_notebook_20260524"
PUBLIC_DIR = MANUSCRIPT_DIR / "public_2025_current_notebook_release_20260525"
R834_ACCOUNTING = MIXED_DIR / "annotation_accounting_r834_20260525"
CURRENT_ACCOUNTING = MIXED_DIR / "annotation_accounting_current_r836_20260525"
CURRENT_BOOX = MIXED_DIR / "boox_delivery_current_r836_20260525"
R6_SUMMARY = (
    MIXED_DIR
    / "pro_review/strict_2025_candidate_r6_20260525/harvest/"
    / "HARVEST_SUMMARY_MIXED_WINDOW_2025_POST_POLISH_STRICT_R6.md"
)
BOOX_DIR = (
    Path.home()
    / "Library/CloudStorage/GoogleDrive-omareth@gmail.com/My Drive/onyx/NoteAir2/Read/fiscal"
)
RCLONE_REMOTE = "gdrive:onyx/NoteAir2/Read/fiscal"

ARTICLE_FILES = {
    "pdf": MANUSCRIPT_DIR / "manuscript_imrad.pdf",
    "epub": MANUSCRIPT_DIR / "manuscript_imrad.epub",
    "html": MANUSCRIPT_DIR / "manuscript_imrad.html",
}
ACCOUNTING_SOURCE_MD = (
    R834_ACCOUNTING
    / "delivery/Annotation_Accounting_2025_Candidate_R834_20260525.md"
)
CURRENT_MD = CURRENT_ACCOUNTING / "delivery/Annotation_Accounting_2025_Current_R836_20260525.md"
CURRENT_HTML = CURRENT_ACCOUNTING / "delivery/Annotation_Accounting_2025_Current_R836_20260525.html"
CURRENT_EPUB = CURRENT_ACCOUNTING / "delivery/Annotation_Accounting_2025_Current_R836_20260525.epub"
CURRENT_REPORT = CURRENT_ACCOUNTING / "REPORT.md"
CURRENT_MANIFEST = CURRENT_ACCOUNTING / "MANIFEST.csv"
CURRENT_QA = CURRENT_ACCOUNTING / "qa/R836_CURRENT_BOOX_QA_20260525.csv"
CURRENT_DELIVERY_REPORT = CURRENT_ACCOUNTING / "delivery/BOOX_DELIVERY_2025_CURRENT_R836_20260525.md"
SHA_FILE = CURRENT_ACCOUNTING / "delivery/SHA256SUMS_CURRENT_R836_20260525.txt"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def currentize_markdown(text: str) -> str:
    marker = "## Pozycje ponownie otwarte po zmianie tekstu lub liczby"
    rest = text[text.index(marker) :] if marker in text else text
    rest = rest.replace(
        "**Status teraz:** ponownie otwarte po najnowszej zmianie tekstu lub liczby.",
        "**Status po R6:** objete audytem Pro R6; brak wymaganej poprawki. Historycznie pozycja byla ponownie otwarta po zmianie tekstu lub liczby.",
    )
    rest = rest.replace(
        "**Status teraz:** ponownie otwarte do ścisłego audytu notebooka i renderów.",
        "**Status po R6:** objete audytem Pro R6; brak wymaganej poprawki. Historycznie pozycja byla ponownie otwarta do scislego audytu notebooka i renderow.",
    )
    rest = rest.replace(
        "**Status teraz:** do przeniesienia tylko po świeżej kontroli punktowej.",
        "**Status po R6:** objete audytem Pro R6; brak wymaganej poprawki. Historycznie pozycja byla przeniesiona tylko po swiezej kontroli punktowej.",
    )
    rest = rest.replace(
        "**Dlaczego nie zamykamy tego automatycznie?**",
        "**Dlaczego ta pozycja byla ryzykowna przed R6?**",
    )
    rest = rest.replace(
        "**Co pozostaje do sprawdzenia:**",
        "**Wynik po R6:**",
    )
    rest = rest.replace(
        "Ten fragment został dotknięty zmianą artykułu po aktualizacji danych, liczb i powierzchni artykułu. Stare zamknięcie traci moc dla tej wersji i trzeba sprawdzić obecny tekst.",
        "Ten fragment byl ryzykowny, bo zmiana danych, liczb albo powierzchni artykulu mogla uniewaznic starsze zamkniecie. Pro R6 sprawdzil obecna wersje i nie wskazal wymaganej poprawki.",
    )
    rest = rest.replace(
        "Kontrola obecnego fragmentu i ewentualna punktowa naprawa tekstu przed audytem Pro.",
        "Pro R6 potwierdzil brak wymaganej poprawki dla biezacej wersji 2025; pozycja zostaje w rozliczeniu jako slad tego, co bylo ponownie sprawdzane.",
    )
    rest = rest.replace(
        "To jest problem protokołu ścisłego audytu, a nie zwykła uwaga redakcyjna. Musi zostać oceniony na świeżej wersji notebooka oraz obecnych tabel, figur i renderów.",
        "To byl problem protokolu scislego audytu, a nie zwykla uwaga redakcyjna. Pro R6 ocenil swieza wersje notebooka, obecne tabele, figury i rendery.",
    )
    rest = rest.replace(
        "Pełny audyt zgodności aktualnego notebooka, tabel, figur, appendixu i renderów.",
        "Pro R6 uznal notebook za wiazacy zapis obliczen i potwierdzil zgodnosc liczb, tabel, figur, p-wartosci, sciezek reakcji, sciezek dlugu i mapowania do artykulu.",
    )
    rest = rest.replace(
        "Ta część artykułu nie zmieniła się po przebudowie liczb, ale nie wolno jej przenieść automatycznie. Wymagana jest krótka kontrola, czy stary fragment i stara odpowiedź nadal pasują do obecnego renderu.",
        "Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starego zamkniecia bez sprawdzenia obecnego renderu. Pro R6 nie wskazal wymaganej poprawki.",
    )
    rest = rest.replace(
        "Świeża kontrola punktowa obecnego renderu oraz zgodności starego uzasadnienia z obecnym tekstem.",
        "Pro R6 potwierdzil brak wymaganej poprawki dla biezacego renderu; pozycja zostaje w rozliczeniu jako slad kontroli punktowej.",
    )
    header = """# Aktualne rozliczenie anotacji po R6 dla wersji 2025

Data: 2026-05-25

Ten dokument jest aktualna warstwa kontrolna do czytania na Boox. Zastepuje ostrozna etykiete uzywana przed R6: po audycie Pro R6 wersja mixed-window 2025 ma `PASS`, `10/10` i moze zastapic wersje 2022 jako biezaca wersja paperu.

## Najkrotszy wynik

Rozliczenie obejmuje 40 pozycji: 13 bylo ponownie otwartych przez zmiane tekstu lub liczb, 11 przez wymog scislego audytu notebooka i odtwarzalnosci, a 16 przeniesiono dopiero po swiezej kontroli punktowej. Pro R6 nie wskazal zadnych wymaganych poprawek. Strategicznie oznacza to, ze rozliczenie Boox, notebook i artykul mowia teraz o tej samej biezacej wersji 2025.

## Co sprawdzil Pro w R6

- zgodnosc obecnego tekstu z dawnymi anotacjami po zmianie liczb;
- jawna reprodukcje danych zrodlowych, brakow, zmiennych, proby, rownan, wspolczynnikow, p-wartosci, sciezek reakcji, sciezek dlugu, tabel i wykresow w notebooku;
- zasade mixed-window: Eurostat do 2025 tam, gdzie dane istnieja, Irlandia utrzymana wszedzie poza obliczeniami wymagajacymi brakujacej komorki finansowej, TiVA bez dorabiania lat po 2022;
- brak ukrytego zewnetrznego estymatora jako biezacej maszynerii obliczen;
- zgodnosc polishu, renderow, tabel, figur i mapowania liczb do artykulu.

## Jak czytac ponizszy spis

Ponizsze pozycje zachowuja historie ryzyk sprzed R6, bo to wlasnie one mialy zostac sprawdzone. Status "po R6" nie znaczy, ze problem byl ignorowany; znaczy, ze zostal objety audytem R6 i nie zostawil wymaganej poprawki dla biezacej wersji 2025.

"""
    return header + rest


def render_current_accounting() -> None:
    CURRENT_MD.parent.mkdir(parents=True, exist_ok=True)
    text = currentize_markdown(ACCOUNTING_SOURCE_MD.read_text(encoding="utf-8"))
    CURRENT_MD.write_text(text, encoding="utf-8")
    subprocess.run(
        [
            "pandoc",
            str(CURRENT_MD),
            "-o",
            str(CURRENT_HTML),
            "--standalone",
            "--metadata",
            "title=Aktualne rozliczenie anotacji po R6 dla wersji 2025",
        ],
        check=True,
    )
    subprocess.run(
        [
            "pandoc",
            str(CURRENT_MD),
            "-o",
            str(CURRENT_EPUB),
            "--metadata",
            "title=Aktualne rozliczenie anotacji po R6 dla wersji 2025",
        ],
        check=True,
    )


def copy_article_current_files() -> list[Path]:
    CURRENT_BOOX.mkdir(parents=True, exist_ok=True)
    copied = []
    for suffix, src in ARTICLE_FILES.items():
        dst = CURRENT_BOOX / f"Self_Defeating_Public_Investment_Cuts_2025_Current_R836_20260525.{suffix}"
        shutil.copy2(src, dst)
        copied.append(dst)
    return copied


def write_hashes(files: list[Path]) -> None:
    lines = [f"{sha256(path)}  {path.name}" for path in files]
    SHA_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def copy_to_boox(files: list[Path]) -> list[dict[str, str]]:
    BOOX_DIR.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, str]] = []
    for src in files:
        local_dst = BOOX_DIR / src.name
        shutil.copy2(src, local_dst)
        subprocess.run(
            ["rclone", "copyto", str(src), f"{RCLONE_REMOTE}/{src.name}"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        rows.append(
            {
                "file": src.name,
                "local_sha256": sha256(src),
                "boox_local_sha256": sha256(local_dst),
                "status": "PASS" if sha256(src) == sha256(local_dst) else "FAIL",
            }
        )
    return rows


def rclone_listing() -> str:
    proc = subprocess.run(
        ["rclone", "lsf", RCLONE_REMOTE, "--format", "pst"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    wanted = [
        "Annotation_Accounting_2025_Current_R836_20260525",
        "Self_Defeating_Public_Investment_Cuts_2025_Current_R836_20260525",
        "SHA256SUMS_CURRENT_R836_20260525",
        "BOOX_DELIVERY_2025_CURRENT_R836_20260525",
    ]
    return "\n".join(line for line in proc.stdout.splitlines() if any(w in line for w in wanted))


def write_reports(files: list[Path], boox_rows: list[dict[str, str]], listing: str) -> None:
    CURRENT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    report = f"""# Current Boox and annotation accounting after R6

Date: {date.today().isoformat()}

## Scope

This refresh removes the stale pre-R6 label from the reader-facing delivery layer after strict Pro R6 returned `PASS` and `10/10`. It does not recompute estimates. It carries forward the R834 annotation-accounting evidence and adds the R6 verdict as the current status layer.

## Result

- current paper status: accepted current 2025 version after Pro R6
- current annotation accounting: `Annotation_Accounting_2025_Current_R836_20260525.epub`
- current Boox article files: PDF, EPUB and HTML with `Current_R836_20260525` filenames
- R6 source: `{R6_SUMMARY.relative_to(ROOT)}`

## Files

"""
    for path in files:
        report += f"- `{path.relative_to(ROOT)}` sha256 `{sha256(path)}`\n"
    report += """
## Strategic meaning

The Boox layer now matches the paper-truth state: it no longer presents the 2025 paper as a pre-verdict review object after R6. This matters because operator annotations, the public notebook and the accepted article now refer to the same current object. The remaining risk is historical: older pre-R6 files may still exist as archive copies, but the active files are the `Current_R836_20260525` delivery files listed here.
"""
    CURRENT_REPORT.write_text(report, encoding="utf-8")

    lines = [
        "# Aktualna dostawa Boox po R6",
        "",
        f"Data: {date.today().isoformat()}",
        "",
        "To jest aktualna wersja po audycie Pro R6: `PASS`, `10/10`, brak wymaganych poprawek. Starsze pliki sprzed R6 pozostaja tylko historia.",
        "",
        "| Plik | SHA-256 | Status kopii Boox |",
        "|---|---|---|",
    ]
    for row in boox_rows:
        lines.append(f"| `{row['file']}` | `{row['local_sha256']}` | `{row['status']}` |")
    lines.extend(["", "## Zdalna weryfikacja rclone", "", "```text", listing, "```", ""])
    lines.append("Znaczenie merytoryczne: Boox pokazuje teraz ta sama biezaca wersje 2025, ktora Pro R6 dopuscil jako aktualna prawde paperu.")
    CURRENT_DELIVERY_REPORT.write_text("\n".join(lines), encoding="utf-8")

    manifest_rows = []
    for path in [*files, CURRENT_REPORT, CURRENT_DELIVERY_REPORT]:
        manifest_rows.append(
            {"path": str(path.relative_to(ROOT)), "sha256": sha256(path), "bytes": path.stat().st_size}
        )
    CURRENT_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with CURRENT_MANIFEST.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["path", "sha256", "bytes"])
        writer.writeheader()
        writer.writerows(manifest_rows)


def move_stale_public_dirs() -> None:
    moves = [
        (
            PUBLIC_DIR / "annotation_accounting_current_20260525",
            PUBLIC_DIR / "annotation_accounting_pre_r6_r834_20260525",
        ),
        (
            PUBLIC_DIR / "boox_delivery_current_20260525",
            PUBLIC_DIR / "boox_delivery_pre_r6_r834_20260525",
        ),
    ]
    for src, dst in moves:
        if src.exists():
            if dst.exists():
                shutil.rmtree(dst)
            src.rename(dst)


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def refresh_public_package() -> None:
    move_stale_public_dirs()
    copy_tree(CURRENT_ACCOUNTING, PUBLIC_DIR / "annotation_accounting_current_r836_20260525")
    copy_tree(CURRENT_BOOX, PUBLIC_DIR / "boox_delivery_current_r836_20260525")
    docs = PUBLIC_DIR / "docs"
    copy_tree(CURRENT_ACCOUNTING / "delivery", docs / "annotation_accounting_current_r836_20260525")
    copy_tree(CURRENT_BOOX, docs / "boox_delivery_current_r836_20260525")
    qa_dst = PUBLIC_DIR / "qa/R836_CURRENT_BOOX_QA_20260525.csv"
    qa_dst.parent.mkdir(parents=True, exist_ok=True)
    if CURRENT_QA.exists():
        shutil.copy2(CURRENT_QA, qa_dst)

    index = docs / "index.html"
    html = index.read_text(encoding="utf-8")
    link = (
        '    <a class="card" href="annotation_accounting_current_r836_20260525/'
        'Annotation_Accounting_2025_Current_R836_20260525.epub"><strong>Open annotation accounting</strong>'
        '<span class="small">Current Boox audit layer after R6</span></a>\n'
    )
    if "Annotation_Accounting_2025_Current_R836_20260525.epub" not in html:
        html = html.replace(
            '    <a class="card" href="pro_r6_summary.md"><strong>Read Pro R6 summary</strong><span class="small">10/10 verdict summary</span></a>\n',
            '    <a class="card" href="pro_r6_summary.md"><strong>Read Pro R6 summary</strong><span class="small">10/10 verdict summary</span></a>\n'
            + link,
        )
    index.write_text(html, encoding="utf-8")


def iter_files(base: Path):
    for path in sorted(base.rglob("*")):
        if not path.is_file():
            continue
        if ".DS_Store" in path.name or "__pycache__" in path.parts:
            continue
        yield path


def write_public_manifest_and_zip() -> tuple[Path, str]:
    docs = PUBLIC_DIR / "docs"
    manifest = docs / "release_manifest.csv"
    zip_path = docs / "downloads/full_public_2025_repro_package.zip"
    sha_path = docs / "downloads/full_public_2025_repro_package.zip.sha256"
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    for old in [zip_path, sha_path]:
        if old.exists():
            old.unlink()

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in iter_files(PUBLIC_DIR):
            if path == zip_path or path == sha_path:
                continue
            rel = path.relative_to(PUBLIC_DIR)
            zf.write(path, rel.as_posix())
    zip_sha = sha256(zip_path)
    sha_path.write_text(f"{zip_sha}  {zip_path.name}\n", encoding="utf-8")

    rows = []
    for path in iter_files(docs):
        if path == manifest:
            continue
        rel = path.relative_to(PUBLIC_DIR)
        rows.append({"path": rel.as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)})
    with manifest.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["path", "bytes", "sha256"])
        writer.writeheader()
        writer.writerows(rows)
    shutil.copy2(manifest, PUBLIC_DIR / "qa/public_2025_release_manifest.csv")
    return zip_path, zip_sha


def write_qa(files: list[Path], boox_rows: list[dict[str, str]], listing: str) -> None:
    rows = [
        {"check": "r6_summary_pass_10_10", "status": "PASS" if "10/10" in R6_SUMMARY.read_text(encoding="utf-8") else "FAIL", "detail": str(R6_SUMMARY.relative_to(ROOT))},
        {"check": "current_accounting_epub_present", "status": "PASS" if CURRENT_EPUB.exists() else "FAIL", "detail": CURRENT_EPUB.name},
        {"check": "current_article_boox_files_present", "status": "PASS" if all(path.exists() for path in files) else "FAIL", "detail": str(len(files))},
        {"check": "boox_hash_copies_match", "status": "PASS" if all(row["status"] == "PASS" for row in boox_rows) else "FAIL", "detail": str(len(boox_rows))},
        {"check": "rclone_current_listing_present", "status": "PASS" if "Current_R836_20260525" in listing else "FAIL", "detail": listing.replace("\n", " | ")},
        {"check": "public_docs_current_accounting_present", "status": "PASS" if (PUBLIC_DIR / "docs/annotation_accounting_current_r836_20260525/Annotation_Accounting_2025_Current_R836_20260525.epub").exists() else "FAIL", "detail": "docs current accounting"},
        {"check": "public_docs_index_links_current_accounting", "status": "PASS" if "Annotation_Accounting_2025_Current_R836_20260525.epub" in (PUBLIC_DIR / "docs/index.html").read_text(encoding="utf-8") else "FAIL", "detail": "current accounting link"},
    ]
    CURRENT_QA.parent.mkdir(parents=True, exist_ok=True)
    with CURRENT_QA.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["check", "status", "detail"])
        writer.writeheader()
        writer.writerows(rows)
    public_qa = PUBLIC_DIR / "qa/R836_CURRENT_BOOX_QA_20260525.csv"
    public_qa.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(CURRENT_QA, public_qa)


def main() -> None:
    render_current_accounting()
    article_current = copy_article_current_files()
    all_delivery_files = [
        CURRENT_MD,
        CURRENT_HTML,
        CURRENT_EPUB,
        *article_current,
    ]
    write_hashes(all_delivery_files)
    all_delivery_files.extend([SHA_FILE])
    boox_rows = copy_to_boox(all_delivery_files)
    listing = rclone_listing()
    write_reports(all_delivery_files, boox_rows, listing)
    copy_to_boox([CURRENT_DELIVERY_REPORT])
    listing = rclone_listing()
    write_reports(all_delivery_files, boox_rows, listing)
    copy_to_boox([CURRENT_DELIVERY_REPORT])
    refresh_public_package()
    write_qa(all_delivery_files, boox_rows, listing)
    refresh_public_package()
    zip_path, zip_sha = write_public_manifest_and_zip()
    print(f"current Boox refresh complete: {CURRENT_ACCOUNTING}")
    print(f"current accounting epub sha256: {sha256(CURRENT_EPUB)}")
    print(f"public package zip: {zip_path}")
    print(f"public package zip sha256: {zip_sha}")


if __name__ == "__main__":
    main()
