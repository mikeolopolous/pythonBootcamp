import random
import turtle as t

GRADES = [0, 90, 180, 270]

dot = t.Turtle()
dot.shape('circle')
dot.pensize(10)
t.colormode(255)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return red, green, blue


for _ in range(250):
    dot.color(random_color())
    dot.setheading(random.choice(GRADES))
    dot.forward(25)

screen = t.Screen()
screen.exitonclick()
