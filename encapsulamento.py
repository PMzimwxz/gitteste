class ContaBancaria:
    def __init__(self, numero_conta):
        self.__saldo = 0

        self.numero_conta = numero_conta

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente. Operação de saque não realizada.")

    def get_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(numero_conta=12345)

conta.depositar(1000)
print("Saldo após depósito:", conta.get_saldo())

conta.sacar(500)
print("Saldo após saque:", conta.get_saldo())

conta.sacar(700)
print("Saldo após tentativa de saque:", conta.get_saldo())