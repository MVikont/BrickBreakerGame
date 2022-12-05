from turtle import *
from scoreboard import Scoreboard
from random import choice
from colors import colorList

BRICK_WIDTH = 2.5
BRICK_SPACE = 5

class Brick:
    def __init__(self):
        self.allBricks = []
        self.coordY = 320
        self.coordX = -320

    def layDownBricks(self, lvl):
        self.coordY = 320
        for i in range(2 + lvl):
            for j in range(11):
                newBrick = Turtle()
                newBrick.penup()
                newBrick.shape("square")
                newBrick.shapesize(stretch_len=BRICK_WIDTH, stretch_wid=1)
                newBrick.speed(0)
                newBrick.goto(self.coordX, self.coordY)
                newBrick.color(choice(colorList))
                self.allBricks.append(newBrick)
                self.coordX += 62
            self.coordY -= 30
            self.coordX = -320






