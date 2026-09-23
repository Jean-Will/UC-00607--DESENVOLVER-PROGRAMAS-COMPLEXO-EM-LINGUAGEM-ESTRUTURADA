from tkinter import *
from time import strftime


def clock():
    hours = strftime("%H:%M:%S") # Letra Maiuscula da hora minuscula devolve a data
    timeLabel.configure(text=hours)
    timeLabel.after(1000,clock)


#############################################################

windows = Tk()

windows.title("Exercicio 15 ")
windows.geometry("500x350")
windows.iconbitmap("logopy.ico")

#############################################################


## Definicao de zonas da janela WINDOWS
f1 = Frame(windows)
f2 = Frame(windows)
f3 = Frame(windows)
f4 = Frame(windows)

#############################################################


f1.pack(pady=10)
nameLabel = Label(f1,text="Nome:")
entryName = Entry(f1)
nameLabel.grid(row=0, column=0)
entryName.grid(row=0, column=1)

addressLabel = Label(f1,text="Morada")
addressEntry = Entry(f1)
addressLabel.grid(row=1, column=0)
addressEntry.grid(row=1, column=1)

###############################################################



f2.pack(pady=20)
btn1Read = Button(f2, text="Ler Dados", width=10, )
btn1Read.grid( row=0,column=0,padx=3)
btn1Read.configure(bd=3)



btn2Clean = Button(f2, text="Limpar", width=10,)
btn2Clean.grid(row=0,column=1,padx=3)
btn2Clean.configure(bd=3)

btn3Exit = Button(f2, text="Sair", bg="red", fg="White", command=windows.destroy)
btn3Exit.grid(row=0, column=2,padx=3)
btn3Exit.configure(bd=3)

########################################################################################################################


f3.pack(pady=10)
dateLabe = Label(f3, text="Os dados lidos sao:")
dateLabe.grid(row=0, column=1)

dateNameLabel = Label(f3)
dateAddressLabel = Label(f3)

########################################################################################################################


f4.pack(pady=20)

timeLabel = Label(f4, text="12:00:00", font=("Arial",16, "bold"))
timeLabel.pack(side="right")

clock()






windows.mainloop()