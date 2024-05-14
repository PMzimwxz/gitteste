contatos = {
    "Paulo Martinho": "123456789",
    "Havilla": "987654321",
    "Cainã": "111223344",
    "Alex": "555666777",
    "Paulo Flávio": "999888777"
}

def buscar_telefone(contatos, nome):
    if nome in contatos:
        return contatos[nome]
    else:
        return "Contato não encontrado."

nome_contato = input("Digite o nome do contato que deseja buscar: ")

telefone = buscar_telefone(contatos, nome_contato)
print(f"O telefone de {nome_contato} é :{telefone}")