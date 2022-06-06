import time
from turtle import Turtle, Screen
from slider import Slider
from ball import Ball
from score_board import ScoreBoard
sc = Screen()
sc.bgcolor("black")
sc.setup(width=1.0, height=1.0)
sc.tracer(0)
sc.title("WELCOME TO PONG!")

right_slider = Slider(620,0)
left_slider = Slider(-630, 0)
b = Ball()
s = ScoreBoard()

sc.listen()
sc.onkey(right_slider.upkey, "q")
sc.onkey(right_slider.downkey, "w")
sc.onkey(left_slider.upkey, "a")
sc.onkey(left_slider.downkey, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    sc.update()
    b.move()
    if b.ycor() > 310 or b.ycor() < -300:
        b.bounce_y()
    if b.distance(right_slider) < 50 and b.xcor() > 590 or b.distance(left_slider) < 50 and b.xcor() < -600:
        b.bounce_x()
    if b.xcor() > 615:
        b.res()
        s.l_point()
    if b.xcor() < -625:
        b.res()
        s.r_point()

sc.exitonclick()
