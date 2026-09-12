from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import os 

root = Tk()

contactlist = {}

# address, mobile, email, birthday

def adddetails():
    name = nameentry.get()
    if name != '':
        address = addressentry.get()
        mobile = mobileentry.get()
        email = emailentry.get()
        birthday = birthdayentry.get()

        if name not in contactlist:
            filelist.insert(END, name)

        contactlist[name] = [address, mobile, email, birthday]
        print(contactlist)
        clearentries()

    else:
       showerror('error','You have not defined a name!')

def clearentries():
    nameentry.delete(0, END)
    addressentry.delete(0, END)
    mobileentry.delete(0, END)
    emailentry.delete(0, END)
    birthdayentry.delete(0, END)

def resetapp():
    clearentries()
    filelist.delete(0, END)
    contactlist.clear()
    filename.config(text = 'address')

def editkey():
    clearentries()
    selected = filelist.curselection()
    if selected:
        selectedname = filelist.get(selected)
        nameentry.insert(0, selectedname)
        details = contactlist.get(selectedname)
        addressentry.insert(0, details[0])
        mobileentry.insert(0, details[1])
        emailentry.insert(0, details[2])
        birthdayentry.insert(0, details[3])
    else:
        showerror('error','You have not selected a value from the list!')

def deletevalue():
    selected = filelist.curselection()
    if selected:
        selectedname = filelist.get(selected)
        del contactlist[selectedname] #deletes key value from dictionary
        filelist.delete(selected)
        print(contactlist)

    else:
        showerror('error','You have not selected a value from the list!')

def savefile():
    filesave = asksaveasfile(defaultextension = '.txt')
    if filesave is not None:
        print(contactlist, file = filesave)
        resetapp()
    else:
        showerror('error','File not saved.')

def openfiles():
    global contactlist
    fileread = askopenfile(filetypes = [('Text Document', '.txt')])

    if fileread is not None:
        resetapp()
        contactlist = eval(fileread.read()) #evaluates the type of value you are reading

        for name in contactlist:
            filelist.insert(END, name)

        print(contactlist)

        filename.config(text = os.path.basename(fileread.name))

    else:
        showerror('error','File not opened.')


topframe = Frame(root) #--------------------------------------------- topframe -------------------------------------------------------------------------------------------
topframe.pack()

filename = Label(topframe, text = 'address')
filename.grid(row = 0, column = 0, columnspan = 3)

middleframe = Frame(root) #------------------------------------------- middleframe ------------------------------------------------------------------------------------------
middleframe.pack()

filelist = Listbox(middleframe) # listbox --|0
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

editbutton = Button(bottomframe, text = 'Edit', command = editkey)
editbutton.grid(row = 1, column = 0, padx = 20)

deletebutton = Button(bottomframe, text = 'Delete', command = deletevalue)
deletebutton.grid(row = 1, column = 1, padx = 20)

openfile = Button(bottomframe, text = 'Open', command = openfiles)
openfile.grid(row = 0, column = 2, rowspan = 2, padx = 15)

savebutton = Button(bottomframe, text = 'Save', command = savefile)
savebutton.grid(row = 0, column = 3, rowspan = 2)

root.mainloop()
