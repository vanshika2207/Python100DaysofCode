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
