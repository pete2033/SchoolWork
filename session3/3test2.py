import time

class Human(object):
    def __init__(self, name, height, weight, haircolour, eyecolour):
        self.name=name
        self.height=height
        self.weight=weight
        self.haircolour=haircolour
        self.eyecolour=eyecolour

    def Blink(self):
        #colour=self.eyecolour
        #print(colour)
        print("( \33[37mo\33[00m )")#.format(colour))
        time.sleep(1)
        print("\n"*30)
        print("-----")
        time.sleep(1)
        print("\n"*30)
        print("( \33[37mo\33[00m )")#.format(colour))


adam=Human("Adam",1.75,70,"Brown","Brown")
eve=Human("Eve",1.60,55,"Blonde","Green")
Dr=Human("J.Smith",1.70,65,"Brown","Blue")

Dr.Blink()
