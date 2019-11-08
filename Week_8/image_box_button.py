# import tkinter module
from tkinter import *
from tkinter import messagebox

# function
def btn_func():
    messagebox.showinfo("my message", "hello!~")

# Tk instance
win = Tk()
win.title("python window")

# button
img_ok = PhotoImage(file="btn_ok.png")
btn_ok = Button(win, image=img_ok, command=btn_func)
btn_ok.pack()

img_exit = PhotoImage(file="btn_exit.png")
btn_exit = Button(win, image=img_exit, command=quit)
btn_exit.pack()

win.mainloop()