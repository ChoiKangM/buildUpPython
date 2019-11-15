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