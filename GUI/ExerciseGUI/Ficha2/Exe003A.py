from tkinter import *


"""def ver():
    x = varS.get()
    sexo = "Feminino" if x == 1 else "Masculino"

    y = varN.get()
    nacionalidade = "Brasileiro" if y ==1 else "Portugues"
    print(f"O Sexo e: {sexo}, e a Nacionalidade e: {nacionalidade}")
"""

w = Tk()

w.geometry("300x300")
varS = IntVar()
varN = IntVar()

zona = LabelFrame(w, text="Escolha o Sexo...")
zona.pack(expand=True, fill=BOTH, padx=50,pady=50)

r1 = Radiobutton(zona, text="Feminino",   value=1, variable=varS)
r2 = Radiobutton(zona, text="Masculino",  value=2, variable=varS)
r3 = Radiobutton(zona, text="NS/NR",      value=3, variable=varS)


r1.pack(anchor="w")
r2.pack(anchor="w")
r3.pack(anchor="w")






w.mainloop()