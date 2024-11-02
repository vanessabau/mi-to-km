from cProfile import label
from tkinter import *

window = Tk()
window.title=("Miles to KM Converter")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)

def button_clicked():
    miles = float(input.get())
    km = miles * 1.60934
    label3.config(text=km)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()