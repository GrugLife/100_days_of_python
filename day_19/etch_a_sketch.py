from turtle import Turtle, Screen

grug = Turtle()
screen = Screen()


def move_forward():
    grug.forward(10)


def move_backward():
    grug.backward(10)


def move_left():
    grug.left(10)


def move_right():
    grug.right(10)


def clear_screen():
    grug.penup()
    grug.clear()
    grug.home()
    grug.pendown()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
