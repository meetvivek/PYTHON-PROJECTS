from turtle import Turtle, Screen
import random
from tkinter import messagebox

is_race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)

# Set the background image
my_screen.bgpic("bg.png")

user_input = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\n"
                                                               "Enter a color: ('red', 'yellow', 'green', 'blue', "
                                                               "'orange', 'purple')").lower()

color = ["red", "yellow", "green", "blue", "orange", "purple"]

turtle_list = []

y = -150
for i in range(6):
    my_turtle = Turtle("turtle")
    my_turtle.color(color[i])
    my_turtle.penup()
    my_turtle.goto(x=-230, y=y)
    turtle_list.append(my_turtle)
    y += 60

if user_input:
    is_race_on = True
while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                messagebox.showinfo(title="Game Result",
                                    message=f"You've won! The {winning_color} turtle is the winner!")
            else:
                messagebox.showinfo(title="Game Result",
                                    message=f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

my_screen.exitonclick()
