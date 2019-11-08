# import tkinter module
from tkinter import *

# function
def radio_func():
    if var_lang.get() == 1:
        la_result.configure(text="Python")
    elif var_lang.get() == 2:
        la_result.configure(text="Java")
    else:
        la_result.configure(text="C++")

# Tk instance
win = Tk()
win.title("python window")

# radio variable of int type
var_lang = IntVar()

# radio button
rb1 = Radiobutton(win, text="Python", variable=var_lang, value=1, command=radio_func)
rb2 = Radiobutton(win, text="Java", variable=var_lang, value=2, command=radio_func)
rb3 = Radiobutton(win, text="C++", variable=var_lang, value=3, command=radio_func)

la_result = Label(win, text="my lang", fg="blue")

rb1.pack()
rb2.pack()
rb3.pack()
la_result.pack()

win.mainloop()