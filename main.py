from turtle import Turtle, Screen
import random

# Create a screen object
screen = Screen()
screen.setup(width=600, height=600)
# Set the background color and title
screen.bgcolor("black")
screen.title("Snake Game")

# Create a turtle object
snake_seg1 = Turtle("square")
snake_seg1.color("white")
snake_seg1.goto(0, 0)

snake_seg2 = Turtle("square")
snake_seg2.color("white")
snake_seg2.goto(-20, 0)

snake_seg3 = Turtle("square")
snake_seg3.color("white")
snake_seg3.goto(-40, 0)

screen.exitonclick()


