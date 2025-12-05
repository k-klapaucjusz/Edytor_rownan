"""
Testy modułu equation_parser.
"""

import pytest
from src.equation_parser import EquationParser, EquationResult


class TestEquationParser:
    """Testy dla klasy EquationParser."""
    
    def test_parse_simple_equation(self):
        """Test parsowania prostego równania."""
        parser = EquationParser()
        equation = parser.parse_equation("a + b")
        assert str(equation) == "a + b"
    
    def test_parse_equation_with_power(self):
        """Test parsowania równania z potęgą."""
        parser = EquationParser()
        equation = parser.parse_equation("a^2 + b^2")
        assert str(equation) == "a**2 + b**2"
    
    def test_calculate_simple_sum(self):
        """Test obliczenia prostej sumy."""
        parser = EquationParser({"a": 5, "b": 3})
        result = parser.calculate("a + b")
        assert result == 8.0
    
    def test_calculate_with_sqrt(self):
        """Test obliczenia z pierwiastkiem."""
        parser = EquationParser({"a": 9})
        result = parser.calculate("sqrt(a)")
        assert result == 3.0
    
    def test_calculate_pythagorean(self):
        """Test obliczenia twierdzenia Pitagorasa."""
        parser = EquationParser({"a": 3, "b": 4})
        result = parser.calculate("sqrt(a^2 + b^2)")
        assert result == 5.0
    
    def test_to_latex(self):
        """Test konwersji do LaTeX."""
        parser = EquationParser()
        equation = parser.parse_equation("sqrt(a^2 + b^2)")
        latex_str = parser.to_latex(equation)
        assert "sqrt" in latex_str or "\\sqrt" in latex_str
    
    def test_process_equation(self):
        """Test pełnego przetwarzania równania."""
        parser = EquationParser({"a": 3, "b": 4})
        result = parser.process_equation("Pitagoras", "sqrt(a^2 + b^2)")
        
        assert isinstance(result, EquationResult)
        assert result.name == "Pitagoras"
        assert result.original_equation == "sqrt(a^2 + b^2)"
        assert result.result == 5.0
    
    def test_format_equation_with_values(self):
        """Test formatowania równania z podstawionymi wartościami."""
        parser = EquationParser({"a": 5, "b": 3})
        formatted = parser.format_equation_with_values("a + b")
        assert "5" in formatted
        assert "3" in formatted
    
    def test_set_variables(self):
        """Test ustawiania zmiennych."""
        parser = EquationParser()
        parser.set_variables({"x": 10})
        result = parser.calculate("x * 2")
        assert result == 20.0
