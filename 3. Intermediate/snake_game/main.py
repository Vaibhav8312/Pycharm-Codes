from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        # is_game_on = False
        # scoreboard.game_over()


    # Used the concept of slicing
    # Detect collision with tail
    for segment in snake.segments[1:]:
        # if head collides with any segment in the tail:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # is_game_on = False
            # Trigger game_over
            # scoreboard.game_over()

    # # Detect collision with tail
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     # if head collides with any segment in the tail:
    #     elif snake.head.distance(segment) < 10:
    #         is_game_on = False
    #         # Trigger game_over
    #         scoreboard.game_over()



screen.exitonclick()
