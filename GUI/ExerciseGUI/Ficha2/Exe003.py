from tkinter import *


def ver():
    x = varS.get()
    sexo = "Feminino" if x == 1 else "Masculino"

    y = varN.get()
    nacionalidade = "Brasileiro" if y ==1 else "Portugues"
    print(f"O Sexo e: {sexo}, e a Nacionalidade e: {nacionalidade}")


w = Tk()

w.geometry("300x300")
varS = IntVar()
varN = IntVar()

r1 = Radiobutton(w, text="Feminino",   value=1, variable=varS)
r2 = Radiobutton(w, text="Masculino",  value=2, variable=varS)
r3 = Radiobutton(w, text="Brasileiro", value=1, variable=varN)
r4 = Radiobutton(w, text="Portugues",  value=2, variable=varN)

r1.pack()
r2.pack()
r3.pack()
r4.pack()

btn = Button(w, text="Ver Escolha", command=ver)
btn.pack()




w.mainloop()