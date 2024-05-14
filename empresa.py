class Fucionário:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    def calcular_bonus(self):
        return 0.10 * self.salario
    
class Gerente(Fucionário):
    def calcular_bonus(self):
        return 0.15 * self.salario
    
class Vendedor(Fucionário):
    def calcular_bonus(self):
        return 0.05 * self.salario + 500.00
    
gerente1 = Gerente("João", "Gerente de vendas", 5000.00)
vendedor1 = Vendedor("Maria", "Vendedor", 3000.00)

bonus_gerente = gerente1.calcular_bonus()
bonus_vendedor = vendedor1.calcular_bonus()

print("Bônus do gerente: R${bonus_gerente:.2f}")
print(f"Bônus do vendedor: R${bonus_vendedor:.2f}")