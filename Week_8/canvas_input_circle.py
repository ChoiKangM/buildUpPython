from tkinter import *
import turtle
import random

def create_circle():
    num = int(in_num.get())

    for i in range(num):
        circle = turtle.RawTurtle(drw)
        circle.color("red")
        circle.shape("circle")
        circle.penup()
        circle.goto(x=random.randint(-200, 200), y=random.randint(-200, 200))

        a.append(circle)

# main window
win = Tk()
win.title("Turtle Canvas")

# circle list
a = []

# canvas
drw = Canvas(win, width=500, height=500)
drw.pack()

# label
la_txt = Label(win, text="개수 입력 : ")
la_txt.pack(side=LEFT)

# text box
in_num = Entry(win)
in_num.pack(side=LEFT)

# button
btn_ok = Button(win, text="확인", command=create_circle)
btn_ok.pack(side=LEFT)

win.mainloop()