from tkinter import *


font = ("Comic Sans MS", 14, "bold")

w = Tk()



w.title("FRAMES")
w.geometry("550x350")
w.iconbitmap("logopy.ico")

f1 = Frame(w)
f1.pack(pady=10)

l1 = Label(f1, text="Label 1",fg="white", bg="red", font=font)
l2 = Label(f1, text="Label 2",fg="white", bg="green",font=font)
l3 = Label(f1, text="Label 3",fg="white",   bg="blue",font=font)
l4 = Label(f1, text="Label 4",fg="white",  bg="brown",font=font)
l5 = Label(f1, text="Label 5",fg="white" , bg="light blue",font=font)
l6 = Label(f1, text="Label 6", fg="white",     bg="orange",font=font)
l7 = Label(f1, text="Label 7",fg="white", bg="light green",font=font)



l1.grid(row=0, column=0, rowspan=2, sticky="ns")
l2.grid(row=0, column=1)
l3.grid(row=0, column=2)
l4.grid(row=1, column=1, columnspan=2,sticky="we" )
l5.grid(row=2, column=0, columnspan=2,sticky="we")
l6.grid(row=2, column=2, rowspan=2, sticky="ns")
l7.grid(row=3, column=0, columnspan=2, sticky="we")


w.mainloop()