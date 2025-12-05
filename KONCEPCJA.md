# Koncepcja Wstępna - Edytor Równań

## Opis projektu

Program w języku Python, który:
1. Wczytuje dane z pliku Excel
2. Wykonuje obliczenia według przygotowanych funkcji
3. Generuje dokument Word z równaniami oraz równaniami z podstawionymi danymi

---

## Proponowane biblioteki i moduły

### 1. Obsługa plików Excel

| Biblioteka | Opis | Zastosowanie |
|------------|------|--------------|
| **openpyxl** | Biblioteka do odczytu i zapisu plików Excel (.xlsx) | Główna biblioteka do wczytywania danych wejściowych |
| **pandas** | Biblioteka do analizy danych | Ułatwia manipulację danymi tabelarycznymi |

```python
# Przykład użycia
import pandas as pd
from openpyxl import load_workbook

# Wczytanie danych
df = pd.read_excel('dane.xlsx', sheet_name='Dane')
```

### 2. Obsługa plików Word

| Biblioteka | Opis | Zastosowanie |
|------------|------|--------------|
| **python-docx** | Biblioteka do tworzenia i edycji dokumentów Word (.docx) | Tworzenie dokumentu wynikowego |

```python
# Przykład użycia
from docx import Document

doc = Document()
doc.add_heading('Obliczenia', level=1)
doc.add_paragraph('Równanie: a + b = c')
doc.save('wynik.docx')
```

### 3. Obsługa równań matematycznych

| Biblioteka | Opis | Zastosowanie |
|------------|------|--------------|
| **sympy** | Biblioteka do obliczeń symbolicznych | Parsowanie i obliczanie równań matematycznych |
| **latex2mathml** | Konwersja LaTeX do MathML | Formatowanie równań w dokumencie Word |

```python
# Przykład użycia SymPy
from sympy import symbols, sympify, latex

x, y = symbols('x y')
equation = sympify('x**2 + 2*x + 1')
result = equation.subs(x, 5)  # Podstawienie wartości
latex_eq = latex(equation)    # Konwersja do LaTeX
```

### 4. Dodatkowe moduły standardowe

| Moduł | Opis | Zastosowanie |
|-------|------|--------------|
| **pathlib** | Obsługa ścieżek do plików | Zarządzanie plikami wejściowymi/wyjściowymi |
| **typing** | Typowanie statyczne | Poprawa czytelności kodu |
| **dataclasses** | Klasy danych | Struktury danych dla równań |

---

## Proponowana architektura

### Struktura projektu

```
edytor_rownan/
├── src/
│   ├── __init__.py
│   ├── excel_reader.py      # Moduł do wczytywania danych z Excel
│   ├── equation_parser.py   # Moduł do parsowania i obliczania równań
│   ├── word_writer.py       # Moduł do generowania dokumentu Word
│   └── main.py              # Główny punkt wejścia programu
├── templates/
│   └── szablon_excel.xlsx   # Szablon pliku Excel z danymi
├── tests/
│   ├── __init__.py
│   ├── test_excel_reader.py
│   ├── test_equation_parser.py
│   └── test_word_writer.py
├── requirements.txt
├── README.md
└── KONCEPCJA.md
```

### Diagram przepływu danych

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Plik Excel    │────▶│   Parser równań  │────▶│  Dokument Word  │
│ (dane + wzory)  │     │   (obliczenia)   │     │   (wyniki)      │
└─────────────────┘     └──────────────────┘     └─────────────────┘
        │                        │                        │
        ▼                        ▼                        ▼
   - Wartości              - Parsowanie             - Równania
   - Typ obliczeń          - Podstawianie           - Wartości podstawione
   - Wzory                 - Obliczanie             - Wyniki
```

---

## Proponowany format danych w Excel

### Arkusz "Dane"

| Nazwa zmiennej | Wartość | Jednostka |
|----------------|---------|-----------|
| a              | 5       | m         |
| b              | 3       | m         |
| c              | 4       | m         |

### Arkusz "Równania"

| ID | Nazwa równania | Wzór          | Opis                    |
|----|----------------|---------------|-------------------------|
| 1  | Suma           | a + b         | Suma dwóch wartości     |
| 2  | Pitagoras      | sqrt(a^2+b^2) | Twierdzenie Pitagorasa  |
| 3  | Pole           | a * b / 2     | Pole trójkąta           |

---

## Proponowany przepływ pracy programu

### 1. Wczytanie danych

```python
class ExcelReader:
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def read_variables(self) -> dict:
        """Wczytuje zmienne z arkusza 'Dane'"""
        df = pd.read_excel(self.file_path, sheet_name='Dane')
        return dict(zip(df['Nazwa zmiennej'], df['Wartość']))
    
    def read_equations(self) -> list:
        """Wczytuje równania z arkusza 'Równania'"""
        df = pd.read_excel(self.file_path, sheet_name='Równania')
        return df.to_dict('records')
```

### 2. Parsowanie i obliczanie równań

```python
from sympy import sympify, symbols, latex
from sympy.parsing.sympy_parser import parse_expr

class EquationParser:
    def __init__(self, variables: dict):
        self.variables = variables
    
    def parse_equation(self, equation_str: str):
        """Parsuje równanie do postaci symbolicznej"""
        return sympify(equation_str)
    
    def substitute_values(self, equation):
        """Podstawia wartości zmiennych do równania"""
        return equation.subs(self.variables)
    
    def calculate(self, equation) -> float:
        """Oblicza wartość równania"""
        result = self.substitute_values(equation)
        return float(result.evalf())
    
    def to_latex(self, equation) -> str:
        """Konwertuje równanie do formatu LaTeX"""
        return latex(equation)
```

### 3. Generowanie dokumentu Word

```python
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

class WordWriter:
    def __init__(self, output_path: str):
        self.doc = Document()
        self.output_path = output_path
    
    def add_equation_section(self, name: str, equation_str: str, 
                             equation_with_values: str, result: float):
        """Dodaje sekcję z równaniem do dokumentu"""
        self.doc.add_heading(name, level=2)
        self.doc.add_paragraph(f'Wzór: {equation_str}')
        self.doc.add_paragraph(f'Po podstawieniu: {equation_with_values}')
        self.doc.add_paragraph(f'Wynik: {result}')
    
    def save(self):
        """Zapisuje dokument"""
        self.doc.save(self.output_path)
```

---

## Wymagania systemowe

### requirements.txt

```
openpyxl>=3.1.0
pandas>=2.0.0
python-docx>=1.0.0
sympy>=1.12
```

### Wersja Pythona

- Python 3.10 lub nowszy

---

## Możliwe rozszerzenia

1. **GUI** - Interfejs graficzny z użyciem `tkinter` lub `PyQt`
2. **Obsługa jednostek** - Biblioteka `pint` do konwersji jednostek
3. **Szablony Word** - Możliwość użycia szablonów dokumentów
4. **Walidacja danych** - Sprawdzanie poprawności danych wejściowych
5. **Obsługa MathML/OMML** - Lepsze formatowanie równań w Word

---

## Następne kroki

1. ✅ Opracowanie koncepcji wstępnej
2. ⬜ Utworzenie struktury projektu
3. ⬜ Implementacja modułu `excel_reader`
4. ⬜ Implementacja modułu `equation_parser`
5. ⬜ Implementacja modułu `word_writer`
6. ⬜ Integracja modułów w `main.py`
7. ⬜ Testy jednostkowe
8. ⬜ Dokumentacja użytkownika
