#pedir 5 nomes completos ao user
# gravar esses 5 nomes num ficheiro "names.txt"

way = "UC00607/names.txt"
names = []

for x in range(1,4):
    name = input(f"Insira {x} nomes: ")
    names.append(name + "\n")



with open(way,"a", encoding="utf-8") as fp: # W apaga e cria com os novos dados (A) faz apende e mantem os dados 
    fp.writelines(names)

print("Gravacao do ficheiro feita com sucesso!")        