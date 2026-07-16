class Pessoa:
    def __init__(self,nome, idade, morada):
        self.nome = nome
        self.idade = idade
        self.morada = morada


x = Pessoa("Ana", 20, "Porto")        
        
print(x.nome)        