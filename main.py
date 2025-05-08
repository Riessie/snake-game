from turtle import Turtle, Screen
import random

# Create a screen object
screen = Screen()
screen.setup(width=600, height=600)
# Set the background color and title
screen.bgcolor("black")
screen.title("Snake Game")

sections = []
for i in range(3):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(-20 * i, 0)
    sections.append(new_segment)

# loop to move the snake
game_on = True
while game_on:
    for segment in sections:
        segment.forward(20)
        # Change the color of the segments randomly
        # segment.color(random.choice(["red", "green", "blue", "yellow", "purple"]))

    # Check for collision with the screen edges
    if sections[0].xcor() > 290 or sections[0].xcor() < -290 or sections[0].ycor() > 290 or sections[0].ycor() < -290:
        game_on = False 
screen.exitonclick()


