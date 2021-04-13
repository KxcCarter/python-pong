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

    def move(self):
        # self.goto(random.choice(LEFT_OR_RIGHT), self.random_y)
        new_x = self.xcor() + 5
        new_y = self.ycor() + 5
        self.goto(new_x, new_y)



    # automate movement
    def move_ball(self):
        random_x = random.randint(-330, 330)
        random_y = random.randint(-260, 260)