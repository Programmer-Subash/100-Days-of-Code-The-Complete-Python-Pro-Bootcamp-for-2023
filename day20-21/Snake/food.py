from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, width, height, food_color="green"):
        """This creates a food and place in random coordinate in the screen
        where width and height are the width and height of the screen window"""
        super().__init__()
        self.color(food_color)
        self.penup()
        self.shape("circle")
        self.width = width
        self.height = height
        self.shapesize(0.5)

    def refresh(self):
        x = random.randint(int(-self.width / 2 + 40), int(self.width / 2 - 40))
        y = random.randint(int(-self.height / 2 + 40), int(self.height / 2 - 40))
        self.goto(x, y)
