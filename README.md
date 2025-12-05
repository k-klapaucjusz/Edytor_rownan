# Edytor Równań

Program w języku Python do przetwarzania danych z plików Excel lub CSV i generowania dokumentów Word z równaniami matematycznymi.

## Funkcjonalności

- 📊 Wczytywanie danych z plików Excel (.xlsx) lub CSV (.csv)
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

### Linia poleceń - z plikiem Excel

```bash
python -m src.main dane.xlsx -o wynik.docx
```

### Linia poleceń - z plikiem CSV

```bash
python -m src.main dane.csv -e "Prąd fazowy:P / (sqrt(3) * U * cos_phi)" -o wynik.docx -t "Obliczenia elektryczne"
```

Dla plików CSV równania podaje się jako argumenty `-e` w formacie `Nazwa:wzór`. Można podać wiele równań:

```bash
python -m src.main dane.csv \
    -e "Prąd fazowy:P / (sqrt(3) * U * cos_phi)" \
    -e "Moc pozorna:P / cos_phi" \
    -o wynik.docx
```

### Jako moduł Python - Excel

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

### Jako moduł Python - CSV

```python
from src.main import process_csv_equations

equations = [
    {"name": "Prąd fazowy", "formula": "P / (sqrt(3) * U * cos_phi)"},
    {"name": "Moc pozorna", "formula": "P / cos_phi"},
]

output_file = process_csv_equations(
    csv_path="dane.csv",
    output_path="wynik.docx",
    equations=equations,
    title="Obliczenia elektryczne"
)
print(f"Wygenerowano: {output_file}")
```

## Format pliku CSV

```csv
Nazwa zmiennej,Wartość,Jednostka,Opis
P,15000,W,Moc czynna
U,400,V,Napięcie międzyfazowe
cos_phi,0.85,-,Współczynnik mocy
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

## Przykład: Obliczenia prądu 3-fazowego

Plik z danymi `examples/dane_prad_3fazowy.csv`:

```csv
Nazwa zmiennej,Wartość,Jednostka,Opis
P,15000,W,Moc czynna
U,400,V,Napięcie międzyfazowe
cos_phi,0.85,-,Współczynnik mocy
```

Generowanie dokumentu:

```bash
python -m src.main examples/dane_prad_3fazowy.csv \
    -e "Prąd fazowy:P / (sqrt(3) * U * cos_phi)" \
    -o obliczenia_prad_3fazowy.docx \
    -t "Obliczenia prądu w układzie trójfazowym"
```

Wynik: dokument Word zawierający:
- Tabelę z danymi wejściowymi (P, U, cos_phi)
- Wzór prądu fazowego
- Podstawione wartości
- Wynik obliczeń (~25.47 A)

## Struktura projektu

```
edytor_rownan/
├── src/
│   ├── __init__.py
│   ├── excel_reader.py      # Wczytywanie danych z Excel i CSV
│   ├── equation_parser.py   # Parsowanie i obliczanie równań
│   ├── word_writer.py       # Generowanie dokumentu Word
│   └── main.py              # Główny punkt wejścia
├── tests/
│   ├── test_equation_parser.py
│   └── test_csv_word_integration.py
├── examples/
│   └── dane_prad_3fazowy.csv
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
