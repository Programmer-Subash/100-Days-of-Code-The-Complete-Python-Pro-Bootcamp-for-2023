import random
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score


class SnakeGame:

    def __init__(self, width: int, height: int, title: str = "Snake Game", bg_color: str = "black",
                 snake_color: str = "white"):
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = Screen()
        self.screen.setup(self.WIDTH, self.HEIGHT)
        self.screen.bgcolor(bg_color)
        self.screen.title(title)
        self.screen.tracer(0)
        self.screen.colormode(255)
        self.snake = Snake(snake_color=snake_color)
        self.food = Food(width=self.WIDTH, height=self.HEIGHT, food_color="green")
        self.score = Score(self.HEIGHT)

    def game_loop(self):
        self.snake.create_snake()
        self.food.refresh()
        is_game_over = False
        while not is_game_over:
            self.score.scoreboard()
            self.screen.update()
            time.sleep(0.09)

            self.screen.onkey(fun=self.snake.move_up, key='Up')
            self.screen.onkey(fun=self.snake.move_down, key='Down')
            self.screen.onkey(fun=self.snake.move_right, key='Right')
            self.screen.onkey(fun=self.snake.move_left, key='Left')
            self.screen.listen()
            self.snake.move_snake_body()

            # detect collision with food
            if self.snake.segments[0].distance(self.food) <= 25:
                self.food.refresh()
                self.score.update_score(1)
                self.snake.extend_snake()

            # detect collision with wall
            x, y = self.snake.segments[0].pos()
            if x < -self.WIDTH / 2 + 10 or x > self.WIDTH / 2 - 10 or y < -self.HEIGHT / 2 + 10 or y > self.HEIGHT / 2 - 10:
                is_game_over = True
                self.score.game_over()

            # detect collision with tail
            for segment in self.snake.segments[1:]:
                if self.snake.segments[0].distance(segment) < 5:
                    is_game_over = True
                    self.score.game_over()
