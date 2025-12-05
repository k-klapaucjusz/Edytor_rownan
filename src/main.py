"""
Główny moduł programu Edytor równań.

Program wczytuje dane z pliku Excel, wykonuje obliczenia
i generuje dokument Word z wynikami.
"""

import argparse
from pathlib import Path

from .excel_reader import ExcelReader
from .equation_parser import EquationParser
from .word_writer import WordWriter


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
        description="Edytor równań - generowanie dokumentów Word z obliczeń Excel"
    )
    parser.add_argument(
        "excel_file",
        help="Ścieżka do pliku Excel z danymi i równaniami"
    )
    parser.add_argument(
        "-o", "--output",
        default="wynik.docx",
        help="Ścieżka do pliku Word wyjściowego (domyślnie: wynik.docx)"
    )
    parser.add_argument(
        "--variables-sheet",
        default="Dane",
        help="Nazwa arkusza ze zmiennymi (domyślnie: Dane)"
    )
    parser.add_argument(
        "--equations-sheet",
        default="Równania",
        help="Nazwa arkusza z równaniami (domyślnie: Równania)"
    )
    
    args = parser.parse_args()
    
    try:
        output_file = process_equations(
            args.excel_file,
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
