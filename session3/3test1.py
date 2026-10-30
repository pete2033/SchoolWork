class Car:
    make="Mercedes"
    model="S-Class"
    Year=2019
    manual=False
    colour="Blue"

mycar=Car()
print(mycar.colour)

mycar.colour="Grey"
print(mycar.colour)



class vehicle(object):
    def __init__(self, make, model, year, colour, manual, speed):
        self.make=make
        self.model=model
        self.year=year
        self.colour=colour
        self.manual=manual
        self.speed=speed


    def accelerate(self):
        self.speed=self.speed + 10
        print("Vehicles speed has increased to",self.speed)

    def SlowDown(self):
        self.speed=self.speed-10
        print("Vehicles speed has slowed to",self.speed)

    def SetColour(self,clrIN):
        self.colour=clrIN

    def GetAttribute(self, Attribute):
        print(Attribute)
        #print(self.)
        
firstTest=vehicle("Cessna",172, 1955, "White", False, 0)

firstTest.accelerate()
firstTest.SlowDown()
firstTest.SetColour("Blue")
firstTest.GetAttribute("colour")

        