from turtle import Turtle
finish_line = 280
starting_position  = (0,-280)
class Timturtle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("black")
        self.penup()

        self.go_to_start()
    def go_up(self):
        road = self.ycor() + 20
        self.goto(0,road)

    def go_to_start(self):
        self.goto(starting_position)

    def is_finish(self):
        if self.ycor() > finish_line:
            return True
        else:
            return False

