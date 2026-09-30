from tkinter import *
from posicao import centrar

windows = Tk()

wLarg = 300
wAlt = 100

windows.title("FRAMES")
windows.geometry(centrar(windows, wLarg, wAlt))
windows.iconbitmap("logopy.ico")

f1 = Frame(windows)
f2 = Frame(windows)

f1.pack(pady=10)

nameLabel = Label(f1, text="Utilizador:")
entryName = Entry(f1)

nameLabel.grid(row=0, column=0)
entryName.grid(row=0, column=1)

entryName.focus()

passLabel = Label(f1, text="Password")
passEntry = Entry(f1)

passLabel.grid(row=1, column=0)
passEntry.grid(row=1, column=1)

f2.pack(pady=5)

btn1Login = Button(f2, text="Login", width=10)
btn1Login.grid(row=0, column=0, padx=1)
btn1Login.configure(bd=3)

windows.mainloop()
