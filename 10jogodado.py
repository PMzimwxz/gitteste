import random
import math

class JogoDado:
    def lançar_dado(self):
        numero_aleatorio = random.randint(1, 6)
        raiz_quadrada = math.sqrt(numero_aleatorio)
        print(f'O número gerado foi: {numero_aleatorio}, e a raiz quadrada é: {raiz_quadrada}')

jogo = JogoDado()
jogo.lançar_dado()