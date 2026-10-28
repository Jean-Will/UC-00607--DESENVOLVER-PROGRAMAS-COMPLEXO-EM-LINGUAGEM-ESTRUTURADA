

nomes =[
"Ana", "Rui","Eva","Xico","Jean","Lula","To","Ze","Nela","Mito","Necas",
"Ana", "Rui","Eva","Xico","Jean","Lula","To","Ze","Nela","Mito","Necas",
"Ana", "Rui","Eva","Xico","Jean","Lula","To","Ze","Nela","Mito","Necas"]

fonte = ["Times New Roman", 16, "bold"]

def apagar():
    indsel = lbox.curselection()
    indsel = indsel[::-1]
    if len(indsel) > 0:
        for elem in indsel:
            lbox.delete(elem)
    else:
        messagebox.showwarning("Aviso", "Selecione um elemento para apagar")



from tkinter import *
from tkinter import messagebox
jan = Tk()
jan.title("ScrollBar")
jan.iconbitmap("logopy.ico")
jan.geometry("500x450")



lbox = Listbox(jan, width=30, height=15, font=fonte,
               selectmode="extended")
lbox.grid(row=0, column=0)

for elem in nomes:
    lbox.insert(END, elem)

sbar = Scrollbar(jan, command=lbox.yview)
sbar.grid(row=0, column=1, sticky="ns")   

# Fixar o botao da scroll a zona da list box
lbox.configure(yscrollcommand=sbar.set)

bdel = Button(jan, text="Apagar",font="Arial", bd=4,bg="Pink", activebackground="Blue",command= apagar)
bdel.grid(row=1, column=0)


jan.mainloop()