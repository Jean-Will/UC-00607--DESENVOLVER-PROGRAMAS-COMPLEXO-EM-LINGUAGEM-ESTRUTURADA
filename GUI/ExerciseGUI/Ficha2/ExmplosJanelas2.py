from tkinter import *

def nova():
    
    winds2 = Tk()
    winds2.title("Exemplo de Janelas 2")
    winds2.geometry("500x350")
    winds2["bg"] = "lightgreen"
    btnExit = Button(winds2, text="Sair", command=winds2.destroy, width=30)
    btnExit.pack(expand=True)

    

    winds2.mainloop(winds.destroy())

######################################################################################



winds = Tk()
winds.title("Exemplo de Janelas 1")
winds.geometry("500x350")
winds["bg"] = "lightblue"

btn = Button(winds, text="Janela 2", command=nova, width=30)
btn.pack(expand=True)

winds.mainloop()