from tkinter import *

root = Tk()

scroller = Scrollbar(root)
scroller.pack(side = LEFT, fill = Y)

lists = Listbox(root, yscrollcommand = scroller.set)
lists.pack()

scroller.config(command = lists.yview)

for i in range(25):
    lists.insert(END, i + 1)

root.mainloop()