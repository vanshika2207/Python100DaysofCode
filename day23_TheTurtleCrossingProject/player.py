STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.reset_position()
        self.left(90)
    def move_forward(self):

        new_y=self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),new_y)



    def reset_position(self):
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])

