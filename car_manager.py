from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.allcars=[]
        self.move_time=0.1

    def create(self):
        #every 6 times the loop runs, a new car will be generated
        rand_choice = random.randint(1,6)
        if rand_choice == 1:
            newCar = Turtle()
            newCar.penup()
            newCar.shape("square")
            newCar.shapesize(1, 2)
            newCar.goto(250, random.randint(-250, 250))
            newCar.color(random.choice(COLORS))
            self.allcars.append(newCar)
    def move(self):
        for car in self.allcars:
            newx=car.xcor()-10
            car.goto(newx, car.ycor())
    def car_increase_speed(self):
        self.move_time*=0.9