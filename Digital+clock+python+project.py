# Importing Python Modules
from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")

label = Label(root, font=("areal", 160, "bold"), bg="Pink", fg="white")
label.pack(anchor="center", fill="both", expand=1)

def Time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, Time)

Time()
root.mainloop()


