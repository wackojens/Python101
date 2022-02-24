from math import sqrt
import turtle, time

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(0,0)
p2 = Point(100,0)
p3 = Point(100,100)
p4 = Point(0,100)

s = turtle.getscreen()
t = turtle.Turtle()

"""t.goto(p1.x,p1.y)
t.goto(p2.x,p2.y)
t.goto(p3.x,p3.y)
t.goto(p4.x,p4.y)
t.goto(p1.x,p1.y)

t.lt(90)
t.circle(90)

t.rt(90)
t.fd(100)
t.rt(135)
length = int(sqrt((200*200)/2))
t.fd(length)
t.rt(90)
t.fd(length)
t.rt(135)
t.fd(100)"""

t.speed("fastest")

for i in range(0,750,5):
    t.fd(i)
    t.rt(70)

t.rt(180)

for i in range(750, 0, 5):
    t.fd(i)
    t.lt(71)

turtle.done()