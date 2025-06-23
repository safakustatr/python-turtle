from turtle import Turtle, Screen
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

# for i in range(3,11):
#     timmy.pencolor(generate_random_color())
#     draw_shape(i)

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












screen = Screen()
screen.exitonclick()