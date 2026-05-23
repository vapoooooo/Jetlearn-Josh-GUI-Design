from tkinter import *

def login():
    print('login successful')
    logins.config(text = 'Login Successful, welcome '+ usernamee.get()+'.')
    logins.place(x = 300, y = 300)

root = Tk()

root.geometry('800x512')
root.config(background = 'grey')
root.title('login')

username = Label(root, text= 'Username')     #makes text on the window
username.place(x = 100, y = 100)        #place helps align features in specific areas

password = Label(root, text= 'Password')
password.place(x = 100, y = 200)


logins = Label(root)



usernamee = Entry(root, width = 50)      #makes widget where you can type into
usernamee.place(x = 250, y = 100)

passwordd = Entry(root, width = 50)
passwordd.place(x = 250, y = 200)



close = Button(root, text = 'Cancel', command = root.destroy, width = 20, height= 5)
close.place(x = 150, y = 350)

login = Button(root, text = 'Login', command = login, width = 20, height= 5)
login.place(x = 500, y = 350)

root.mainloop()