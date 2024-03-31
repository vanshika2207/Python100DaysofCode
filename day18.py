import random
# import turtle
# from turtle import Turtle, Screen
# 
# # color=['light steel blue','cyan','aquamarine',
# #        'green yellow','olive','lemon chiffon',
# #        'peru','orange','indian red','magenta',
# #        'hotpink','indigo','tomato','lime green',
# #        'steel blue','yellow','crimson','plum',
# #        'medium orchid','dark magenta','blue violet']
# tim=Turtle()
# # timmy_the_turtle.shape('turtle')
# # timmy_the_turtle.color("cyan4")
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)
# 
# ## Draw a square
# '''
# tim.shape('arrow')
# tim.color('magenta')
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
# '''
# ##Draw a dashed line
# '''
# tim.shape('classic')
# tim.color('dark olive green')
# for i in range(30):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)
# '''
# ### draw triangle to decagon
# '''
# tim.shape('square')
# for i in range(3,11):
#     a=random.choice(color)
#     color.remove(a)
#     tim.color(a)
#     angle=360/i
#     for j in range(i):
#         tim.forward(100)
#         tim.right(angle)
# 
# '''
# #random colour
# turtle.colormode(255)
# def random_colour():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
# 
#     tuple1=(r,g,b)
#     return tuple1
# 
# #draw a random walk
# '''
# tim.shape('circle')
# tim.speed("fastest")
# tim.width(15)
# 
# movement=[0,90,100,270]
# 
# for i in range(200):
#     tim.color(random_colour())
#     tim.forward(30)
#     tim.setheading(random.choice(movement))
# '''
# #make spirograph
# tim.speed("fastest")
# tim.shape('circle')
# def size_of_gap(size_of_gap):
#     for i in range(360//size_of_gap):
#         tim.color(random_colour())
#         tim.circle(100)
#         current_heading=tim.heading()
#         tim.setheading(tim.heading()+size_of_gap)
# size_of_gap(1)
# screen=Screen()
# screen.exitonclick()
##final project
# import colorgram
# colors=colorgram.extract('art.png',20)
#
# a=[]
# for i in range(len(colors)):
#     r=colors[i].rgb[0]
#     g=colors[i].rgb[1]
#     b=colors[i].rgb[2]
#     rgb=(r,g,b)
#     a.append(rgb)
# print(a)
from turtle import Turtle,Screen
import random
colors=[(238, 228, 217), (217, 157, 97), (125, 166, 192), (45, 109, 149), (214, 232, 223), (236, 216, 223), (201, 138, 159), (151, 67, 89), (127, 183, 157), (211, 225, 234), (35, 131, 99), (211, 92, 65), (233, 199, 105), (163, 76, 57), (192, 87, 114), (165, 159, 46), (65, 165, 135), (232, 165, 182), (42, 158, 186), (16, 95, 70)]
tim=Turtle()
# Set the color mode to 255 for RGB tuples
Screen().colormode(255)
tim.speed("fastest")
tim.pu()
tim.hideturtle()
tim.setheading(225)
tim.forward(100)
tim.setheading(0)
number_of_dots=100
for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(colors))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen=Screen()
screen.exitonclick()
