from turtle import Turtle, Screen
import random

t = Turtle()
t.speed(100)
t.pensize(2)

screen = Screen()
screen.colormode(255)

for i in range(120):
    if i % 2 == 0:
        t.pencolor((252, 237, 218))
    else:
        t.pencolor((238, 78, 52))
    t.right(3)
    t.circle(150)

screen.mainloop()
