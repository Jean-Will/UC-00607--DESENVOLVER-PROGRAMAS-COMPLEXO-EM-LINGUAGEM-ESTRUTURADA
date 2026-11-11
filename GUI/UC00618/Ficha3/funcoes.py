from tkinter.messagebox import showinfo, showerror

from WinLogin import *
from WinDados import *
from WinNewUser import *

def gravar(WinNewUser):

    user = WinNewUser.entryName.get()
    password = WinNewUser.entryPassword.get()
    full_name = WinNewUser.entryFullName.get()
    address = WinNewUser.entryAddress.get()
    children = WinNewUser.spinChildren.get()
    #sexo = WinNewUser.sexo.get()
    cores = []
    if WinNewUser.redVar.get():
        cores.append("Red")
    if WinNewUser.blueVar.get():
        cores.append("Blue")
    if WinNewUser.greenVar.get():
        cores.append("Green")

    colorFAvorite = ":".join(cores)    
    line = f"{user},{password},{full_name},{address},{children},{sexo},{colorFAvorite}\n"

    if user not in userDic:
        with open(way, "a", encoding="utf-8") as fp:
            cont = fp.read()
            if len(cont) != 0:
                fp.write("\n" + line)
            else:
                fp.write(line)
            showinfo("Gravar", "Dados gravados com sucesso!")   
    else:
        showerror("Erro", "Nome de usuário já existe. Por favor, escolha outro nome de usuário.")
        



def cancelar(winds3):
    winds3.destroy()

    