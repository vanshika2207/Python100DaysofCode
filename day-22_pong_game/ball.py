#create the ball and make it move
from turtle import  Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.color("white")
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1
    def move(self):
        random_x=self.xcor()+self.x_move
        random_y=self.ycor()+self.y_move
        self.goto(random_x,random_y)

    def bounce_y(self):
        self.y_move*=-1
        self.move_speed*=0.9

    def bounce_x(self):
        self.x_move*=-1



    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()




