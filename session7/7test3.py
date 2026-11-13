from tkinter import *

window=Tk()
window.title("Sign up")
window.minsize(500, 300)

NameLbael=Label(window, text="Name : ").grid(column=1,row=0)
PasswordLabel=Label(window, text="Enter Password : ").grid(column=1,row=2)
ConfirmLabel=Label(window, text="Confirm Paswword : ").grid(column=1,row=4)
NameEntry=Entry(window, width= 50).grid(column=2,row=0)
PasswordEntry=Entry(window, width= 50).grid(column=2,row=2)
ConfirmEntry=Entry(window, width= 50).grid(column=2,row=4)

singupbutton=Button(window, text="Signup",width=15).grid(column=2,row=5)
closeButton=Button(window, text="Close",width=15).grid(column=2,row=6)
window.mainloop()