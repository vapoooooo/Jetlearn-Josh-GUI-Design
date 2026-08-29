from tkinter import *
from tkinter.filedialog import *

def addingvalue():
    value = addvalue.get()
    valuelist.insert(END, value)
    addvalue.delete(0, END)

def deletingvalue():
    value = valuelist.curselection()
    print(value)
    value = value[::-1]
    for i in value:
        valuelist.delete(i)

def savefile():
    filec = asksaveasfile(defaultextension = '.txt')
    if filec is not None:
        for i in valuelist.get(0, END):
            print(i, file = filec)
        valuelist.delete(0, END)

root = Tk()

savebutton = Button(root, text = 'SAVE', command = savefile)
savebutton.grid(row = 0, column = 0, pady = 15, padx = 15)

addvalue = Entry(root)
addvalue.grid(row = 1, column = 0, columnspan = 2, pady = 10)

openbutton = Button(root, text = 'OPEN')
openbutton.grid(row = 0, column = 1, padx = 15)

addbutton = Button(root, text = 'ADD VALUE', command = addingvalue)
addbutton.grid(row = 2, column = 0, padx = 20)

deletebutton = Button(root, text = 'DELETE VALUE', command = deletingvalue)
deletebutton.grid(row = 2, column = 1, padx = 20)

listframe = Frame(root)
listframe.grid(row = 3, column = 0, columnspan = 2, pady = 15)

scroller = Scrollbar(listframe)
scroller.pack(side = LEFT, fill = Y)

valuelist = Listbox(listframe, yscrollcommand = scroller, selectmode = MULTIPLE)
valuelist.pack(side = LEFT)

scroller.config(command = valuelist.yview)


root.mainloop()
