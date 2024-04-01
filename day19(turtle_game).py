import turtle
from turtle import Turtle, Screen
import random
##Etch a skech app
# def move_forward():
#     tim.forward(10)
#
# def move_backword():
#     tim.backward(10)
#
# def counter_clockwise():
#     tim.left(10)
#
# def clockwise():
#     tim.right(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen=Screen()
# screen.listen()
# #screen.onkey(key="space",fun=move_forward)
# screen.onkey(key="w",fun=move_forward)
# screen.onkey(key="s",fun=move_forward)
# screen.onkey(key="a",fun=counter_clockwise)
# screen.onkey(key="d",fun=clockwise)
# screen.onkey(key="c",fun=clear)
all_turtle=[]
##Turtle race app
colors=["red","orange","yellow","green","blue","purple"]
is_race_on=False
y_pos=[-100,-60,-20,20,60,100]
for turtle_index in range(0,6):
    tim=Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=y_pos[turtle_index])
    all_turtle.append(tim)
# tim1.penup()

# tim1.goto(x=-230,y=-100)
# tim1.color(colors[0])
# tim2=Turtle(shape="turtle")
# tim2.penup()
# tim2.goto(x=-230,y=-60)
# tim2.color(colors[1])
# tim3=Turtle(shape="turtle")
# tim3.penup()
# tim3.goto(x=-230,y=-20)
# tim3.color(colors[2])
# tim4=Turtle(shape="turtle")
# tim4.penup()
# tim4.goto(x=-230,y=20)
# tim4.color(colors[3])
# tim5=Turtle(shape="turtle")
# tim5.penup()
# tim5.goto(x=-230,y=60)
# tim5.color(colors[4])
# tim6=Turtle(shape="turtle")
# tim6.penup()
# tim6.goto(x=-230,y=100)
# tim6.color(colors[5])
#


screen=Screen()
screen.setup(width=500,height=400) #screen setup
user_text=screen.textinput(title="Make your bet",prompt="Which turtle will win the race ? Enter a color:")
if user_text:
    is_race_on=True
while is_race_on:
    for turtle in all_turtle:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_text:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
