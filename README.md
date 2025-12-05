# Edytor Równań

Program w języku Python do przetwarzania danych z plików Excel i generowania dokumentów Word z równaniami matematycznymi.

## Funkcjonalności

- 📊 Wczytywanie danych z plików Excel (.xlsx)
- 🔢 Parsowanie i obliczanie równań matematycznych
- 📝 Generowanie dokumentów Word z wynikami
- ✨ Obsługa notacji matematycznej (potęgi, pierwiastki, etc.)

## Instalacja

```bash
# Klonowanie repozytorium
git clone https://github.com/k-klapaucjusz/Edytor_rownan.git
cd Edytor_rownan

# Utworzenie środowiska wirtualnego
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# lub
.venv\Scripts\activate  # Windows

# Instalacja zależności
pip install -r requirements.txt
```

## Użycie

### Linia poleceń

```bash
python -m src.main dane.xlsx -o wynik.docx
```

### Jako moduł Python

```python
from src.main import process_equations

output_file = process_equations(
    excel_path="dane.xlsx",
    output_path="wynik.docx",
    variables_sheet="Dane",
    equations_sheet="Równania"
)
print(f"Wygenerowano: {output_file}")
```

## Format pliku Excel

### Arkusz "Dane"

| Nazwa zmiennej | Wartość | Jednostka |
|----------------|---------|-----------|
| a              | 5       | m         |
| b              | 3       | m         |
| c              | 4       | m         |

### Arkusz "Równania"

| Nazwa równania | Wzór            | Opis                    |
|----------------|-----------------|-------------------------|
| Suma           | a + b           | Suma dwóch wartości     |
| Pitagoras      | sqrt(a^2 + b^2) | Twierdzenie Pitagorasa  |
| Pole           | a * b / 2       | Pole trójkąta           |

## Struktura projektu

```
edytor_rownan/
├── src/
│   ├── __init__.py
│   ├── excel_reader.py      # Wczytywanie danych z Excel
│   ├── equation_parser.py   # Parsowanie i obliczanie równań
│   ├── word_writer.py       # Generowanie dokumentu Word
│   └── main.py              # Główny punkt wejścia
├── tests/
│   └── test_equation_parser.py
├── templates/
├── requirements.txt
├── KONCEPCJA.md
└── README.md
```

## Biblioteki

- **openpyxl** - obsługa plików Excel
- **pandas** - manipulacja danymi
- **python-docx** - generowanie dokumentów Word
- **sympy** - obliczenia symboliczne

## Licencja

MIT License

## Autor

k-klapaucjusz
