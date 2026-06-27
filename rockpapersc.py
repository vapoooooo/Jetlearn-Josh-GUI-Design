from tkinter import *
import tkinter.font as fo #font
import random

root = Tk()

root.geometry('800x512')
root.title('Rock Paper Scissors')

possiblechoices = ['rock','paper','scissors']

pscore = 0
cscore = 0

def playgame(playinput):
    global pscore, cscore
    computerinput = random.choice(possiblechoices)

    if playinput == computerinput:
        result = 'Tie.'

    elif (playinput == 'paper' and computerinput == 'scissors') or (playinput == 'rock' and computerinput == 'paper') or (playinput == 'scissors' and computerinput == 'rock'):
        result = 'You lose...'
        cscore += 1
        compscore.config(text = cscore)

    else:
        result = 'You win!'
        pscore += 1
        playscore.config(text = pscore)

    playerchoice.config(text = 'PLAYER CHOSE: '+ playinput)
    botchoice.config(text = 'COMPUTER CHOSE: '+ computerinput)
    results.config(text = 'Results: '+ result)
    


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

topframe = Frame(root) #code for topframe under here
topframe.pack()

font1 = fo.Font(family = 'Ariel', size = 20, weight = 'normal')

font2 = fo.Font(family = 'Ariel', size = 20, weight = 'bold')

title = Label(topframe, text = 'Rock Paper Scissors', fg = 'grey', font = ('Ariel', 30, 'bold'))
title.grid(row = 0, column = 0, columnspan = 2, padx = 50) #row = horizontal, column = vertical, columnspan = how many columns the widget will take over in the grid

# ---------------------------------------------------------------------------------------------

selectop = Label(topframe, text = 'Select an option:', fg = 'grey', font = ('Ariel', 25))
selectop.grid(row = 1, column = 0, columnspan = 2, pady = 20)

# ---------------------------------------------------------------------------------------------

compscoretitle = Label(topframe, text = 'CPU:', fg = 'grey', font = font1) #the labels for the score (not the score itself)
compscoretitle.grid(row = 0, column = 2)

playscoretitle = Label(topframe, text = 'PLA:', fg = 'grey', font = font1) #the labels for the score (not the score itself)
playscoretitle.grid(row = 1, column = 2)

# --------------------------------------------------------------------------------------------

compscore = Label(topframe, text = '0', fg = 'red', font = font2) #scores themselves
compscore.grid(row = 0, column = 3)

playscore = Label(topframe, text = '0', fg = 'blue', font = font2) #scores themselves
playscore.grid(row = 1, column = 3)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

middleframe = Frame(root) #code for middleframe under here
middleframe.pack(pady = 20)

rockwidget = Button(middleframe, text = 'Rock', bg = 'grey', fg = 'white', font = font2, width = 8, command = lambda:playgame('rock')) #buttons for rock, paper, scissors
rockwidget.grid(row = 0, column = 0, padx = 20)

paperwidget = Button(middleframe, text = 'Paper', bg = 'grey', fg = 'white', font = font2, width = 8, command = lambda:playgame('paper'))
paperwidget.grid(row = 0, column = 1, padx = 20)

scissorswidget = Button(middleframe, text = 'Scissors', bg = 'grey', fg = 'white', font = font2, width = 8, command = lambda:playgame('scissors'))
scissorswidget.grid(row = 0, column =  2, padx = 20)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bottomframe = Frame(root) #code for bottomframe here
bottomframe.pack()

results = Label(bottomframe, text = 'Results: ', fg = 'grey', font = font2)
results.grid(row = 0, column = 0, columnspan = 3, pady = 25)

botchoice = Label(bottomframe, text = 'COMPUTER CHOSE: ', fg = 'grey', font = font1)
botchoice.grid(row = 1, column = 0, padx = 20)

playerchoice = Label(bottomframe, text = 'PLAYER CHOSE: ', fg = 'grey', font = font1)
playerchoice.grid(row = 1, column = 1, padx = 20)

root.mainloop()
