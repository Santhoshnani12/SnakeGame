from turtle import *
from scorecard import Scorecard
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.count = 0
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.refresh()
        self.speed("fastest")

    
    def refresh(self):
        self.shapesize(0.5, 0.5)
        if self.count % 5 == 0 and self.count != 0:
            self.shapesize(1, 1, 2)
        x = random.randint(-270, 270)
        y = random.randint(-270, 250)
        self.goto(x ,y)
        self.count += 1
    
    def reset(self):
        self.count = 0