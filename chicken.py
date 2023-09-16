from turtle import Turtle


class Chicken(Turtle):

    def __init__(self):
        super().__init__()
        self.create_chicken()

    def create_chicken(self):
        self.shape('turtle')
        self.penup()
        self.goto(0, -300)
        self.setheading(90)

    def move_u(self):
        self.forward(20)
