"""
4. Menu de restaurante
Crie um dicionário {"prato": preço} com pelo menos 5 itens. Peça ao
utilizador o nome de um prato e mostre o preço (ou uma mensagem caso
não exista).

"""
dici = {"Francesinha": 13.98, "Arroz doce": 4.0, "Pizzas": 16.99,"Arroz de pato":8.99,"Hamburger":7.99 }

prato = input("Qual o prato?: ")
if prato in dici:
    valor = dici[prato]
    print(f"Prato: {prato} custa: {valor:.2f}")
else:
    print("Esse prato nao existe")

