import random

def gerar_numeros_mega_sena():
    numeros_mega_sena = random.sample(range(1, 11), 9)
    return numeros_mega_sena

numeros_sorteados = gerar_numeros_mega_sena()

print("Números sorteados na Mega Sena:", numeros_sorteados )