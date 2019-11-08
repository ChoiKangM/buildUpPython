# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# label
la_str1 = Label(win, text="basic string")
la_str1.pack()

# font
la_str2 = Label(win, text="font string", font=("궁서체", 20), fg="blue")
la_str2.pack()

# background
# anchor = CENTER(default), N, NE, NW, S SE, SW, E, W
la_str3 = Label(win, text="bg string", bg="black",fg="white",width=20,height=2,anchor=SE)
la_str3.pack()

win.mainloop()