from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.chk = 1
        self.goto(0, 350)
        self.write(f'ROUND: {self.chk}', align='center', font=('Arial', 20, 'normal'))
        self.hideturtle()

    def next_round(self):
        self.clear()
        self.chk += 1
        self.write(f'ROUND: {self.chk}', align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.color('black')
        self.penup()
        self.goto(0, 0)
        self.write(f'FENITA', align='center', font=('Arial', 20, 'normal'))
