STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle,Screen
screen=Screen()
class Player(Turtle):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.penup()
        self.goto(0,-280)
        self.setheading(90)
        self.shape('turtle')

    def move(self):
        self.forward(5)




