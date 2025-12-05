# Koncepcja - Edytor Równań (Rewizja)

## Spis treści

1. [Opis projektu](#opis-projektu)
2. [Cele projektu](#cele-projektu)
3. [Przegląd założeń](#przegląd-założeń)
4. [Etapy projektu](#etapy-projektu)
5. [Szczegółowy plan zadań](#szczegółowy-plan-zadań)
6. [Architektura systemu](#architektura-systemu)
7. [Wymagania techniczne](#wymagania-techniczne)
8. [Ryzyka i mitygacja](#ryzyka-i-mitygacja)
9. [Harmonogram](#harmonogram)

---

## Opis projektu

**Edytor Równań** to aplikacja w języku Python służąca do automatyzacji procesu przetwarzania danych z plików Excel i generowania dokumentów Word zawierających równania matematyczne wraz z obliczonymi wynikami.

### Główne funkcjonalności

1. 📊 Wczytywanie danych (zmiennych i ich wartości) z plików Excel (.xlsx)
2. 🔢 Parsowanie i obliczanie równań matematycznych z użyciem symboli
3. 📝 Generowanie profesjonalnych dokumentów Word z wynikami obliczeń
4. ✨ Obsługa notacji matematycznej (potęgi, pierwiastki, funkcje trygonometryczne)

---

## Cele projektu

### Cele główne

| Cel | Opis | Priorytet |
|-----|------|-----------|
| **C1** | Automatyzacja obliczeń inżynierskich | Wysoki |
| **C2** | Generowanie czytelnej dokumentacji obliczeń | Wysoki |
| **C3** | Eliminacja ręcznego przepisywania wzorów | Średni |
| **C4** | Standaryzacja formatu dokumentacji | Średni |

### Cele szczegółowe

- Skrócenie czasu przygotowania dokumentacji obliczeń o 70%
- Eliminacja błędów przy przepisywaniu wzorów i wartości
- Możliwość wielokrotnego generowania dokumentów dla różnych danych

---

## Przegląd założeń

### Status realizacji założeń

| Założenie | Status | Uwagi |
|-----------|--------|-------|
| Wczytywanie danych z Excel | ✅ Zaimplementowane | Moduł `excel_reader.py` |
| Parsowanie równań (SymPy) | ✅ Zaimplementowane | Moduł `equation_parser.py` |
| Generowanie dokumentów Word | ✅ Zaimplementowane | Moduł `word_writer.py` |
| Interfejs CLI | ✅ Zaimplementowane | Moduł `main.py` |
| Testy jednostkowe | 🟡 Częściowo | Tylko `test_equation_parser.py` |
| Obsługa jednostek | ⬜ Do zrobienia | Rozszerzenie |
| GUI | ⬜ Do zrobienia | Rozszerzenie |
| Formatowanie OMML | ⬜ Do zrobienia | Rozszerzenie |

### Weryfikacja bibliotek

| Biblioteka | Wersja min. | Status | Wykorzystanie |
|------------|-------------|--------|---------------|
| openpyxl | 3.1.0 | ✅ Aktywna | Odczyt plików Excel |
| pandas | 2.0.0 | ✅ Aktywna | Manipulacja danymi |
| python-docx | 1.0.0 | ✅ Aktywna | Generowanie Word |
| sympy | 1.12 | ✅ Aktywna | Obliczenia symboliczne |

---

## Etapy projektu

Projekt podzielony jest na **4 główne etapy**:

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ETAPY PROJEKTU                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ETAP 1: Fundament        ──────────────────────────►  ✅ UKOŃCZONY │
│  (Podstawowa funkcjonalność)                                        │
│                                                                     │
│  ETAP 2: Stabilizacja     ──────────────────────────►  🟡 W TRAKCIE│
│  (Testy i walidacja)                                                │
│                                                                     │
│  ETAP 3: Rozszerzenie     ──────────────────────────►  ⬜ PLANOWANY│
│  (Dodatkowe funkcje)                                                │
│                                                                     │
│  ETAP 4: Produkcja        ──────────────────────────►  ⬜ PLANOWANY│
│  (GUI i dokumentacja)                                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Szczegółowy plan zadań

### ETAP 1: Fundament (Podstawowa funkcjonalność) ✅

**Cel etapu:** Stworzenie działającego prototypu z podstawową funkcjonalnością.

#### Zadanie 1.1: Struktura projektu ✅

| Podzadanie | Opis | Status | Plik/Lokalizacja |
|------------|------|--------|------------------|
| 1.1.1 | Utworzenie struktury katalogów | ✅ | `src/`, `tests/`, `templates/` |
| 1.1.2 | Konfiguracja zależności | ✅ | `requirements.txt` |
| 1.1.3 | Dokumentacja wstępna | ✅ | `README.md`, `KONCEPCJA.md` |
| 1.1.4 | Konfiguracja Git i GitHub | ✅ | `.git/`, `.github/` |

**Kryteria akceptacji:**
- [x] Struktura katalogów zgodna z konwencją Python
- [x] Plik requirements.txt z wszystkimi zależnościami
- [x] README z instrukcją instalacji i użycia

---

#### Zadanie 1.2: Moduł wczytywania danych (ExcelReader) ✅

| Podzadanie | Opis | Status | Metoda/Funkcja |
|------------|------|--------|----------------|
| 1.2.1 | Walidacja ścieżki do pliku | ✅ | `__init__()` |
| 1.2.2 | Wczytywanie zmiennych | ✅ | `read_variables()` |
| 1.2.3 | Wczytywanie równań | ✅ | `read_equations()` |
| 1.2.4 | Listowanie arkuszy | ✅ | `get_sheet_names()` |

**Kryteria akceptacji:**
- [x] Obsługa plików .xlsx
- [x] Elastyczne nazwy kolumn
- [x] Obsługa błędów (brak pliku)

**Kod źródłowy:** `src/excel_reader.py`

---

#### Zadanie 1.3: Moduł parsowania równań (EquationParser) ✅

| Podzadanie | Opis | Status | Metoda/Funkcja |
|------------|------|--------|----------------|
| 1.3.1 | Parsowanie wyrażeń tekstowych | ✅ | `parse_equation()` |
| 1.3.2 | Podstawianie wartości | ✅ | `substitute_values()` |
| 1.3.3 | Obliczanie wyników | ✅ | `calculate()` |
| 1.3.4 | Konwersja do LaTeX | ✅ | `to_latex()` |
| 1.3.5 | Formatowanie z wartościami | ✅ | `format_equation_with_values()` |
| 1.3.6 | Przetwarzanie pełne | ✅ | `process_equation()` |

**Kryteria akceptacji:**
- [x] Obsługa operatorów: +, -, *, /, ^, **
- [x] Obsługa funkcji: sqrt, sin, cos, tan, log
- [x] Poprawna konwersja ^ na **
- [x] Struktura danych EquationResult

**Kod źródłowy:** `src/equation_parser.py`

---

#### Zadanie 1.4: Moduł generowania dokumentów (WordWriter) ✅

| Podzadanie | Opis | Status | Metoda/Funkcja |
|------------|------|--------|----------------|
| 1.4.1 | Inicjalizacja dokumentu | ✅ | `__init__()`, `_setup_document()` |
| 1.4.2 | Dodawanie sekcji równań | ✅ | `add_equation_section()` |
| 1.4.3 | Tabela zmiennych | ✅ | `add_variables_table()` |
| 1.4.4 | Sekcja wyników | ✅ | `add_results_section()` |
| 1.4.5 | Zapis dokumentu | ✅ | `save()` |

**Kryteria akceptacji:**
- [x] Generowanie plików .docx
- [x] Formatowanie tabel
- [x] Konfigurowalana precyzja wyników

**Kod źródłowy:** `src/word_writer.py`

---

#### Zadanie 1.5: Integracja i CLI (main.py) ✅

| Podzadanie | Opis | Status | Funkcja |
|------------|------|--------|---------|
| 1.5.1 | Funkcja przetwarzania | ✅ | `process_equations()` |
| 1.5.2 | Parser argumentów CLI | ✅ | `main()` |
| 1.5.3 | Obsługa błędów | ✅ | try/except |
| 1.5.4 | Mapowanie nazw kolumn | ✅ | `get_column_value()` |

**Kryteria akceptacji:**
- [x] Działający interfejs CLI
- [x] Obsługa parametrów wejściowych
- [x] Informacyjne komunikaty błędów

**Kod źródłowy:** `src/main.py`

---

### ETAP 2: Stabilizacja (Testy i walidacja) 🟡

**Cel etapu:** Zapewnienie jakości kodu i stabilności działania.

#### Zadanie 2.1: Testy jednostkowe

| Podzadanie | Opis | Status | Plik testowy |
|------------|------|--------|--------------|
| 2.1.1 | Testy EquationParser | ✅ | `tests/test_equation_parser.py` |
| 2.1.2 | Testy ExcelReader | ⬜ | `tests/test_excel_reader.py` (do utworzenia) |
| 2.1.3 | Testy WordWriter | ⬜ | `tests/test_word_writer.py` (do utworzenia) |
| 2.1.4 | Testy integracyjne main | ⬜ | `tests/test_main.py` (do utworzenia) |

**Kryteria akceptacji:**
- [ ] Pokrycie kodu testami > 80%
- [ ] Wszystkie testy przechodzą
- [ ] Testy przypadków brzegowych

---

#### Zadanie 2.2: Walidacja danych wejściowych

| Podzadanie | Opis | Status | Lokalizacja |
|------------|------|--------|-------------|
| 2.2.1 | Walidacja formatu Excel | ⬜ | `excel_reader.py` |
| 2.2.2 | Walidacja składni równań | ⬜ | `equation_parser.py` |
| 2.2.3 | Sprawdzanie kompletności zmiennych | ⬜ | `equation_parser.py` |
| 2.2.4 | Informacyjne komunikaty błędów | ⬜ | Wszystkie moduły |

**Kryteria akceptacji:**
- [ ] Czytelne komunikaty błędów
- [ ] Walidacja przed przetwarzaniem
- [ ] Sugestie naprawy błędów

---

#### Zadanie 2.3: Obsługa błędów i wyjątków

| Podzadanie | Opis | Status | Typ wyjątku |
|------------|------|--------|-------------|
| 2.3.1 | Błędy plików | 🟡 | `FileNotFoundError` |
| 2.3.2 | Błędy parsowania | ⬜ | `SyntaxError`, `ValueError` |
| 2.3.3 | Błędy obliczeń | ⬜ | `ZeroDivisionError`, `MathError` |
| 2.3.4 | Własne wyjątki domenowe | ⬜ | `EquationError`, `DataError` |

**Kryteria akceptacji:**
- [ ] Hierarchia własnych wyjątków
- [ ] Graceful degradation
- [ ] Logging błędów

---

### ETAP 3: Rozszerzenie (Dodatkowe funkcje) ⬜

**Cel etapu:** Dodanie zaawansowanych funkcjonalności.

#### Zadanie 3.1: Obsługa jednostek miary

| Podzadanie | Opis | Status | Biblioteka |
|------------|------|--------|------------|
| 3.1.1 | Integracja biblioteki pint | ⬜ | `pint` |
| 3.1.2 | Wczytywanie jednostek z Excel | ⬜ | - |
| 3.1.3 | Konwersja jednostek | ⬜ | - |
| 3.1.4 | Wyświetlanie jednostek w Word | ⬜ | - |

**Kryteria akceptacji:**
- [ ] Obsługa jednostek SI
- [ ] Automatyczna konwersja
- [ ] Walidacja zgodności jednostek

---

#### Zadanie 3.2: Formatowanie równań OMML

| Podzadanie | Opis | Status | Opis techniczny |
|------------|------|--------|-----------------|
| 3.2.1 | Konwersja LaTeX → OMML | ⬜ | Office Math Markup Language |
| 3.2.2 | Wstawianie obiektów matematycznych | ⬜ | `python-docx` + lxml |
| 3.2.3 | Style równań | ⬜ | Formatowanie wizualne |
| 3.2.4 | Numeracja równań | ⬜ | Automatyczna numeracja |

**Kryteria akceptacji:**
- [ ] Równania jako obiekty OMML w Word
- [ ] Poprawne renderowanie w MS Word
- [ ] Edytowalność równań

---

#### Zadanie 3.3: Szablony dokumentów

| Podzadanie | Opis | Status | Format |
|------------|------|--------|--------|
| 3.3.1 | System szablonów Word | ⬜ | `.dotx` |
| 3.3.2 | Placeholdery w szablonach | ⬜ | `{{zmienna}}` |
| 3.3.3 | Style z szablonu | ⬜ | Dziedziczenie stylów |
| 3.3.4 | Predefiniowane szablony | ⬜ | Obliczenia, Raport |

**Kryteria akceptacji:**
- [ ] Obsługa szablonów .dotx
- [ ] Personalizacja wyglądu dokumentów
- [ ] Zachowanie formatowania szablonu

---

#### Zadanie 3.4: Rozszerzona notacja matematyczna

| Podzadanie | Opis | Status | Przykład |
|------------|------|--------|----------|
| 3.4.1 | Sumy i produkty | ⬜ | `Σ`, `Π` |
| 3.4.2 | Całki | ⬜ | `∫` |
| 3.4.3 | Macierze | ⬜ | `[[a,b],[c,d]]` |
| 3.4.4 | Indeksy górne/dolne | ⬜ | `x_1`, `x^2` |

**Kryteria akceptacji:**
- [ ] Obsługa zaawansowanych symboli
- [ ] Poprawne renderowanie w Word
- [ ] Dokumentacja składni

---

### ETAP 4: Produkcja (GUI i dokumentacja) ⬜

**Cel etapu:** Przygotowanie aplikacji do użycia produkcyjnego.

#### Zadanie 4.1: Interfejs graficzny (GUI)

| Podzadanie | Opis | Status | Technologia |
|------------|------|--------|-------------|
| 4.1.1 | Wybór frameworka | ⬜ | tkinter / PyQt |
| 4.1.2 | Okno główne | ⬜ | Layout, menu |
| 4.1.3 | Wybór plików | ⬜ | File dialogs |
| 4.1.4 | Podgląd danych | ⬜ | Tabele, listy |
| 4.1.5 | Podgląd wyników | ⬜ | Preview |
| 4.1.6 | Ustawienia | ⬜ | Preferences |

**Kryteria akceptacji:**
- [ ] Intuicyjny interfejs
- [ ] Obsługa drag & drop
- [ ] Podgląd przed generowaniem

---

#### Zadanie 4.2: Dokumentacja użytkownika

| Podzadanie | Opis | Status | Format |
|------------|------|--------|--------|
| 4.2.1 | Instrukcja instalacji | 🟡 | README.md |
| 4.2.2 | Podręcznik użytkownika | ⬜ | docs/manual.md |
| 4.2.3 | Przykłady użycia | ⬜ | examples/ |
| 4.2.4 | FAQ | ⬜ | docs/faq.md |
| 4.2.5 | Changelog | ⬜ | CHANGELOG.md |

**Kryteria akceptacji:**
- [ ] Kompletna dokumentacja
- [ ] Przykłady dla każdej funkcji
- [ ] Zrzuty ekranu GUI

---

#### Zadanie 4.3: Dokumentacja techniczna

| Podzadanie | Opis | Status | Narzędzie |
|------------|------|--------|-----------|
| 4.3.1 | Docstrings API | 🟡 | Istniejące |
| 4.3.2 | Generowanie dokumentacji | ⬜ | Sphinx / MkDocs |
| 4.3.3 | Diagramy UML | ⬜ | PlantUML / Mermaid |
| 4.3.4 | Architektura systemu | ⬜ | docs/architecture.md |

**Kryteria akceptacji:**
- [ ] Dokumentacja API online
- [ ] Diagramy klas i sekwencji
- [ ] Opis architektury

---

#### Zadanie 4.4: Dystrybucja i wdrożenie

| Podzadanie | Opis | Status | Narzędzie |
|------------|------|--------|-----------|
| 4.4.1 | Pakiet PyPI | ⬜ | setuptools / poetry |
| 4.4.2 | Executable (Windows) | ⬜ | PyInstaller |
| 4.4.3 | CI/CD pipeline | ⬜ | GitHub Actions |
| 4.4.4 | Wersjonowanie | ⬜ | Semantic Versioning |

**Kryteria akceptacji:**
- [ ] Możliwość instalacji przez pip
- [ ] Plik .exe dla Windows
- [ ] Automatyczne testy i release

---

## Architektura systemu

### Diagram komponentów

```
┌────────────────────────────────────────────────────────────────────────┐
│                            EDYTOR RÓWNAŃ                               │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐             │
│  │    main.py   │───▶│ CLI / GUI    │───▶│   Output     │             │
│  │  (Kontroler) │    │  Interface   │    │   Handler    │             │
│  └──────┬───────┘    └──────────────┘    └──────────────┘             │
│         │                                                              │
│         ▼                                                              │
│  ┌──────────────────────────────────────────────────────────────────┐ │
│  │                         WARSTWA LOGIKI                           │ │
│  ├──────────────────┬───────────────────┬──────────────────────────┤ │
│  │                  │                   │                          │ │
│  │  ExcelReader     │  EquationParser   │  WordWriter              │ │
│  │  ┌────────────┐  │  ┌─────────────┐  │  ┌─────────────┐        │ │
│  │  │read_vars() │  │  │parse_eq()   │  │  │add_section()│        │ │
│  │  │read_eqs()  │  │  │calculate()  │  │  │add_table()  │        │ │
│  │  │get_sheets()│  │  │to_latex()   │  │  │save()       │        │ │
│  │  └────────────┘  │  └─────────────┘  │  └─────────────┘        │ │
│  │                  │                   │                          │ │
│  └──────────────────┴───────────────────┴──────────────────────────┘ │
│         │                   │                   │                     │
│         ▼                   ▼                   ▼                     │
│  ┌──────────────────────────────────────────────────────────────────┐ │
│  │                      WARSTWA ZEWNĘTRZNA                          │ │
│  ├────────────────┬─────────────────┬───────────────────────────────┤ │
│  │   pandas       │    sympy        │    python-docx                │ │
│  │   openpyxl     │                 │                               │ │
│  └────────────────┴─────────────────┴───────────────────────────────┘ │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### Przepływ danych

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Excel     │     │   Python    │     │   SymPy     │     │    Word     │
│   (.xlsx)   │────▶│   Dict      │────▶│   Expr      │────▶│   (.docx)   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
      │                   │                   │                   │
      ▼                   ▼                   ▼                   ▼
  Zmienne            Struktury           Obliczenia          Dokument
  Równania           danych             symboliczne          wynikowy
```

---

## Wymagania techniczne

### Środowisko

| Wymaganie | Wersja min. | Zalecana |
|-----------|-------------|----------|
| Python | 3.10 | 3.11+ |
| pip | 21.0 | Najnowsza |
| Pamięć RAM | 512 MB | 2 GB |
| Miejsce na dysku | 100 MB | 500 MB |

### Zależności

```
# requirements.txt
openpyxl>=3.1.0      # Obsługa Excel
pandas>=2.0.0        # Manipulacja danymi
python-docx>=1.0.0   # Generowanie Word
sympy>=1.12          # Obliczenia symboliczne

# Opcjonalne (Etap 3-4)
# pint>=0.22         # Jednostki miary
# PyQt6>=6.5.0       # GUI (alternatywa)
```

---

## Ryzyka i mitygacja

### Macierz ryzyk

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja |
|--------|-------------------|-------|-----------|
| Błędy w parsowaniu złożonych równań | Średnie | Wysoki | Rozbudowane testy, walidacja wejścia |
| Niekompatybilność formatów Excel | Niskie | Średni | Obsługa wielu formatów kolumn |
| Problemy z formatowaniem OMML | Wysokie | Średni | Fallback do tekstu, dokumentacja |
| Wydajność przy dużych plikach | Niskie | Niski | Lazy loading, optymalizacja |
| Zależności zewnętrzne | Niskie | Wysoki | Pinowanie wersji, testy CI |

### Plan działań naprawczych

1. **Błędy parsowania:** Dodać tryb "verbose" z logowaniem kroków parsowania
2. **Format Excel:** Implementacja wielu parserów z automatycznym wykrywaniem
3. **OMML:** Przygotować dokumentację ograniczeń i workaroundów

---

## Harmonogram

### Oś czasu projektu

> **Uwaga:** Poniższy harmonogram przedstawia planowany przebieg projektu. Etap 1 został ukończony, pozostałe etapy są w trakcie realizacji lub planowane.

```
2024 Q4         2025 Q1         2025 Q2         2025 Q3
   │               │               │               │
   ├───ETAP 1──────┤               │               │
   │   ████████████│               │               │
   │   Fundament   │ (ukończony)   │               │
   │               │               │               │
   │               ├───ETAP 2──────┤               │
   │               │   ████████████│               │
   │               │  Stabilizacja │               │
   │               │               │               │
   │               │               ├───ETAP 3──────┤
   │               │               │   ████████████│
   │               │               │   Rozszerzenie│
   │               │               │               │
   │               │               │               ├───ETAP 4───▶
   │               │               │               │   ██████████
   │               │               │               │   Produkcja
   │               │               │               │
```

### Kamienie milowe

| Milestone | Opis | Data docelowa | Status |
|-----------|------|---------------|--------|
| **M1** | Działający prototyp CLI | 2024 Q4 | ✅ Ukończony |
| **M2** | Pełne pokrycie testami | 2025 Q1 | 🟡 W trakcie |
| **M3** | Obsługa jednostek i OMML | 2025 Q2 | ⬜ Planowany |
| **M4** | Wersja produkcyjna z GUI | 2025 Q3 | ⬜ Planowany |

---

## Podsumowanie statusu

### Aktualny postęp

| Etap | Postęp | Zadania ukończone |
|------|--------|-------------------|
| Etap 1: Fundament | 100% | 5/5 |
| Etap 2: Stabilizacja | 20% | 1/3 (częściowo) |
| Etap 3: Rozszerzenie | 0% | 0/4 |
| Etap 4: Produkcja | 5% | 0/4 (częściowo dokumentacja) |

### Następne kroki

1. ⬜ Dokończyć testy jednostkowe (Zadanie 2.1)
2. ⬜ Implementacja walidacji danych (Zadanie 2.2)
3. ⬜ Rozbudowa obsługi błędów (Zadanie 2.3)
4. ⬜ Planowanie Etapu 3 - analiza priorytetów rozszerzeń

---

## Przypadek użycia: Obliczenia prądu w układzie 3-fazowym

### Opis przypadku

Generowanie dokumentu Word z obliczeniami prądu fazowego w trójfazowym układzie elektrycznym na podstawie danych wejściowych: moc (P), napięcie (U), współczynnik mocy (cos φ).

### Plik danych wejściowych

**Lokalizacja:** `examples/dane_prad_3fazowy.csv`

```csv
Nazwa zmiennej,Wartość,Jednostka,Opis
P,15000,W,Moc czynna
U,400,V,Napięcie międzyfazowe
cos_phi,0.85,-,Współczynnik mocy
```

### Wzory matematyczne (LaTeX)

#### Wzór główny - prąd fazowy

```latex
I = \frac{P}{\sqrt{3} \cdot U \cdot \cos(\varphi)}
```

**Renderowanie:** 

$$I = \frac{P}{\sqrt{3} \cdot U \cdot \cos(\varphi)}$$

#### Po podstawieniu wartości

```latex
I = \frac{15000}{\sqrt{3} \cdot 400 \cdot 0.85} = \frac{15000}{588.88} \approx 25.48 \, \text{A}
```

---

### Plan działania - szczegółowe zadania

#### Faza 1: Przygotowanie danych (Dane wejściowe)

| Zadanie | Opis | Status | Plik/Moduł |
|---------|------|--------|------------|
| **1.1** | Utworzyć plik CSV z danymi | ✅ | `examples/dane_prad_3fazowy.csv` |
| **1.2** | Zdefiniować strukturę danych (zmienne) | ✅ | P, U, cos_phi |
| **1.3** | Określić jednostki miar | ✅ | W, V, - |
| **1.4** | Przygotować wzór matematyczny | ✅ | `I = P / (sqrt(3) * U * cos_phi)` |

---

#### Faza 2: Wczytywanie danych z CSV

| Zadanie | Opis | Status | Plik/Moduł |
|---------|------|--------|------------|
| **2.1** | Rozszerzyć ExcelReader o obsługę CSV | ⬜ | `src/excel_reader.py` |
| **2.2** | Parsowanie kolumn: nazwa, wartość, jednostka | ⬜ | `read_variables()` |
| **2.3** | Walidacja danych wejściowych | ⬜ | Sprawdzenie typów |
| **2.4** | Obsługa błędów (brakujące kolumny) | ⬜ | Exception handling |

**Kryteria akceptacji:**
- [ ] Moduł wczytuje dane z pliku CSV
- [ ] Zmienne są poprawnie mapowane do słownika
- [ ] Jednostki są zachowane w metadanych

---

#### Faza 3: Definiowanie równania

| Zadanie | Opis | Status | Plik/Moduł |
|---------|------|--------|------------|
| **3.1** | Zdefiniować równanie w formacie tekstowym | ⬜ | `P / (sqrt(3) * U * cos_phi)` |
| **3.2** | Parsowanie równania przez SymPy | ⬜ | `equation_parser.py` |
| **3.3** | Generowanie wersji LaTeX równania | ⬜ | `to_latex()` |
| **3.4** | Podstawienie wartości liczbowych | ⬜ | `substitute_values()` |
| **3.5** | Obliczenie wyniku końcowego | ⬜ | `calculate()` |

**Kryteria akceptacji:**
- [ ] Równanie jest poprawnie parsowane
- [ ] LaTeX: `\frac{P}{\sqrt{3} \cdot U \cdot \cos(\varphi)}`
- [ ] Wynik: ~25.48 A

---

#### Faza 4: Generowanie dokumentu Word

| Zadanie | Opis | Status | Plik/Moduł |
|---------|------|--------|------------|
| **4.1** | Utworzyć strukturę dokumentu | ⬜ | `word_writer.py` |
| **4.2** | Dodać nagłówek "Obliczenia elektryczne" | ⬜ | `add_heading()` |
| **4.3** | Wstawić tabelę z danymi wejściowymi | ⬜ | `add_variables_table()` |
| **4.4** | Wstawić wzór oryginalny (LaTeX/OMML) | ⬜ | `add_equation_section()` |
| **4.5** | Wstawić wzór z podstawionymi wartościami | ⬜ | Format: `I = 15000/(1.732*400*0.85)` |
| **4.6** | Wstawić wynik z jednostką | ⬜ | `I = 25.48 A` |
| **4.7** | Zapisać dokument jako .docx | ⬜ | `save()` |

**Kryteria akceptacji:**
- [ ] Dokument zawiera wszystkie sekcje
- [ ] Wzory są czytelne i poprawnie sformatowane
- [ ] Wynik jest zaokrąglony do 2 miejsc po przecinku

---

#### Faza 5: Formatowanie równań (LaTeX → Word)

| Zadanie | Opis | Status | Plik/Moduł |
|---------|------|--------|------------|
| **5.1** | Konwersja LaTeX → OMML (Office Math) | ⬜ | Nowy moduł lub biblioteka |
| **5.2** | Wstawianie obiektów matematycznych | ⬜ | `python-docx` + `lxml` |
| **5.3** | Obsługa symboli specjalnych (√, φ) | ⬜ | Unicode / OMML |
| **5.4** | Fallback do tekstu ASCII jeśli OMML nie działa | ⬜ | `sqrt(3)` zamiast `√3` |

**Kryteria akceptacji:**
- [ ] Równania wyświetlają się poprawnie w MS Word
- [ ] Symbole matematyczne są czytelne
- [ ] Dokument otwiera się bez błędów

---

#### Faza 6: Testowanie i walidacja

| Zadanie | Opis | Status | Plik/Moduł |
|---------|------|--------|------------|
| **6.1** | Test wczytywania CSV | ⬜ | `tests/test_csv_reader.py` |
| **6.2** | Test parsowania równania 3-fazowego | ⬜ | `tests/test_equation_parser.py` |
| **6.3** | Test generowania dokumentu | ⬜ | `tests/test_word_writer.py` |
| **6.4** | Test end-to-end (CSV → Word) | ⬜ | `tests/test_integration.py` |
| **6.5** | Walidacja ręczna dokumentu w MS Word | ⬜ | Sprawdzenie wizualne |

**Kryteria akceptacji:**
- [ ] Wszystkie testy przechodzą
- [ ] Wynik obliczeń jest poprawny matematycznie
- [ ] Dokument Word otwiera się bez błędów

---

### Przepływ danych dla przypadku 3-fazowego

```
┌─────────────────────┐
│  dane_prad_3fazowy  │
│       .csv          │
│                     │
│  P = 15000 W        │
│  U = 400 V          │
│  cos_phi = 0.85     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   CSVReader         │
│   (wczytanie)       │
│                     │
│  variables = {      │
│    'P': 15000,      │
│    'U': 400,        │
│    'cos_phi': 0.85  │
│  }                  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  EquationParser     │
│                     │
│  wzór: P/(sqrt(3)   │
│        *U*cos_phi)  │
│                     │
│  LaTeX: \frac{P}... │
│  wynik: 25.48       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    WordWriter       │
│                     │
│  1. Nagłówek        │
│  2. Tabela danych   │
│  3. Wzór (LaTeX)    │
│  4. Podstawienie    │
│  5. Wynik           │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  obliczenia_prad    │
│     _3fazowy.docx   │
│                     │
│  ┌───────────────┐  │
│  │ Dane wejściowe│  │
│  │ P=15000W      │  │
│  │ U=400V        │  │
│  │ cosφ=0.85     │  │
│  ├───────────────┤  │
│  │ Wzór:         │  │
│  │ I = P/(√3·U·  │  │
│  │     ·cosφ)    │  │
│  ├───────────────┤  │
│  │ Obliczenie:   │  │
│  │ I = 15000/    │  │
│  │   (1.732·400· │  │
│  │    ·0.85)     │  │
│  ├───────────────┤  │
│  │ Wynik:        │  │
│  │ I = 25.48 A   │  │
│  └───────────────┘  │
└─────────────────────┘
```

---

### Przykładowa zawartość dokumentu wynikowego

**Tytuł:** Obliczenia prądu w układzie trójfazowym

**1. Dane wejściowe:**

| Symbol | Wartość | Jednostka | Opis |
|--------|---------|-----------|------|
| P | 15000 | W | Moc czynna |
| U | 400 | V | Napięcie międzyfazowe |
| cos φ | 0.85 | - | Współczynnik mocy |

**2. Wzór:**

$$I = \frac{P}{\sqrt{3} \cdot U \cdot \cos(\varphi)}$$

**3. Podstawienie wartości:**

$$I = \frac{15000}{\sqrt{3} \cdot 400 \cdot 0.85}$$

**4. Obliczenie:**

$$I = \frac{15000}{1.732 \cdot 400 \cdot 0.85} = \frac{15000}{588.88} = 25.48$$

**5. Wynik:**

$$\boxed{I = 25.48 \, \text{A}}$$

---

### Podsumowanie zadań

| Faza | Nazwa | Liczba zadań | Status |
|------|-------|--------------|--------|
| 1 | Przygotowanie danych | 4 | ✅ Ukończone |
| 2 | Wczytywanie CSV | 4 | ⬜ Do zrobienia |
| 3 | Definiowanie równania | 5 | ⬜ Do zrobienia |
| 4 | Generowanie Word | 7 | ⬜ Do zrobienia |
| 5 | Formatowanie LaTeX | 4 | ⬜ Do zrobienia |
| 6 | Testowanie | 5 | ⬜ Do zrobienia |
| **Razem** | | **29 zadań** | **4/29 (14%)** |

---

*Ostatnia aktualizacja: grudzień 2024*
