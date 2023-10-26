from tkinter import *

root = Tk()  # создаем корневой объект - окно
root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
root.geometry("300x300")  # устанавливаем размеры окна

label = Label(text="Hello")  # создаем текстовую метку
label.pack()  # размещаем метку в окне

root.mainloop()

