from turtle import Turtle


class Scoreboard(Turtle):


   def __init__(self):
       super().__init__()
       self.color("white")
       self.hideturtle()
       self.penup()
       self.goto(0, 260)
       self.l_score = 0
       self.r_score = 0
       self.write(f"{self.l_score} | {self.r_score}", False, align="center", font=('Arial', 24, 'normal'))


   def increase_rscore(self):
       self.clear()
       self.r_score += 1
       self.write(f"{self.l_score} | {self.r_score}", False, align="center", font=('Arial', 24, 'normal'))


   def increase_lscore(self):
       self.clear()
       self.l_score += 1
       self.write(f"{self.l_score} | {self.r_score}", False, align="center", font=('Arial', 24, 'normal'))


   def winner(self):
       if self.l_score == 5:
           self.goto(0,200)
           self.write("Left Player Wins!", move=False, align="center", font=('Arial', 24, 'normal'))
       else:
           self.goto(0, 200)
           self.write("Right Player Wins!", move=False, align="center", font=('Arial', 24, 'normal'))
