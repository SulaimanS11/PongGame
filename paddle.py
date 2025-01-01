from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, width = -350, height = 0):
        super().__init__()
        self.widthPos = width
        self.heightPos = height
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.widthPos,self.heightPos)
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

    def returnWidth(self):
        return self.shapesize()[0] * 20
    
    def returnLength(self):
        return self.shapesize()[1] * 20

