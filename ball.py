from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0,0)
    
    def move(self):
        self.goto(self.xcor() + 10, self.ycor() + 10)

    def bounce(self):
        self.goto(self.xcor() - 10, self.ycor() - 10)

    def reset(self):
        self.goto(0,0)
        self.bounce()
        self.move()
    
    def check_collision(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.bounce()
        if self.xcor() > 390 or self.xcor() < -390:
            self.reset()
        return False
    
    def check_paddle_collision(self):
        if self.xcor() > 340 and self.ycor() < 50 and self.ycor() > -50:
            self.bounce()
        if self.xcor() < -340 and self.ycor() < 50 and self.ycor() > -50:
            self.bounce()
        return False
    
    
