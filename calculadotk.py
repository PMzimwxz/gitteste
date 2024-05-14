import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")

rotulo1 = tk.Label(janela, text="Informe o primeiro número:")
rotulo1.pack()

entrada_num1 = tk.Entry(janela)
entrada_num1.pack(padx=10, pady=10)

rotulo2 = tk.Label(janela, text="Informe o segundo número:")
rotulo2.pack()

entrada_num2 = tk.Entry(janela)
entrada_num2.pack(padx=10, pady=10)

opcao = tk.IntVar()

rb_soma = tk.Radiobutton(janela, text="+", variable=opcao, value=1)
rb_soma.pack()

rb_subtracao = tk.Radiobutton(janela, text="-", variable=opcao, value=2)
rb_subtracao.pack()

rb_multiplicacao = tk.Radiobutton(janela, text="*", variable=opcao, value=3)
rb_multiplicacao.pack()

rb_divisao = tk.Radiobutton(janela, text="/", variable=opcao, value=4)
rb_divisao.pack()

rb_espoecial = tk.Radiobutton(janela, text="",variable=opcao, value=5)
rb_espoecial.pack()

def calcular():

    num1 = float(entrada_num1.get())
    num2 = float(entrada_num2.get())
    operacao = opcao.get()

    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        if num2 == 0:
            resultado = "Erro: Divisão por zero"
        else:
            resultado = num1 / num2
    else:
        resultado = num1 = num2
        resultado = "Erro: Operação inválida"
    print(resultado)
    lb_resultado.config(text=resultado)

botao = tk.Button(janela , text="Calcular", width=15, bg="pink", fg="navy", command=calcular)
botao.pack()


lb_resultado = tk.Label(janela, text="O resultado será exibido aqui! ")
lb_resultado.pack(pady=10, padx=10)
janela.geometry("300x300")

janela.mainloop()