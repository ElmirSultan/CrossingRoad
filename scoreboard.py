from turtle import Turtle

font = ("Courier", 24 , "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.write(f"Level: {self.level}",align="left",font=font)

    def update_score(self):
         self.clear()
         self.write(f"Level: {self.level}",align="left",font=font)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=font)
