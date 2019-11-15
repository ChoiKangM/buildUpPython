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