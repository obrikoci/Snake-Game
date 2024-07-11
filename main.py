from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     Detect collision with food
    if snake.head.distance(food) < 16 :
        food.refresh()
        snake.extend()
        scoreboard.update_score()

#         Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -300 or snake.head.ycor() > 295 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()


#     Detect collision with tail(using slicing)
    for segment in snake.snake:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
