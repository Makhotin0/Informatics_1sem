from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        kg1 = float(kg.get())
        length1 = float(length.get())
        index.set(kg1/(length1*0.01)**2)
        index1 = kg1/(length1)**2
        if index1 <= 16:
            diagnoz1 = 'Выраженный дефицит массы тела'
        elif index1 > 16 and index1 <= 18.5:
            diagnoz1 = 'Недостаточная (дефицит) масса тела'
        elif index1 > 18.5 and index1 <= 25:
            diagnoz1 = 'Норма'
        elif index1 > 25 and index1 <= 30:
            diagnoz1 = 'Избыточная масса тела (предожирение)'
        elif index1 > 30 and index1 <= 35:
            diagnoz1 = 'Ожирение 1 степени'
        elif index1 > 35 and index1 <= 40:
            diagnoz1 = 'Ожирение 2 степени'
        else:
            diagnoz1 = 'Ожирение 3 степени'
        diagnoz.set(diagnoz1)
    except ValueError:
        pass

root = Tk()
root.title("Индекс массы тела")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

kg = StringVar()
kg_entry = ttk.Entry(mainframe, width=7, textvariable=kg)
kg_entry.grid(column=2, row=1, sticky=(W, E))

length = StringVar()
length_entry = ttk.Entry(mainframe, width=7, textvariable=length)
length_entry.grid(column=2, row=2, sticky=(W,E))

index = StringVar()
ttk.Label(mainframe, textvariable=index).grid(column=2, row=3, sticky=(W, E))

diagnoz = StringVar()
ttk.Label(mainframe, textvariable=diagnoz).grid(column=2, row=4, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=2, row=5, sticky=W)

ttk.Label(mainframe, text="Масса").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Рост").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Индекс").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="Диагноз").grid(column=3, row=4, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

kg_entry.focus()

root.bind("<Return>", calculate)

root.mainloop()