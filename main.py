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
ball = Ball()
scoreboard = Scoreboard()


def stop_game():
    global GAME_IS_ON
    GAME_IS_ON = False


screen.listen()


screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")

screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")
screen.onkey(stop_game, "space")


while GAME_IS_ON:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with upper or lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # detect collision with paddles
    if (ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50) and (ball.xcor() > 320 or ball.xcor() < -320):
        ball.x_bounce()

    # detect if ball has gone beyond paddles
    if ball.xcor() > 350 or ball.xcor() < -350:

        if ball.xcor() > 350:
            print("Right Paddle Loses")
            scoreboard.add_point("left")
        else:
            print("Left Paddle Loses")
            scoreboard.add_point("right")

        time.sleep(1)
        ball.reset_ball()


screen.exitonclick()