
nome = "Jean Will"
formador = "Julio Magalhaes"
curso = "CET-35"

dici = {}
novoDici = {}

def funcionarios(conteudo):
    dici = {}
    for linha in conteudo:
        linha = linha.strip()
        if linha:
            cod, nome, salario, profissao = linha.split(";")
            dici[cod] = {
                "nome": nome.strip(),
                "salario": float(salario),
                "profissao": profissao.strip()
            }
    return dici


def nomes(dici):
    nomesLista = []
    for funcionario in dici.values():
        nomesLista.append(funcionario["nome"])
    return nomesLista


def mairSalario(dici):
    maiorSalario = 0
    funcionarioMaiorSalario = None
    for funcionario in dici.values():
        if funcionario["salario"] > maiorSalario:
            maiorSalario = funcionario["salario"]
            funcionarioMaiorSalario = funcionario
    return funcionarioMaiorSalario


def quantidades(dici):
    novoDici = {}
    for funcionario in dici.values():
        profissao = funcionario["profissao"]
        if profissao in novoDici:
            novoDici[profissao] += 1
        else:
            novoDici[profissao] = 1
    return novoDici


# Criado para testar O CSV
way = "Revisao/info.csv"  
with open(way, "r", encoding="utf-8") as fp:
    conteudo = fp.read().split("\n")
#Caminho original do TESTE
 #with open("C:/teste/info.csv","r",encoding="utf-8") as fp:
    #conteudo = fp.read().split("\n")


for linha in conteudo:
    info = linha.split(";")  
    
    cod = info[0]
    nome = info[1]
    salario = info[2]
    profissao = info[3]
    print(linha)

#print(f"{conteudo} ") 
fun = dici
print("### Funcao abaixo")
print(f"{dici} + {fun} + {cod} ")

# fazer a media dos salarios
media = 0
for salario in dici.values():
    info = salario.split(";")
    sal = float(info[2])
    salTotal += sal
    media = salTotal / len(dici)


print(f"Média dos salários: {media:.2f}")    
print(f"nomes: {nomes(dici)}")
print(f"quantidades: {quantidades(dici)}")
print(f"Funcionário com maior salário: {mairSalario(dici)['nome']}")