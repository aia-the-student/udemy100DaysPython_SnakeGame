from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)

screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_scoreboard = Scoreboard()


def right():
    my_snake.change_heading("right")


def left():
    my_snake.change_heading("left")


def up():
    my_snake.change_heading("up")


def down():
    my_snake.change_heading("down")


screen.listen()
screen.onkey(key='Up', fun=up)
screen.onkey(key='Down', fun=down)
screen.onkey(key='Right', fun=right)
screen.onkey(key='Left', fun=left)

screen.update()
game_is_on = True
while game_is_on:
    my_snake.move()
    screen.update()

    # detect if food is touched
    dist = my_food.distance(my_snake.body[0].pos())
    if dist < 15:
        my_snake.grow()
        my_food.change_pos()
        my_scoreboard.add_counter()
    time.sleep(0.20)

    # detect if collision with the wall
    head_pos = my_snake.head.pos()
    if max(abs(head_pos[0]), abs(head_pos[1])) > 280:
        #game_is_on = False
        #my_scoreboard.game_over()
        my_scoreboard.reset_hs()
        my_snake.reset()

    # detect collisions with its tail
    for segment in my_snake.body[1:]:
        if my_snake.head.distance(segment.pos()) < 10:
            #game_is_on = False
            #my_scoreboard.game_over()
            my_scoreboard.reset_hs()
            i = my_snake.snake_len #??? not sure that what it is for
            my_snake.reset()

screen.exitonclick()
