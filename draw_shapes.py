from turtle import Turtle
import random

timmy = Turtle()

def generate_random_color():
    r = random.randint(0, 100)/100
    g = random.randint(0, 100)/100
    b = random.randint(0, 100)/100
    return r, g, b

def draw_shape(edge):
    degree = 360 / edge
    for _ in range(edge):
        timmy.forward(100)
        timmy.right(degree)

for i in range(3,11):
    timmy.pencolor(generate_random_color())
    draw_shape(i)













screen = Screen()
screen.exitonclick()
