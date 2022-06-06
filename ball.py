from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10


    def move(self):
        new_xc = self.xcor() + self.x_move
        new_yc = self.ycor() + self.y_move
        self.goto(new_xc, new_yc)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def res(self):
        self.goto(0,0)
        self.bounce_x()

