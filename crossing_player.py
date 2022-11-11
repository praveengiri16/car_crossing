from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.shape("turtle")
        self.penup()
        self.goto(x=0, y=-260)
        self.setheading(90)

    def move(self):
        self.forward(20)

    def finish(self):
        if self.ycor() > 260:
            return True

