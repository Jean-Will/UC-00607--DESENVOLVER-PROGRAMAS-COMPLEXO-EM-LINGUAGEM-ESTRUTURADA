"""
O programa deve:

Abrir e ler o ficheiro.

Percorrer as linhas do ficheiro.

Separar os dados de cada aluno.

Calcular a média das duas notas de cada aluno.

Mostrar o nome e a média de cada aluno, arredondada a uma casa decimal.

"""

way = "Revisao/notas.csv"

with open(way,"r",encoding="utf-8") as fp:
    conteudo = fp.read().split("\n")

for linha in conteudo:
    info = linha.split(";")
    nome = info[0]
    nota1 = int(info[1])
    nota2 = int(info[2])
    nota3 = int(info[3])
    disciFavo = info[4]
    media = ( nota1 + nota2 + nota3 / (len(info) -2))
    media = round(media,1)
    print(f"{nome} - media: {media:.1f}")

for linha in conteudo:
    info = linha.split(";")
    nome = info[0]
    notas = [int(info[1]),int(info[2]), int(info[3])]
    maximo = max(notas)
    minimo = min(notas) 
    print(f"{nome} tem a maxima: {maximo} e minimo: {minimo}")

d ={}   

for linha in conteudo:
    info = linha.split(";")
    disciplina = info[4]
    if disciplina not in d:
        d[disciplina] = info[4]
    else:
        d[disciplina] +=1
    print(f"Qtds favoritas {d}")        