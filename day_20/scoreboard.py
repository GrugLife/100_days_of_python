from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f"Score = {self.score} ", align="center", font=("Arial", 24, "normal")
        )

    def increase_score(self):
        self.score += 1
        self.clear()  # this clears the previous score
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Arial", 50, "bold"))
