from tkinter import *
import turtle
import random

def turtle_left(event):
    t.left(30)
def turtle_right(event):
    t.right(30)
def turtle_go(event):
    t.forward(30)

def play():
    global cnt

    for mv_a in a:
        mv_a.right(random.randint(0,100))
        mv_a.forward(40)

        if t.distance(mv_a) < 30:
            cnt += 1
            str_cnt = str(cnt) + "점"
            la_result.configure(text=str_cnt)

    scr.ontimer(play, 300)

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
cnt = 0

# canvas
drw = Canvas(win, width=500, height=500)
drw.pack()

# label
la_txt1 = Label(win, text="개수 입력 : ")
la_txt1.pack(side=LEFT)

# text box
in_num = Entry(win)
in_num.pack(side=LEFT)

# button
btn_ok = Button(win, text="확인", command=create_circle)
btn_ok.pack(side=LEFT)

# label
la_txt2 = Label(win, text="점수 : ")
la_txt2.pack(side=LEFT, padx=10)

# result
la_result = Label(win)
la_result.pack(side=LEFT)

# button
btn_exit = Button(win, text="종료", command=quit)
btn_exit.pack(side=RIGHT)

# turtle
t = turtle.RawTurtle(drw)
t.shape("turtle")
t.color("blue")
t.speed(0)
t.penup()

scr = t.getscreen()
scr.bgcolor("black")
play()

win.bind("<Left>", turtle_left)
win.bind("<Right>", turtle_right)
win.bind("<Up>", turtle_go)

win.mainloop()