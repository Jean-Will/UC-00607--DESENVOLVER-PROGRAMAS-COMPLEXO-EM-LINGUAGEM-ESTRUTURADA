
"""2. Contador de palavras
Dada uma frase, conte quantas vezes cada palavra aparece e guarde o
resultado num dicionário {palavra: contagem}. Apresente o dicionário."""

frase = "As ferias foram poucas . As aulas foram esquecidas ."
dici = {}
lst = frase.split()


for palavra in lst:
    if palavra in dici:
        dici[palavra] = dici[palavra] +1
    else:
        dici[palavra] = 1

print(dici)