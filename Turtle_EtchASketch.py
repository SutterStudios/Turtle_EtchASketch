#Author: Alexander Sutter
import turtle

screen = turtle.Screen()

move = 50 #steps
turn = 90 #degrees

def w():
  turtle.fd(move)
def a():
  turtle.lt(turn)
def s():
  turtle.bk(move)
def d():
  turtle.rt(turn)


screen.onkey(w, "Up")
screen.onkey(s, "Down")
screen.onkey(a, "Left")
screen.onkey(d, "Right")

screen.listen()
turtle.done()

#try adding up and down too
