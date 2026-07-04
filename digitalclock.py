from tkinter import *
import tkinter.font as fo 
from time import strftime
import random 


colors = ['blue','red','green','yellow','orange','pink','purple','cyan','magenta','turquoise','violet']


def fetchtime():
    timee = strftime('%I:%M:%S %p')
    dayy = strftime('%A, %d %B')
    foreground = random.choice(colors)
    background = random.choice(colors)
    while foreground == background:
        background = random.choice(colors)
    dayytime.config(text = dayy, fg = foreground, bg = background)
    clockk.config(text = timee, fg = foreground, bg = background)
    clockk.after(1000,fetchtime)

root = Tk()

root.config(bg = 'black')

font1 = fo.Font(family = 'Ariel', size = 20, weight = 'normal')
root.geometry('640x310')

dayytime = Label(root, text = '', font = font1)
dayytime.pack(side = TOP, padx = 50, pady = 50)

clockk = Label(root, text = '',font = font1)
clockk.pack(side = BOTTOM, padx = 50, pady = 50)

fetchtime()

root.mainloop()
