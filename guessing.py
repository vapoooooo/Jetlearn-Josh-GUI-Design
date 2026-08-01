from tkinter import *
from tkinter import messagebox
import tkinter.font as fo
import random

root = Tk()

font1 = fo.Font(family = 'Ariel', size = 20, weight = 'normal')
font2 = fo.Font(family = 'Ariel', size = 15, weight = 'normal')

root.title('Guessing Game')
root.geometry('400x206')

nameframe = Frame(root)
nameframe.pack()

gameframe = Frame(root)

guesses = 5
botchoice = random.randint(1,20)

def startgame():
    names = nameanswer.get()
    messagebox.showinfo('Hello!', ' Well '+ names+'! I am thinking of a number inbetween 1 and 20! Can you figure out the number I am thinking of in 5 guesses?')

    nameframe.pack_forget()
    gameframe.pack()

def guessgame():
    global guesses
    valueguess = int(numberentry.get())
    print(valueguess)

    if valueguess > botchoice:
        guesses = guesses - 1
        messagebox.showwarning('Guess','Your answer is too large! You now have '+ str(guesses)+' guesses left! Try again!')
        guessesleft.config(text = 'Guesses Left: '+ str(guesses))

    elif valueguess < botchoice:
        guesses = guesses - 1
        messagebox.showwarning('Guess','Your answer is too small! You now have '+ str(guesses)+' guesses left! Try again!')
        guessesleft.config(text = 'Guesses Left: '+ str(guesses))

    else:
        messagebox.showinfo('Correct!','You guessed my number correct! Good job!')
        root.destroy()

    if guesses < 1:
        messagebox.showerror('You lost!','You lost! My number was '+ str(botchoice)+'! Try again next time!')
        root.destroy()

    
namequestion = Label(nameframe, text = 'What is your name?', fg = 'black', font = font1)
namequestion.grid(column = 0, row = 0)

nameanswer = Entry(nameframe, fg = 'black', font = font2)
nameanswer.grid(column = 0, row = 1)

confirmname = Button(nameframe, text = 'Confirm', command = startgame, fg = 'black', font = font1)
confirmname.grid(column = 0, row = 2)

enternumber = Label(gameframe, text = 'Enter a value.', fg = 'black', font = font1)
enternumber.pack()

numberentry = Entry(gameframe, fg = 'black', font = font2)
numberentry.pack()

confirmvalue = Button(gameframe, text = 'Confirm', command = guessgame, fg = 'black', font = font2)
confirmvalue.pack()

guessesleft = Label(gameframe, text = 'Guesses Left: '+ str(guesses), fg = 'black', font = font2)
guessesleft.pack()

root.mainloop()