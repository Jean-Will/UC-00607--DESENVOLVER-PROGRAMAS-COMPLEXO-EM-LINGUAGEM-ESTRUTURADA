def junta_fich(nome1,nome2):

   
    with open("UC00607/ficha01/f1.txt", "r", encoding="utf-8") as fp1:
        content = fp1.read()
        
    with open("UC00607/ficha01/f2.txt", "r", encoding="utf8") as fp2:
        content2 = fp2.read()

        final = content + "\n" + content2

        nomeFinal =  input("Qual o nome do ficheiro final? ")


    with open("UC00607/ficha01/nomeFinal.txt","w",encoding="utf8") as fpf:
        fpf.write(final)    

        print(f"Ficheiro {nomeFinal} criado com Sucesso!! ")

    return


nome1= input("Nome do Ficheiro: ")
nome2= input("Nome do Ficheiro: ")
junta_fich(nome1,nome2)
