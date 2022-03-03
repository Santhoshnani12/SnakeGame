from turtle import *
import time
from snake import Snake
from food import Food
from scorecard import Scorecard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scorecard = Scorecard()

is_true = True

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while is_true:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    if snake.head.distance(food) < 15:
        scorecard.incrementScoreCard()
        food.refresh()
        snake.extend_turtle()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 250 or snake.head.ycor() < -280:
        scorecard.reset()
        food.reset()
        snake.reset()

    for i in snake.turtle_list[1:]:
        if snake.head.distance(i) < 10:
            scorecard.reset()
            food.reset()
            snake.reset()

screen.exitonclick()