class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        self.idade += anos

    def crescer(self, anos=1):
        if self.idade < 21:
            self.altura +=anos * 0.5

pessoa1 = Pessoa(nome="João", idade=18, peso=70, altura=175)

print(f"{pessoa1.nome} tem {pessoa1.idade} anos, pesa {pessoa1.peso} kg e mede {pessoa1.altura} cm.")
pessoa1.envelhecer()
pessoa1.crescer()
print(f"Agora, {pessoa1.nome} tem {pessoa1.idade} anos, pesa {pessoa1.peso} kg e mede {pessoa1.altura} cm.")