from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, key="Up")
screen.onkeypress(r_paddle.go_down, key="Down")

screen.onkeypress(l_paddle.go_up, key="w")
screen.onkeypress(l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

screen.exitonclick()
