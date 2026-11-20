from tkinter import *
from tkinter import ttk
from time import sleep

window =Tk()
window.title("Hotel Management")
window.geometry("500x500")


MainMenuFrame=Frame(window)
MainMenuFrame.grid(column=0, row=0, padx=5, pady=5)


def BookingMenu():
    print("Booking Button pressed")
    MainMenuButton.grid()
    MainMenuFrame.grid_forget()

def AvailRoomMenu():
    print("Avail Room Button pressed")
    MainMenuButton.grid()
    MainMenuFrame.grid_forget()

def ShowMainMenu():
    MainMenuButton.grid_forget()
    MainMenuFrame.grid()
    print("Main Menu Button pressed")

BookingButton=Button(MainMenuFrame, text="Book", width=30, height=10,command=lambda:BookingMenu()).grid(row=0, column=0)
spacer1=(ttk.Separator(MainMenuFrame, orient="horizontal").grid(row=0, column=1))
AvailRoomButton=(Button(MainMenuFrame, text="See Available Rooms", width=30, height=10,command=lambda:AvailRoomMenu()).grid(row=0, column=2))

MainMenuButton=Button(window, text="MainMenu", width=30, height=5, command=lambda:ShowMainMenu())
MainMenuButton.grid(row=4, column=0)
MainMenuButton.grid_forget()

window.mainloop()