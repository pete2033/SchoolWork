from tkinter import *

window = Tk()
window.title("aah")
window.minsize(width=500, height=300)

label=Label(window, text="I am a label", font=("Arial 24 bold"),fg="red").pack()
button=Button(window, text="I am button").pack()
entry=Entry(window, width=30).pack()
checkButton=Checkbutton(window, text="yes,", bg="orange", bd=1).pack()

tkvar=StringVar(window)
tkvar.set("Select")

optionmenu=OptionMenu(window, tkvar, "opt1","opt2","opt3").pack()

v="rad"
radio=Radiobutton(window, text="Python",padx=20, variable=v, value=1).pack()
radio1=Radiobutton(window, text="not",padx=20, variable=v, value=2).pack()

scroller=Scrollbar(window, orient=VERTICAL, command=Scrollbar.set).pack()
window.mainloop()


