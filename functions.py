from tkinter import *
from tkinter import ttk
from time import sleep
#import statements for tkinter
#and ttk for some extra stuff


class Room(object):
    NoOfRooms=50
    roomList=[(1,"",0,30,False, "premium"),(2,"",0,30,False,"standard"),(50, "", 0, 30, False, "standard")]
    #list format = ( roomNum,  Name,  NumberOfPeople,  RoomCost,   RoomBooked,  RoomType)
    #roomNum, RoomCost never need to be changed for that room
    #roomType also will not change for the room number
    def __init__(self, roomNum, Name, NumberOfPeople, RoomCost, RoomBooked, RoomType):
        self.roomNum = roomNum
        self.Name = Name
        self.NumberOfPeople = NumberOfPeople
        self.RoomCost = RoomCost
        self.RoomBooked= RoomBooked
        self.RoomType = RoomType



    def BookRoom(self, Name, NumberOfPeople):
        self.RoomBooked=True
        self.Name=Name
        self.NumberOfPeople=NumberOfPeople

    def CancelBooking(self, Name):
        self.RoomBooked=False
        self.Name=""
        self.NumberOfPeople=0

    def SaveChanges(self):
        roomList=[]




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


def createRoom():
    searchlist=Room.roomList
    print(searchlist)
    #print(searchlist[0][0])
    currentHighest=searchlist[0][0]
    counter=0
    while counter<len(searchlist):
        if searchlist[counter][0]>currentHighest:
            previousHighest=currentHighest
            currentHighest=searchlist[counter][0]
        counter+=1
#if all 50 rooms are booked, cannot book a new room
#will return an error statement to say no more
    if currentHighest==50:
        if previousHighest==50:
            print("No more rooms available")
            return
        else:
            currentHighest=previousHighest+1
#if room number is even, room type is standard
#if room number if odd, room type is premium
    if currentHighest%2==0:
        roomType="standard"
    else:
        roomType="premium"

    toAppend=(currentHighest,"",0, 30, False, roomType)
    Room.roomList.append(toAppend)
    Room.roomList.sort()
    print(Room.roomList)


createRoom()
window.mainloop()
