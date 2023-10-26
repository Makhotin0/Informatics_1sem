from tkinter import *
from tkinter import ttk  # подключаем пакет ttk

root = Tk()
root.title("Hello")
root.geometry("250x250")

btn = ttk.Button(text="Click")  # создаем кнопку из пакета ttk
btn.pack()  # размещаем кнопку в окне

root.mainloop()