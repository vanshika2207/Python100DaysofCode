FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level=1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-210,250)
        self.write(f"LEVEL :{self.level}",align="center",font=FONT)

    def level_up(self):
        self.level+=1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

