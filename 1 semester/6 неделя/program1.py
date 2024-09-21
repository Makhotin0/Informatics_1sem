from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = number.get()
        result.set(eval(value))
    except ValueError:
        pass

root = Tk()
root.title("калькулятор")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky = (N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

number = StringVar()
number_entry = ttk.Entry(mainframe, width=7, textvariable=number)
number_entry.grid(column=2, row=1, sticky=(W, E))

result = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Выражение").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Результат").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

number_entry.focus()

root.bind("<Return>", calculate)

root.mainloop()