import random
import turtle as t
import colorgram

grug = t.Turtle()
grug.shape("turtle")
t.colormode(255)

colors = colorgram.extract("image.jpg", 15)


def random_color():
    color = random.randint(0, 14)
    r = colors[color].rgb.r
    g = colors[color].rgb.g
    b = colors[color].rgb.b
    return r, g, b


# 10 x 10 picture with 20 size dots space of 50
grug.penup()
x = -270
y = -270
grug.setpos(x, y)


def dot_line(n):
    for _ in range(n):
        grug.dot(20, random_color())
        grug.forward(50)


for _ in range(10):
    dot_line(10)
    y += 50
    grug.setpos(x, y)
grug.speed("fastest")
screen = t.Screen()
screen.exitonclick()
