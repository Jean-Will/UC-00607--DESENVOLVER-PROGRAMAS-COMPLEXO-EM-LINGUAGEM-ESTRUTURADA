from tkinter import *

def ver():
    gosto = []
    if marca1.get():
        gosto.append(r1["text"])
    if marca2.get():
        gosto.append(r2["text"])    
    if marca3.get():
        gosto.append(r3["text"])
    print(gosto)    

w = Tk()

w.geometry("300x300")
marca1 = IntVar()
marca2 = IntVar()
marca3 = IntVar()

zona = LabelFrame(w, text="Escolha as Marcas Favoritas")
zona.pack(expand=True, fill=BOTH, padx=50,pady=50)

r1 = Checkbutton(zona, text="BMW",              variable=marca1)
r2 = Checkbutton(zona, text="Mercedez Benz",    variable=marca2)
r3 = Checkbutton(zona, text="VolksWagen",       variable=marca3)


r1.pack(anchor="w")
r2.pack(anchor="w")
r3.pack(anchor="w")

btn = Button(zona, text="Verificar" , command=ver)
btn.pack()



w.mainloop()