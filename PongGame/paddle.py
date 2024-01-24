from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color('tomato')
        self.shapesize(stretch_wid=20, stretch_len=100)

        self.goto(x=350, y=0)
