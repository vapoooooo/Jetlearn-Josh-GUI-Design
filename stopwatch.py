from tkinter import *
import tkinter.font as fo 
import time
from tkinter import messagebox

root = Tk()

root.config(bg = 'grey')

font1 = fo.Font(size = 14)

root.geometry('612x400')

hours = StringVar()
minutes = StringVar()
seconds = StringVar()

def reset():
    hours.set('00')
    minutes.set('00')
    seconds.set('00')

reset()

def countdown():
    hourentry.config(state = DISABLED)
    minuteentry.config(state = DISABLED)
    secondentry.config(state = DISABLED)
    trigger.config(state = DISABLED)

    try:
        totalseconds = int(secondentry.get()) + int(minuteentry.get())*60 + int(hourentry.get())*3600

    except:
        messagebox.showerror('Error','Please input a valid integer.')

    while totalseconds > 0:
        m,s = divmod(totalseconds, 60)
        h = 0

        if m > 60:
            h,m = divmod(m, 60)

        hours.set(h)
        minutes.set(m)
        seconds.set(s)

        root.update()

        time.sleep(1)
        totalseconds = totalseconds - 1

hourentry = Entry(root, width = 10, font = font1, textvariable= hours)
hourentry.place(x = 80, y = 50)

minuteentry = Entry(root, width = 10, font = font1, textvariable= minutes)
minuteentry.place(x = 230, y = 50)

secondentry = Entry(root, width = 10, font = font1, textvariable= seconds)
secondentry.place(x = 380, y = 50)


trigger = Button(root, text = 'start timer', command = countdown, font = font1)
trigger.place(x = 250, y = 200)


root.mainloop()