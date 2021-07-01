from turtle import Turtle, Screen
import random

screen = Screen()

colors = ['red', 'blue', 'black', 'yellow', 'green', 'brown', 'purple', 'indigo', 'pink', 'grey']
y = 150
x = -350

all_turtles = []

for i in range(0, 7):
    tim = Turtle(shape='turtle')
    tim.color(colors[i])
    tim.penup()
    tim.goto(x, y)
    y-= 50
    all_turtles.append(tim)

screen.setup(width=800, height=800)
user_bet = screen.textinput(prompt="Bet which turtle's gonsta win. Pick color", title="Turtle Race bois!!!!")

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for i in all_turtles:
        if i.xcor() > 400:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print('Yes you\'ve won. Now fuck off')
            else:
                print('Ya lost. Now fuck off.')
        rand_dist = random.randint(0, 15)
        i.forward(rand_dist)

screen.exitonclick()
