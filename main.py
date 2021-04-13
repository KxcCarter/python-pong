from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

player_paddle = Paddle()
scoreboard = Scoreboard()
ball = Ball()

screen = Screen()

screen.listen()

# These could be turned into methods within the paddle class
def paddle_up():
    player_paddle.setheading(270)


def paddle_down():
    player_paddle.setheading(90)


screen.onkey(paddle_up, "Up")
screen.onkey(paddle_down, "Down")