import math
class ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distancia_origem (self):
        return math.sqrt (self.x**2 + self.y**2)
    
ponto_exemplo = ponto(3, 4)
distacia = ponto_exemplo.distancia_origem()
print(f'a distancia do ponto e: {distacia}')