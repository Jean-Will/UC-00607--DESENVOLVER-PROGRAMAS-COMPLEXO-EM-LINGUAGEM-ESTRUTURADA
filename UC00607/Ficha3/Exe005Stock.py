"""
5. Gestão de stock
Simule o stock de uma loja com um dicionário {"produto": quantidade}.
Implemente um menu com opções para: adicionar produto, remover
produto, atualizar quantidade e listar todo o stock. Os dados iniciais
deverão estar num ficheiro em formato csv. Quando terminar o programa,
atualize o ficheiro com os dados que se encontram no dicionário.

"""
def adicionar():
    produto = input("Nome do produto: ").lower()
    quant = int(input(f"Quantidade do produto: {produto} "))
    dici[produto] = quant
    print(dici)
    

def remover():
    nome = input("Qual produto deseja remover?: ")
    if nome in dici:
        del(dici[nome])
    else:
        print("Esse produto nao existe! ")

    print(dici)


def atualizar():
    nome = input("Qual o nome do produto a actualizar a quantidade?: ")
    novaqt = int(input(f"Qual a nova quantidade do produto {nome}?: "))
    dici[nome] = novaqt
    print(dici)

def listar():
   for nome,qt in dici.items():
    print(f"{qt:4} - {nome}")
  

def sair():
    lista_linhas = []
    for nome, qt in dici.items():
        linha = nome + ";" + str(qt)
        lista_linhas.append(linha)

    conteudo = "\n".join(lista_linhas) #junta todas as linhas separadas

    with open(way,"w",encoding="utf-8") as fp:
        fp.write(conteudo)
     


dici = {}

way = "./UC00607/stock.csv"

with open(way,"r",encoding="utf8") as fp:
    dados = fp.read().split("\n")

for linha in dados:
    info = linha.split(";")
    nome = info[0]
    qt = float(info[1])
    dici[nome] = qt

while True:
    print("(1) Adicionar produto")
    print("(2) Remover produto")
    print("(3) Atualizar Quantidade")
    print("(4) Listar Stock")
    print("(5) Sair")
    op = int(input("Escolha uma Opcao: \n"))
    match op:
        case 1:
            adicionar()
        case 2:
            remover()
        case 3:
            atualizar()
        case 4:
            listar()
        case 5:
            sair() 
            print("Encerrando programa...")
            
            break           
        case _:
            print("Opcao invalida! \n")

    input(" < Enter > para continuar: \n")   


