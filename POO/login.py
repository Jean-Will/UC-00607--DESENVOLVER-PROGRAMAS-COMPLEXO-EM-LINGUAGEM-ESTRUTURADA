from tkinter import *

janela = Tk()
janela.title("Jean Will")
janela.geometry("600x500")


lUserName = Label(janela, text="Nome de Utilizador: ")
eusername = Entry(janela, fg="blue", bg="gray", font=("Comic Sans MS",20))

lUserName.pack()
eusername.pack()

lSenha = Label(janela, text="Password: ")
eSenha =  Entry(janela, fg="blue", bg="gray", show="*", font=("Comic Sans MS",20))

lSenha.pack()
eSenha.pack()




janela.mainloop()