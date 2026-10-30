class Circle(object):
    def __init__(self, size, area):
        self.size=size
        self.area=area

    def __add__(self, other):
        return(self.area+other.area)

C1=Circle(4)
C2=Circle(10)

print(C1+C2)