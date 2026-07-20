ficheiroAnterior = "UC00607/Dicionarios/Ficha2/colour.csv"

"""
2. A partir do ficheiro criado no exercício anterior, carregue o dicionário para 
memória. Altere o dicionário por forma a acrescentar as cores em francês. Assim, 
o seu dicionário obteria as traduções de português para inglês e francês.
Espera-se obter o dicionário {Preto: (Black, Noir), Branco: (White, Blanc), Azul: 
(Blue, Bleu), Verde: (Green, Vert), Vermelho: (Red, Rouge), Amarelo: (Yellow, 
Jaune), Castanho: (Brown, Marron), Rosa: (Pink, Rose), Laranja: (Orange, 
Orange), Cinzento: (Gray, Gris)}
Guarde num ficheiro os elementos do dicionário (estrutura: corPT;corING:corFR)

{'Preto': ('Black', 'Noir'), 'Branco': ('White', 'Blanc'),
'Azul': ('Blue', 'Bleu'), 'Verde': ('Green', 'Vert'), 'Vermelho': ('Red', 'Rouge'),
'Amarelo': ('Yellow', 'Jeune'), 'Castanho': ('Brown', 'Marron'),
'Rosa': ('Pink', 'Rose'), 'Laranja': ('Orange', 'Oranje'), 'Cinzento': ('Gray', 'Gris')}

"""
"""

with open(ficheiroAnterior , "r", encoding='utf-8') as fp:
    conteudo = fp.read().split("\n")

d = {}
for linha in conteudo:
    dados = linha.split(";")
    corPt = dados[0]
    corIng = dados[1]
    corFr = input(f"Qual a cor em Frances para {corPt} ?: ").strip().title()
    d[corPt] = (corIng, corFr)

print(d)   """



d = {'Preto': ('Black', 'Noir'), 'Branco': ('White', 'Blanc'), 'Azul': ('Blue', 'Bleu'),
     'Verde': ('Green', 'Vert'), 'Vermelho': ('Red', 'Rouge'), 'Amarelo': ('Yellow', 'Jeune'), 
     'Castanho': ('Brown', 'Marron'), 'Rosa': ('Pink', 'Rose'), 
     'Laranja': ('Orange', 'Oranje'), 'Cinzento': ('Gray', 'Gris')}

lista = []
for c,v in d.items():
    linha = c + ";" + v[0] + ";" + v[1]
    lista.append(linha)

conteudo = "\n".join(lista)    
    

with open(ficheiroAnterior, 'w', encoding='utf-8') as fp:
    fp.write(conteudo)

print(f"Dados no ficheiro atualizados com sucesso !!")    