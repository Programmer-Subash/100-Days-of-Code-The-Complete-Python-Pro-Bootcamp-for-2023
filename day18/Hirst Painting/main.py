import os
import colorgram
import random
from turtle import Turtle, Screen

path = os.path.join("Image", "download.jpeg")
colors_object = colorgram.extract(path, 200)

colors = []
for i in colors_object:
    colors.append(i.rgb)

t = Turtle()
t.speed(1000)

screen = Screen()
screen.colormode(255)
screen.setworldcoordinates(0, 0, 1000, 1200)
WIDTH = screen.window_width()
HEIGHT = screen.window_height()

x, y = t.pos()
while y < HEIGHT:
    t.hideturtle()
    x,y = t.pos()
    t.pendown()
    t.dot(10, random.choice(colors))
    t.penup()
    t.forward(30)
    if x > WIDTH:
        t.setpos(0, y+40)

screen.mainloop()
