from turtle import Turtle
import random
SPEED_UP = 5
colors = ["red", "green","blue", "black","brown","yellow"]

class moving_car(Turtle):

    def __init__(self):
        super().__init__()
        self.car_speed = SPEED_UP
        self.all_cars = []

    def next_car(self):
        random_choice = random.randint(1, 5)
        self.hideturtle()
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2.5, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(colors))
            y_pos = random.randint(-230, 230)
            new_car.goto(380, y_pos)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += 2