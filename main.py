import turtle
import time
from paddle import Paddle
from turtle import Screen, Turtle
from ball import Ball

# screen commands
screen = Screen()
WIDTH = 800
HEIGHT = 600
screen.bgcolor("lightgrey")
screen.setup(WIDTH, HEIGHT)
screen.title("Pong")
screen.tracer(0)

#object inits
paddle = Paddle()
opp_paddle = Paddle()
ball = Ball(HEIGHT, WIDTH)

opp_paddle.change_starting_position(350, 0)

# movement funciton calls
screen.listen()

screen.onkey(paddle.paddle_up, "w")
screen.onkey(paddle.paddle_down, "s")
screen.onkey(opp_paddle.paddle_up, "Up")
screen.onkey(opp_paddle.paddle_down, "Down")



game_on = True

while game_on:
    time.sleep(0.01)
    screen.update()
    ball.move()


screen.exitonclick()