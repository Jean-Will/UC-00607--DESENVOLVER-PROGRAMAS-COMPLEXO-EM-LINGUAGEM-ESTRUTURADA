from tkinter import *
from tkinter.ttk import Treeview

win = Tk()
win.geometry("700x500")

tree = Treeview(win, columns=("Nome","Idade","Pais"),show="headings")
tree.pack()

tree.heading("Nome",text="Full Name")
tree.heading("Idade",text="Age")
tree.heading("Pais", text="Country")

# inserir valores 

tree.insert("", END, values=("Ana","20","Mocambique"))
tree.insert("", END, values=("Anabela","10","Portugal"))
tree.insert("", END, values=("Thaysa","50","Brasil"))





win.mainloop()