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

def move_random():
    timmy.pencolor(generate_random_color())
    left_or_right = random.randint(0, 3)
    if left_or_right == 0:
        timmy.right(90)
    elif left_or_right == 1:
        timmy.left(90)
    elif left_or_right == 2:
        timmy.right(180)
    else:
        pass
    timmy.forward(50)

timmy.pensize(10)
for _ in range(100):
    move_random()


screen = t.Screen()
screen.exitonclick()
