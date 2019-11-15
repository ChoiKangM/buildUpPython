# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# left button
la_name = Label(win, text="<<이전")
la_grid(row=0,column=0)

# right button
la_name = Label(win, text="다음>>")
la_grid(row=0,column=1)




win.mainloop()