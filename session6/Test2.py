import turtle
oogway=turtle.Turtle()

oogway.right(90)
oogway.forward(130)
oogway.left(60)
oogway.backward(100)
oogway.color("light green")

oogway.goto(0,0)
oogway.circle(60)
oogway.color("black")
oogway.dot(15)


pyxiss=turtle.Turtle()
for i in range(4):
    pyxiss.fd(50)
    pyxiss.rt(90)

pyxissthesequel=turtle.Turtle()
for i in range(5):
    pyxiss.fd(50)
    pyxiss.rt(144)

colors=["red","purple","blue","green","darkolivegreen","darksalmon"]
gay=turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
    gay.pencolor(colors[x%6])
    gay.width(x/100 +1)
    gay.forward(x)
    gay.left(59)

oogway.clear()
pyxiss.clear()
pyxissthesequel.clear()

galaxy=turtle.Screen()

for i in range (30):
    turtle.circle(5*i)
    turtle.color("red")
    turtle.circle(-5*i)
    turtle.color("blue")
    turtle.left(i)

galaxy.clear()

turtle.mainloop()

print("test")
