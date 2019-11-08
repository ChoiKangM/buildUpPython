# import tkinter module
from tkinter import *
from tkinter import messagebox

# function
def my_func(event):
    txt = "push key : " + chr(event.keycode)
    messagebox.showinfo("my message", txt)

# Tk instance
win = Tk()
win.title("python window")

# bind (base window, button)
win.bind("<Key>", my_func)

win.mainloop()