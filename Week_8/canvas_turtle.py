from tkinter import *
import turtle

# main window
win = Tk()
win.title("Turtle Canvas")

# canvas
drw = Canvas(win, width=500, height=500)
drw.pack()

# turtle
t = turtle.RawTurtle(drw)
t.shape("turtle")
t.color("blue")
t.circle(50)

win.mainloop()