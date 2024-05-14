import random
class Dado:
    def __init__(self, lados):
        self.lados = lados

    def lancar_dado(self):
        return random.randint(1, self.lados)
d4 = Dado(4)
d6 = Dado(6)
d8 = Dado(8)
d10 = Dado(10)
d12 = Dado(12)
d20 = Dado(20)

print(f"lançamento do d4:{d4.lancar_dado()}")
print(f"lançamento do d4:{d6.lancar_dado()}")
print(f"lançamento do d4:{d8.lancar_dado()}")
print(f"lançamento do d4:{d10.lancar_dado()}")
print(f"lançamento do d4:{d12.lancar_dado()}")
print(f"lançamento do d4:{d20.lancar_dado()}")