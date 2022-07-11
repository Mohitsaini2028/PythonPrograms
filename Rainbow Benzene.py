# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
import time

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
turtle.Screen().setup(width=1.0, height=1.0)
time.sleep(5)
turtle.speed(150)
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x//100 + 1)
	t.forward(x)
	t.left(59)
