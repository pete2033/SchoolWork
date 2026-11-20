from tkinter import *
from tkinter import ttk
from time import sleep

#import statements for tkinter
#and ttk for some extra stuff
window =Tk()
window.title("Hotel Management")
window.geometry("500x500")
#setting up the window
#neccessary

MainMenuFrame=Frame(window)
MainMenuFrame.grid(column=0, row=0, padx=5, pady=5)
#for grid.forget() to work properly these have to be .grid on a seperate line
BookingFrame=Frame(window)
BookingFrame.grid(column=0, row=0, padx=5, pady=5)
labelBkngMnu=Label(BookingFrame, text="Room Booking").grid(row=0, column=0)
BookingFrame.grid_forget()
#menus other than main menu should also be hidden immediately
#as to only display the main menu,
#can be placed in the same space

AvailRoomFrame=Frame(window)
AvailRoomFrame.grid(column=0, row=0, padx=5, pady=5)
labelAvailRooms=Label(AvailRoomFrame, text="Rooms currently available are").grid(row=0, column=0)
AvailRoomFrame.grid_forget()

def BookingMenu():
    print("Booking Button pressed")
    BookingFrame.grid()
    MainMenuFrame.grid_forget()

def AvailRoomMenu():
    print("Avail Room Button pressed")
    AvailRoomFrame.grid()
    MainMenuFrame.grid_forget()

def ShowMainMenu():
    AvailRoomFrame.grid_forget()
    BookingFrame.grid_forget()
    MainMenuFrame.grid()
    print("Main Menu Button pressed")

BookingButton=Button(MainMenuFrame, text="Book", width=30, height=10,command=lambda:BookingMenu()).grid(row=0, column=0)
spacer1=(ttk.Separator(MainMenuFrame, orient="horizontal").grid(row=0, column=1))
AvailRoomButton=(Button(MainMenuFrame, text="See Available Rooms", width=30, height=10,command=lambda:AvailRoomMenu()).grid(row=0, column=2))

MainMenuButtonBKNGMNU=Button(BookingFrame, text="MainMenu", width=30, height=5, command=lambda:ShowMainMenu())
MainMenuButtonBKNGMNU.grid(row=4, column=0)

MainMenuButtonAVLRMS=Button(AvailRoomFrame, text="MainMenu", width=30, height=5, command=lambda:ShowMainMenu())
MainMenuButtonAVLRMS.grid(row=4, column=0)

window.mainloop()