
from tkinter import *

def newWindow():
    winds2 = Tk()
    winds2.title("Dados do Utilizador")
    winds2.iconbitmap("logopy.ico")
    winds2.geometry("400x300")
    largura = 400
    altura = 300

    x = (winds2.winfo_screenwidth() - largura) // 2
    y = (winds2.winfo_screenheight() - altura) // 2

    winds2.geometry(f"{largura}x{altura}+{x}+{y}")



    


    winds2.mainloop()