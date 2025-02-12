from src.calculadora import Calculadora
import pytest


class TestCalculadora:
    @pytest.fixture
    def calc(self):
        return Calculadora()

    def test_adicao(self, calc):
        assert calc.adicao(2, 3) == 5

    def test_subtracao(self, calc):
        assert calc.subtracao(5, 3) == 2

    def test_multiplicacao(self, calc):
        assert calc.multiplicacao(4, 3) == 12

    def test_divisao(self, calc):
        assert calc.divisao(10, 2) == 5
