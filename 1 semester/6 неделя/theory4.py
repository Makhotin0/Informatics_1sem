from tkinter import *
from tkinter import ttk

root = Tk()
root.title("HELLO")
root.geometry("250x250")

btn = ttk.Button()
btn.pack()
# устанавливаем параметр text
btn["text"] = "Send"
# получаем значение параметра text
btnText = btn["text"]
print(btnText)

root.mainloop()