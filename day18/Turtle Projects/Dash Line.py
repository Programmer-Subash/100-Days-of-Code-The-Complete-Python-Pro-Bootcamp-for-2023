from turtle import Turtle,Screen

t = Turtle()

for i in range(10):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)
screen = Screen()
screen.mainloop()