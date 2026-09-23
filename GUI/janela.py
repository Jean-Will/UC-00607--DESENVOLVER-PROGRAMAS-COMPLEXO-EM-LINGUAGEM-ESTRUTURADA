from tkinter import *

fonte1 = ("Comic Sans MS", 14)
fonte2 = ("Arial", 16, "bold")

janela = Tk()
janela.title("ESPECIALISTA")
janela.geometry("500x350")
janela.resizable(False,False)

b1 = Button(janela, text="Sair", font=fonte1, width=5, bg="salmon",fg="white", command=janela.destroy)
#b1.place(x=400,y=250)
#b1.grid
b1.pack(side="right", anchor=SE)


janela.mainloop()
