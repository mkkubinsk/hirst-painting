# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# palette = []
#
# for i in colors:
#     palette.append((i.rgb.r, i.rgb.g, i.rgb.b))
#
# print(palette)
import turtle as t
import random

color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216),
              (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
              (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28),
              (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199),(179, 17, 8),
              (233, 66, 34)]

timmy = t.Turtle()

t.colormode(255)
t.penup()
t.hideturtle()
for vertical in range(10):
    y = vertical * 50
    offsy = y - 200
    t.goto(0, offsy)
    for horizontal in range(10):
        x = horizontal * 50
        offsx = x - 200
        t.goto(offsx, offsy)
        t.dot(20, random.choice(color_list))

screen = t.Screen()
screen.exitonclick()
