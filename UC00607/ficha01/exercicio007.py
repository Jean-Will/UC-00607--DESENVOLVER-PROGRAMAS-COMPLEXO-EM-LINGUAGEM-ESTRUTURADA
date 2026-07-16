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
    #else:
        #print(f"Nome {nome} invalido ")

#print(f"Os clientes {nomeClientes} cidade: {cidadeCliente} ")

cidade = input("Digite o nome da cidade: ").title().strip()
qtCidade = 0


for cliente in listaConteudo:
    dados = cliente.split(";")
    if cidade == dados[1]:
        qtCidade =+1

print(f"E) A cidade {cidade} tem {qtCidade}  habitantes \n")


cidades =[]
maximo = 0
nomeMaximo = ""


for linha in listaConteudo:
    dados = linha.split(";")
    cidades.append(dados[1])

cidadesSemRepetir = list(set(cidades))    

for cid in cidadesSemRepetir:
    cidades.append(dados[1])
    qt = cidades.count(cid)
    if qt > maximo:
        maximo = qt
        nomeMaximo = cid

print(f" F) A cidade  com mais habitante e: {nomeMaximo} com o total de {maximo} de habitantes \n")        

################

cidades =[]

for linha in listaConteudo:
    dados = linha.split(";")
    cidades.append(dados[1])

cidadesSemRepetir = list(set(cidades))    

for cid in cidadesSemRepetir:
    qt = cidades.count(cid)
    total = len(listaConteudo)
    porcentagem = qt * 100 / total

    print(f" G){cid}: {qt}: {porcentagem:.1f}% ")        

#################################### alterar o campo e voltar a refazer com os novos dados 

city = input("Digite o nome da cidade: ").title().strip()
for pos, linha in enumerate(listaConteudo):
    dados = linha.split(";")
    if dados[1] == city:
        op = input(f"Deseja mudar o user: {dados[0]}? (s/n) ").lower().strip()
        if op[0] == 's':
            newCity = input(f"Para qual nova cidade ira o user {dados[0]}? ").title().strip()
            dados[1] = newCity
            newLine = ";".join(dados)
            listaConteudo[pos] = newLine

print(f"H) {listaConteudo}")            
#########################################

print(" I)")
newCont = "\n".join(listaConteudo)
with open ("UC00607/ficha01/clients.csv","w",encoding="utf-8") as fp:
    fp.write(newCont)
print(f"Dados gravados no ficheiro com sucesso!!!")

