way = "UC00607/info.txt"
name = input("Insira um nome: ")
age = input("Insira a idade: ")

info = name + " "  + age 


with open(way,"a", encoding="utf-8") as fp: # W apaga e cria com os novos dados (A) faz apende e mantem os dados 
    fp.write(info)

print("Gravacao do ficheiro feita com sucesso!")     