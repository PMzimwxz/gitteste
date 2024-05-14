import random
class jogodeAdivinhacao:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
    def jogar( self, palpite):
        self.tentativas += 1
        if palpite == self.numero_secreto:
            return f'parabems! voce acertou o numero {self.numero_secreto} em {self.tentativas}'
        elif palpite < self.numero_secreto:
            return 'tente um numero maior'
        else :
            return 'tente um numero menor.'
jogo = jogodeAdivinhacao()
while True:
    palpite_usuario = int(input('digite seu palpite ( entre 1 e 100)'))
    resultado = jogo.numero_secreto

    print(resultado)
    if palpite_usuario == jogo.numero_secreto:
        break