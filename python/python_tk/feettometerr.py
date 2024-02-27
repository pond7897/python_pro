from tkinter import *
from tkinter import ttk


def calculate():
    return 

root = Tk()
root.title("Feet to meters")
root.geometry("400x200")

l1 = Label(root,text="Feet")
l1.place(x = 240, y = 10)
l2 = Label(root,text="is equivalent to ")
l2.place(x = 50, y = 40)
l3 = Label(root,text="meters")
l3.place(x= 240, y = 40)
l4 = Label(root,text="0.00")
l4.place(x = 200, y = 40)

b1 = Button(root,text="Calculate")
b1.place(x = 240, y = 70)


meter = StringVar()
e1 = ttk.Entry(root,width=10)
e1.pack(pady=10)
e1.focus()

root.bind("<Return>", calculate)
root.mainloop()
