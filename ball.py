from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball = Turtle("square")
        self.ball.color("white")
        self.ball.random_y = random.randint(-250, 250)
        self.ball.penup()
        self.ball.goto(-260, self.random_y)



    # automate movement
    def move_ball(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)