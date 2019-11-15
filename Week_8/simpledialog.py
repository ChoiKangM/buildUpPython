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