from turtle import Turtle, Screen
START_POSITION = [(380, 0), (-380, 0)]




class Paddle:


   def __init__(self):
       self.r_paddle = []
       self.l_paddle = []
       self.screen = Screen()
       self.go_to()


   def go_to(self):
       self.r_paddle.append(self.create_paddle(START_POSITION[0]))
       self.l_paddle.append(self.create_paddle(START_POSITION[1]))


   def create_paddle(self, position):
       paddle = Turtle("square")
       paddle.penup()
       paddle.color("white")
       paddle.shapesize(stretch_wid=5, stretch_len=1)
       paddle.goto(position)
       self.screen.update()
       return paddle


   def move_up(self):
       new_y = self.r_paddle[0].ycor() + 20
       self.r_paddle[0].goto(self.r_paddle[0].xcor(), new_y)
       self.screen.update()


   def move_down(self):
       new_y = self.r_paddle[0].ycor() - 20
       self.r_paddle[0].goto(self.r_paddle[0].xcor(), new_y)
       self.screen.update()


   def left_up(self):
       new_y = self.l_paddle[0].ycor() + 20
       self.l_paddle[0].goto(self.l_paddle[0].xcor(), new_y)
       self.screen.update()


   def left_down(self):
       new_y = self.l_paddle[0].ycor() - 20
       self.l_paddle[0].goto(self.l_paddle[0].xcor(), new_y)
       self.screen.update()
