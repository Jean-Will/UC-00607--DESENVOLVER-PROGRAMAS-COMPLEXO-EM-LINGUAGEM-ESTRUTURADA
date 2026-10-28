

nomes =[
"Ana", "Rui","Eva","Xico","Jean","Lula","To","Ze","Nela","Mito","Necas",
"Ana", "Rui","Eva","Xico","Jean","Lula","To","Ze","Nela","Mito","Necas",
"Ana", "Rui","Eva","Xico","Jean","Lula","To","Ze","Nela","Mito","Necas"]

fonte = ["Times New Roman", 16, "bold"]

from tkinter import *
from tkinter import messagebox
jan = Tk()
jan.title("ScrollBar")
jan.iconbitmap("logopy.ico")
jan.geometry("500x450")



lbox = Listbox(jan, width=30, height=15, font=fonte)
lbox.grid(row=0, column=0)

for elem in nomes:
    lbox.insert(END, elem)

sbar = Scrollbar(jan)
sbar.grid(row=0, column=1, sticky="ns")   




jan.mainloop()