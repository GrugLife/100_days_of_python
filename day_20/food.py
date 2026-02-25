import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
