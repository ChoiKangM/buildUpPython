# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# buttons
btn1 = Button(win, text="BUTTON 1")
btn2 = Button(win, text="BUTTON 2")
btn3 = Button(win, text="BUTTON 3")

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)

win.mainloop()