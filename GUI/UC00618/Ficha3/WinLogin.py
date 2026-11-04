from tkinter import *
from tkinter import messagebox
from WinDados import newWindow
from WinNewUser import newWindowUser


def login():
    username = entryName.get()
    password = entryPassword.get()

    userDic = {}

    with open(way, "r", encoding="utf-8") as fp:


        for line in fp:
            dados = line.strip().split(",")

            if len(dados) == 7:
                userDic[dados[0]] = {
                    "password": dados[1],
                    "nome": dados[2],
                    "localidade": dados[3],
                    "idade": dados[4],
                    "sexo": dados[5],
                    "cores": dados[6]
                }

    if username in userDic and userDic[username]["password"] == password:
        print("Login bem-sucedido!")
        messagebox.showinfo("Login", "Login bem-sucedido!")
        newWindow()
        return

    messagebox.showerror("Login", "Nome de usuário ou senha incorretos.")




    
 

#######################################

way = "GUI/UC00618/pass.csv"

windows = Tk()
windows.title(" -- Login -- ")
windows.iconbitmap("logopy.ico")
windows.geometry("400x300")
largura = 400
altura = 300

x = (windows.winfo_screenwidth() - largura) // 2
y = (windows.winfo_screenheight() - altura) // 2

windows.geometry(f"{largura}x{altura}+{x}+{y}")



######################################

f1 = Frame(windows)
f2 = Frame(windows)

#######################################

f1.pack(pady=10)

userNameLabel = Label(f1,text="UserName:")
entryName = Entry(f1)
userNameLabel.grid(row=0, column=0)
entryName.grid(row=0, column=1)
entryName.focus() 

passwordLabel = Label(f1,text="Password:")
entryPassword = Entry(f1)
passwordLabel.grid(row=1, column=0, pady=5)
entryPassword.grid(row=1, column=1, pady=5)

##################################################

f2.pack(pady=20)

btnLogin = Button(f2, text="Login", width=10, command=login)
btnLogin.grid( row=0,column=0,padx=3)

btnNewUser = Button(f2, text="Novo User", width=10, command=newWindowUser)
btnNewUser.grid(row=0,column=1,padx=3)

btnExit = Button(f2, text="Sair", bg="red", fg="White",width=10 ,command=windows.destroy)
btnExit.grid(row=0, column=2,padx=3)

windows.mainloop()