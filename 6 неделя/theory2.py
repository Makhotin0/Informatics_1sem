from tkinter import *


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения. обратите внимание, что к root обращаемся как к глобальной переменной
    print("App closed")


root = Tk()
root.geometry("250x200")

root.title("Hello")
root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()