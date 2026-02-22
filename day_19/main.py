from turtle import Turtle, Screen
import random


x_axis = -230
y_axis = [-70, -40, -10, 20, 50, 80]
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bettors_winner = screen.textinput(
    "Make your bet", "Which turtle are you betting to win the race: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for n in range(0, 6):
    grug = Turtle(shape="turtle")
    grug.color(colors[n])
    grug.penup()
    grug.goto(x_axis, y_axis[n])
    all_turtles.append(grug)

if bettors_winner:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == bettors_winner:
                print(f"you won the bet on turtle {winner}")
            else:
                print(f"you lost, winning turtle was {winner}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
