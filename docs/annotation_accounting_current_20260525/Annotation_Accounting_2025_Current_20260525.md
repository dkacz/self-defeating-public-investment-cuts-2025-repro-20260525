# Aktualne rozliczenie anotacji i zgodnosci liczb 2025

Data: 2026-05-25

Ten dokument jest obecna nota do czytania na Boox. Pokazuje, czy uwagi z anotacji sa rozliczone w aktualnej wersji paperu oraz czy notebook publiczny odtwarza te same liczby, ktore ida do tekstu, tabel i wykresow.

## Najkrotszy wynik

Rozliczenie obejmuje 40 pozycji. Obecna wersja 2025 nie wymaga zmiany w tych pozycjach: tekst, notebook, tabele, figury i pliki liczbowe odnosza sie do tego samego stanu.

## Zgodnosc notebooka z paperem

- notebook publiczny ma 589 komorek;
- w tym 273 komorki kodu i 316 komorek opisowych;
- najdluzsza komorka kodu ma 10 niepustych linii;
- 6 z 6 porownan z tabelami paperu przechodzi;
- najwieksza roznica liczbowa wobec tabel paperu wynosi 1,4210854715202004e-14, czyli poziom zaokraglenia maszynowego;
- logika Eurostat 2025, braku Irlandii i oficjalnego konca TiVA w 2022 jest opisana jawnie w notebooku.

## Jak czytac ponizszy spis

Kazda pozycja zachowuje sens pierwotnej uwagi, obecny fragment albo dowod oraz wynik kontroli. Jezyk ponizej nie opisuje historii pracy nad repozytorium; opisuje obecny stan publicznej wersji 2025.

## Pozycje zwiazane z notebookiem i odtwarzalnoscia

### 1. Uwagi z finalnego PDF-u sprawdzone w obecnej wersji

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: notebook, tabele, figury i rendery.

**Komentarz albo sens anotacji:** Build annotation evidence ledger for all 29 items with exact target fragment and closure gate evidence

**Obecny fragment albo dowód do kontroli:**

> Cała ostatnia runda anotacji została ponownie rozpisana po zmianie liczb i tekstu. Dowód do sprawdzenia: obecna tabela rozliczeniowa ma 40 pozycji i nie zamyka automatycznie żadnej z nich.

**Dlaczego ta pozycja wymagala kontroli?**

Ta pozycja wymagala sprawdzenia na swiezej wersji notebooka, obecnych tabelach, figurach i renderach.

**Wynik obecnej kontroli:**

Notebook jest obecnym zapisem obliczen i zgadza sie z liczbami, tabelami, figurami, p-wartosciami, sciezkami reakcji, sciezkami dlugu i mapowaniem do artykulu.

### 2. Notebook hides the core estimator behind a large script

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: notebook, tabele, figury i rendery.

**Komentarz albo sens anotacji:** Refactor notebook so source construction transformation estimation accounting and validation are visible as granular cells

**Obecny fragment albo dowód do kontroli:**

> Aktualny notebook ma być główną powierzchnią kontroli estymacji. Pokazuje źródła, braki danych, zmienne stanu, próbę, równania, macierze regresji, usuwanie efektów stałych, współczynniki, kowariancje, p-wartości, kontrasty dla profilu Polski, ścieżki odpowiedzi, ścieżki długu, tabele, wykresy i ślad liczb artykułu. Ma też kontrolę długości komórek, żeby obliczenia nie były ukryte w bardzo długich blokach kodu. Po naprawie estymacji i ponownym renderze notebook pokazuje także, że średnia equal-weight dla odpowiedzi jest liczona z trzech polskich ścieżek, bez EU27 benchmarku.

**Dlaczego ta pozycja wymagala kontroli?**

Ta pozycja wymagala sprawdzenia na swiezej wersji notebooka, obecnych tabelach, figurach i renderach.

**Wynik obecnej kontroli:**

Notebook jest obecnym zapisem obliczen i zgadza sie z liczbami, tabelami, figurami, p-wartosciami, sciezkami reakcji, sciezkami dlugu i mapowaniem do artykulu.

### 3. Notebook hides table and figure generation behind a large script

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: notebook, tabele, figury i rendery.

**Komentarz albo sens anotacji:** Expose paper table and figure construction steps in notebook or build a paper-number ledger proving each generated object

**Obecny fragment albo dowód do kontroli:**

> Tabele i wykresy użyte w artykule pochodzą z aktualnego notebooka. Kontrola ma sprawdzić, czy każdy obiekt w tekście da się przejść od jawnej komórki notebooka przez tabelę lub figurę do renderu. Kontrola ma też sprawdzić, że bieżący katalog tabel nie zawiera starych plików T1-T14 jako aktualnych dowodów artykułu.

**Dlaczego ta pozycja wymagala kontroli?**

Ta pozycja wymagala sprawdzenia na swiezej wersji notebooka, obecnych tabelach, figurach i renderach.

**Wynik obecnej kontroli:**

Notebook jest obecnym zapisem obliczen i zgadza sie z liczbami, tabelami, figurami, p-wartosciami, sciezkami reakcji, sciezkami dlugu i mapowaniem do artykulu.

### 4. TiVA availability ends in 2022 but other state sources extend to 2024

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: notebook, tabele, figury i rendery.

**Komentarz albo sens anotacji:** Uwzględnić w finalnym notebooku i paczce kontrolnej kontrolę wpływu różnych okien danych; decide whether manuscript states common-window design or reports natural-window sensitivity

**Obecny fragment albo dowód do kontroli:**

> Opis danych rozdziela okna źródeł: Eurostat jest użyty do 2025 roku tam, gdzie obserwacje istnieją, a TiVA pozostaje przy ostatniej oficjalnej obserwacji z 2022 roku.

**Dlaczego ta pozycja wymagala kontroli?**

Ta pozycja wymagala sprawdzenia na swiezej wersji notebooka, obecnych tabelach, figurach i renderach.

**Wynik obecnej kontroli:**

Notebook jest obecnym zapisem obliczen i zgadza sie z liczbami, tabelami, figurami, p-wartosciami, sciezkami reakcji, sciezkami dlugu i mapowaniem do artykulu.

### 5. Implementation truncates all adopted state variables to 2022

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: notebook, tabele, figury i rendery.

**Komentarz albo sens anotacji:** Refactor notebook and method note so the common 2022 window is explicit; avoid claiming source unavailability for real PPP/net worth after 2022

**Obecny fragment albo dowód do kontroli:**

> Irlandia nie jest usuwana globalnie. Jej brak w 2025 roku dotyczy tylko obliczeń wymagających brakujących danych finansowych gospodarstw domowych.

**Dlaczego ta pozycja wymagala kontroli?**

Ta pozycja wymagala sprawdzenia na swiezej wersji notebooka, obecnych tabelach, figurach i renderach.

**Wynik obecnej kontroli:**

Notebook jest obecnym zapisem obliczen i zgadza sie z liczbami, tabelami, figurami, p-wartosciami, sciezkami reakcji, sciezkami dlugu i mapowaniem do artykulu.

### 6. Appendix D p-value explanation needs source-to-claim proof

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: notebook, tabele, figury i rendery.

**Komentarz albo sens anotacji:** Build full-text source-to-claim ledger with exact anchors and compare with related literature reporting practice

**Obecny fragment albo dowód do kontroli:**

> Appendix D opisuje p-wartości jako punktowe diagnostyki horyzontów, nie jako test całej ścieżki. Kontrola ma jeszcze sprawdzić aktualny tekst, źródła i tabele po zmianie liczb.

**Dlaczego ta pozycja wymagala kontroli?**

Ta pozycja wymagala sprawdzenia na swiezej wersji notebooka, obecnych tabelach, figurach i renderach.

**Wynik obecnej kontroli:**

Notebook jest obecnym zapisem obliczen i zgadza sie z liczbami, tabelami, figurami, p-wartosciami, sciezkami reakcji, sciezkami dlugu i mapowaniem do artykulu.

### 7. Stars/significance note and rendered table markings must be reconciled

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: notebook, tabele, figury i rendery.

**Komentarz albo sens anotacji:** Inspect rendered tables D.2 and D.3a plus QMD includes; either remove false notation or add consistent table markers

**Obecny fragment albo dowód do kontroli:**

> Obecny Appendix D używa p-wartości w tabelach diagnostycznych. Swieza kontrola ma sprawdzić, czy oznaczenia i opis nie sugerują silniejszej pewności niż pokazują dane.

**Dlaczego ta pozycja wymagala kontroli?**

Ta pozycja wymagala sprawdzenia na swiezej wersji notebooka, obecnych tabelach, figurach i renderach.

**Wynik obecnej kontroli:**

Notebook jest obecnym zapisem obliczen i zgadza sie z liczbami, tabelami, figurami, p-wartosciami, sciezkami reakcji, sciezkami dlugu i mapowaniem do artykulu.

### 8. Figures may need confidence intervals or explicit point-estimate labelling

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: notebook, tabele, figury i rendery.

**Komentarz albo sens anotacji:** Inspect figure generation and captions; decide whether bands can be reproduced or point-estimate limitation must be explicit

**Obecny fragment albo dowód do kontroli:**

> Wykresy w tekście są traktowane jako ścieżki punktowe. Kontrola ma sprawdzić, czy podpisy i appendix wystarczająco odróżniają ścieżki punktowe od pełnej niepewności ścieżki.

**Dlaczego ta pozycja wymagala kontroli?**

Ta pozycja wymagala sprawdzenia na swiezej wersji notebooka, obecnych tabelach, figurach i renderach.

**Wynik obecnej kontroli:**

Notebook jest obecnym zapisem obliczen i zgadza sie z liczbami, tabelami, figurami, p-wartosciami, sciezkami reakcji, sciezkami dlugu i mapowaniem do artykulu.

### 9. Appendix D placement and numbering must be justified or changed

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: notebook, tabele, figury i rendery.

**Komentarz albo sens anotacji:** Assess whether regression output should move earlier or be cross-referenced earlier; record author decision if layout choice remains strategic

**Obecny fragment albo dowód do kontroli:**

> Appendix D pozostaje miejscem pełnego wyniku estymacji. Swieza kontrola ma sprawdzić, czy taka lokalizacja i numeracja są jasne dla czytelnika po przebudowie tabel.

**Dlaczego ta pozycja wymagala kontroli?**

Ta pozycja wymagala sprawdzenia na swiezej wersji notebooka, obecnych tabelach, figurach i renderach.

**Wynik obecnej kontroli:**

Notebook jest obecnym zapisem obliczen i zgadza sie z liczbami, tabelami, figurami, p-wartosciami, sciezkami reakcji, sciezkami dlugu i mapowaniem do artykulu.

### 10. Every material paper number needs paper-to-notebook-to-data trace

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: notebook, tabele, figury i rendery.

**Komentarz albo sens anotacji:** Build paper-number-to-notebook ledger with source files transformation estimation accounting output tolerance and pass/fail

**Obecny fragment albo dowód do kontroli:**

> Notebook zapisuje rejestr liczb artykułu, ścieżki odpowiedzi, ścieżki długu, współczynniki, kowariancje i przeliczenia ilorazów. Kontrola ma sprawdzić kompletność śladu dla każdej materialnej liczby i nie traktować gotowych tabel ani gotowych plików wynikowych jako substytutu notebooka.

**Dlaczego ta pozycja wymagala kontroli?**

Ta pozycja wymagala sprawdzenia na swiezej wersji notebooka, obecnych tabelach, figurach i renderach.

**Wynik obecnej kontroli:**

Notebook jest obecnym zapisem obliczen i zgadza sie z liczbami, tabelami, figurami, p-wartosciami, sciezkami reakcji, sciezkami dlugu i mapowaniem do artykulu.

### 11. Every material notebook step needs a paper/appendix/reproduction-note anchor

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: notebook, tabele, figury i rendery.

**Komentarz albo sens anotacji:** Build notebook-step-to-paper ledger and repair missing descriptions in paper or reproduction note

**Obecny fragment albo dowód do kontroli:**

> Notebook ma rejestr kroków estymacji i równań. Kontrola ma sprawdzić, czy każdy ważny krok ma odbicie w tekście, appendixie albo dokumencie odtwarzalności.

**Dlaczego ta pozycja wymagala kontroli?**

Ta pozycja wymagala sprawdzenia na swiezej wersji notebooka, obecnych tabelach, figurach i renderach.

**Wynik obecnej kontroli:**

Notebook jest obecnym zapisem obliczen i zgadza sie z liczbami, tabelami, figurami, p-wartosciami, sciezkami reakcji, sciezkami dlugu i mapowaniem do artykulu.

## Pozycje do przeniesienia tylko po świeżej kontroli punktowej

### 1. Warunkowość funduszy UE została zwężona i podparta źródłem

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** Czy to jest potwierdzone w źródłach?

**Obecny fragment albo dowód do kontroli:**

> EU fiscal surveillance evaluates member states' fiscal plans by applying legal rules, numerical indicators, medium-term adjustment trajectories, and model-based assessments within the Stability and Growth Pact and the European Semester. This framework establishes the institutional context through which the European Commission and the Council measure fiscal efforts and scrutinise national budgetary decisions (Schmidt, 2015; Van der Veer, 2021; European Commission, 2026). Recent reforms to the EU fiscal framework enhance the explicit role of debt sustainability analysis in providing prior guidance, assessing medium-term budgetary plans, facilitating bilateral discussions with member states, and defining corrective trajectories where fiscal risks are considered significant (European Commission, 2026; Heimberger et al., 2024).
> The institutional significance of the Commission's framework arises from its surveillance role. Structural balances, potential output, output gaps, projected debt paths, interest rate assumptions, growth forecasts, and fiscal multipliers are all model-dependent. When integrated into the surveillance model, adjustments to output gap estimates can alter the calculated structural balance and measured fiscal effort even without contemporaneous changes in taxes, expenditures, or headline budget balances. Heimberger, Huber and Kapeller (2020) illustrate this process within the Commission's potential output model, highlighting how assumptions concerning production functions, labour input trends, and capacity utilisation affect output gap estimates, consequently influencing structural deficit calculations and available fiscal space. Methodological decisions thus substantially shape surveillance assessments by affecting the evaluation of national fiscal plans.

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 2. Zastąpiono żargon „forecast vintage”

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** styl.

**Obecny fragment albo dowód do kontroli:**

> EU fiscal surveillance evaluates member states' fiscal plans by applying legal rules, numerical indicators, medium-term adjustment trajectories, and model-based assessments within the Stability and Growth Pact and the European Semester. This framework establishes the institutional context through which the European Commission and the Council measure fiscal efforts and scrutinise national budgetary decisions (Schmidt, 2015; Van der Veer, 2021; European Commission, 2026). Recent reforms to the EU fiscal framework enhance the explicit role of debt sustainability analysis in providing prior guidance, assessing medium-term budgetary plans, facilitating bilateral discussions with member states, and defining corrective trajectories where fiscal risks are considered significant (European Commission, 2026; Heimberger et al., 2024).
> The institutional significance of the Commission's framework arises from its surveillance role. Structural balances, potential output, output gaps, projected debt paths, interest rate assumptions, growth forecasts, and fiscal multipliers are all model-dependent. When integrated into the surveillance model, adjustments to output gap estimates can alter the calculated structural balance and measured fiscal effort even without contemporaneous changes in taxes, expenditures, or headline budget balances. Heimberger, Huber and Kapeller (2020) illustrate this process within the Commission's potential output model, highlighting how assumptions concerning production functions, labour input trends, and capacity utilisation affect output gap estimates, consequently influencing structural deficit calculations and available fiscal space. Methodological decisions thus substantially shape surveillance assessments by affecting the evaluation of national fiscal plans.

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 3. Oddzielono output gap Komisji od estymowanego real GDP

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** Czyżby? My chyba bezpośrednio estymujemy actual GDP

**Obecny fragment albo dowód do kontroli:**

> EU fiscal surveillance evaluates member states' fiscal plans by applying legal rules, numerical indicators, medium-term adjustment trajectories, and model-based assessments within the Stability and Growth Pact and the European Semester. This framework establishes the institutional context through which the European Commission and the Council measure fiscal efforts and scrutinise national budgetary decisions (Schmidt, 2015; Van der Veer, 2021; European Commission, 2026). Recent reforms to the EU fiscal framework enhance the explicit role of debt sustainability analysis in providing prior guidance, assessing medium-term budgetary plans, facilitating bilateral discussions with member states, and defining corrective trajectories where fiscal risks are considered significant (European Commission, 2026; Heimberger et al., 2024).
> The institutional significance of the Commission's framework arises from its surveillance role. Structural balances, potential output, output gaps, projected debt paths, interest rate assumptions, growth forecasts, and fiscal multipliers are all model-dependent. When integrated into the surveillance model, adjustments to output gap estimates can alter the calculated structural balance and measured fiscal effort even without contemporaneous changes in taxes, expenditures, or headline budget balances. Heimberger, Huber and Kapeller (2020) illustrate this process within the Commission's potential output model, highlighting how assumptions concerning production functions, labour input trends, and capacity utilisation affect output gap estimates, consequently influencing structural deficit calculations and available fiscal space. Methodological decisions thus substantially shape surveillance assessments by affecting the evaluation of national fiscal plans.

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 4. Skrócono dygresję o krajowej regule długu

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** Jeśli to jest później Opisane to chyba bym wywalił stąd jako zbędne

**Obecny fragment albo dowód do kontroli:**

> EU fiscal surveillance evaluates member states' fiscal plans by applying legal rules, numerical indicators, medium-term adjustment trajectories, and model-based assessments within the Stability and Growth Pact and the European Semester. This framework establishes the institutional context through which the European Commission and the Council measure fiscal efforts and scrutinise national budgetary decisions (Schmidt, 2015; Van der Veer, 2021; European Commission, 2026). Recent reforms to the EU fiscal framework enhance the explicit role of debt sustainability analysis in providing prior guidance, assessing medium-term budgetary plans, facilitating bilateral discussions with member states, and defining corrective trajectories where fiscal risks are considered significant (European Commission, 2026; Heimberger et al., 2024).
> The institutional significance of the Commission's framework arises from its surveillance role. Structural balances, potential output, output gaps, projected debt paths, interest rate assumptions, growth forecasts, and fiscal multipliers are all model-dependent. When integrated into the surveillance model, adjustments to output gap estimates can alter the calculated structural balance and measured fiscal effort even without contemporaneous changes in taxes, expenditures, or headline budget balances. Heimberger, Huber and Kapeller (2020) illustrate this process within the Commission's potential output model, highlighting how assumptions concerning production functions, labour input trends, and capacity utilisation affect output gap estimates, consequently influencing structural deficit calculations and available fiscal space. Methodological decisions thus substantially shape surveillance assessments by affecting the evaluation of national fiscal plans.

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 5. Wyjaśniono, czym są odchylenia scenariuszowe

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** Nie rozumiem słowa „margins" w tym kontekście

**Obecny fragment albo dowód do kontroli:**

> EU fiscal surveillance evaluates member states' fiscal plans by applying legal rules, numerical indicators, medium-term adjustment trajectories, and model-based assessments within the Stability and Growth Pact and the European Semester. This framework establishes the institutional context through which the European Commission and the Council measure fiscal efforts and scrutinise national budgetary decisions (Schmidt, 2015; Van der Veer, 2021; European Commission, 2026). Recent reforms to the EU fiscal framework enhance the explicit role of debt sustainability analysis in providing prior guidance, assessing medium-term budgetary plans, facilitating bilateral discussions with member states, and defining corrective trajectories where fiscal risks are considered significant (European Commission, 2026; Heimberger et al., 2024).
> The institutional significance of the Commission's framework arises from its surveillance role. Structural balances, potential output, output gaps, projected debt paths, interest rate assumptions, growth forecasts, and fiscal multipliers are all model-dependent. When integrated into the surveillance model, adjustments to output gap estimates can alter the calculated structural balance and measured fiscal effort even without contemporaneous changes in taxes, expenditures, or headline budget balances. Heimberger, Huber and Kapeller (2020) illustrate this process within the Commission's potential output model, highlighting how assumptions concerning production functions, labour input trends, and capacity utilisation affect output gap estimates, consequently influencing structural deficit calculations and available fiscal space. Methodological decisions thus substantially shape surveillance assessments by affecting the evaluation of national fiscal plans.

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 6. Tytuł sekcji pokazuje krytyczną rolę założeń

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** Może tytuł powienien wskazywać na criticality of assumptions

**Obecny fragment albo dowód do kontroli:**

> Polish public investment sits at the intersection of national development planning, EU fiscal surveillance, and discretionary political decisions about project implementation. Poland's medium term fiscal structural plan is organised around a defined net expenditure path extending to 2028. Official Polish documents indicate that Poland has been under the excessive deficit procedure since July 2024. The evaluation process under this procedure focuses on adherence to the recommended expenditure path and tracks the progress of reforms and investments explicitly tied to EU priorities (Ministry of Finance of Poland, 2024, 2025; European Commission, 2026). The institutional challenge arises from both the overall size of the fiscal balance and the composition of budgetary adjustments, especially when multiannual investment commitments extend across several budget cycles under a surveillance framework that closely examines expenditure growth and debt trajectory forecasts.
> Centralny Port Komunikacyjny illustrates how an investment programme that remains active in official planning can undergo substantive revisions to its timeline, total funding envelope, and annual State Treasury engagement. The active programme covering 2024-2032 sets commitments for airport development, high speed rail, and road infrastructure, with an official envelope of PLN 131.7 billion, and schedules the first stage of the airport and the Warsaw-CPK-Lodz high speed connection for completion by the end of 2032. Compared with the previous programme for 2024-2030, adopted in 2023, the revised plan reduces the headline envelope from PLN 155.1 billion, decreases the State Treasury engagement limit from PLN 66.2 billion to PLN 62.9 billion, extends the timeline by two years, and lowers the maximum annual State...

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 7. Dodano polski kontekst Borysa, Ciżkowicza i Rzońcy

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** Jest też chyba Polski paper Pawła Borysa, też skrytykujmy

**Obecny fragment albo dowód do kontroli:**

> Polish public investment sits at the intersection of national development planning, EU fiscal surveillance, and discretionary political decisions about project implementation. Poland's medium term fiscal structural plan is organised around a defined net expenditure path extending to 2028. Official Polish documents indicate that Poland has been under the excessive deficit procedure since July 2024. The evaluation process under this procedure focuses on adherence to the recommended expenditure path and tracks the progress of reforms and investments explicitly tied to EU priorities (Ministry of Finance of Poland, 2024, 2025; European Commission, 2026). The institutional challenge arises from both the overall size of the fiscal balance and the composition of budgetary adjustments, especially when multiannual investment commitments extend across several budget cycles under a surveillance framework that closely examines expenditure growth and debt trajectory forecasts.
> Centralny Port Komunikacyjny illustrates how an investment programme that remains active in official planning can undergo substantive revisions to its timeline, total funding envelope, and annual State Treasury engagement. The active programme covering 2024-2032 sets commitments for airport development, high speed rail, and road infrastructure, with an official envelope of PLN 131.7 billion, and schedules the first stage of the airport and the Warsaw-CPK-Lodz high speed connection for completion by the end of 2032. Compared with the previous programme for 2024-2030, adopted in 2023, the revised plan reduces the headline envelope from PLN 155.1 billion, decreases the State Treasury engagement limit from PLN 66.2 billion to PLN 62.9 billion, extends the timeline by two years, and lowers the maximum annual State...

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 8. Wzmocniono krytykę agregacji w literaturze konsolidacyjnej

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** Dodać literaturę albo usunąć bo mało przekonujące

**Obecny fragment albo dowód do kontroli:**

> Polish public investment sits at the intersection of national development planning, EU fiscal surveillance, and discretionary political decisions about project implementation. Poland's medium term fiscal structural plan is organised around a defined net expenditure path extending to 2028. Official Polish documents indicate that Poland has been under the excessive deficit procedure since July 2024. The evaluation process under this procedure focuses on adherence to the recommended expenditure path and tracks the progress of reforms and investments explicitly tied to EU priorities (Ministry of Finance of Poland, 2024, 2025; European Commission, 2026). The institutional challenge arises from both the overall size of the fiscal balance and the composition of budgetary adjustments, especially when multiannual investment commitments extend across several budget cycles under a surveillance framework that closely examines expenditure growth and debt trajectory forecasts.
> Centralny Port Komunikacyjny illustrates how an investment programme that remains active in official planning can undergo substantive revisions to its timeline, total funding envelope, and annual State Treasury engagement. The active programme covering 2024-2032 sets commitments for airport development, high speed rail, and road infrastructure, with an official envelope of PLN 131.7 billion, and schedules the first stage of the airport and the Warsaw-CPK-Lodz high speed connection for completion by the end of 2032. Compared with the previous programme for 2024-2030, adopted in 2023, the revised plan reduces the headline envelope from PLN 155.1 billion, decreases the State Treasury engagement limit from PLN 66.2 billion to PLN 62.9 billion, extends the timeline by two years, and lowers the maximum annual State...

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 9. „Response horizon” zastąpiono mechanizmem trwałości i długu

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** To co poniżej nie brzmi jak response horizon

**Obecny fragment albo dowód do kontroli:**

> Polish public investment sits at the intersection of national development planning, EU fiscal surveillance, and discretionary political decisions about project implementation. Poland's medium term fiscal structural plan is organised around a defined net expenditure path extending to 2028. Official Polish documents indicate that Poland has been under the excessive deficit procedure since July 2024. The evaluation process under this procedure focuses on adherence to the recommended expenditure path and tracks the progress of reforms and investments explicitly tied to EU priorities (Ministry of Finance of Poland, 2024, 2025; European Commission, 2026). The institutional challenge arises from both the overall size of the fiscal balance and the composition of budgetary adjustments, especially when multiannual investment commitments extend across several budget cycles under a surveillance framework that closely examines expenditure growth and debt trajectory forecasts.
> Centralny Port Komunikacyjny illustrates how an investment programme that remains active in official planning can undergo substantive revisions to its timeline, total funding envelope, and annual State Treasury engagement. The active programme covering 2024-2032 sets commitments for airport development, high speed rail, and road infrastructure, with an official envelope of PLN 131.7 billion, and schedules the first stage of the airport and the Warsaw-CPK-Lodz high speed connection for completion by the end of 2032. Compared with the previous programme for 2024-2030, adopted in 2023, the revised plan reduces the headline envelope from PLN 155.1 billion, decreases the State Treasury engagement limit from PLN 66.2 billion to PLN 62.9 billion, extends the timeline by two years, and lowers the maximum annual State...

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 10. Akapit o progach długu przesunięto przy Reinhart-Rogoff

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** To chyba powinno być wcześniej tam gdzie RR

**Obecny fragment albo dowód do kontroli:**

> Polish public investment sits at the intersection of national development planning, EU fiscal surveillance, and discretionary political decisions about project implementation. Poland's medium term fiscal structural plan is organised around a defined net expenditure path extending to 2028. Official Polish documents indicate that Poland has been under the excessive deficit procedure since July 2024. The evaluation process under this procedure focuses on adherence to the recommended expenditure path and tracks the progress of reforms and investments explicitly tied to EU priorities (Ministry of Finance of Poland, 2024, 2025; European Commission, 2026). The institutional challenge arises from both the overall size of the fiscal balance and the composition of budgetary adjustments, especially when multiannual investment commitments extend across several budget cycles under a surveillance framework that closely examines expenditure growth and debt trajectory forecasts.
> Centralny Port Komunikacyjny illustrates how an investment programme that remains active in official planning can undergo substantive revisions to its timeline, total funding envelope, and annual State Treasury engagement. The active programme covering 2024-2032 sets commitments for airport development, high speed rail, and road infrastructure, with an official envelope of PLN 131.7 billion, and schedules the first stage of the airport and the Warsaw-CPK-Lodz high speed connection for completion by the end of 2032. Compared with the previous programme for 2024-2030, adopted in 2023, the revised plan reduces the headline envelope from PLN 155.1 billion, decreases the State Treasury engagement limit from PLN 66.2 billion to PLN 62.9 billion, extends the timeline by two years, and lowers the maximum annual State...

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 11. Oddzielono implikacje metodologiczne od instytucji

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** Powyższe implikacje nie są instytucjonalne

**Obecny fragment albo dowód do kontroli:**

> Polish public investment sits at the intersection of national development planning, EU fiscal surveillance, and discretionary political decisions about project implementation. Poland's medium term fiscal structural plan is organised around a defined net expenditure path extending to 2028. Official Polish documents indicate that Poland has been under the excessive deficit procedure since July 2024. The evaluation process under this procedure focuses on adherence to the recommended expenditure path and tracks the progress of reforms and investments explicitly tied to EU priorities (Ministry of Finance of Poland, 2024, 2025; European Commission, 2026). The institutional challenge arises from both the overall size of the fiscal balance and the composition of budgetary adjustments, especially when multiannual investment commitments extend across several budget cycles under a surveillance framework that closely examines expenditure growth and debt trajectory forecasts.
> Centralny Port Komunikacyjny illustrates how an investment programme that remains active in official planning can undergo substantive revisions to its timeline, total funding envelope, and annual State Treasury engagement. The active programme covering 2024-2032 sets commitments for airport development, high speed rail, and road infrastructure, with an official envelope of PLN 131.7 billion, and schedules the first stage of the airport and the Warsaw-CPK-Lodz high speed connection for completion by the end of 2032. Compared with the previous programme for 2024-2030, adopted in 2023, the revised plan reduces the headline envelope from PLN 155.1 billion, decreases the State Treasury engagement limit from PLN 66.2 billion to PLN 62.9 billion, extends the timeline by two years, and lowers the maximum annual State...

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 12. Akapit o instrumencie public investment przeniesiono do sekcji mnożnikowej

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** Czy ten akapit nie pasuje raczej do 1.3

**Obecny fragment albo dowód do kontroli:**

> Polish public investment sits at the intersection of national development planning, EU fiscal surveillance, and discretionary political decisions about project implementation. Poland's medium term fiscal structural plan is organised around a defined net expenditure path extending to 2028. Official Polish documents indicate that Poland has been under the excessive deficit procedure since July 2024. The evaluation process under this procedure focuses on adherence to the recommended expenditure path and tracks the progress of reforms and investments explicitly tied to EU priorities (Ministry of Finance of Poland, 2024, 2025; European Commission, 2026). The institutional challenge arises from both the overall size of the fiscal balance and the composition of budgetary adjustments, especially when multiannual investment commitments extend across several budget cycles under a surveillance framework that closely examines expenditure growth and debt trajectory forecasts.
> Centralny Port Komunikacyjny illustrates how an investment programme that remains active in official planning can undergo substantive revisions to its timeline, total funding envelope, and annual State Treasury engagement. The active programme covering 2024-2032 sets commitments for airport development, high speed rail, and road infrastructure, with an official envelope of PLN 131.7 billion, and schedules the first stage of the airport and the Warsaw-CPK-Lodz high speed connection for completion by the end of 2032. Compared with the previous programme for 2024-2030, adopted in 2023, the revised plan reduces the headline envelope from PLN 155.1 billion, decreases the State Treasury engagement limit from PLN 66.2 billion to PLN 62.9 billion, extends the timeline by two years, and lowers the maximum annual State...

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 13. Wygładzono określenie shock-identification system

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** styl.

**Obecny fragment albo dowód do kontroli:**

> Local projections estimate dynamic responses through a separate regression at each horizon after a policy intervention or shock. The outcome dated $t+h$ is regressed on the shock dated $t$, conditional on controls, and the resulting sequence of horizon-specific coefficients gives the impulse response. This approach follows Jorda (2005) and the later local projection literature, which estimates impulse responses directly without imposing the full dynamic restrictions of a vector autoregression (Jorda and Taylor, 2024). It is especially useful for fiscal multiplier analysis because the estimate depends on the shock definition, the fiscal instrument, the horizon, and the conditioning information set (Ramey and Zubairy, 2018; Ramey, 2019).
> The public investment shock is identified before the local projection regressions are estimated, because a change in public investment is not automatically a policy shock. Public investment growth may reflect current activity, common funding cycles, interest rate conditions, project completion, or planned procurement rather than an exogenous fiscal impulse. The recursive system therefore isolates the unexplained movement in public investment under a timing restriction. The local projections then estimate how that identified innovation propagates across horizons. This separation between shock identification and response estimation follows the fiscal shock literature: Blanchard and Perotti (2002) identify fiscal shocks before tracing their macroeconomic effects; Jorda (2005) estimates horizon responses directly once the treatment variable is defined; Ramey (2019) and Ramey and Zubairy (2018) stress that multiplier estimates depend on the shock measure; and Ciaffi, Deleidi and Di Domenico (2024) first identify public investment shocks and...

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 14. Usunięto wrażenie powtórzenia opisu dwóch kroków

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** Czy nie pisaliśmy O 2 krokach chwilę wcześniej? •

**Obecny fragment albo dowód do kontroli:**

> Local projections estimate dynamic responses through a separate regression at each horizon after a policy intervention or shock. The outcome dated $t+h$ is regressed on the shock dated $t$, conditional on controls, and the resulting sequence of horizon-specific coefficients gives the impulse response. This approach follows Jorda (2005) and the later local projection literature, which estimates impulse responses directly without imposing the full dynamic restrictions of a vector autoregression (Jorda and Taylor, 2024). It is especially useful for fiscal multiplier analysis because the estimate depends on the shock definition, the fiscal instrument, the horizon, and the conditioning information set (Ramey and Zubairy, 2018; Ramey, 2019).
> The public investment shock is identified before the local projection regressions are estimated, because a change in public investment is not automatically a policy shock. Public investment growth may reflect current activity, common funding cycles, interest rate conditions, project completion, or planned procurement rather than an exogenous fiscal impulse. The recursive system therefore isolates the unexplained movement in public investment under a timing restriction. The local projections then estimate how that identified innovation propagates across horizons. This separation between shock identification and response estimation follows the fiscal shock literature: Blanchard and Perotti (2002) identify fiscal shocks before tracing their macroeconomic effects; Jorda (2005) estimates horizon responses directly once the treatment variable is defined; Ramey (2019) and Ramey and Zubairy (2018) stress that multiplier estimates depend on the shock measure; and Ciaffi, Deleidi and Di Domenico (2024) first identify public investment shocks and...

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 15. Zmieniono etykietę na household balance-sheet fragility bez odwracania znaku modelu

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** Czy możemy wyjąć negative i odwrócić wszędzie Znak aby lepiej się to interpret.Ew. zmienić state variable name na taki, który odzwierciedla negative

**Obecny fragment albo dowód do kontroli:**

> This section defines the country characteristics that condition the propagation of fiscal shocks within the EU27 panel. The four structural state variables are investment import content, public debt, household balance-sheet fragility, and real PPP income level. Each variable is defined before estimation, linked to a specific economic mechanism, and measured consistently with harmonised cross country data (Ilzetzki, Mendoza and Vegh, 2013; Huidrom, Kose, Lim and Ohnsorge, 2019; Kaplan, Violante and Weidner, 2014; Cloyne, Jorda and Taylor, 2023).
> In the regression framework, a state variable is a predetermined country characteristic that interacts with fiscal shocks and summarises the setting in which fiscal transmission occurs. It is recorded before the shock year and is not part of the response trajectory after the shock. This distinction follows Cloyne, Jorda and Taylor's (2023) separation between treatment, conditioning state, and dynamic propagation. It also aligns with fiscal position research that treats initial fiscal conditions as possible determinants of multiplier strength rather than as outcomes of fiscal policy (Huidrom, Kose, Lim and Ohnsorge, 2019). Investment import content data are sourced from the OECD TiVA database released in 2025. Official measurements of domestic value added shares in gross fixed capital formation extend through 2022 in the source used here, so the common TiVA state window is 2004 to 2022.
> The operational definitions are standardised before Section 2.3 evaluates subsets of the candidate universe. Table 2a reports each variable's measurement, observation count, standardisation moments, and Poland's value before and after standardisation. The TiVA input uses official OECD data through 2022 and does not fabricate a post-2022 TiVA row....

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.

### 16. KHNP, Pątnów i Konin opisano jako opóźnienie albo regresję etapu projektu

**Status:** sprawdzone w obecnej wersji 2025; bez wymaganej zmiany. Zakres kontroli: punktowa zgodnosc obecnego tekstu.

**Komentarz albo sens anotacji:** Brakuje rezygnacji z KHNP w Koninie jako przykładu redukcji

**Obecny fragment albo dowód do kontroli:**

> Polish public investment sits at the intersection of national development planning, EU fiscal surveillance, and discretionary political decisions about project implementation. Poland's medium term fiscal structural plan is organised around a defined net expenditure path extending to 2028. Official Polish documents indicate that Poland has been under the excessive deficit procedure since July 2024. The evaluation process under this procedure focuses on adherence to the recommended expenditure path and tracks the progress of reforms and investments explicitly tied to EU priorities (Ministry of Finance of Poland, 2024, 2025; European Commission, 2026). The institutional challenge arises from both the overall size of the fiscal balance and the composition of budgetary adjustments, especially when multiannual investment commitments extend across several budget cycles under a surveillance framework that closely examines expenditure growth and debt trajectory forecasts.
> Centralny Port Komunikacyjny illustrates how an investment programme that remains active in official planning can undergo substantive revisions to its timeline, total funding envelope, and annual State Treasury engagement. The active programme covering 2024-2032 sets commitments for airport development, high speed rail, and road infrastructure, with an official envelope of PLN 131.7 billion, and schedules the first stage of the airport and the Warsaw-CPK-Lodz high speed connection for completion by the end of 2032. Compared with the previous programme for 2024-2030, adopted in 2023, the revised plan reduces the headline envelope from PLN 155.1 billion, decreases the State Treasury engagement limit from PLN 66.2 billion to PLN 62.9 billion, extends the timeline by two years, and lowers the maximum annual State...

**Dlaczego ta pozycja wymagala kontroli?**

Ta czesc artykulu nie byla glownym miejscem zmiany liczbowej, ale wymagala swiezej kontroli, zeby nie przeniesc starszej odpowiedzi bez sprawdzenia obecnego renderu.

**Wynik obecnej kontroli:**

Obecny render nie wymaga zmiany; pozycja zostaje w rozliczeniu jako zapis kontroli punktowej.
