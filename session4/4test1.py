class Aircraft(object):
    def __init__(self, name, model, capacity, speed, engines):
        self.name=name
        self.model=model
        self.capacity=capacity
        self.speed=speed
        self.engines=engines

    def Fly(self):
        print("This aircraft can fly")

    def Info(self):
        print("The make: {}\nand model: {}".format(self.name, self.model))

    def runwayLength(self, length):
        print("The runway needed for a {} {} is {}".format(self.name, self.model, length))

class Civilian(Aircraft):
    def __init__(self, name, model, capacity, speed, engines, wings):
        super().__init__(name, model, capacity, speed, engines,)
        self.wings=wings

    def passengerSeats(self):
        print("Civilian aircraft have more seats")

    def wingspan(self):
        print("The wingspan for a {} {} is {}".format(self.name, self.model, self.wings))
    

class Fighter(Aircraft):
    def Stealth(self):
        print("The {} {} can operate in a stealth regime".format(self.name,self.model))    



Airbus=Civilian("Airbus","A320neo",190,340,"CFM LEAP", "35m")

Airbus.Fly()
Airbus.passengerSeats()
Airbus.Info()
Airbus.runwayLength("2.2km")
Airbus.wingspan()

F18=Fighter("Boeing","Super Hornet",1,980,"GE F414-GE-400")
F18.Fly()
F18.Stealth()
F18.runwayLength("1km")



