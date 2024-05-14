class ContaCorrente:
    def __init__(self , numero_conta, nome_correntista, saldo=0):
    
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor

conta = ContaCorrente(numero_conta=123, nome_correntista="Paulo", saldo=1000)
conta.deposito(500)
conta.saque(200)
print(f"Saldo final: {conta.saldo}")