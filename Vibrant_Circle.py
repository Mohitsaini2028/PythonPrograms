import turtle
import time

import random
color =["red","green","blue","orange","purple","yellow"] 
t = turtle.Turtle()
s = turtle.Screen()

s.setup(width=1.0, height=1.0)
s.bgcolor("black")
t.pencolor("white")

time.sleep(10)

t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()

a = 0
b = 0
count=0

while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    count+=1
    #if count%1000:
        #t.color(random.choice(color))
    if b ==210:
        break
    t.hideturtle()
turtle.done()
