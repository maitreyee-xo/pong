from turtle import Turtle


class Slider(Turtle):
    def __init__(self, xc, yc):
        super().__init__()
        self.clear()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.right(90)
        self.penup()
        self.goto(xc, yc)

    def upkey(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def downkey(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
