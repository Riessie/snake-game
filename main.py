from turtle import Turtle, Screen
import random

# Create a turtle object
snake = Turtle()
snake.shape("square")
snake.color("white")
snake.shapesize(stretch_wid=0.5, stretch_len=0.5)
snake.penup()
snake.speed(0)

# Create a screen object
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.exitonclick()
