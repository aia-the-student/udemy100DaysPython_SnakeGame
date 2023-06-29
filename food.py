from turtle import Turtle
import random

COLOR = 'white'
SHAPE = 'square'
X_START = -260
X_END = 260
Y_START = -260
Y_END = 260


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color('blue')
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.change_pos()

    def change_pos(self):
        x = random.randint(a=X_START, b=X_END)
        y = random.randint(a=Y_START, b=Y_END)
        self.setpos(x, y)
