import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # 3. Control the snake

    # 4. Detect collision with food

    # 5. create a scoreboard

    # 6. detect collision with wall
"""
    if segments[0].xcor() in [-300, 300] or segments[0].ycor() in [-300, 300]:
        game_is_on = False
        print("you hit the wall and lose")
        """
# 7. detect colision with tail


screen.exitonclick()
