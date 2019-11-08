# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# button
btn_ok = Button(win,text="종료", width=10, height=2, command=quit)
btn_ok.pack()

win.mainloop()