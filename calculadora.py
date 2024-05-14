class Calculadora:
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    def multiplicacao(self, a, b):
        return a* b
    
    def divisao(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero"
        

calc = Calculadora()
resultado_soma = calc.soma(5, 3)
resultado_subtracao = calc.subtracao(8, 2)
resultado_multiplicacao = calc.multiplicacao(4, 6)
resultado_divisao = calc.divisao(9, 3)

print(f"Soma: {resultado_soma}")
print(f"Subtração: {resultado_subtracao}")
print(f"Multiplicação: {resultado_multiplicacao}")
print(f"Divisão: {resultado_divisao}")