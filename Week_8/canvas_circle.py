from tkinter import *
import turtle
import random

# main window
win = Tk()
win.title("Turtle Canvas")

# canvas
drw = Canvas(win, width=500, height=500)
drw.pack()

# circle list
a = []
for i in range(10):
    circle = turtle.RawTurtle(drw)
    circle.color("red")
    circle.shape("circle")
    circle.penup()
    circle.speed(0)
    circle.goto(x=random.randint(-200,200), y=random.randint(-200,200))

    a.append(circle)

win.mainloop()