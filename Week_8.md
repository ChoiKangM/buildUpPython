# `Tkinter`
> GUI 관련 파이썬 표준 라이브러리

`first_tkinter.py`  
```python
# import tkinter module
from tkinter import *

# Tk instance
win = Tk()

win.mainloop()
```

## 기본 윈도우 창
`basic_window.py`
```python
# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")
win.geometry("400x100")
win.resizable(width=False, height=False)

win.mainloop()
```

## 기본 위젯 사용
`basic_widget.py`
```python
# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")
# win.geometry("400x100")
# win.resizable(width=False, height=False)

# label
la_name = Label(win, text="이름")
la_name.pack()

# textbox
in_tb = Entry(win)
in_tb.pack()

# button
btn_ok = Button(win, text="확인")
btn_ok.pack()

win.mainloop()
```

## Label
`label.py`
```python
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
```

## PhotoImage
`photoImage.py`
```python
# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# label
image = PhotoImage(file="cafe.gif")
la_img = Label(win, image=image)
la_img.pack()

win.mainloop()
```

## Button
`quit_button.py`
```python
# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# button
btn_ok = Button(win,text="종료", width=10, height=2, command=quit)
btn_ok.pack()

win.mainloop()
```

`image_box_button.py`
```python
# import tkinter module
from tkinter import *
from tkinter import messagebox

# function
def btn_func():
    messagebox.showinfo("my message", "hello!~")

# Tk instance
win = Tk()
win.title("python window")

# button
img_ok = PhotoImage(file="btn_ok.png")
btn_ok = Button(win, image=img_ok, command=btn_func)
btn_ok.pack()

img_exit = PhotoImage(file="btn_exit.png")
btn_exit = Button(win, image=img_exit, command=quit)
btn_exit.pack()

win.mainloop()
```

## Checkbox
`checkbox.py`
```python
# import tkinter module
from tkinter import *
from tkinter import messagebox

# function
def check_func():
    if var_chk.get() == 1:
        la_result.configure(text="check!~")
    else:
        la_result.configure(text="")

# Tk instance
win = Tk()
win.title("python window")

# check variable of int type
var_chk = IntVar()

# check button
chk_ok = Checkbutton(win, text="Python", variable=var_chk, command=check_func)

# result text label
la_result = Label(win)

chk_ok.pack()
la_result.pack()

win.mainloop()
```

## RadioButton
`radiobutton.py`
```python
# import tkinter module
from tkinter import *

# function
def radio_func():
    if var_lang.get() == 1:
        la_result.configure(text="Python")
    elif var_lang.get() == 2:
        la_result.configure(text="Java")
    else:
        la_result.configure(text="C++")

# Tk instance
win = Tk()
win.title("python window")

# radio variable of int type
var_lang = IntVar()

# radio button
rb1 = Radiobutton(win, text="Python", variable=var_lang, value=1, command=radio_func)
rb2 = Radiobutton(win, text="Java", variable=var_lang, value=2, command=radio_func)
rb3 = Radiobutton(win, text="C++", variable=var_lang, value=3, command=radio_func)

la_result = Label(win, text="my lang", fg="blue")

rb1.pack()
rb2.pack()
rb3.pack()
la_result.pack()

win.mainloop()
```

## 수평 정렬
`arrangeHWidget.py`
```python
# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# buttons
btn1 = Button(win, text="BUTTON 1")
btn2 = Button(win, text="BUTTON 2")
btn3 = Button(win, text="BUTTON 3")

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)

win.mainloop()
```
## 수직 정렬
`arrangeVWidget.py`
```python
# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# buttons
btn1 = Button(win, text="BUTTON 1")
btn2 = Button(win, text="BUTTON 2")
btn3 = Button(win, text="BUTTON 3")

btn1.pack(side=TOP)
btn2.pack(side=TOP)
btn3.pack(side=TOP)

win.mainloop()
```

## 정렬 및 폭 맞추기
`width_100.py`
```python
# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# buttons
btn1 = Button(win, text="BUTTON 1")
btn2 = Button(win, text="BUTTON 2")
btn3 = Button(win, text="BUTTON 3")

btn1.pack(side=TOP, fill=X)
btn2.pack(side=TOP, fill=X)
btn3.pack(side=TOP, fill=X)

win.mainloop()
```

## 위젯 여백
`padding.py`
```python
# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# buttons
btn1 = Button(win, text="BUTTON 1")
btn2 = Button(win, text="BUTTON 2")
btn3 = Button(win, text="BUTTON 3")

btn1.pack(side=TOP, fill=X, padx=10, pady=10, ipadx=10, ipady=10)
btn2.pack(side=TOP, fill=X, padx=10, pady=10, ipadx=10, ipady=10)
btn3.pack(side=TOP, fill=X, padx=10, pady=10, ipadx=10, ipady=10)

win.mainloop()
```

## 고정 위치 배치
`fixed_position.py`
```python
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
```

## 레이아웃 배치
`layout_arrange1.py`
```python
# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# label
la_name = Label(win, text="이름")
la_name.grid(row=0, column=0)

# textbox
in_tb = Entry(win)
in_tb.grid(row=0, column=1)

# button
btn_ok = Button(win, text="확인")
btn_ok.grid(row=1, column=1)

win.mainloop()
```

`layout_arrange2.py`
```python
# import tkinter module
from tkinter import *

# Tk instance
win = Tk()
win.title("python window")

# label
la_name = Label(win, text="이름")
la_name.grid(row=0, column=0)

# textbox
in_tb = Entry(win)
in_tb.grid(row=0, column=1)

# button
btn_ok = Button(win, text="확인")
btn_ok.grid(row=1, column=2)

win.mainloop()
```

## 버튼 기본 이벤트
`button_event.py`
```python
# import tkinter module
from tkinter import *
from tkinter import messagebox

# function
def btn_func():
    str_output = in_tb.get()
    messagebox.showinfo("my message", str_output)

# Tk instance
win = Tk()
win.title("python window")

# label
la_name = Label(win, text="이름")
la_name.grid(row=0, column=0)

# textbox
in_tb = Entry(win)
in_tb.grid(row=0, column=1)

# button
btn_ok = Button(win, text="확인", command=btn_func)
btn_ok.grid(row=1, column=2)

win.mainloop()
```

## 마우스 이벤트 + 버튼 이벤트 바인딩
`button_event_binding1.py`
```python
# import tkinter module
from tkinter import *

# function
def my_func(event):
    txt = ""

    # click event : left / right
    if event.num == 1:
        txt = "left button ("
    elif event.num == 3:
        txt = "right button ("

    # click position
    pos_x = event.x
    pos_y = event.y
    txt += str(pos_x) + "," + str(pos_y) + ")"

    # label txt
    la_txt.configure(text=txt)

# Tk instance
win = Tk()
win.title("python window")
win.geometry("400x400")

# bind (bind windowm button)
win.bind("<Button>", my_func)

# label
la_txt = Label(win)
la_txt.pack(expand=True, anchor=CENTER)

win.mainloop()
```

`button_event_binding2.py`
```python
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
```

# 윈도우 메뉴
## 메뉴 생성
`make_menu.py`
```python
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
```

`make_menu2.py`
```python
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
menu2 = Menu(main_menu)

# main-sub menu cascade
main_menu.add_cascade(label="Menu 1", menu=menu1)
main_menu.add_cascade(label="Menu 2", menu=menu2)

# add sub menu (menu 1)
menu1.add_command(label="Menu 1-1")
menu1.add_separator()
menu1.add_command(label="Menu 1-2")

# add sub menu (menu 2)
menu2.add_command(label="Menu 2-1")
menu2.add_command(label="Menu 2-2")
menu2.add_command(label="Menu 3-2")

win.mainloop()
```

`real_menu.py`
```python
# import tkinter module
from tkinter import *

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
menu1_file.add_command(label="Open")
menu1_file.add_separator()
menu1_file.add_command(label="Exit")

win.mainloop()
```
`real_menu2.py`
```python
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
```

# Dialog 연동
`simpledialog`
```python
# import tkinter module
from tkinter import *
from tkinter.simpledialog import *

# main window
win = Tk()
win.title("python Programming")
win.geometry("400x100")

# label
la_var = Label(win, text="입력된 값")
la_var.pack(side=LEFT)

# dialog
value = askinteger("확대배수", "주사위 숫자(1~6)을 입력하세요", minvalue=1, maxvalue=6)

# show result
la_var.configure(text=str(value))

win.mainloop()
```

`filedialog.py`
```python
# import tkinter module
from tkinter import *
from tkinter.filedialog import *

# main window
win = Tk()
win.title("python Programming")
win.geometry("400x100")

# label
la_var = Label(win, text="선택된 파일명")
la_var.pack(side=LEFT)

# dialog
filename = askopenfilename(parent=win, filetypes=(("GIF 파일", "*.gif"),("모든 파일", "*.*")))

# show result
la_var.configure(text=filename)

win.mainloop()
```

# Canvas
## Canvas
> 그래프를 그리거나, 다른 것들을 그릴 수 있는 위젯  

`canvas.py`
```python
from tkinter import *

# main window
win = Tk()
win.title("My Canvas")

# canvas
drw = Canvas(win, width=200, height=100)
drw.pack()

# canvas line
drw.create_line(0, 0, 200, 100)
drw.create_line(0, 100, 200, 0, fill="red", dash=(4))

# canvas rectangle
drw.create_rectangle(50, 25, 150, 75, fill="blue")

win.mainloop()
```

`canvas2.py`
```python
from tkinter import *

# main window
win = Tk()
win.title("Canvas line")

# canvas
drw = Canvas(win, width=500, height=500, bg="black")
drw.pack()

# canvas line
Q = [430,300, 315,400, 175,400, 151,300, 300,180, 325,70, 200,35, 180,120, 430,385]
drw.create_line(0, 0, 200, 100)
# smooth의 유뮤 확인
drw.create_line(Q, smooth="true", dash=(4), fill="white", width=5)

win.mainloop()
```
`canvas_turtle.py`
```python
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
```

`canvas_circle.py`
```python
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
```

`canvas_input_circle.py`
```python
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
```

# Turtle Game
`turtle_game_circle_moving.py`
```python
from tkinter import *
import turtle
import random

def play():
    for mv_a in a:
        mv_a.right(random.randint(0,100))
        mv_a.forward(40)

    scr.ontimer(play, 500)

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

# turtle
t = turtle.RawTurtle(drw)
t.shape("turtle")
t.color("blue")
t.speed(0)
t.penup()

scr = t.getscreen()
play()

win.mainloop()
```

`turtle_game_key_play.py`
```python
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
```