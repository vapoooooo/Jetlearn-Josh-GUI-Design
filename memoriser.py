from tkinter import *
from tkinter.filedialog import *

root = Tk()

savebutton = Button(root, text = 'SAVE')
savebutton.grid(row = 0, column = 0, columnspan = 2, pady = 15)

addvalue = Entry(root)
addvalue.grid(row = 1, column = 0, columnspan = 2, pady = 10)

addbutton = Button(root, text = 'ADD VALUE')
addbutton.grid(row = 2, column = 0, padx = 20)

deletebutton = Button(root, text = 'DELETE VALUE')
deletebutton.grid(row = 2, column = 1)

root.mainloop()