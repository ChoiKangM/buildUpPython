# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")
# win.geometry("400x100")
# win.resizable(width=False, height=False)

# label
la_name = Label(win, text="이름")
la_name.pack()

# textbox
in_tb = Entry(win)
in_tb.pack()

# button
btn_ok = Button(win, text="확인")
btn_ok.pack()

win.mainloop()