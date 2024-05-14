import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0: 
        return a / b
    else:
        return "Erro: divisão por zero."
    
def raiz_quadrada(a):
    return math.sqrt(a)

operacao = input("Escolha a operação(soma, subtração, multiplicação, divisão, raiz quadrada): ")

if operacao != "raiz quadrada":
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

if operacao == "soma":
    resultado = soma(valor1, valor2)
elif operacao == "subtração":
    resultado = subtracao(valor1, valor2)
elif operacao == "multiplicação":
    resultado = multiplicacao(valor1, valor2)
elif operacao == "divisão":
    resultado = divisao(valor1, valor2)
elif operacao == "raíz quadrada":
    valor = float(input("Digite o valor para a raíz quadrada: "))
    resultado = raiz_quadrada(valor)
else:
    resultado = "Operação inválida."

print(f"Resultado da operação {operacao}:{resultado}")