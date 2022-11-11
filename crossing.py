from turtle import Screen
from crossing_player import Player
import time
from crossing_car import moving_car
from crossing_scoreboard import Scoreboard
game_on = True

s = Screen()
s.setup(width=800, height=600)
s.tracer(0)

player = Player()

s.listen()
s.onkey(fun=player.move, key="Up")

cars = moving_car()
score = Scoreboard()

while game_on:
    time.sleep(0.1)
    score.print_score()
    cars.next_car()
    s.update()
    cars.move()
    for car in cars.all_cars:
        if car.distance(player) < 25:
            game_on = False
            score.game_over()
    if player.finish():
        player.create_player()
        cars.increase_speed()
        score.increase_score()

s.exitonclick()
