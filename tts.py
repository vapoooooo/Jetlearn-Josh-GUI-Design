from tkinter import *
from gtts import gTTS

root = Tk()

def createtts():
    audiofile = gTTS(inputtext.get(), lang = "en")
    audiofile.save(f'{nameinput.get()}.wav')

root.geometry('300x240')
title = Label(root, text = 'Text To Speech Software')
title.pack(padx = 50, pady = 35)

inputtext = Entry(root, width = 20)
inputtext.pack(padx = 50, pady = 25)

nameinput = Entry(root, width = 15)
nameinput.pack(padx = 50, pady = 10)

ttsbutton = Button(root, text = 'Create TTS File', command = createtts)
ttsbutton.pack(pady = 20)

root.mainloop()