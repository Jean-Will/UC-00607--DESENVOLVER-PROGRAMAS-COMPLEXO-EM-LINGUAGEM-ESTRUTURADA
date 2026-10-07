from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo, showerror
from time import sleep



cidades = ["Porto","Recife","Ji-Parana","Gondomar"]

def carregar():

    for cid in cidades:
        sleep(0.3)
        lst.insert(END, cid)
        

        """showerror(title="Error",message="Tem que selecionar um nome na lista")
    else:
        showinfo("Selecao", message=f"A cidade selecionado e: {cid}")"""


def eliminar():
    x = lst.curselection()
    if len(x) != 0:
        pos = x[0]
        lst.delete(pos)   



winds = Tk()
winds.geometry("500x350")
winds.iconbitmap("logopy.ico")

lst = Listbox(winds,width=50,height=20)
lst.pack()

btnCarregar = Button(winds, text="Carregar", command=carregar)
btnCarregar.pack()

btnLimpar = Button(winds, text="Eliminar", command=eliminar)
btnLimpar.pack()



winds.mainloop()