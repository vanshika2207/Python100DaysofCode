from turtle import Turtle

#create and move the paddle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position[0],position[1])
    def up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
    def down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)



