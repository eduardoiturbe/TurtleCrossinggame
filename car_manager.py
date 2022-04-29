import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
LEVEL = 15
LENGTH = 2


class CarManager(Turtle):

    def __init__ (self):
        self.all_cars = []


    def create_cars(self):
        random_chance = random.randint(1,LEVEL)
        stretch_len = random.randint(2,LENGTH)
        y_range = random.randrange(-260, 250)
        if random_chance <= 3:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=stretch_len)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, y_range)
            new_car.x_move = STARTING_MOVE_DISTANCE
            self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)



