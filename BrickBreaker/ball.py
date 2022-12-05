from turtle import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.ballX = 0
        self.ballY = -250
        self.goto(self.ballX, self.ballY)
        self.speed(0)
        self.xMove = 12
        self.yMove = 12

    def ballMotion(self):
        self.ballX = self.xcor() - self.xMove
        self.ballY = self.ycor() + self.yMove
        self.goto(self.ballX, self.ballY)

    def bounceVertical(self):
        self.yMove *= -1

    def plateBounceNear(self):
        self.yMove *= -1
        if self.xMove < 0:
            self.xMove = 4
        elif self.xMove > 0:
            self.xMove = -4
        self.xMove *= -1

    def plateBounceMid(self):
        self.yMove *= -1
        if self.xMove < 0:
            self.xMove = 8
        elif self.xMove > 0:
            self.xMove = -8
        self.xMove *= -1

    def plateBounceFar(self):
        self.yMove *= -1
        if self.xMove < 0:
            self.xMove = 12
        elif self.xMove > 0:
            self.xMove = -12
        self.xMove *= -1

    def bounceHorizontal(self):
        self.xMove *= -1

    def resetBall(self):
        self.ballX = 0
        self.ballY = -250
        self.goto(self.ballX, self.ballY)
        self.xMove = 12
        self.yMove = 12
        self.ballMotion()






