# import tkinter module
from tkinter import *
from tkinter.filedialog import *

# func
def func_open():
    filename = askopenfilename(parent=win, filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file=filename)
    la_image.configure(image=photo)
    la_image.image = photo

def func_exit():
    win.quit()
    win.destroy()

# main window
win = Tk()
win.title("Viewer Photo")
win.geometry("400x400")
main_menu = Menu(win)
win.config(menu=main_menu)

# create sub menu
menu1_file = Menu(main_menu)

# main-sub menu cascade
main_menu.add_cascade(label="File", menu=menu1_file)

# add sub menu(open, exit)
menu1_file.add_command(label="Open", command=func_open)
menu1_file.add_separator()
menu1_file.add_command(label="Exit", command=func_exit)

# image label
la_image = Label(win)
la_image.pack(expand=True, anchor=CENTER)

win.mainloop()