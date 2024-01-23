import random
from turtle import Turtle, Screen


timmy = Turtle()
timmy.shape("turtle")

colors = ['LightSlateBlue', 'DodgerBlue2', 'PaleGreen3',
          'maroon2', 'tomato', 'LightSlateGray', 'HotPink2',
          'khaki2']


def draw_shape(num_sides):
    timmy.color(random.choice(colors))
    angle = int(360 / num_sides)

    for _ in range(num_sides):
        timmy.right(angle)
        timmy.forward(100)


for side in range(3, 11):
    draw_shape(side)

screen = Screen()
screen.exitonclick()
