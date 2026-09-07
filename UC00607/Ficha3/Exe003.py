""" 
3. Conversão de listas
Tendo duas listas: nomes = ["Ana", "Bruno", "Carla"] e notas = [15, 12, 18],
construa um dicionário que associe cada nome à respetiva nota. Apresente
o dicionário.

"""
nomes = ["Ana", "Bruno", "Carla"]
notas = [15, 12, 18]
dici = {}

for pos, nome in  enumerate(nomes):
    nota = notas[pos]
    dici[nome] =  nota 
    #print(f"{dici}") para  ver o passo a passo 

print(f"{dici}\n")    