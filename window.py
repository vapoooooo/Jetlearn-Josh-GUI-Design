from tkinter import * #* = everything

root = Tk() #start

root.geometry('512x512') #size
root.config(background = 'grey') #configers the window
root.title('menu thing')  #gives title to the window

buttonn = Button(root, text= 'close', command= root.destroy, width= 20, height = 5) #makes a button (parent node first)     //    text='close' means that button is named 'close'     //     command = root.destroy means that when you click the button it will close the root
buttonn.pack(side= BOTTOM, pady= 50) #puts button to assigned location      //      padx and pady creates a small barrier between the button and the border of the window

root.mainloop() #end
