from tkinter import *
import speech_recognition as sr

root = Tk()

def recordspeech():
    recognition = sr.Recognizer()
    print('working1')
    with sr.Microphone() as source:
        print('working2')
        audiofile = recognition.listen(source)
        print('working3')
        try:
            textfile = recognition.recognize_google(audiofile)
            textentry.insert(END, textfile)
            print(textfile)
        except:
            textentry.insert(END, 'Sorry, we could not understand that.')
            print('not working')

root.config(bg='blue')

recordbutton = Button(root, text='Record Voice', command = recordspeech)
recordbutton.pack(side = LEFT, padx = 10)

textentry = Text(root, width = 25, height= 6)
textentry.pack(side= LEFT, pady = 20, padx = 20)

savetextbutton = Button(root, text = 'Save Text')
savetextbutton.pack(side = LEFT, padx = 10)

root.mainloop()