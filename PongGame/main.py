from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")

paddle = Turtle()
paddle.shape('square')
paddle.color('tomato')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(x=350, y=0)

screen.exitonclick()
