from turtle import Screen
import time
from snake import Snake
from food import Food


screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)

screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

my_snake = Snake()
my_food = Food()

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
i = 0
while game_is_on:
    my_snake.move()
    screen.update()
    i = i + 1
    if i > 30:
        game_is_on = False
    time.sleep(0.5)


screen.exitonclick()