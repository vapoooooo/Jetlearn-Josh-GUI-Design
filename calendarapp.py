from tkinter import *
import calendar
import datetime 

def opencalendar():

    calendarar = Tk()

    year = int(yeartype.get())
    calendardata = calendar.calendar(year)

    calendaroutput = Text(calendarar, height = 40)

    currentdate = datetime.datetime.now()
    currentdate = currentdate.strftime('%d-%m-%y')
    currentday = Label(calendarar, text = 'Current day: '+str(currentdate)+'.')
    currentday.place(x = 250, y = 600)

    calendaroutput.pack(padx = 20, pady = 20)
    calendaroutput.insert(END, calendardata)

    calendarar.mainloop()
 
root = Tk()#FFD6EF

root.geometry('612x400')
root.config(background='#B572ED')
root.title('Calendar')

caltitle = Label(root, text= 'Calendar', width= 15, height = 3, bg = '#FFD6EF')
caltitle.place(x = 256, y = 100)

yearr = Label(root, text = 'Enter Year', bg = '#FFD6EF')
yearr.place(x = 280, y = 165)

yeartype = Entry(root, width = 15)
yeartype.place(x = 263, y = 200)

showyear = Button(root, text = 'Show Calendar', command = opencalendar, bg = '#FFD6EF')
showyear.place(x = 266, y = 240)

exitt = Button(root, text = 'Exit', command = root.destroy, bg = '#E85A7F', width = 8) #'command = exit' closes all windows associated with root
exitt.place(x = 276, y = 275)

root.mainloop()