from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.last_input = 0

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        newsegment = Turtle('square')
        newsegment.color('green')
        newsegment.penup()
        newsegment.goto(position)
        self.segments.append(newsegment)

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.last_input = self.head.heading()

    def up(self):
        if self.last_input != DOWN:
            self.head.setheading(90)

    def left(self):
        if self.last_input != RIGHT:
            self.head.setheading(180)

    def down(self):
        if self.last_input != UP:
            self.head.setheading(270)

    def right(self):
        if self.last_input != LEFT:
            self.head.setheading(0)

    def grow(self):
        self.add_segment(self.segments[-1].position())

