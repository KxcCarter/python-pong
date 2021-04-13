from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Pong")



player_paddle = Paddle()
scoreboard = Scoreboard()
# ball = Ball()



screen.listen()


screen.onkey(player_paddle.paddle_up, "Up")
screen.onkey(player_paddle.paddle_down, "Down")


screen.exitonclick()