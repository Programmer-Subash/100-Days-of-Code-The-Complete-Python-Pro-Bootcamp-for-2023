from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self, snake_color: str = "white"):
        self.segments = []
        self.snake_color = snake_color

    def create_snake(self):
        staring_position = [(0, 0), (-20, 0), (-40, 0)]
        for position in staring_position:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.shape('square')
        segment.color(self.snake_color)
        segment.goto(position)
        self.segments.append(segment)

    def extend_snake(self):
        position = self.segments[-1].position()
        self.add_segment(position)

    def move_snake_body(self):
        """x ,y are coordinates"""
        for i in range(len(self.segments) - 1, 0, -1):
            first_segment = self.segments[i - 1]
            second_segment = self.segments[i]
            second_segment.goto(first_segment.position())
        self.segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        head = self.segments[0]
        if not int(head.heading()) == DOWN:
            head.setheading(UP)

    def move_down(self):
        head = self.segments[0]
        if not int(head.heading()) == UP:
            head.setheading(DOWN)

    def move_right(self):
        head = self.segments[0]
        if not int(head.heading()) == LEFT:
            head.setheading(RIGHT)

    def move_left(self):
        head = self.segments[0]
        if not int(head.heading()) == RIGHT:
            head.setheading(LEFT)
