from turtle import Screen
from snake import Snake
import time
from scoreboard import Scoreboard
from food import Food
# Create a screen object
screen = Screen()
screen.setup(width=600, height=600)
# Set the background color and title
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off the screen updates

snake = Snake()
food = Food()
scoresboard = Scoreboard()

screen.listen()  # Listen for keyboard input
screen.onkey(snake.move, "Up")  # Move the snake up when 'Up' key is pressed
screen.onkey(snake.move, "Down")  # Move the snake down when 'Down' key is pressed
screen.onkey(snake.move, "Left")  # Move the snake left when 'Left' key is pressed
screen.onkey(snake.move, "Right")  # Move the snake right when 'Right' key is pressed
# loop to move the snake
game_on = True
while game_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Control the speed of the snake
    snake.move()  # Move the snake
    # Check for collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        self.extend_snake()
        scoresboard.increase_score()
         # If the snake's head is close to the food
        food.goto(100, 100)  # Move the food to a new random position
        new_segment = snake.segments[-1].clone()  # Create a new segment
        snake.segments.append(new_segment)  # Add the new segment to the snake
    # Check for collision with the screen edges
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False 
        scoresboard.game_over()
    # Check for collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoresboard.game_over()

        
screen.exitonclick()


