from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo, showerror




paises = sorted(["Congo", "Brasil", "Canada", "Portugal","Italia"])


def ler():
    pais = cb.get()
    if pais == "Escolha o Pais:":
        showerror(title="Erro", message="Tem que selecionar um Pais na lista")
    else:    
        showinfo("Selecao", message=f"O pais selecionado foi: {pais}")


windows = Tk()
windows.geometry("500x350")
windows.iconbitmap("logopy.ico")


cb = Combobox(windows, values=paises, state="readonly", justify="center")
posicao = paises.index("Portugal")
#cb.set(paises[posicao])
cb.set("Escolha o Pais:")
cb.pack()


btn = Button(windows, text="Ler", command=ler)
btn.pack()




windows.mainloop()