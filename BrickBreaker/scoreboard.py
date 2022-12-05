from turtle import Turtle

FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-340, -340)
        self.speed(0)

    def writeLevel(self, lvl):
        self.write(arg=f"Level: {lvl} of 4", font=FONT, move=False)

    def updateLevel(self, lvl):
        self.clear()
        self.write(arg=f"Level: {lvl} of 4", font=FONT, move=False)

class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.lives = 3
        self.hideturtle()
        self.goto(250, -340)
        self.speed(0)

    def writeLives(self):
        self.write(arg=f"Lives: {self.lives}", font=FONT, move=False)

    def updateLives(self):
        self.clear()
        self.writeLives()

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def gameOverMsg(self):
        self.color("white")
        self.write(arg="GAME OVER", align="center", font=("Arial", 40, "bold"), move=False)

    def congratsMsg(self):
        self.color("blue")
        self.write(arg="CONGRATULATIONS!", align="center", font=("Arial", 40, "bold"), move=False)