


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
    notas = [int(info[1]), int(info[2]), int(info[3])] #LISTA DE NOTAS
    maximo = max(notas)
    minimo = min(notas)
    print(f"\nO {nome} tem a nota maxima:{maximo} e a minima: {minimo}")

# Disciplina + Favorita e - favorita dos alunos
d = {}
for linha in conteudo:
    info = linha.split(";")
    disciplina = info[4]
    if disciplina not in d:
        d[disciplina] = info[4]
    else:
        d[disciplina] +=1
print(f"Qtds favoritas: \n{d}")

maiorqt = max(d.values())
menorqt = min(d.values())
maisfavo = ""
menosfavo = ""

for disciplina, valor in d.items():
    if valor == maiorqt:
        maisfavo = disciplina
    if valor == menorqt:
        menosfavo = disciplina      
print(f"Favorita: {maisfavo}:{maiorqt}")
print(f"Menos Favorita: {menosfavo}:{menorqt} \n")        

# percentual de alunos que gostam de cada disciplina 
total = len(conteudo)
for nome, qtd in d.items():
    x = qtd * 100 / total
    print (f"{nome} - {qtd} corresponde a {x:.1f} %\n")    

# Quem Reprovou e quem Passou

for linha in conteudo:
    info = linha.split(";")
    nome = info[0]
    #media = sum( map(int,[info[1], info[2], info[3]] ) ) /3
    media = (int(info[1]) + int(info[2]) + int(info[3]) /3)
    if media < 10:
        classificacao = "! Reprovado !"
    else:
        classificacao = "Aprovado"    

    print(f"Nome: {nome}  media:{media:.1f} Classificacao: {classificacao} ")        