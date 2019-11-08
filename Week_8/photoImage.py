# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# label
image = PhotoImage(file="cafe.gif")
la_img = Label(win, image=image)
la_img.pack()

win.mainloop()