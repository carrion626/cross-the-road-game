from turtle import Turtle
import random

COLORS = ['black', 'red', 'purple', 'orange', 'green', 'blue']


class Traffic:

    def __init__(self):
        self.cars = []
        self.x = 5

    def create_traffic(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(400, random_y)
            new_car.setheading(180)
            self.cars.append(new_car)

    def car_move(self):
        for i in self.cars:
            i.forward(self.x)

    def new_level(self):
        self.x += 1
