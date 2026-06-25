from time import sleep

way = "UC00607/ficha01/names.txt"
with open(way,"r",encoding="utf-8") as fp:
    content = fp.read().split("\n")

#print(f"O Conteudo do ficheiro e:\n{content}")    
for frase in content:
    #print(frase)
    info = frase.split(";")
    #print(f"{info[0:2]}")
    nome = info[0]
    idade = info[2]
    print(f"A pessoa com o nome {nome} tem a idade {idade}")
    sleep(1.5)    
    