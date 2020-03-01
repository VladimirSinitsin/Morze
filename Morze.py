from tkinter import *
import time
import pygame

from coder import morze

window = Tk()
window.title("Morze")
window.geometry('1000x600+450+250')

pygame.init()
pygame.mixer.music.load("beep.mp3")

message = StringVar()

lbl = Label(window, text="HELL0 MY FRIEND", font=("Fira Mono OT", 50))
lbl.place(x=200, y=50)

runl = Label(window, font=("Fira Mono OT", 20))
runl.place(x=300, y=200)
runl.focus()

txt = Entry(window, textvariable=message, font=("Fira Mono OT", 10), width=75)
txt.place(x=200, y=300)			

def show():
	text = ' ' * 25 + morze(message.get())
	for i in range(len(text)-24):
		time.sleep(0.4)
		if (text[i+24] == '.'):
			runl.config(text=text[i:i+25])
			pygame.mixer.music.play()
			time.sleep(0.1)
		elif(text[i+24] == '-'):
			pygame.mixer.music.play()
			time.sleep(0.2)
			pygame.mixer.music.play()
			runl.config(text=text[i:i+25])
			time.sleep(0.1)
		runl.update()
		
def show_message():
    lbl.config(text=message.get())

btn = Button(text="Text.ToMorze()", command=show)
btn.place(x=450, y=350)

window.mainloop()
