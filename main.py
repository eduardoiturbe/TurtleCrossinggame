import time
from turtle import Screen

import score_points
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from score_points import Points

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
score_points = Points()


screen.listen()
screen.onkey(player.move_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()
    if player.ycor() > 280:
        scoreboard.increase_level()
        player.is_a_finish_line()
    score_points.points()



    #detect colision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False




screen.exitonclick()



