from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import random
import time

screen=Screen()
screen.setup(width=800,height=800)
screen.bgcolor("black")

snake=Snake()
snake.create_snake()
snake.move()

food=Food()
score=Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

game_on=True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        score.increase()
        snake.increase()
        food.refresh()

    for s in snake.segments:
        if s == snake.head:
            pass
        elif snake.head.distance(s) < 10:
            score.reset()
            snake.reset_snake()


    if snake.head.xcor() > 380 or snake.head.xcor()< -380 or snake.head.ycor() > 380 or snake.head.ycor()< -380:
        score.reset()
        snake.reset_snake()

screen.exitonclick()