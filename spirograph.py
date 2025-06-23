import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def spirograph(angle):
    for _ in range(360 // angle):
        timmy.color(generate_random_color())
        timmy.circle(100)
        timmy.right(angle)

spirograph(5)


screen = t.Screen()
screen.exitonclick()