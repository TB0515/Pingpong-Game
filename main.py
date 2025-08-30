from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pingpong Game")
screen.listen()
screen.tracer(0)


paddle = Paddle()
ball = Ball()
score = Scoreboard()
speed = 0.1


screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")
screen.onkey(paddle.left_up, "w")
screen.onkey(paddle.left_down, "s")


game_is_on = True


while game_is_on:
   screen.update()
   time.sleep(speed)
   ball.move_ball()
   r_collide = ball.distance(paddle.r_paddle[0].pos())
   l_collide = ball.distance(paddle.l_paddle[0].pos())
   if score.l_score == 5 or score.r_score == 5:
       game_is_on = False
       score.winner()
   elif ball.ycor() <= -280 or ball.ycor() >= 280:
       ball.bounce()
   elif r_collide <= 45 and ball.xcor() > 360 or l_collide <= 45 and ball.xcor() < -360:
       ball.played()
       if speed != 0:
           speed -= 0.01
   elif ball.xcor() > 380:
       ball.reset_position()
       score.increase_lscore()
   elif ball.xcor() < -380:
       ball.reset_position()
       score.increase_rscore()

screen.exitonclick()