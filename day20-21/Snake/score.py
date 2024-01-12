from turtle import Turtle


class Score(Turtle):

    def __init__(self, height):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, height / 2 - 40)

    def update_score(self, new_score):
        self.score += new_score
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))

    def get_score(self):
        return self.score
