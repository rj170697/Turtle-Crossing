COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle


class CarManager():
    def __init__(self):
       self.all_cars=[]

    def create_car(self):
        newcar=Turtle()
        newcar.penup()
        newcar.shape('square')
        newcar.shapesize(0.5,1.5)
        newcar.color(random.choice(COLORS))
        newcar.goto(300,random.choice(range(-300,300,30)))
       # newcar.setheading(270)
        self.all_cars.append(newcar)

    def move(self):
        for i in self.all_cars:
            i.backward(STARTING_MOVE_DISTANCE)




   # pass
