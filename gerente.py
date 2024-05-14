class Fucionário:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    def calcular_bonus(self):
        return 0.1 * self.salario
    
funcionario1 = Fucionário("João", "Analista", 5000)
bonus_funcionario1 = funcionario1.calcular_bonus()

print(f"Nome:{funcionario1.nome}, Cargo:{funcionario1.cargo}, Salário:R${funcionario1.salario}")
print(f"Bônus: R${bonus_funcionario1}")                                                                                      