import time
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        # create ad update scoreboard
        scoreboard.increase_score()
        # add a new food item
        food.new_food()

    # 6. detect collision with wall
    if snake.head.xcor() in [-300, 300] or snake.head.ycor() in [-300, 300]:
        game_is_on = False
        scoreboard.game_over()
# 7. detect colision with tail


screen.exitonclick()
