
from tkinter import *

#1-comece por criar uma janela 
windows = Tk()

#2- Acrescente o titulo "Primeira Janela em Tk"
windows.title("First Windows in Tk")

#3- Altere o fundo da janela para laranja 
windows["bg"] = "gray"

#4- Altere as dimensoes
windows.geometry("500x350")

#5- nao deixe redimensionar a janela
windows.resizable(False,False)

#6- defina uma variavel "fonte" 
font = ("Comic Sans Ms",14, "bold") 

#7- altere o icone da janela para um a seu gosto para ".ico"
windows.iconbitmap("logopy.ico")

#8- alter o lugar aonde a janela vai arrancar ( abri na tela ) 300+500
windows.geometry("500x350+400+50")

#9- Coloque o rotulo (label) "Ola Python"
aLabel = Label(windows, text="Hello Python") 
aLabel.grid(row=0, column=0)
#aLabel.place(x=200,y=180)

#10 -Formate o rotulo para a fonte definida anteriormente
aLabel.configure(text="Not today->", font=font, padx=5)


#11- Coloque uma caixa de texto Entry()
entryText = Entry(windows, font=font)
entryText.grid(row=0, column=2, padx=10)

#12- coloque um botao / 13- coloque um evento no botao
bExit = Button(windows,text="Sair", command=windows.destroy,font=font)
bExit.grid(row=2, column=2, columnspan=2 , sticky="we" , pady=10)

#14- mude a cor do botao 
###bExit["bg"] = "salmon"
bExit.configure(bg="salmon", fg="white", bd=3)


#Feche a janela 
windows.mainloop()