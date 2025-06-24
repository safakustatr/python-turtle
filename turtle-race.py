from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "green", "blue", "yellow", "purple"]
turtles = []
x = -230
y = -100
is_race_on = True

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x, y)
    y += 40
    turtles.append(new_turtle)

while is_race_on:
    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            if user_bet == turtle.fillcolor():
                print(f"You win, {turtle.fillcolor()} turtle won the race!")
            else:
                print(f"You lose, {turtle.fillcolor()} turtle won the race!")


screen.exitonclick()
