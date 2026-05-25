# Harvest summary: Mixed-window 2025 post-polish strict R6

Data harvestu: 2026-05-25

Źródło: `https://chatgpt.com/c/6a13c8d9-5194-83eb-b374-db273f735d7d`

Pełna odpowiedź: `PRO_MIXED_WINDOW_2025_POST_POLISH_STRICT_R6_RESPONSE.md`

Marker końcowy: `=== MIXED WINDOW 2025 POST POLISH STRICT R6 VERDICT ===`

SHA-256 odpowiedzi: `4c688f868d649ae08631b771cb848ea92d3ba9d2f0cc08062572390e6aabe2f2`

## Werdykt

`PASS`.

## Score

`10/10`.

## Czy wersja 2025 może zastąpić 2022 jako bieżąca wersja paperu?

Tak. Pro stwierdza, że post-polish mixed-window 2025 candidate może zastąpić starszą zaakceptowaną wersję common-window 2022 jako bieżącą wersję paperu po zapisaniu tego harvestu. Wersja 2022 zostaje historycznie zaakceptowaną wersją odniesienia, ale nie jest już jedyną bieżącą prawdą paperu po ingescie R6.

## Strict notebook impact

Pro uznał notebook za wiążący zapis obliczeń. Notebook nie jest tylko uruchomieniem ukrytego skryptu ani zbiorem gotowych CSV. Widoczne komórki pokazują drogę od danych źródłowych, braków danych, reguły TiVA i konstrukcji zmiennych przez próbę, równania, macierze, współczynniki, błędy standardowe, p-values, ścieżki reakcji, ścieżki długu, tabele, wykresy i mapowanie liczb do artykułu. QA notebooka: `60/60`; kontrakt granularności: `18/18`; visibility audit: `18/18`; visibility contract: `4/4`.

## Number-to-notebook impact

Pro potwierdził zgodność głównych liczb z notebookiem: Table 2a, Table 2b, Table 3, Table 4, Table 5, Appendix B, Appendix C, Appendix D i wszystkie cztery figury. P-values, współczynniki, błędy standardowe, bloki kowariancji, kontrasty profilu Polski i arytmetyka response ratios są wystarczająco odsłonięte. Stary zewnętrzny estimator nie jest bieżącą maszynerią estymacji.

## Post-polish article impact

R805/R833/R834 nie zmieniły zamrożonej treści empirycznej. Pro potwierdził, że polish zachował liczby, tabele, figury, równania, cytowania, etykiety scenariuszy, reguły okna danych i sens ścieżki notebookowej. Skan artykułu nie znalazł wycieków języka roboczego ani nazw rund w tekście paperu.

## Ireland/TiVA impact

Reguła mixed-window przeszła. Eurostat jest użyty do 2025 tam, gdzie dane są dostępne. Irlandia zostaje w obliczeniach, gdzie ma dane, a jej braki w danych finansowych wpływają tylko na obliczenia wymagające tych komórek. TiVA pozostaje official-only: panel TiVA kończy się w 2022, nie ma fabrykowania 2023-2025, a polski profil 2025 używa oficjalnej wartości TiVA 2022 jako oznaczonego profilu.

## Annotation-accounting impact

R834 annotation accounting jest aktualne i uczciwe względem post-polish surface. Nie udaje, że starsze zamknięcia automatycznie certyfikują nową wersję. Ledger ma `40` wierszy: `13` reopened after manuscript change, `11` reopened for strict notebook/repro audit, `16` carry-forward only after spot check, `0` finally closed. QA: `10/10`; Boox hash checks: `3/3`.

## Boox impact

R834 Boox delivery przeszło. PDF, EPUB i HTML są zgodne hashami z post-polish renderami. Pro uznał ostrożną etykietę candidate review copy za poprawną przed R6; po R6 nie jest to bloker.

## Package hygiene

Paczka jest czysta dla decyzji R6. Packet QA: `33/33 PASS`. Aktywny katalog artykułu ma tylko bieżące pliki QMD/HTML/PDF/EPUB, cztery figury, formatting header i aktywne tabele Appendix D. Legacy tables i wcześniejsze naprawy są oddzielone jako historia/kontekst, nie jako bieżące dowody artykułu.

## Paper-truth impact

Status prawdy paperu zmienia się po ingescie harvestu: mixed-window 2025 post-polish candidate staje się bieżącą wersją paperu. Wersja 2022 pozostaje historycznie zaakceptowaną wersją, ale przestaje być jedyną bieżącą wersją do cytowania. Cytowalne po R6 są: R834 post-polish current article, matching R834 HTML/PDF/EPUB, granularny notebook jako zapis obliczeń, R834 Boox delivery i R834 annotation accounting.

## Mandatory fixes

Brak.

## Bundle gap

Brak zidentyfikowanej luki dla wymaganej decyzji R6.
