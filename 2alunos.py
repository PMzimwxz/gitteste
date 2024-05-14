dados_aluno = {}
menu = 1
while menu != 0:
    acao = input("Que ação deseja realizar: \n1 -> Adicionar aluno \n2 -> Inserir nota \n Sair")
    if acao == 1:
        inserir_nome = input("Informe o nome do aluno: ")
        dados_aluno['Nome'] = inserir_nome
    elif acao == 2:
        inserir_nota = input("Informe a nota do aluno: ")
        dados_aluno['Nota'] = inserir_nota
    elif acao == 3:
        menu = 0

