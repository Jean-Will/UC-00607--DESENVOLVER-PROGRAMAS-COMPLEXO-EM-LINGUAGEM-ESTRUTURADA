#Considere a seguinte lista de cores 
# ['Preto', 'Branco', 'Azul', 'Verde', 'Vermelho', 
#'Amarelo', 'Castanho', 'Rosa', 'Laranja', 'Cinzento']
#  UC00607/Dicionarios/Ficha2/

"""['Black', 'White', 'Blue', 'Green', 'Red',
 'Yellow', 'Brown', 'Pink', 'Orange', 'Gray'] """

"""
d = {} # dicionario vazio 
lCores = ['Preto', 'Branco', 'Azul', 'Verde', 'Vermelho', 
          'Amarelo', 'Castanho', 'Rosa', 'Laranja', 'Cinzento']

for corPt in lCores:
    corIng = input(f"Qual a traducao para {corPt} ?: ")
    d[corPt] = corIng

print(d)    """ 


d = {'Preto':'Black','Branco':'White', 'Azul':'Blue', 'Verde': 'Green',
     'Vermelho': 'Red','Amarelo': 'Yellow','Castanho': 'Brown',
     'Rosa': 'Pink','Laranja': 'Orange','Cinzento': 'Gray'}

lista = []
for c,v in d.items():
    linha = c + ";" + v
    lista.append(linha)

conteudo = "\n".join(lista)    


with open("UC00607/Dicionarios/Ficha2/colour.csv", "w" , encoding="utf-8") as fp:
    fp.write(conteudo)

print(f"fciheiro Criado com sucesso!")