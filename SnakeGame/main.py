from turtle import Screen, Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")

for position in STARTING_POSITIONS:
    new_segment = Turtle(shape="square")
    new_segment.color('white')
    new_segment.goto(position)

screen.exitonclick()
