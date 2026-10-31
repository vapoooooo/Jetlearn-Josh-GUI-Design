from tkinter import *

root = Tk()
root.geometry('480x640')

topframe = Frame(root)
topframe.pack()

paintop = Button(topframe, text = 'Brush/Pen', command = None)
paintop.grid(row = 0, column = 0, padx = 25)

eraser = Button(topframe, text = 'Eraser', command = None)
eraser.grid(row = 0, column = 1, padx = 25)

colourop = Button(topframe, text = 'Switch Colour', command = None)
colourop.grid(row = 0, column = 2, padx = 25)

thicknesscale = Scale(topframe, from_=1, to_=25, orient = HORIZONTAL)
thicknesscale.grid(row = 0, column = 3, padx = 25)

root.mainloop()