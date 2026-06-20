from tkinter import *
import tkinter.font as fo #font

root = Tk()

root.geometry('800x512')
root.title('Rock Paper Scissors')

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

compscoretitle = Label(topframe, text = 'COM:', fg = 'grey', font = font1) #the labels for the score (not the score itself)
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

rockwidget = Button(middleframe, text = 'Rock', bg = 'grey', fg = 'white', font = font2, width = 8) #buttons for rock, paper, scissors
rockwidget.grid(row = 0, column = 0, padx = 20)

paperwidget = Button(middleframe, text = 'Paper', bg = 'grey', fg = 'white', font = font2, width = 8)
paperwidget.grid(row = 0, column = 1, padx = 20)

scissorswidget = Button(middleframe, text = 'Scissors', bg = 'grey', fg = 'white', font = font2, width = 8)
scissorswidget.grid(row = 0, column =  2, padx = 20)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bottomframe = Frame(root) #code for bottomframe here
bottomframe.pack()

results = Label(bottomframe, text = 'Results: ', fg = 'grey', font = font2)
results.grid(row = 0, column = 0, columnspan = 3)

compresulttitle = Label(bottomframe, text = 'COM:', fg = 'grey', font = font2)


root.mainloop()