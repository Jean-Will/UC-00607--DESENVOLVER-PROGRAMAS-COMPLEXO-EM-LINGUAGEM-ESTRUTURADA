"""
a. Quantas pessoas se encontram registadas?
b. Qual a quantidade de pessoas distribuídas pelas zonas do país (Norte, 
Centro, Sul)?
c. Dada a zona do país, determine a média de idades.
d. Dado o nome de uma pessoa, mostrar onde ela vive (nome da cidade). 
Deve mostrar todas as ocorrências do nome dado.
e. Dada uma cidade, calcular quantas pessoas lá vivem.
f. Qual a cidade com mais habitantes registados no ficheiro?
g. Determinar a quantidade de pessoas em todas as cidades e qual a 
percentagem correspondente.
h. Dado o nome de uma cidade, perguntar se para a respetiva pessoa, 
pretende mudar de cidade. Se sim, então deve substituir o nome da cidade 
registado pelo nome da nova cidade.
i. Crie um novo ficheiro com a informação que está em memória, respeitando 
o formato do csv.

"""

with open("UC00607/ficha01/clients.csv","r",encoding="utf-8") as fp:
    conteudo = fp.read()
    listaConteudo = conteudo.split("\n")

qt = len(listaConteudo)
print(f"A) O ficheiro contem o registo de {qt} clientes \n")    


qtN,qtC,qtS = 0, 0, 0


for cliente in listaConteudo:
    dados = cliente.split(";")
    if dados[-1] == "Norte":
        qtN += 1
    elif dados[-1] == "Centro":
        qtC += 1
    elif dados[-1] == "Sul":
        qtS += 1
    else:
        print(f"Dados invalidos")           
print(f"B) No Norte: {qtN} clientes,\nno Centro: {qtC} clientes,\nno Sul: {qtS} clientes. \n")        


zona = input("Qual a zona do pais que pretende calcular a media: ").title().strip()
somaIdade = 0
qt = 0

for cliente in listaConteudo:
    dados = cliente.split(";")
    if zona == dados[3]:
        somaIdade = somaIdade + int(dados[2])
        qt = qt +1

media = somaIdade / qt

print(f"C) A media de idades da {zona} e de media de  {media:.1f} anos ")


nome = input("Qual o nome do Cliente: ").title().strip()
nomeClientes = []
cidadeCliente = []


for cliente in listaConteudo:
    dados = cliente.split(";")
    if nome == dados[0]:
        print(f"O cliente {nome} habita em {dados[1]} \n")
        #nomeClientes.append(cliente)
        #cidadeCliente.append(cliente[1])
    else:
        print(f"Nome {nome} invalido ")

#print(f"Os clientes {nomeClientes} cidade: {cidadeCliente} ")

cidade = input("Digite o nome da cidade: ")
qtCidade = 0


for cliente in listaConteudo:
    dados = cliente.split(";")
    if cidade == dados[1]:
        qtCidade =+1

print(f"E) A cidade {cidade} tem {qtCidade}  habitantes \n")

