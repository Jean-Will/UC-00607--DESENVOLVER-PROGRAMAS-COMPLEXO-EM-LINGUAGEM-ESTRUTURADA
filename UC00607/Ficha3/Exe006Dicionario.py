"""
6. Agenda telefónica
Crie um programa que permita adicionar, pesquisar, atualizar e apagar
contactos, guardados como {"nome": {"telefone": ..., "email": ...}} (dicionário
de dicionários). Os dados iniciais deverão estar num ficheiro em formato
csv. Quando terminar o programa, atualize o ficheiro com os dados que se
encontram no dicionário. """

from time import sleep

def adicionar():
    nome = input("Nome: ").title()
    while nome in dados:
        nome = input(f"O nome {nome} ja existe! Qual o novo nome? || << fim >> para sair \n").title()
        if nome == "Fim":
            return
    telemovel = int(input(f"Qual o seu Telemovel: "))
    email = input(f"Qual o seu email: ")

    dados[nome] = {"telemovel":telemovel , "email":email}
    print(dados)
   


def pesquisar():
    for chave, valor in dados.items():
        nome = chave
        telef = valor["Telefone"]
        email = valor["Email"]
        print(f"O utilizador {nome} tel:{telef} e o Email: {email}")
    


def atualizar():
    nome = input("Qual o nome do user para eliminar? ").title()
    telef = input(f"Qual o novo telefone do {nome}? ")
    email = input(f"Qual o novo email do {nome}? ")

    dados[nome] = {"Telefone":telef, "Email":email}



def apagar():
    nome = input("Qual o nome do user para eliminar? ").title()
    if nome in dados:
        del(dados[nome])
    else:
        print(f"Esse nome {nome} nao existe...")



def gravar():
    linhas = [] # para guardar as linhas que vao atualizar o ficheiro
    for chave, valor in dados.items():
        nome = chave
        telef = valor["Telefone"]
        email = valor["Email"]
        frase = nome + ";" + telef + ";" + email
        linhas.append(frase)

    conteudo = "\n".join(linhas)

    with open(way,"w",encoding="utf-8")as fp:
        fp.write(conteudo)    



dados = {} # dicionario vazio
way = "./UC00607/Ficha3/Agenda.csv"

with open(way, "r", encoding="utf-8") as fp:
    cont = fp.read().split("\n") # lista de linhas 
    for linha in cont:
        info = linha.split(";")
        nome = info[0]
        telemovel = info[1]
        email =  info[2]

        dados[nome] = {"Telefone":telemovel ,"Email":email}




while True:
    print("1) Adicionar ")
    print("2) Pesquisar ")
    print("3) Atualizar ")
    print("4) Apagar ")
    print("5) Sair ")

    op = int(input("\n\nQual a sua opcao? "))

    match op:
        case 1:
            adicionar()
        case 2:
            pesquisar()
        case 3:
            atualizar()
        case 4:
            apagar()
        case 5:
            gravar()    
            print("Guardando dados...")
            sleep(2)
            print("Encerrando programa...")
            break
        case _:
            print("Opcao invalida!")

    input("\n Carregue << Enter >> para continuar...")