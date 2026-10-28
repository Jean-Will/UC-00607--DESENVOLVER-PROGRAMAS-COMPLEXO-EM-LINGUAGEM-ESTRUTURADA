from tkinter import *
fonte = ("Arial",16)

way = "GUI/UC00618/textExemplo.md"
def ler():
    with open(way,"r",encoding="utf-8") as fp:
        conteudo = fp.read()
    tarea.delete(1.0,END)    
    tarea.insert(1.0,conteudo)    


def gravar():
    conteudo = tarea.get(1.0, END)
    with open(way,"w",encoding="utf-8") as fp:
        fp.write(conteudo)




jan = Tk()
jan.title("Text")
jan.iconbitmap("logopy.ico")
jan.geometry("700x550")
tarea = Text(jan, width=50, height=27, bg="grey",wrap="word")
tarea.grid(row=0, column=0, padx=20,pady=20, )

scroll = Scrollbar(jan, orient="vertical",command=tarea.yview)
scroll.grid(row=0,column=1,sticky="ns")

tarea.configure(yscrollcommand=scroll.set)

bler =    Button(jan,     text="Carregar",    command=ler,      font=fonte)
bgravar = Button(jan,     text="Gravar",      command=gravar,   font=fonte)
bler.grid(row=1,column=0)
bgravar.grid(row=1,column=1)

nomes = ["Ana","Rui", "Ze"]
sbox = Spinbox(jan,values=nomes, font=fonte, wrap=True)
sbox.grid(row=2, column=0)

jan.mainloop()