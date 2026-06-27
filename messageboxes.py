from tkinter import *
from tkinter import messagebox

root = Tk()

messagebox.showinfo('Info','Information')
messagebox.showerror('Error','Error')
messagebox.showwarning('Warning', 'Warning')
print(messagebox.askquestion('Are you sure?','Are you sure?')) #stores 'yes' or 'no'
print(messagebox.askokcancel('Would you like to...','Would you like to go through with this?')) #stores 'true' or 'false'
print(messagebox.askyesno('Are you sure?','Are you sure?')) #stores 'true' or 'false'
print(messagebox.askretrycancel('Error','There was an error in your request. Would you like to retry?')) #stores 'true' or 'false'

root.mainloop()