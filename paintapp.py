from tkinter import *
from tkinter.colorchooser import askcolor

root = Tk()
root.geometry('580x720')
root.config(background='grey')

def activatebutton(button, erasemode = False):
    global selectedbutton, eraseractive
    selectedbutton.config(relief='raised')
    selectedbutton = button
    selectedbutton.config(relief='sunken')
    eraseractive = erasemode

def usebrush():
    activatebutton(paintop)

def useeraser():
    activatebutton(eraser, True)

def usecolour():
    global color
    activatebutton(colourop)
    color = askcolor(color=color)[1]
    print(color)
    activatebutton(paintop)

def drawing(movemouse):
    global prevx, prevy, color
    if eraseractive:
        c = 'white'
    else:
        c = color
    if prevx and prevy:
        paintcanvas.create_line(prevx, prevy, movemouse.x, movemouse.y, width = thicknesscale.get(), fill=c, capstyle='round', smooth = True)

    prevx = movemouse.x
    prevy = movemouse.y

def resetdraw(release):
    global prevx, prevy
    prevx = None
    prevy = None

def cleardrawing():
    paintcanvas.delete('all')


topframe = Frame(root)
topframe.pack(pady=25)

bottomframe = Frame(root)
bottomframe.pack(pady = 25)

paintop = Button(topframe, text = 'Brush/Pen', command = usebrush)
paintop.grid(row = 0, column = 0, padx = 25)

eraser = Button(topframe, text = 'Eraser', command = useeraser)
eraser.grid(row = 0, column = 1, padx = 25)

colourop = Button(topframe, text = 'Switch Colour', command = usecolour)
colourop.grid(row = 0, column = 2, padx = 25)

thicknesscale = Scale(topframe, from_=1, to_=25, orient = HORIZONTAL)
thicknesscale.grid(row = 0, column = 3, padx = 25)

paintcanvas = Canvas(bottomframe, width = 480, height = 480, bg='white') #paint
paintcanvas.pack()

clearcanvas = Button(bottomframe, text = 'Clear Drawing', command = cleardrawing)
clearcanvas.pack(pady = 25)

#initial setup ---------------------------------------------

prevx = None
prevy = None
color = 'black'
thickness=8
thicknesscale.set(thickness)
selectedbutton = paintop
selectedbutton.config(relief='sunken')
eraseractive = False
paintcanvas.bind('<B1-Motion>', drawing)
paintcanvas.bind('<ButtonRelease-1>', resetdraw)

root.mainloop()