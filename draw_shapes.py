import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_shape(edge):
    degree = 360 / edge
    for _ in range(edge):
        timmy.forward(100)
        timmy.right(degree)

for i in range(3,11):
    timmy.pencolor(generate_random_color())
    draw_shape(i)


screen = t.Screen()
screen.exitonclick()
