class Pigeon():
    def fly(self):
        print("A pigeon can fly")
    def eat(self):
        print("A pigeon can eat")
    def run(self):
        print("a pigeon can sort of run")

class Sparrow():
    def fly(self):
        print("A Sparrow can fly")
    def eat(self):
        print("A sparrow can eat")
    def run(self):
        print("a sparrow can run")

pigeon=Pigeon()
sparrow=Sparrow()

for bird in (pigeon, sparrow):
    bird.run()
    bird.eat()
    bird.fly()



