"""
Moduł do wczytywania danych z plików Excel.
"""

from pathlib import Path
from typing import Any

import pandas as pd


class ExcelReader:
    """Klasa do wczytywania danych i równań z pliku Excel."""
    
    def __init__(self, file_path: str | Path):
        """
        Inicjalizuje czytnik Excel.
        
        Args:
            file_path: Ścieżka do pliku Excel
        """
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"Plik nie istnieje: {self.file_path}")
    
    def read_variables(self, sheet_name: str = "Dane") -> dict[str, Any]:
        """
        Wczytuje zmienne z arkusza Excel.
        
        Args:
            sheet_name: Nazwa arkusza z danymi
            
        Returns:
            Słownik z nazwami zmiennych i ich wartościami
        """
        df = pd.read_excel(self.file_path, sheet_name=sheet_name)
        
        # Zakładamy kolumny: "Nazwa zmiennej", "Wartość"
        if "Nazwa zmiennej" in df.columns and "Wartość" in df.columns:
            return dict(zip(df["Nazwa zmiennej"], df["Wartość"]))
        
        # Alternatywny format: pierwsza kolumna to nazwa, druga to wartość
        return dict(zip(df.iloc[:, 0], df.iloc[:, 1]))
    
    def read_equations(self, sheet_name: str = "Równania") -> list[dict[str, Any]]:
        """
        Wczytuje równania z arkusza Excel.
        
        Args:
            sheet_name: Nazwa arkusza z równaniami
            
        Returns:
            Lista słowników z danymi równań
        """
        df = pd.read_excel(self.file_path, sheet_name=sheet_name)
        return df.to_dict("records")
    
    def get_sheet_names(self) -> list[str]:
        """
        Zwraca listę nazw arkuszy w pliku Excel.
        
        Returns:
            Lista nazw arkuszy
        """
        xl = pd.ExcelFile(self.file_path)
        return xl.sheet_names
