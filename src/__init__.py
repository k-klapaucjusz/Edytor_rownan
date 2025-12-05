"""
Edytor równań - pakiet główny

Program do wczytywania danych z Excel lub CSV, wykonywania obliczeń
i generowania dokumentów Word z równaniami.
"""

__version__ = "0.1.0"

from .excel_reader import CSVReader, ExcelReader
from .equation_parser import EquationParser, EquationResult
from .word_writer import WordWriter
from .main import process_csv_equations, process_equations

__all__ = [
    "CSVReader",
    "ExcelReader",
    "EquationParser",
    "EquationResult",
    "WordWriter",
    "process_csv_equations",
    "process_equations",
]
