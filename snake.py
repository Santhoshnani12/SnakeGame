from turtle import *

POSITION = [(0, 0), (-20, 0), (-40, 0)]
forward_distance = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for i in POSITION:
            self.add_turtle(i)
    
    def add_turtle(self, pos):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(pos)
        self.turtle_list.append(t)
    
    def extend_turtle(self):
        self.add_turtle(self.turtle_list[-1].position())

    def move(self):
        for i in range(len(self.turtle_list)-1, 0, -1):
            x = self.turtle_list[i-1].xcor()
            y = self.turtle_list[i-1].ycor()
            self.turtle_list[i].goto(x, y)
        self.head.forward(forward_distance)
    
    def reset(self):
        for i in self.turtle_list:
            i.goto(1000, 1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)