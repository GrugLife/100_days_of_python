import random
import turtle as t

grug = t.Turtle()
grug.shape("turtle")
t.colormode(255)
grug.pensize(10)
direction = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def random_walk(length):
    for _ in range(length):
        grug.pencolor(random_color())
        grug.forward(30)
        grug.setheading(random.choice(direction))


random_walk(1000)
screen = t.Screen()
screen.exitonclick()
