
nome = "Jean Will"
formador = "Julio Magalhaes"
curso = "CET-35"

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
    lista_nomes = []
    for funcionario in dici.values():
        lista_nomes.append(funcionario["nome"])
    return lista_nomes


# Criado para testar
way = "Revisao/info.csv"
with open(way, "r", encoding="utf-8") as fp:
    dici = funcionarios(fp)

print(dici)
print(nomes(dici))

if dici:
    total_salarios = 0
    for funcionario in dici.values():
        total_salarios += funcionario["salario"]

    media_salarios = total_salarios / len(dici)
    print(f"Média dos salários: {media_salarios:.2f}")
else:
    print("Não existem funcionários para calcular a média.")