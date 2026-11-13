from tkinter import *


activity= Tk()

activity.title("activity")
activity.minsize(width=250, height=150)
window_colour="#328ab3"
activity.config(bg=window_colour)
namelabel=Label(activity, text="Name", bg="orange", fg="white", width=30).grid(column=0,row=0)
numlabel=Label(activity, text="Number",bg="orange", fg="white", width=30).grid(column=0,row=1)
nameEntry=Entry(activity, width=50).grid(column=1,row=0)
numEntry=Entry(activity, width=50).grid(column=1,row=1)

def printInput():
    print("h")
    
printButton=Button(activity, text="Print", command=printInput).grid(column=1,row=2)



activity.mainloop()

