import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Simulator")
screen.tracer(0)

game_is_on = True
snake = Snake()
scoreboard = Scoreboard()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 16:
        food.refresh()
        snake.add_segment()
        scoreboard.increase_score()

    if (snake.head.xcor() > 285 or snake.head.xcor() < -285) or (snake.head.ycor() > 285 or snake.head.ycor() < -285):
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
