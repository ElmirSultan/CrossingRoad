from turtle import Turtle,Screen
from myturtle import Timturtle
from cars import CarManager
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

my_turtle = Timturtle((0,-280))
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(my_turtle.go_up,"Up")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(my_turtle) < 20:
            game_on = False
            scoreboard.game_over()
    if my_turtle.is_finish():
        my_turtle.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()