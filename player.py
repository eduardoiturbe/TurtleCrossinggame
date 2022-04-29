from turtle import Turtle
import car_manager




STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
SCORE = 0


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        global SCORE
        SCORE = SCORE + 1

        print(SCORE)



    def is_a_finish_line(self):
        if self.ycor() > 280:
            self.goto(STARTING_POSITION)
            car_manager.LEVEL = car_manager.LEVEL - 1
            car_manager.STARTING_MOVE_DISTANCE = car_manager.STARTING_MOVE_DISTANCE + car_manager.MOVE_INCREMENT
            if car_manager.LEVEL < 10:
                car_manager.LENGTH = car_manager.LENGTH +  1

