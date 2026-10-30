class Employee(object):
    companyname="Micrsoft"
    manager="J. Bond"
    def __init__(self, name, id, salary):
        self.name=name
        self.id=id
        self.salary=salary

    def show(self):
        print("The employee",self.name,"is ID no.:",self.id,",and has a salary of",self.salary)

    def department(x):
        print("Static method output is department",x)


emp1=Employee("J. Smith", 203, 30000)
#emp2=Employee("J. Doe",658, 20000)
#emp2.show()

#emp2=Employee()
Employee.department("Hr")

class TV(object):
    def __init__(self, brand, size, resolution):
        self.brand=brand
        self.size=size
        self.resolution=resolution

    def model(y):
        print("The model of this TV is:",y)


Tele1=TV("Samsung",50, "4K")
TV.model("SM590")
        


