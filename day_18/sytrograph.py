import random
import turtle as t

grug = t.Turtle()
grug.shape("turtle")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def circle(size_of_gap):
    for n in range(0, 360, size_of_gap):
        grug.color(random_color())
        grug.circle(100)
        grug.setheading(n)


grug.speed("fastest")
circle(2)
screen = t.Screen()
screen.exitonclick()
