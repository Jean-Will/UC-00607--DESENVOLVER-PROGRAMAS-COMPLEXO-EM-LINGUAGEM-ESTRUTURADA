#ler o conteudo do ficheiro "name.txt"
#indicar quantos nomes estao registado

way = "UC00607/names.txt"

with open(way,"r", encoding="utf-8") as fp: # W apaga e cria com os novos dados (A) faz apende e mantem os dados 
    content = fp.read().split("\n")
    qt = len(content)


print(qt)