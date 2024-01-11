import turtle
from turtle import Turtle,Screen
import random

t = Turtle()
t.pensize(10)
t.speed(100)

screen = Screen()
screen.colormode(255)


def random_walk():
    angle = random.randint(0,3) * 90
    t.setheading(angle)
    t.forward(30)


def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    t.pencolor((r,g,b))


while True:
    random_color()
    random_walk()


screen.mainloop()