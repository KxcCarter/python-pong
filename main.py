from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)
GAME_IS_ON = True


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()



screen.listen()


screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")

screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")


while GAME_IS_ON:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        print("Oh man I lost my ball :[")
        ball.y_bounce()
    # detect collision with paddle
    if (ball.distance(r_paddle) < 50 or ball.distance(l_paddle)) and (ball.xcor() > 340 or ball.xcor() < -340):
        print('we bouncin')
        ball.x_bounce()


screen.exitonclick()