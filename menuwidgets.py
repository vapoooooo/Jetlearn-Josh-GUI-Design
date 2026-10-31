from tkinter import *
from tkinter.ttk import *
import time

root = Tk()

def triggerprog():
    spinn = spinb.get()
    for i in range(0,int(spinn),5):
        progress['value'] = i
        root.update_idletasks()
        time.sleep(1)

meny = Menu(root)
file = Menu(meny)
edit = Menu(meny)

meny.add_cascade(label = 'File', menu = file)
file.add_command(label = 'Save', command = None)
file.add_command(label = 'Save As..', command = None)
file.add_separator()
file.add_command(label = 'Open File', command = None)
file.add_command(label = 'New File', command = None)
file.add_separator()
file.add_command(label = 'Exit', command = root.destroy)

meny.add_cascade(label = 'Edit', menu = edit)
edit.add_command(label = 'Undo', command = None)
edit.add_command(label = 'Redo', command = None)
edit.add_separator()
edit.add_command(label = 'Cut', command = None)
edit.add_command(label = 'Copy      Ctrl+C', command = None)
edit.add_command(label = 'Paste      Ctrl+V', command = None)

spinb = Spinbox(root, from_=0, to_=100)
spinb.pack()

progress = Progressbar(root, orient = HORIZONTAL, length = 150, mode = 'indeterminate') #mode = determinate-indeterminate
progress.pack()

progressstart = Button(root, text = 'Start', command = triggerprog)
progressstart.pack()

root.config(menu = meny)
root.mainloop()