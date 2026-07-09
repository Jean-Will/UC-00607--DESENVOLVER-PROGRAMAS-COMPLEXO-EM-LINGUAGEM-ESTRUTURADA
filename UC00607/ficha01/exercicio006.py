
def juntar(nome1,nome2):

    with open (nome1,"r",encoding="utf-8") as fp:
        content = fp.read()  # le conteudo como string

    with open (nome2,"r",encoding="utf-8") as fp2:
        #content2  = fp.readline(reversed=True)   
        content2 = fp2.readlines()
        content2 = content2[::-1] # inverte a linha


    with open("final.txt","w",encoding="utf-8") as fp3:
        fp3.write(content+"\n")
        
        ultima = content2[0]
        ult_caracter = ultima[-1]
        if ult_caracter != "\n":
            ultima = ultima + "\n"
            content2[0] = ultima


        primeira = content2[-1] #e a ultima pq o conteudo esta invertido
        if primeira[-1] == "\n":
            primeira = primeira[0:len(primeira)-1]
            content2[-1] = primeira

        fp3.writelines(content2)



nome1 = "UC00607/ficha01/f1.txt"
nome2 = "UC00607/ficha01/f2.txt"
juntar(nome1,nome2)
print("O ficheiro foi guardado com sucesso! ")

