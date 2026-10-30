class Animal(object):
    def __init__(self, name, legs):
        self.name=name
        self.legs=legs

    def walk(self):
        print("All animals can walk")


zebra=Animal("Zebra", 4)

class Dog(Animal):
    def __init__(self, name, legs, eyes):
        super().__init__(name, legs)
        self.eyes=eyes

    def howmanyeyes(self):
        print(self.eyes)


dog=Dog("dog", 4, 2)

#dog.walk()
#dog.howmanyeyes()


class Screensize(object):
    def __init__(self, height, width):
        self.height=height
        self.width=width

    def showScreensize(self):
        print("Height={}\nWidth={}".format(self.height, self.width))

class Display(object):
    def __init__(self, Density, colour):
        self.Density=Density
        self.colour=colour

    def showDisplay(self):
        print("Pixel Density={}\nColour={}".format(self.Density, self.colour))

class TV(Screensize, Display):
    def __init__(self, height, width, Density, colour, tvname):
        Screensize.__init__(self,height, width)
        Display.__init__(self, Density, colour)
        self.tvname=tvname

    def DisplayInfo(self):
        print("child class of screensize and display")

tele1=TV(1440, 1220, "4K", "Full Range", "Samsung")
tele1.DisplayInfo()


