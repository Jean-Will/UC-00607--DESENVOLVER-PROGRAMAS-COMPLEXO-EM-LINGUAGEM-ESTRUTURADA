from tkinter import *

fonte = ("Arial", 18, "bold")

winds = Tk()
winds.title("Exercicio 8")
winds.geometry("500x250")

def mix(value):
    red = int(esc1.get())
    green = int(esc2.get())
    blue = int(esc3.get())
    color = f"#{red:02x}{green:02x}{blue:02x}"
    labColor.config(bg=color)
    labMostra.config(text=color)
    




esc1 = Scale(winds,orient="horizontal", font=fonte, from_=0, to=255, command= mix)
esc1.grid(row=0, column=1,sticky="w")
labRed = Label(winds, text="Red", font=fonte,fg="red")
labRed.grid(row=0, column=0)

esc2 = Scale(winds,orient="horizontal", font=fonte, from_=0, to=255, command= mix)
esc2.grid(row=1, column=1,sticky="w")
labGreen = Label(winds, text="Green", font=fonte,fg="green" )
labGreen.grid(row=1, column=0)

esc3 = Scale(winds,orient="horizontal", font=fonte, from_=0, to=255, command= mix)
esc3.grid(row=2, column=1,sticky="w")   
labBlue = Label(winds, text="Blue", font=fonte,fg="blue")
labBlue.grid(row=2, column=0)

labColor = Label(winds, text="Color", font=fonte, bg="black", fg="white",width=20)
labColor.grid(row=0, column=3, rowspan=3, sticky="ns")

labMostra = Label(winds,text="#000000", font=fonte)
labMostra.grid(row=3, column=3, columnspan=3)


winds.mainloop()