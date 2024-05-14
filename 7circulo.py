import math
class Circulo:

    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi  * self.raio
    
raio_do_circulo = 5
meu_circulo = Circulo(raio_do_circulo)

area = meu_circulo.calcular_area()
perimetro = meu_circulo.calcular_perimetro()

print (f"Àrea do círculo: {area}")
print(f"Perímetro do círculo: {perimetro}")