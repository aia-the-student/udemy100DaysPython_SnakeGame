from turtle import Turtle

COLOR = 'white'
SHAPE = 'square'

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color('blue')
        self.shape('circle')
        self.penup()
        self.shapesize(0.5,0.5)
        self.setpos(50,50)