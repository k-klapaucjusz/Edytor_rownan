"""
Główny moduł programu Edytor równań.

Program wczytuje dane z pliku Excel lub CSV, wykonuje obliczenia
i generuje dokument Word z wynikami.
"""

import argparse
from pathlib import Path

from .excel_reader import CSVReader, ExcelReader
from .equation_parser import EquationParser
from .word_writer import WordWriter


def process_csv_equations(
    csv_path: str | Path,
    output_path: str | Path,
    equations: list[dict[str, str]],
    title: str = "Obliczenia",
) -> Path:
    """
    Przetwarza równania z danymi z pliku CSV i generuje dokument Word.
    
    Args:
        csv_path: Ścieżka do pliku CSV z danymi (zmiennymi)
        output_path: Ścieżka do pliku Word wyjściowego
        equations: Lista równań do przetworzenia, każde jako słownik
                   z kluczami 'name' (nazwa) i 'formula' (wzór)
        title: Tytuł dokumentu
        
    Returns:
        Ścieżka do wygenerowanego dokumentu
        
    Example:
        >>> equations = [
        ...     {"name": "Prąd fazowy", "formula": "P / (sqrt(3) * U * cos_phi)"}
        ... ]
        >>> process_csv_equations("dane.csv", "wynik.docx", equations)
    """
    # Wczytaj dane z CSV
    reader = CSVReader(csv_path)
    variables = reader.read_variables()
    
    # Przetwórz równania
    parser = EquationParser(variables)
    results = []
    
    for eq_data in equations:
        name = eq_data.get("name", "Równanie")
        formula = eq_data.get("formula", "")
        
        if formula:
            result = parser.process_equation(name, formula)
            results.append(result)
    
    # Generuj dokument Word
    writer = WordWriter(output_path)
    
    # Nadpisz tytuł dokumentu
    writer.doc.paragraphs[0].text = title
    
    writer.add_variables_table(variables)
    writer.add_results_section(results)
    
    return writer.save()


def process_equations(
    excel_path: str | Path,
    output_path: str | Path,
    variables_sheet: str = "Dane",
    equations_sheet: str = "Równania",
) -> Path:
    """
    Przetwarza równania z pliku Excel i generuje dokument Word.
    
    Args:
        excel_path: Ścieżka do pliku Excel z danymi
        output_path: Ścieżka do pliku Word wyjściowego
        variables_sheet: Nazwa arkusza ze zmiennymi
        equations_sheet: Nazwa arkusza z równaniami
        
    Returns:
        Ścieżka do wygenerowanego dokumentu
    """
    # Wczytaj dane z Excel
    reader = ExcelReader(excel_path)
    variables = reader.read_variables(variables_sheet)
    equations = reader.read_equations(equations_sheet)
    
    # Przetwórz równania
    parser = EquationParser(variables)
    results = []
    
    # Mapowanie alternatywnych nazw kolumn
    name_columns = ["Nazwa równania", "Nazwa", "Name"]
    formula_columns = ["Wzór", "Formula", "Equation"]
    
    def get_column_value(data: dict, columns: list, default: str = "") -> str:
        """Pobiera wartość z pierwszej znalezionej kolumny."""
        for col in columns:
            if col in data and data[col]:
                return str(data[col])
        return default
    
    for eq_data in equations:
        name = get_column_value(eq_data, name_columns, "Równanie")
        formula = get_column_value(eq_data, formula_columns)
        
        if formula:
            result = parser.process_equation(name, formula)
            results.append(result)
    
    # Generuj dokument Word
    writer = WordWriter(output_path)
    writer.add_variables_table(variables)
    writer.add_results_section(results)
    
    return writer.save()


def main():
    """Główna funkcja programu - interfejs wiersza poleceń."""
    parser = argparse.ArgumentParser(
        description="Edytor równań - generowanie dokumentów Word z obliczeń Excel lub CSV"
    )
    parser.add_argument(
        "input_file",
        help="Ścieżka do pliku z danymi (Excel .xlsx lub CSV .csv)"
    )
    parser.add_argument(
        "-o", "--output",
        default="wynik.docx",
        help="Ścieżka do pliku Word wyjściowego (domyślnie: wynik.docx)"
    )
    parser.add_argument(
        "--variables-sheet",
        default="Dane",
        help="Nazwa arkusza ze zmiennymi - tylko dla plików Excel (domyślnie: Dane)"
    )
    parser.add_argument(
        "--equations-sheet",
        default="Równania",
        help="Nazwa arkusza z równaniami - tylko dla plików Excel (domyślnie: Równania)"
    )
    parser.add_argument(
        "-e", "--equation",
        action="append",
        metavar="NAME:FORMULA",
        help="Równanie w formacie 'Nazwa:wzór' (dla CSV). Można użyć wielokrotnie."
    )
    parser.add_argument(
        "-t", "--title",
        default="Obliczenia",
        help="Tytuł dokumentu (domyślnie: Obliczenia)"
    )
    
    args = parser.parse_args()
    
    try:
        input_path = Path(args.input_file)
        
        # Rozpoznaj typ pliku na podstawie rozszerzenia
        if input_path.suffix.lower() == ".csv":
            # Tryb CSV - równania muszą być podane jako argumenty
            if not args.equation:
                print("Błąd: Dla plików CSV musisz podać równania przez -e/--equation")
                print("Przykład: -e 'Prąd:P / (sqrt(3) * U * cos_phi)'")
                return 1
            
            # Parsuj równania z argumentów
            equations = []
            for eq_str in args.equation:
                if ":" in eq_str:
                    name, formula = eq_str.split(":", 1)
                    equations.append({"name": name.strip(), "formula": formula.strip()})
                else:
                    equations.append({"name": "Równanie", "formula": eq_str.strip()})
            
            output_file = process_csv_equations(
                args.input_file,
                args.output,
                equations,
                args.title,
            )
        else:
            # Tryb Excel (domyślny)
            output_file = process_equations(
                args.input_file,
                args.output,
                args.variables_sheet,
                args.equations_sheet,
            )
        
        print(f"Dokument wygenerowany pomyślnie: {output_file}")
    except FileNotFoundError as e:
        print(f"Błąd: {e}")
        return 1
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
