from tkinter import *

color = str(input())
root = Tk()
root.title("")
root.geometry("300x300")

num_color = []
for i in range(len(color)):
    if color[i] == 'A' or color[i] == 'a':
        num_color.append(10)
    elif color[i] == 'B' or color[i] == 'b':
        num_color.append(11)
    elif color[i] == 'C' or color[i] == 'c':
        num_color.append(12)
    elif color[i] == 'D' or color[i] == 'd':
        num_color.append(13)
    elif color[i] == 'E' or color[i] == 'e':
        num_color.append(14)
    elif color[i] == 'F' or color[i] == 'f':
        num_color.append(15)
    else:
        num_color.append(int(color[i]))

comp_color_dec = []
i = 0
while i < len(num_color):
    color_dec = 0
    for j in range(i, i+2, 1):
        color_dec += int(num_color[2*i+1-j]) * (16 ** (j - i))
    comp_color_dec.append(255 - color_dec)
    i += 2

comp_color = []
for i in range(len(comp_color_dec)):
    comp_color_number = format(comp_color_dec[i], "x")
    if len(comp_color_number) == 1:
        comp_color_number = '0' + comp_color_number
    comp_color.append(comp_color_number)
comp_color = ''.join(comp_color)
print(color)
print(comp_color)

label = Label(text="                                    ", background = '#' + color)
label1 = Label(text="                                    ", background = '#' + comp_color)
label.pack()
label1.pack()

root.mainloop()