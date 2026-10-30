#sets the format to be a clear background, to format the Command Line Interface easily.
print("\33[1m")
#create the class with which to do methods with
#these can be called to do anything to a book.
class Book(object):
    #creates lists to store all created books
    #two lists, one to store available books
    #one to store borrowed books
    #so that they can be stored easily without being deleted
    AvailBookList=[]
    borrowedBookList=[]
    def __init__(self):
        pass
#simple method to output all in the available list
# #mostly for testing, but was intergrated into the actual solution for ease  
    def AllAvail(cls):
        print(cls.AvailBookList)
#method to add to the available list, and take off the borrowed list
#this shcould only be called if the book has been borrowed already
    def AddToAvail(cls, bookToBorrow):
        cls.AvailBookList.append(bookToBorrow)
        cls.borrowedBookList.remove(bookToBorrow)
#opposite thing, swapping from borrowed to available list
#again, should only be used for existing items
    def MakeUnavail(cls, bookToRemove):
        cls.AvailBookList.remove(bookToRemove)
        cls.borrowedBookList.append(bookToRemove)
#takes inputs for a book's data, adds to the available list
    def AddBook(cls):
        newBookTitle=input("Enter new Book's title here: ")
        newBookAuthor=input("Enter new Book's author here: ")
        newBookID=input("Enter new Book's ID here: ")
        newBookTuple=[newBookTitle, newBookAuthor, newBookID]
        cls.AvailBookList.append(newBookTuple)
#takes a books' ID and finds it in the available list
#if it exists in the available list, call the AddToAvail() method
#otherwise, do not borrow
    def BorrowBook(cls):
        AvailableCheck=False
        BorrowedBook=input("Enter the book ID you would like to borrow:\n")
        ItemCounter=0
        while ItemCounter<len(cls.AvailBookList):
            currentBook=cls.AvailBookList[ItemCounter]
            if BorrowedBook != currentBook[2]:
                ItemCounter=ItemCounter+1
            else:
                print("Found in the Available Books")
                AvailableCheck=True
                break
        if AvailableCheck==True:
            Book.MakeUnavail(Book, currentBook)
            #Book.AddToAvail(Book, currentBook)
            print("\33[32m",Book.AvailBookList,"are currently available\33[00m")
            print("\33[91m",Book.borrowedBookList,"are currently unavail\33[00m")
        else:
            print("\33[32mThis book could not be found to borrow\33[00m")
#does the same thing, finding in the borrowed list, and calls the AddToAvail() method to swap it into the available list
    def ReturnBook(cls):
        AvailableCheck=False
        BorrowedBook=input("Enter the book ID you would like to return:\n")
        ItemCounter=0
        while ItemCounter<len(cls.borrowedBookList):
            currentBook=cls.borrowedBookList[ItemCounter]
            if BorrowedBook != currentBook[2]:
                ItemCounter=ItemCounter+1
            else:
                print("Found in the borrowed Books")
                AvailableCheck=True
                break
        if AvailableCheck==True:
            #Book.MakeUnavail(Book, currentBook)
            Book.AddToAvail(Book, currentBook)
            print("\33[32m",Book.AvailBookList,"are currently available\33[00m")
            print("\33[91m",Book.borrowedBookList,"are currently unavail\33[00m")
        else:
            print("This book was not able to be returned")
#basic function to take an input and call the next method,
#depending on what is needed by the user
nextInput="go"
print("\33[34m=====LIBRARY MANAGEMENT SYSTEM=====\33[00m")
while nextInput !="end":
    nextInput=input("What would you like to do next?\n").lower()
    if nextInput=="add" or nextInput=="a":
        Book.AddBook(Book)
    elif nextInput=="view available" or nextInput=="va":
        Book.AllAvail(Book)
    elif nextInput=="borrow" or nextInput=="b":
        Book.BorrowBook(Book)
    elif nextInput=="return" or nextInput=="r":
        Book.ReturnBook(Book)
#===========STORE FOR COLOUR CODES FOR FORMATTING
#\33[00m
#white text
#\33[32m
#green
#\33[91m
#red
#\33[34m
#blue