import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("lightgrey")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)

paddle.penup()
paddle.goto(-350,0)

paddle.color("black")

def paddle_up():
    y = paddle.ycor()
    y += 20
    paddle.sety(y)

def paddle_down():
    y = paddle.ycor()
    y -= 20
    paddle.sety(y)


game_on = True

screen.onkey(paddle_up, "w")
screen.onkey(paddle_down, "s")
screen.listen()


while game_on:
    


    screen.update()





screen.exitonclick()

