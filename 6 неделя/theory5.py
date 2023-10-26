from tkinter import *


# общий вид функции чтобы рекурсивно вывести информацию обо всех виджетах
def print_info(widget, depth=0):
    widget_class = widget.winfo_class()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    print("   " * depth + f"{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}")
    for child in widget.winfo_children():
        print_info(child, depth + 1)


root = Tk()
root.title("HELLO")
root.geometry("250x250")

btn = Button(
    text="Click")  # кстати, можем добавить параметр state=["disabled"], что сделает кнопку выключенной, пока мы не изменим параметр 'state'
btn.pack()

root.update()  # обновляем информацию о виджетах после их размещения, иначе это произойдет только с вызовом mainloop

print_info(root)  # получаем всю инфу о root. Поскольку у root есть только один виджет, вызовется информация о нем

root.mainloop()