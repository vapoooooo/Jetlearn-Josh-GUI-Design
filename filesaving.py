from tkinter import *
from tkinter.filedialog import *

root = Tk()

def createsave():
    asksaveasfile(defaultextension = '.txt')

def opensave():
    fileread = askopenfile(filetypes = [('Python Files','*.py'),('Text document','*.txt')])
    print(fileread.read())

openbutton = Button(root, text = 'OPEN', command = opensave)
openbutton.pack(side = LEFT)

savebutton = Button(root, text = 'SAVE', command = createsave)
savebutton.pack(side = RIGHT)

root.mainloop()