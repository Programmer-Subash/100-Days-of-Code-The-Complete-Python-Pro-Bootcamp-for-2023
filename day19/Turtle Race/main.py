import random
from turtle import Turtle, Screen

screen = Screen()
WIDTH = screen.window_width()
colors = ['blue', "green", 'red', 'grey', 'yellow']
staring_y_position = [-200, -100, 00, 100, 200]

user_bet_turtle = screen.textinput(title="Make your bet", prompt=f"Who will win the race? \n{','.join([x.capitalize() for x in colors])}\nChoose a color").lower()

turtles = []
for i in range(5):
    t = Turtle()
    t.shape("turtle")
    t.penup()
    t.color(colors[i])
    t.goto(-400, staring_y_position[i])
    turtles.append(t)


def move_forward(t: Turtle):
    step = random.randint(1, 10)
    t.forward(step)


def check_winner(t: Turtle) -> bool:
    """take a turtle object and return True if is cross final position
    :type t: Turtle object
    """
    x = t.pos()[0]
    if x >= WIDTH / 2 - 100:
        return True
    else:
        return False


def draw_finishing_line():
    tur = Turtle()
    tur.hideturtle()
    tur.pensize(2)
    tur.pencolor("red")
    tur.penup()
    tur.goto(380, 250)
    tur.setheading(270)
    tur.pendown()
    tur.forward(500)


draw_finishing_line()
winner: Turtle = None
is_race_off = False
while not is_race_off:
    for t in turtles:
        move_forward(t)
        is_race_off = check_winner(t)
        if is_race_off:
            winner = t
            break

screen.mainloop()
winner_turtle_color = winner.pencolor()
if winner_turtle_color == user_bet_turtle:
    print(f"You win. The {winner_turtle_color} turtle is the winner.")
else:
    print(f"You lose. The {winner_turtle_color} turtle is the winner.")
