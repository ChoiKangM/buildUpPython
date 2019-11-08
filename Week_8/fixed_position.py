# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")
win.geometry("150x90+10+10")

# buttons
btn_list = [None] * 9

# create button
for i in range(9):
    btn_str = format("BTN_%d" % (i+1))
    btn_list[i] = Button(win, text=btn_str)

# set position
num = 0
pos_x, pos_y = 0, 0
for n in range(3):
    for m in range(3):
        btn_list[num].place(x=pos_x, y=pos_y)
        num += 1
        pos_x += 50
    pos_x = 0
    pos_y += 30

win.mainloop()