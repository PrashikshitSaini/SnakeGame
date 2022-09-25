from turtle import Screen
from game import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600) # to set the dimension of the poject
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)  # turn off the turtle animations

snake = Snake()
food = Food()



screen.listen() # to give response to actions or press
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_right, key="Right")
screen.onkey(fun=snake.move_left, key="Left")

game_is_on = True
scoreboard = Scoreboard()

while game_is_on:
    screen.update()  # only update when all segs are in right positions
    time.sleep(0.1)
    snake.move()

    # Detect collision with Food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

        print(f"SCORE = {scoreboard.high_score}")



     # Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            print(f"SCORE = {scoreboard.high_score}")
     # if head collides with any segment in the tail:
          #trigger game_over


screen.exitonclick()
