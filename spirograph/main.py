import random
import turtle as t

t.colormode(255)
shape = t.Turtle()
shape.hideturtle()


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


def draw(size_gap):
    for i in range(int(360 / size_gap)):
        shape.color(random_color())
        shape.circle(100)
        shape.setheading(shape.heading() + size_gap)


draw(5)

screen = t.Screen()
screen.exitonclick()
