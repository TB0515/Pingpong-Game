from turtle import Turtle, Screen


class Ball(Turtle):


   def __init__(self):
       super().__init__()
       self.shape("circle")
       self.color("white")
       self.shapesize(1, 1)
       self.penup()
       self.x = 10
       self.y = 10


   def move_ball(self):
       new_x = self.xcor() + self.x
       new_y = self.ycor() + self.y
       self.goto(new_x, new_y)


   def bounce(self):
       self.y *= -1


   def played(self):
       self.x *= -1


   def reset_position(self):
       self.goto(0,0)
       self.x *= -1
