from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(-350,0)
        self.color("black")
        
    def paddle_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)
    
    def paddle_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)
        
    def move(self):
        self.listen()
        self.onkey(self.paddle_up, "w")
        self.onkey(self.paddle_down, "s")

    def change_starting_position(self, xpos, ypos):
        self.goto(xpos, ypos)

