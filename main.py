from turtle import Turtle, Screen
from snake import Snake
import random
import time

# Create a screen object
screen = Screen()
screen.setup(width=600, height=600)
# Set the background color and title
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off the screen updates

snake = Snake()
# loop to move the snake
game_on = True
while game_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Control the speed of the snake
    snake.move()  # Move the snake
    # Check for collision with the screen edges
    #if segment[0].xcor() > 290 or sections[0].xcor() < -290 or sections[0].ycor() > 290 or sections[0].ycor() < -290:
     #   game_on = False 
        
screen.exitonclick()


