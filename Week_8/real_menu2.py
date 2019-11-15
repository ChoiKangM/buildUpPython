# import tkinter module
from tkinter import *
from tkinter import messagebox


# func
def func_open():
    messagebox.showinfo("select menu", "open menu")
def func_exit():
    win.quit()
    win.destroy()

# Tk instance
win = Tk()
win.title("python window")

# create main menu
main_menu = Menu(win)
win.config(menu=main_menu)

# create sub menu
menu1_file = Menu(main_menu)

# main-sub menu cascade
main_menu.add_cascade(label="File", menu=menu1_file)

# add sub menu (open, exit)
menu1_file.add_command(label="Open", command=func_open)
menu1_file.add_separator()
menu1_file.add_command(label="Exit", command=func_exit)

win.mainloop()