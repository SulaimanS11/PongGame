from turtle import Turtle

class Ball(Turtle):
    def __init__(self, height, width, paddle = None, opp_paddle = None) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0,0)
        self.paddle = paddle
        self.opp_paddle = opp_paddle
        self.height = height
        self.width = width
        self.movex = 1
        self.movey = 1
    
    def move(self) -> None:
        self.goto(self.xcor() + self.movex, self.ycor() + self.movey)
        self.check_WallCollision(height=self.height, width=self.width)
        self.check_PaddleCollision()

    def bounceWall(self) -> None:
        self.movey = -1 * self.movey

    def bouncePaddle(self) -> None:
        self.movex = -1 * self.movex
        

    def reset_pos(self) -> None:
        self.goto(0,0)
        self.move()
    
    def check_WallCollision(self, height, width) -> False:
        if self.ycor() > (height/2) or self.ycor() < -(height/2):
            self.bounceWall()
        if self.xcor() > (width/2) or self.xcor() < -(width/2):
            self.reset_pos()
        return False
    
    def check_PaddleCollision(self) -> False:
        if self.distance(self.paddle) < 50 and self.xcor() < -320:
            self.bouncePaddle()

        if self.distance(self.opp_paddle) < 50 and self.xcor() > 320:
            self.bouncePaddle()

        return False

    
    
