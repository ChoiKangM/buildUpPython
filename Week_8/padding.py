# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# buttons
btn1 = Button(win, text="BUTTON 1")
btn2 = Button(win, text="BUTTON 2")
btn3 = Button(win, text="BUTTON 3")

btn1.pack(side=TOP, fill=X, padx=10, pady=10, ipadx=10, ipady=10)
btn2.pack(side=TOP, fill=X, padx=10, pady=10, ipadx=10, ipady=10)
btn3.pack(side=TOP, fill=X, padx=10, pady=10, ipadx=10, ipady=10)

win.mainloop()