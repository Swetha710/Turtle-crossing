import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p = Player()
car_manager = CarManager()
sb=Scoreboard()

screen.listen()

screen.onkey(p.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_time)
    screen.update()
    sb.levelDisplay()
    car_manager.create()
    car_manager.move()
    for car in car_manager.allcars:
        if car.distance(p) < 20:
            game_is_on=False
            sb.gameOver()
    if p.ycor()>280:
        sb.updateLevel()
        p.goto(0,-280)
        car_manager.car_increase_speed()


screen.exitonclick()