import tkinter as tk

janela = tk.Tk()
janela.title("calculadora")

class Calculadora:
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    def multiplicacao(self, a, b):
        return a* b
    
    def divisao(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero"
        

rotulo = tk.Label()
rotulo.pack

calc = Calculadora()
resultado_soma = calc.soma(5, 3)
resultado_subtracao = calc.subtracao(8, 2)
resultado_multiplicacao = calc.multiplicacao(4, 6)
resultado_divisao = calc.divisao(9, 3)

def click():
    print("envie seu numero")
botao = tk.Button(janela, text="calc", fg="black", bg="pink", font=("times roman", 14, "bold"), height=2, width=9, relief="raised", command=click)
botao.pack()

calc =tk.Entry(janela)
calc.pack()
print("seu calculo ")



janela.mainloop()