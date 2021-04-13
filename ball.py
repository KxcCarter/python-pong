from turtle import Turtle
import random

LEFT_OR_RIGHT = [-330, 330]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.random_y = random.randint(-250, 250)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """
        Direction should be either 1 or -1, which is multiplied by the xcor and ycor to reverse movement.

        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
