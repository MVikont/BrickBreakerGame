from turtle import *

PLATE_Y = -300

class Plate(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.tilt(90)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(0, PLATE_Y)

    def plateLeft(self):
        x = self.xcor()
        x -= 15
        if x > -305:
            self.goto(x, PLATE_Y)

    def plateRight(self):
        x = self.xcor()
        x += 15
        if x < 305:
            self.goto(x, PLATE_Y)

