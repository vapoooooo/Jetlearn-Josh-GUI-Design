from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

root = Tk()

contactlist = {}

def adddetails():
    name = nameentry.get()
    if name != '':
        address = addressentry.get()
        mobile = mobileentry.get()
        email = emailentry.get()
        birthday = birthdayentry.get()
    else:
       showerror('error','You have not defined a name!')

topframe = Frame(root) #--------------------------------------------- topframe -------------------------------------------------------------------------------------------
topframe.pack()

filename = Label(topframe, text = 'address')
filename.grid(row = 0, column = 0, columnspan = 3)

middleframe = Frame(root) #------------------------------------------- middleframe ------------------------------------------------------------------------------------------
middleframe.pack()

filelist = Listbox(middleframe)
filelist.grid(row = 0, column = 2, rowspan = 5, padx = 15)

namelabel = Label(middleframe, text = 'Name: ')
namelabel.grid(row = 0, column = 0)

nameentry = Entry(middleframe)
nameentry.grid(row = 0, column = 1)

addresslabel = Label(middleframe, text = 'Address: ')
addresslabel.grid(row = 1, column = 0)

addressentry = Entry(middleframe)
addressentry.grid(row = 1, column = 1)

mobilelabel = Label(middleframe, text = 'Mobile: ')
mobilelabel.grid(row = 2, column = 0)

mobileentry = Entry(middleframe)
mobileentry.grid(row = 2, column = 1)

emaillabel = Label(middleframe, text = 'Email: ')
emaillabel.grid(row = 3, column = 0)

emailentry = Entry(middleframe)
emailentry.grid(row = 3, column = 1)

birthdaylabel = Label(middleframe, text = 'Birthday: ')
birthdaylabel.grid(row = 4, column = 0)

birthdayentry = Entry(middleframe)
birthdayentry.grid(row = 4, column = 1)

bottomframe = Frame(root) #---------------------------------------- bottomframe ----------------------------------------------------------------------------------------------
bottomframe.pack()

addupdate = Button(bottomframe, text = 'Add/Update', command = adddetails)
addupdate.grid(row = 0, column = 0, columnspan = 2, pady = 5)

editbutton = Button(bottomframe, text = 'Edit')
editbutton.grid(row = 1, column = 0, padx = 20)

deletebutton = Button(bottomframe, text = 'Delete')
deletebutton.grid(row = 1, column = 1, padx = 20)

openfile = Button(bottomframe, text = 'Open')
openfile.grid(row = 0, column = 2, rowspan = 2, padx = 15)

savebutton = Button(bottomframe, text = 'Save')
savebutton.grid(row = 0, column = 3, rowspan = 2)

root.mainloop()