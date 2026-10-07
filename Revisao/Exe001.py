
# 1- Qual o comando para abrir um ficheiro em modo de leitura ?
way = "./UC00607/testeInfo.csv"
with open(way,"r", encoding="utf-8") as fp:
# 2- ler as linhas do ficheiro :
    conteudo = fp.read().split("\n")


    # Essa Cai no TESTE

dici = {}
for linha in conteudo:
    info = linha.split(";")
    cod = info[0]
    nome = info[1]
    salario = info[2]
    prof = info[3]
    dici[cod] = [nome , salario, prof]
print(dici)    

sMaior = 0
nomeProf = ""

for lista in dici.values():
    salario = float(lista[1])
    if salario > sMaior:
        sMaior = salario
        nomeProf = lista[2]
print(f"Maior salario e: {sMaior:.2f} a profissao: {nomeProf}")        


def nomes(dici):
    for lista in dici.values():
        nome = lista[0]
        print(nome)

def quantidades(dici):
    novoDici = {}
    for lista in dici.values():
        profissao = lista [2]
        if profissao not in novoDici:
            novoDici[profissao] = 1
        else:
            novoDici[profissao] +=1
    return novoDici

print (quantidades)
