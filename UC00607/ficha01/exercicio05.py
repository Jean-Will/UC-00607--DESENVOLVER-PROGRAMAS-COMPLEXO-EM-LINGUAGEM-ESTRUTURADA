from time import sleep

''' 
a. Faça um programa que leia o ficheiro anterior e devolva quantas linhas, 
palavras, vogais e consoantes contém esse ficheiro.
b. Solicite uma palavra ao utilizador e informe-o de quantas vezes essa 
palavra ocorre no ficheiro e em que nº da linha.


'''

way = "UC00607/ficha01/pensamentos.txt"
with open(way,"r",encoding="utf-8") as fp:
    content = fp.read()

content2 = content.split("\n") # Cria a lista de linhas
qtLinhas = len(content2) 
print(f"o ficheiro tem {qtLinhas} linhas\n")

#qtPalavras = content.count(" ") + 1 + content.count("\n")
qtPalavras = len(content.split())  
print(f"O ficheiro contem {qtPalavras} Palavras\n")    

vogais= "AaÁáÀàÃãÂâEeÉéÊêIiÍíOoÓóÔôÕõUuÚú"
qtdConsoante, qtVogais = 0,0
for simbolo in content:
    if simbolo.lower() in vogais:
        qtVogais += 1
    elif "a" < simbolo.lower() <= "z" or simbolo.lower() == "ç":
        qtdConsoante += 1
print(f"O ficheiro contem {qtVogais} de vogais e {qtdConsoante} de consoantes\n")        


palavraUtilizador = input("Buscar palavra: ").lower()

#qtPalavraUtilizador = content.lower().count(palavraUtilizador) 
#print(f"A palavra que voce escreveu aparece {qtPalavraUtilizador} X ")

qtPalavraNaLinha= 0
posicaoLinha = []
for pos ,linha in enumerate(content2):
    x = linha.lower().count(palavraUtilizador)
    if x > 0 :
        posicaoLinha.append(pos +1)
        qtPalavraNaLinha += x

print(f"A palavra que voce escreveu aparece {qtPalavraNaLinha} X na(s) linha(s) {posicaoLinha} ")


