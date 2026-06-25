way = "UC00607/ficha01/nomeCompleto.txt"

name = input("Digite seu nome completo: ")

with open (way,'w',encoding="utf-8") as filePointer:
    filePointer.writelines(name)

print("Nome Gravado com suceso!! ")