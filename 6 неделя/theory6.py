from tkinter import *
from PIL import ImageTk, Image
import os
root = Tk()
img = ImageTk.PhotoImage(Image.open("wow-oh-my.gif"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()