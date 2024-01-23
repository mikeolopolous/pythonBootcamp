# import colorgram
#
# colors = colorgram.extract('assets/image.webp', 10)
#
# list_colors = []
# for color in colors:
#     red = color.rgb[0]
#     blue = color.rgb[1]
#     green = color.rgb[2]
#
#     list_colors.append((red, blue, green))

import turtle as t
import random

RGB_COLORS = [
    (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130),
    (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203)
]

t.colormode(255)

dot = t.Turtle(shape="arrow")
dot.hideturtle()
dot.setheading(225)
dot.penup()
dot.forward(300)
dot.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    dot.dot(20, random.choice(RGB_COLORS))
    dot.forward(50)

    if dot_count % 10 == 0:
        dot.setheading(90)
        dot.forward(50)
        dot.setheading(180)
        dot.forward(500)
        dot.setheading(0)

screen = t.Screen()
screen.exitonclick()
