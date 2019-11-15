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