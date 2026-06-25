""" 
Dado um ficheiro de texto e uma palavra (string) solicitada ao utilizador, indique 
quantas vezes ocorre essa palavra (string) no ficheiro.
"""

from os import listdir
lista = listdir("./UC00607/ficha01")
print(F" nome de ficheiros disponiveis: \n{lista}")

#way = "UC00607/ficha01/nomeFinal.txt"
caminho = "./UC00607/ficha01/"

nomefich = input("Qual nome do ficheiro? ")
while nomefich not in lista:
    nomefich = input("Qual nome do ficheiro? ")

caminho = caminho + nomefich
word = input("Qual palavra quer procurar? ")

with open(caminho, "r", encoding="utf-8") as filePointer:
    content = filePointer.read()

qt = content.count(word)

print(f"Essa palavra aparece {qt} x no ficheiro! " )