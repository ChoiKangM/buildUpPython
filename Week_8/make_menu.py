# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# create main menu
main_menu = Menu(win)
win.config(menu=main_menu)

# create sub menu
menu1 = Menu(main_menu)

# main-sub menu cascade
main_menu.add_cascade(label="Menu 1", menu=menu1)

# add sub menu (open, exit)
menu1.add_command(label="Menu 1-1")
menu1.add_separator()
menu1.add_command(label="Menu 1-2")

win.mainloop()