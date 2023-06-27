from turtle import Turtle

MOVE_DISTANCE = 20
UP = (0, 1)
DOWN = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)

class Snake:
    body = [] #list of turtles
    #next_move = []
    color = 'white'
    shape = 'square'
    #head_next_move = (0, 0)
    heading = (1, 0)
    snake_len = 3

    def __init__ (self):
        #self.head_next_move = (self.heading[0]*MOVE_DISTANCE, self.heading[1]*MOVE_DISTANCE)
        #self.next_move = [[self.head_next_move], [self.head_next_move], [self.head_next_move]]
        for i in range(3):
            new_square = Turtle()
            new_square.shape(self.shape)
            new_square.color(self.color)
            new_square.penup()
            start_pos = ((-MOVE_DISTANCE)*i, 0)
            new_square.setpos(start_pos)

            self.body.append(new_square)
            #j = i + 1
            #while j < 3:
            #    self.next_move[j] = [start_pos] + self.next_move[j]
            #    j += 1

    def move(self):
        #self.head_next_move = (self.head_next_move[0]+self.heading[0]*MOVE_DISTANCE
        #                       , self.head_next_move[1]+self.heading[1]*MOVE_DISTANCE)
        #for i in range(self.snake_len):
        #    self.next_move[i].append(self.head_next_move)
        #for i in range(self.snake_len):
        #   move_pos = self.next_move[i].pop(0)
        #    self.body[i].setpos(move_pos)
        current_head_pos = self.body[0].pos()
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


