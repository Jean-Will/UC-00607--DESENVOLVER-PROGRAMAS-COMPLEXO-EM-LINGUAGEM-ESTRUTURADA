dici ={} #dicionario vazio 

nome = input("Insira seu nome: ")
email = input("Insira seu email: ")
idade = int(input("Insira seu idade: "))
telef =  int(input("Insira seu contacto: "))

dici["nome"] = nome
dici["email"] = email
dici["idade"] = idade
dici["telefone"] = telef

print(f"{dici}")