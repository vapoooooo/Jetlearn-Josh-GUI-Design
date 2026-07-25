from tkinter import *
from tkinter.ttk import *
import tkinter.font as fo 

root = Tk()

font1 = fo.Font(family = 'Ariel', size = 20, weight = 'normal')
font2 = fo.Font(family = 'Ariel', size = 15, weight = 'normal')

#leftframe here --------------------------0-----------------------------0 -----------------------------0-------------------------0-------------------------0--

leftframe = Frame(root)
leftframe.pack(side = LEFT, padx = 20)

enternumber = Label(leftframe, text = 'enter number', font = font1)
enternumber.pack(pady = 10)

numvar = IntVar()
numvar.set(1)

rangevarvar = IntVar()
rangevarvar.set(12)

numberchoose = Combobox(leftframe, textvariable = numvar, font = font1)
numberchoose['values'] = tuple(range(1,30))
numberchoose.pack(pady = 20)

selrange = Label(leftframe, text = 'select range', font = font2)
selrange.pack(pady = 20)#

rangevar1 = Radiobutton(leftframe, text = '12', value = 12, variable = rangevarvar)
rangevar1.pack(pady = 5)

rangevar2 = Radiobutton(leftframe, text = '24', value = 24, variable = rangevarvar)
rangevar2.pack(pady = 5)

rangevar3 = Radiobutton(leftframe, text = '36', value = 36, variable = rangevarvar)
rangevar3.pack(pady = 5)

#create table function --------------------------------------0

def createtable():
    result = ''
    for i in range(rangevarvar.get() + 1):
        a = numvar.get() * i
        b = str(numvar.get()) + 'X'+ str(i) + '='+ str(a)
        result = result + b + '\n '

    resulttable.config(text = result)




#rightframe here -----------------------------------0-------------------------------0--------------------------0-----------------------0-----------------

rightframe = Frame(root)
rightframe.pack(side = RIGHT, padx = 20)

enterbutton = Button(rightframe, text = 'create table', command = createtable)
enterbutton.pack(pady = 10)

resulttable = Label(rightframe, text = '', font = font2)
resulttable.pack(pady = 20)


root.mainloop()