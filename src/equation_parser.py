"""
Moduł do parsowania i obliczania równań matematycznych.
"""

from dataclasses import dataclass
from typing import Any

from sympy import Expr, Float, latex, sympify
from sympy.parsing.sympy_parser import (
    convert_xor,
    implicit_multiplication_application,
    parse_expr,
    standard_transformations,
)


@dataclass
class EquationResult:
    """Wynik obliczenia równania."""
    
    name: str
    original_equation: str
    equation_with_values: str
    result: float
    latex_original: str
    latex_with_values: str


class EquationParser:
    """Klasa do parsowania i obliczania równań matematycznych."""
    
    # Transformacje dla parsera SymPy
    TRANSFORMATIONS = standard_transformations + (
        implicit_multiplication_application,
        convert_xor,  # Pozwala używać ^ zamiast **
    )
    
    def __init__(self, variables: dict[str, Any] | None = None):
        """
        Inicjalizuje parser równań.
        
        Args:
            variables: Słownik ze zmiennymi i ich wartościami
        """
        self.variables = variables or {}
    
    def set_variables(self, variables: dict[str, Any]) -> None:
        """
        Ustawia zmienne do podstawienia.
        
        Args:
            variables: Słownik ze zmiennymi i ich wartościami
        """
        self.variables = variables
    
    def parse_equation(self, equation_str: str) -> Expr:
        """
        Parsuje równanie do postaci symbolicznej.
        
        Args:
            equation_str: Równanie jako tekst
            
        Returns:
            Wyrażenie SymPy
        """
        # convert_xor w TRANSFORMATIONS obsługuje konwersję ^ na **
        return parse_expr(equation_str, transformations=self.TRANSFORMATIONS)
    
    def substitute_values(self, equation: Expr) -> Expr:
        """
        Podstawia wartości zmiennych do równania.
        
        Args:
            equation: Wyrażenie SymPy
            
        Returns:
            Wyrażenie z podstawionymi wartościami
        """
        return equation.subs(self.variables)
    
    def calculate(self, equation_str: str) -> float:
        """
        Parsuje i oblicza wartość równania.
        
        Args:
            equation_str: Równanie jako tekst
            
        Returns:
            Wartość liczbowa wyniku
        """
        equation = self.parse_equation(equation_str)
        result = self.substitute_values(equation)
        return float(result.evalf())
    
    def to_latex(self, equation: Expr) -> str:
        """
        Konwertuje równanie do formatu LaTeX.
        
        Args:
            equation: Wyrażenie SymPy
            
        Returns:
            Równanie w formacie LaTeX
        """
        return latex(equation)
    
    def format_equation_with_values(self, equation_str: str) -> str:
        """
        Tworzy tekstową reprezentację równania z podstawionymi wartościami.
        
        Args:
            equation_str: Równanie jako tekst
            
        Returns:
            Równanie z podstawionymi wartościami jako tekst
        """
        result = equation_str
        for var_name, value in self.variables.items():
            result = result.replace(str(var_name), str(value))
        return result
    
    def process_equation(self, name: str, equation_str: str) -> EquationResult:
        """
        Przetwarza równanie i zwraca pełny wynik.
        
        Args:
            name: Nazwa równania
            equation_str: Równanie jako tekst
            
        Returns:
            Obiekt EquationResult z wszystkimi danymi
        """
        equation = self.parse_equation(equation_str)
        equation_with_values = self.substitute_values(equation)
        result = float(equation_with_values.evalf())
        
        return EquationResult(
            name=name,
            original_equation=equation_str,
            equation_with_values=self.format_equation_with_values(equation_str),
            result=result,
            latex_original=self.to_latex(equation),
            latex_with_values=self.to_latex(equation_with_values),
        )
