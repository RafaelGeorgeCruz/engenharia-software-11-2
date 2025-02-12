class Calculadora:
    def adicao(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ValueError(
                "Divisão por zero não é permitida."
                )
        return a / b


# Exemplo de uso
if __name__ == "__main__":
    calc = Calculadora()
    print("Adição: ", calc.adicao(5, 3))
    print("Subtração: ", calc.subtracao(5, 3))
    print("Multiplicação: ", calc.multiplicacao(5, 3))
    print("Divisão: ", calc.divisao(5, 3))
