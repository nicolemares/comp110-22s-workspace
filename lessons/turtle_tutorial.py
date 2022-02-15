
from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(-360, 325)
leo.pendown()
colormode(255)
leo.color(249, 240, 96)

i: int = -350
while i <= 350:
    leo.left(45)
    leo.forward(10)
    leo.right(35)
    leo.forward(2.5)
    leo.right(55)
    leo.forward(7)
    leo.left(190)
    leo.forward(5)
    leo.left(90)
    leo.forward(8)
    leo.setheading(0.0)
    leo.forward(25)
    i = i + 25
    
done()


leo.begin_fill()
n: int = 0
while (n < 3):
    leo.forward(300)
    leo.left(120)
    n += 1
leo.end_fill()
leo.speed(50)


bob: Turtle = Turtle()

colormode(255)
bob.color(43, 41, 16)

side_length: float = 300.00

i: int = 0
while (i < 99):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
    side_length = side_length * 0.97