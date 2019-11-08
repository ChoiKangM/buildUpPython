# import tkinter module
from tkinter import *
from tkinter import messagebox

# function
def my_func(event):
    messagebox.showinfo("my message", "within image")

# Tk instance
win = Tk()
win.title("python window")
win.geometry("400x400")

# label
image = PhotoImage(file="cafe_part.gif")
la_img = Label(win, image=image)
la_img.pack(expand=True, anchor=CENTER)

# bind (image label, button)
la_img.bind("<Button>", my_func)

win.mainloop()