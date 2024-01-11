from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(3)


def move_backward():
    t.backward(3)


def turn_left():
    t.setheading(t.heading() + 3)


def turn_right():
    t.setheading(t.heading() - 3)


def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.listen()

screen.mainloop()
