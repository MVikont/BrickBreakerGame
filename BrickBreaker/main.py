from turtle import *
import time
from plate import Plate
from bricks import *
from ball import *
from scoreboard import *

def clearScreen():
    screen.clear()

isGameOn = True
screen = Screen()
screen.bgcolor("black")
screen.title("Brick Breaker")
screen.setup(width=700, height=700)
screen.tracer(0)
currLvl = 1

# Plate
plate = Plate()
# Lay Down the Bricks
makeBricks = Brick()
makeBricks.layDownBricks(currLvl)
# Level & Lives, or Scoreboard
currentLevel = Scoreboard()
currentLevel.writeLevel(currLvl)
lives = Lives()
lives.writeLives()
# Create Ball
ball = Ball()
ball.resetBall()

screen.update()
screen.tracer(1)
screen.listen()

while isGameOn:
    time.sleep(0.04)
    ball.ballMotion()
    screen.onkeypress(plate.plateLeft, "Left")
    screen.onkeypress(plate.plateRight, "Right")

    # Plate Collision Logic
    if ball.distance(plate) < 25 and ball.ycor() < -280:
        ball.plateBounceNear()
    elif ball.distance(plate) < 35 and ball.ycor() < -280:
        ball.plateBounceMid()
    elif ball.distance(plate) < 45 and ball.ycor() < -280:
        ball.plateBounceFar()

    # Wall and Ceiling Collision Logic
    if ball.xcor() > 320 or ball.xcor() < -320:
        ball.bounceHorizontal()
    if ball.ycor() > 340:
        ball.bounceVertical()

    # Brick Breaking Collision Logic
    for b in makeBricks.allBricks:
        if ball.distance(b) < 28:
            makeBricks.allBricks.remove(b)
            b.hideturtle()
            ball.bounceVertical()

    # Next Level
    if len(makeBricks.allBricks) == 0:
        currLvl += 1
        if currLvl < 5:
            currentLevel.updateLevel(currLvl)
            ball.resetBall()
            makeBricks.layDownBricks(currLvl)
        else:
            isGameOn = False
            clearScreen()
            GameOver().congratsMsg()

    # Ball Lost
    if ball.ycor() < -330:
        lives.lives -= 1
        if lives.lives < 2:
            lives.color("red")
        if lives.lives == 0:
            GameOver().gameOverMsg()
            isGameOn = False
        lives.updateLives()
        ball.resetBall()

    # Game Finished

screen.mainloop()
