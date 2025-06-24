from turtle import Turtle, Screen

jo = Turtle()
screen = Screen()

def clear_screen():
    jo.reset()

def move_forward():
    jo.forward(10)

def move_backward():
    jo.backward(10)

def move_clockwise():
    jo.right(10)
    jo.forward(10)

def move_counterclockwise():
    jo.left(10)
    jo.forward(10)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="space", fun=clear_screen)


screen.exitonclick()
