#pong game
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
#create the screen
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)
#create another paddle
l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
ball=Ball()
score=Scoreboard()
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # detect collision with wall and bounce
    if ball.ycor()>280 or ball.ycor()< (-280):
        #need to bounce
        ball.bounce_y()
    #detect collision with paddle
    if ball.distance(r_paddle) <50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    ##detect when paddle misses
    #detect r paddle misses
    if ball.xcor()>300:
        ball.reset_position()
        score.l_point()
    #detect l paddle misses
    if ball.xcor() < -300:
        ball.reset_position()
        score.r_point()
screen.exitonclick()