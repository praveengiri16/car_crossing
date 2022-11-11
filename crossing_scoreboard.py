from turtle import Turtle

FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-250, y=265)
        self.score = 0

    def print_score(self):
        self.clear()
        self.write(f"Level: {self.score}", move=False, align= "center", font=FONT)

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
