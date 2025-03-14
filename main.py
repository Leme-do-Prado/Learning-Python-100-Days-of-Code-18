import random
from turtle import Turtle, Screen

turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.speed("fastest")
screen = Screen()
screen.colormode(255)
rgb_colors = [
    (217, 232, 242), (166, 174, 119), (100, 107, 71), (207, 217, 211),
    (129, 148, 86), (54, 44, 28), (78, 101, 64), (142, 165, 182),
    (201, 207, 147), (226, 224, 208), (97, 109, 125), (36, 55, 35),
    (154, 169, 158), (53, 74, 45), (232, 224, 228), (75, 68, 43),
    (170, 157, 162), (103, 92, 97), (183, 197, 189), (36, 37, 51),
    (168, 199, 210), (117, 126, 143), (53, 41, 46), (115, 138, 104),
    (183, 190, 203)
]
turtle.setheading(225)
turtle.forward(250)
turtle.setheading(0)

starting_h = turtle.xcor()
starting_v = turtle.ycor()

for _ in range(10):
    for _ in range(10):
        turtle.dot(20, random.choice(rgb_colors))
        turtle.forward(50)
    starting_h += 50
    turtle.goto(starting_h, starting_v)

screen.exitonclick()
