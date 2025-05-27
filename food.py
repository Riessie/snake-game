from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # Standard size is 20x20, so 0.5 makes it 10x10
        self.penup()
        self.speed("fastest")
        self.color("blue")
