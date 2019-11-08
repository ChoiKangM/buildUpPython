# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# label
la_name = Label(win, text="이름")
la_name.grid(row=0, column=0)

# textbox
in_tb = Entry(win)
in_tb.grid(row=0, column=1)

# button
btn_ok = Button(win, text="확인")
btn_ok.grid(row=1, column=2)

win.mainloop()