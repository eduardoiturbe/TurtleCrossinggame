from turtle import Turtle
import player



FONT = ("Courier", 24, "normal")
SCORE = player.SCORE

class Points(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.points()

    def points(self):
        self.goto(280, 250)
        self.clear()
        self.write(f"Points: {player.SCORE}", align="right", font=FONT)




