# import tkinter module
from tkinter import *
from tkinter import messagebox

# function
def check_func():
    if var_chk.get() == 1:
        la_result.configure(text="check!~")
    else:
        la_result.configure(text="")

# Tk instance
win = Tk()
win.title("python window")

# check variable of int type
var_chk = IntVar()

# check button
chk_ok = Checkbutton(win, text="Python", variable=var_chk, command=check_func)

# result text label
la_result = Label(win)

chk_ok.pack()
la_result.pack()

win.mainloop()