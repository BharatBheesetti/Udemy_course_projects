import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game yo")
screen.tracer(0)

game_snake = Snake()
food = Food()
game_score = Score()

screen.listen()
screen.onkey(game_snake.up, "Up")
screen.onkey(game_snake.down, "Down")
screen.onkey(game_snake.left, "Left")
screen.onkey(game_snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    game_snake.move()

# detect snake collision with food
    if game_snake.head.distance(food) < 15:
        food.refresh()
        game_snake.grow()
        game_score.score_refresh()

# detect snake collision with the wall
    if game_snake.head.xcor() > 280 or game_snake.head.xcor() < -280 or game_snake.head.ycor() > 280 or game_snake.head.ycor() < - 280:
        game_is_on = False
        game_score.gameover()

# detect snake collision with itself

    for segment in game_snake.segments[1:]:
        if game_snake.head.distance(segment)<10:
            game_is_on = False
            game_score.gameover()


screen.exitonclick()


