import random
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.colormode(255)

def draw_shape(side,length):
    angle = 360 / side
    for _ in range(side):
        t.forward(140)
        t.right(angle)


t.pensize(5)
for i in range(3,11):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    t.pencolor((r, g, b))
    draw_shape(i,120)


screen.mainloop()
