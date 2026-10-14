


# Importa o ficheiro notas.csv
way = "Revisao/notas.csv" 
with open(way,"r",encoding="utf-8") as fp:
    conteudo = fp.read().split("\n")
# Determinar a media de cada Aluno 
for linha in conteudo:
    info = linha.split(";")
    nome =     info[0]
    nota1 =    int(info[1])
    nota2 =    int(info[2])
    nota3 =    int(info[3])
    favorita = info[4]
    media = (nota1 + nota2 + nota3) / (len(info) -2) # ou de forma estatica /3 pq sei a quantidade de notas
    media = round(media,1)
    print(f"\n{nome} Obteve media final de: {media:.1f}")

# Nota mais alta e mais baixa de cada Aluno
for linha in conteudo:
    info = linha.split(";")
    nome = info[0]
    notas = [int(info[1])], [int(info[2])], [int(info[3])]
    maximo = max(notas)
    minimo = min(notas)
    print(f"O {nome} tem a nota maxima:{maximo} e a minima: {minimo}")

# Disciplina + Favorita e - favorita dos alunos
# percentual de alunos que gostam de cada disciplina 
# Quem Reprovou e quem Passou