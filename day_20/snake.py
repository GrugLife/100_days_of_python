from turtle import Turtle

X_AXIS = 0
Y_AXIS = 0
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    # 1. create the snake body
    def create_snake(self):
        for n in range(0, 3):
            grug = Turtle(shape="square")
            grug.color("white")
            grug.penup()
            grug.goto(X_AXIS - (n * 20), Y_AXIS)
            self.segments.append(grug)

    # 2. move the snake
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
