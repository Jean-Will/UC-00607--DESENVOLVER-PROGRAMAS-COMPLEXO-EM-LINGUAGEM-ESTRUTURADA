"""
Desenvolva um programa que substitua uma palavra (string) por outra num 
ficheiro. As palavras e o nome do ficheiro deverão ser dados pelo utilizador.
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
word = input("Qual palavra quer trocar? ")
newWord = input("Insira a palavra que quer substituir: ")

with open(caminho, "r", encoding="utf-8") as filePointer:
    content = filePointer.read()

rp = content.replace(word, newWord)

with open(caminho, "w" , encoding="utf-8") as fp:
    fp.write(rp)

print(f"A palavra foi substituida com sucesso: \n{rp} ")