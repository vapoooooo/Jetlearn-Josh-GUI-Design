from tkinter import *
from tkinter import messagebox
import random

root = Tk()

root.title('Guessing Game')
root.geometry('800x512')

nameframe = Frame(root)
nameframe.pack()

       
namequestion = Label(nameframe, text = 'What is your name?', fg = 'grey')
namequestion.grid(column = 0, row = 0)

root.mainloop()