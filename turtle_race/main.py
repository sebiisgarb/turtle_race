import random
import turtle
from turtle import *

colors = ["red", "orange", "pink", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)
user_bet = turtle.textinput("BET", "Who is going to win the race? Enter a color:")

ystart = 180
turtles = []
for _ in range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[_])
    turtles.append(tim)
    ystart -= 50
    tim.goto(-175, ystart)

finish = True
if user_bet in colors:
    finish = False

while not finish:
    for turtle in turtles:
        if turtle.pos()[0] >= 175:
            winner = turtle.color()
            finish = True
            break
        pace = random.randint(0, 10)
        turtle.forward(pace)

if winner[1] == user_bet:
    print(f"You won the bet! {user_bet} turtle won!")
else:
    print(f"You lost! {winner[1]} turtle won")
screen.exitonclick()