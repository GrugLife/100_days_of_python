from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
x_axis = 0
y_axis = 0
# 1. create the snake body
for n in range(0, 3):
    grug = Turtle(shape="square")
    grug.color("white")
    grug.penup()
    grug.goto(x_axis - (n * 20), y_axis)

# 2. move the snake

# 3. Control the snake

# 4. Detect collision with food

# 5. create a scoreboard

# 6. detect collision with wall

# 7. detect colision with tail


screen.exitonclick()
