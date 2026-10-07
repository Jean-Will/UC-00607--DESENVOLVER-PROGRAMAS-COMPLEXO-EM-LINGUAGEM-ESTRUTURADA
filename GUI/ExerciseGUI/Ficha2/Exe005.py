from tkinter import *
from tkinter.ttk import Combobox 
from tkinter.messagebox import showinfo, showerror



def ler():
    fruta = cb.get()
    if fruta == "Escolha a Fruta":
        showerror(title="Erro", message="Tem que selecionar uma Fruta na lista")
    else:    
        showinfo("Selecao", message=f"A fruta selecionado foi: {fruta}")

winds = Tk()

frutas = ["Banana","Maca","Uva","Pera","Melao","Laranja"]

winds.geometry("500x350")
winds.iconbitmap("logopy.ico")

cb = Combobox(winds, values=frutas, state="readonly", justify="center")
cb.set("Escolha a Fruta")
cb.pack()

btn = Button(winds,text="Fruta",command=ler)
btn.pack()

winds.mainloop()