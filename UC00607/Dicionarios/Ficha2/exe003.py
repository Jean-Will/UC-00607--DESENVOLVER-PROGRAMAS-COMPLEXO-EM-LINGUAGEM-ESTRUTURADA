"""
23456789;Ana;Lisboa;22;Centro 
987654321;Pedro;Porto;45;Norte 
192837465;Isabel;Coimbra;22;Centro 
564738291;Ana;Chaves;33;Norte 
837465192;José;Beja;45;Sul 
748392615;Francisco;Bragança;19;Norte 
615294837;Pedro;Faro;23;Sul 
294837156;José;Covilhã;56;Centro 
483920176;Marta;Bragança;28;Norte
572940183;Luís;Aveiro;39;Centro
620481739;Carla;Setúbal;31;Sul 
918273645;Rui;Évora;47;Sul 
736291840;Sofia;Viseu;26;Centro 
840192736;Bruno;Guimarães;34;Norte 
369258147;Helena;Évora;52;Sul 
501928374;Tiago;Coimbra;29;Centro 
210394857;Patrícia;Bragança;41;Norte 
475839102;André;Santarém;38;Centro
"""


way ="UC00607/Dicionarios/Ficha2/clientes.csv"
with open(way, "r" , encoding="utf-8") as fp:
   conteudo =  fp.read().split("\n")

dici= {}
lista = []
for linha in conteudo:
   dados = linha.split(";")
   nifCliente = dados[0]
   dici[nifCliente] = dados[1:]

   #nomeCliente = dados[1]
   #cidadeCliente = dados[2]
   #idadeCliente = dados[3]
   #zonaCliente = dados[4]
#for c , v in dici.items():
   #linha = c + ";" + v[0] + ";" + ";" + v[1] + ";" + v[2] + ";" + v[3] + ";" + v[4]
   #lista.append(linha) 
print(f">>>>>> Exercicio Linha (A) <<<<<<<<< \n")
print(f"Linha A-) {dici}\n") 
print(f">>>>>> Exercicio Linha (B) <<<<<<<<< \n")
print(f" Linda B-) Foram importados {len(dici)} registos de clientes\n")

print(f">>>>>> Exercicio Linha (C) <<<<<<<<< \n")
qtd = 0
for dados in dici.values():
   idade = int(dados[2]) # converte a string para inteiro
   if idade > 40:
      qtd +=1
      print(f"Linha C-) {dados[0]}, tem {idade} anos e mora em {dados[1]}, zona {dados[3]}\n")

print(f"Total de pessoa > 40 = {qtd}\n")

print(f">>>>>> Exercicio Linha (D) <<<<<<<<< \n")

zonas = ['Norte','Centro','Sul']
dzonas = dict.fromkeys(zonas,0) # dzonas = {"Norte" :0, "Centro" :0, "Sul" :0}

for dados in dici.values():
   zona = dados[3].strip()
   dzonas[zona] = dzonas[zona] +1  #Esta dando erro nessa linha !!

print(f"{dzonas}")   

print(f">>>>>> Exercicio Linha (E) <<<<<<<<< \n")

soma = 0
for dados in dici.values():
   idade = int(dados[2])
   soma = soma + idade

media = round(soma / len(dici), 1)
print(f"A media de idades e de {media} anos!! \n")
