import random
from turtle import Turtle, Screen
import time


class Snake:

    def __init__(self, width: int, height: int, title: str = "Snake Game", bg_color: str = "black",
                 snake_color: str = "white"):
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = Screen()
        self.screen.setup(self.WIDTH, self.HEIGHT)
        self.screen.bgcolor(bg_color)
        self.screen.title(title)
        self.screen.tracer(0)
        self.snake = []
        self.change_x = 0
        self.change_y = 0
        self.snake_color = snake_color

    def create_snake(self):
        staring_position = [(0, 0), (-20, 0), (-40, 0)]
        for position in staring_position:
            segment = Turtle()
            segment.penup()
            segment.shape('square')
            segment.color(self.snake_color)
            segment.goto(position)
            self.snake.append(segment)

    def move_snake_body(self, x: float, y: float):
        """x ,y are coordinates"""
        for i in range(len(self.snake) - 1, 0, -1):
            first_segment = self.snake[i - 1]
            second_segment = self.snake[i]
            second_segment.goto(first_segment.position())
        self.snake[0].goto(x, y)

    def move_up(self):
        self.change_x = 0
        self.change_y = 20

    def move_down(self):
        self.change_x = 0
        self.change_y = -20

    def move_right(self):
        self.change_x = 20
        self.change_y = 0

    def move_left(self):
        self.change_x = -20
        self.change_y = 0

    def game_loop(self):
        self.create_snake()
        while True:
            self.screen.update()
            time.sleep(0.07)
            self.screen.onkey(fun=self.move_up, key='Up')
            self.screen.onkey(fun=self.move_down, key='Down')
            self.screen.onkey(fun=self.move_right, key='Right')
            self.screen.onkey(fun=self.move_left, key='Left')
            self.screen.listen()
            x, y = self.snake[0].pos()
            self.move_snake_body(x + self.change_x, y + self.change_y)


snake = Snake(width=600, height=600)
snake.game_loop()
