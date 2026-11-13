from tkinter import *

window = Tk()
window.title("aah")
window.minsize(width=500, height=300)

label=Label(window, text="I am a label", font=("Arial 24 bold"),fg="red").pack()
button=Button(window, text="I am button").pack()
entry=Entry(window, width=30).pack()
checkButton=Checkbutton(window, text="yes,", bg="orange", bd=1).pack()


window.mainloop()