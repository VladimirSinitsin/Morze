from tkinter import *

window = Tk()
window.title("Morze")
window.geometry('1000x600+450+250')

lbl = Label(window, text="HELL0 MY FRIEND", font=("Fira Mono OT", 50))
lbl.place(x=200, y=50)

txt = Entry(window,font=("Fira Mono OT", 10), width=10)
txt.place(x=200, y=150)

window.mainloop()
