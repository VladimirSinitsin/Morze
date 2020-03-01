from tkinter import *
import time

window = Tk()
window.title("Morze")
window.geometry('1000x600+450+250')

message = StringVar()

lbl = Label(window, text="HELL0 MY FRIEND", font=("Fira Mono OT", 50))
lbl.place(x=200, y=50)

txt = Entry(window, textvariable=message, font=("Fira Mono OT", 10), width=75)
txt.place(x=200, y=300)

def show():
	text = ' ' * 10 + message.get()
	for i in range(len(text)):
		time.sleep(0.3)
		lbl.config(text=text[i:i+10])
		
def show_message():
    lbl.config(text=message.get())

btn = Button(text="Text.ToMorze()", command=show)
btn.place(x=450, y=350)

window.mainloop()
