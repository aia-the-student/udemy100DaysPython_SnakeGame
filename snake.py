from turtle import Turtle
from turtle import Screen

MOVE_DISTANCE = 20
UP = (0, 1)
DOWN = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)


class Snake:
    body = []   # list of turtles
    # next_move = []
    color = 'white'
    shape = 'square'
    # head_next_move = (0, 0)
    heading = (1, 0)
    snake_len = 0

    def __init__(self):
        # self.head_next_move = (self.heading[0]*MOVE_DISTANCE, self.heading[1]*MOVE_DISTANCE)
        # self.next_move = [[self.head_next_move], [self.head_next_move], [self.head_next_move]]

        # self.snake_len = 0
        # for _ in range(3):
        #     self.grow()
        #     # j = i + 1
        #     # while j < 3:
        #     #     self.next_move[j] = [start_pos] + self.next_move[j]
        #     #     j += 1
        # self.head = self.body[0]
        self.reset()

    def move(self):
        # self.head_next_move = (self.head_next_move[0]+self.heading[0]*MOVE_DISTANCE
        #                        , self.head_next_move[1]+self.heading[1]*MOVE_DISTANCE)
        # for i in range(self.snake_len):
        #     self.next_move[i].append(self.head_next_move)
        # for i in range(self.snake_len):
        #    move_pos = self.next_move[i].pop(0)
        #     self.body[i].setpos(move_pos)

        current_head_pos = self.head.pos()
        for i in range(self.snake_len-1, 0, -1):
            self.body[i].setpos(self.body[i-1].pos())
        self.body[0].setpos((current_head_pos[0]+self.heading[0]*MOVE_DISTANCE,
                             current_head_pos[1]+self.heading[1]*MOVE_DISTANCE))

    def change_heading(self, direction):
        if (direction == 'right') & (self.heading != LEFT):
            self.heading = RIGHT
        if (direction == 'up') & (self.heading != DOWN):
            self.heading = UP
        if (direction == 'left') & (self.heading != RIGHT):
            self.heading = LEFT
        if (direction == 'down') & (self.heading != UP):
            self.heading = DOWN

    def grow(self):
        new_square = Turtle()
        new_square.penup()
        new_square.shape(self.shape)
        new_square.color(self.color)
        if self.snake_len < 4:
            start_pos = ((-MOVE_DISTANCE) * self.snake_len, 0)
        else:
            last_pos = self.body[-1].pos()
            pre_last_pos = self.body[-2].pos()
            start_pos = (2*last_pos[0]-pre_last_pos[0],
                         2*last_pos[1]-pre_last_pos[1])
        new_square.setpos(start_pos)
        self.body.append(new_square)
        self.snake_len += 1

    def reset(self):

        for _ in range(self.snake_len):
            s = self.body.pop()
            s.hideturtle()
            del s

        self.snake_len = 0
        for _ in range(3):
            self.grow()
        self.head = self.body[0]

