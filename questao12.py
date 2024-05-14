import random

numeros = list(set(random.sample(range(1, 61), 6)))

while len(numeros) < 6:
    numeros.extend(random.sample(range(1, 61), 6 - len(numeros)))

numeros.sort()

print("Aqui estão os números gerados em ordem crescente, sem duplicatas:")
for numero in numeros:
    print(numero)

print("O maior valor é:", max(numeros))
print("O menor valor é:", min(numeros))