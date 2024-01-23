from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, key='Up')
screen.onkey(snake.down, key='Down')
screen.onkey(snake.left_move, key='Left')
screen.onkey(snake.right_move, key='Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.new_score()

screen.exitonclick()
