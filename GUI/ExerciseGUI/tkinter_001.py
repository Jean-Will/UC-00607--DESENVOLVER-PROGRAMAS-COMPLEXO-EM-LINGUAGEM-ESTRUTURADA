
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





#Feche a janela 
windows.mainloop()