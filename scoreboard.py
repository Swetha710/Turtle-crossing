from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level=1
    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=(FONT))
    def levelDisplay(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level {self.level}", align="left", font=(FONT))
    def updateLevel(self):
        self.level+=1
        self.levelDisplay()