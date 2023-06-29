from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 10, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.setpos(0, 240)
        self.counter = 0
        self.update_scoreboard()

    def add_counter(self):
        self.counter += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg="Score is: " + str(self.counter),
                   align=ALIGN,
                   font=FONT)

    def game_over(self):
        self.setpos((0, 0))
        self.write(arg="Game Over.",
                   align=ALIGN,
                   font=FONT)
