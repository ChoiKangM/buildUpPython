# import tkinter module
from tkinter import *

# function
def my_func(event):
    txt = ""

    # click event : left / right
    if event.num == 1:
        txt = "left button ("
    elif event.num == 3:
        txt = "right button ("

    # click position
    pos_x = event.x
    pos_y = event.y
    txt += str(pos_x) + "," + str(pos_y) + ")"

    # label txt
    la_txt.configure(text=txt)

# Tk instance
win = Tk()
win.title("python window")
win.geometry("400x400")

# bind (bind windowm button)
win.bind("<Button>", my_func)

# label
la_txt = Label(win)
la_txt.pack(expand=True, anchor=CENTER)

win.mainloop()