from turtle import Screen
from chicken import Chicken
from traffic import Traffic
import time
from score_b import Score

screen = Screen()
screen.setup(800, 800)
screen.tracer(0)
screen.listen()

chik = Chicken()
cars = Traffic()
score = Score()

screen.onkey(key='Up', fun=chik.move_u)

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

    cars.create_traffic()
    cars.car_move()

    for i in cars.cars:
        if i.distance(chik) < 20:
            score.game_over()
            game_on = False

    if chik.ycor() >= 250:
        score.next_round()
        chik.setposition(0, -300)
        cars.new_level()


screen.exitonclick()
