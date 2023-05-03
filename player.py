from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.right(270)
        self.goto(0, -280)
    
    def go_up(self):
        newy=self.ycor()+10
        self.goto(self.xcor(), newy)
    