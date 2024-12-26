import turtle
from paddle import Paddle
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("lightgrey")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()
opp_paddle = Paddle()

opp_paddle.change_starting_position(350, 0)



screen.listen()
screen.onkey(paddle.paddle_up, "w")
screen.onkey(paddle.paddle_down, "s")
screen.onkey(opp_paddle.paddle_up, "Up")
screen.onkey(opp_paddle.paddle_down, "Down")


game_on = True

while game_on:


    screen.update()





screen.exitonclick()

