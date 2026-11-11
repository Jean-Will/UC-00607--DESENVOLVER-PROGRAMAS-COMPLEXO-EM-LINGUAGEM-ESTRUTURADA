from tkinter import *
from tkinter.ttk import Checkbutton
from funcoes import gravar
from funcoes import cancelar



def newWindowUser(windows):

    winds3 = Tk()
    winds3.title("Exemplo de Janelas 3")
    winds3.geometry("400x350")
    largura = 400
    altura = 300

    x = (winds3.winfo_screenwidth() - largura) // 2
    y = (winds3.winfo_screenheight() - altura) // 2

    winds3.geometry(f"{largura}x{altura}+{x}+{y}")

##################################################

    f1 = Frame(winds3)
    f1.pack(pady=20)

    
    userNameLabel = Label(f1,text="UserName:")
    entryName = Entry(f1)
    userNameLabel.grid(row=0, column=0)
    entryName.grid(row=0, column=1)
    entryName.focus() 

    passwordLabel = Label(f1,text="Password:")
    entryPassword = Entry(f1)
    passwordLabel.grid(row=1, column=0, pady=5)
    entryPassword.grid(row=1, column=1, pady=5)

    fullNameLabel = Label(f1,text="Full Name:")
    entryFullName = Entry(f1)
    fullNameLabel.grid(row=2, column=0, pady=5)
    entryFullName.grid(row=2, column=1, pady=5)

    addressLabel = Label(f1,text="Address:")
    entryAddress = Entry(f1)
    addressLabel.grid(row=3, column=0, pady=5)
    entryAddress.grid(row=3, column=1, pady=5)

    childrenLabel = Label(f1,text="Children:")
    spinChildren = Spinbox(f1, from_=0, to=10)
    childrenLabel.grid(row=4, column=0, pady=5)
    spinChildren.grid(row=4, column=1, pady=5)

    sexoLabel = Label(f1,text="Sexo:")
    cheMasculino = Checkbutton(f1, text="Masculino")
    cheFeminino = Checkbutton(f1, text="Feminino")       
    sexoLabel.grid(row=5, column=0, pady=5)
    cheMasculino.grid(row=5, column=1, pady=5)
    cheFeminino.grid(row=5, column=2, pady=5)

    favoriteColorLabel = Label(f1,text="Favorite Color:")
    favoriteColorLabel.grid(row=6, column=0, pady=5)

    redVar = BooleanVar()
    cheRed = Checkbutton(f1, text="Red", variable=redVar)
    cheRed.grid(row=6, column=1, pady=5)

    blueVar = BooleanVar()
    cheBlue = Checkbutton(f1, text="Blue", variable=blueVar)
    cheBlue.grid(row=6, column=2, pady=5)

    greenVar = BooleanVar()
    cheGreen = Checkbutton(f1, text="Green", variable=greenVar)
    cheGreen.grid(row=6, column=3, pady=5)

 

    ####################################################################

    f2 = Frame(winds3)
    f2.pack()

    btnSave = Button(f2, text="Guardar", width=10, command=gravar)
    btnSave.grid( row=9,column=0,padx=10)

    btnCancel = Button(f2, text="Cancelar", width=10, command=lambda: cancelar())
    btnCancel.grid(row=9,column=1)


    winds3.mainloop()