# importing turtle
import turtle
import time

# initialise the turtle instance
animation = turtle.Turtle()

#creating animation
# changes speed of turtle
animation.speed(0)
turtle.Screen().setup(width=1.0, height=1.0)
time.sleep(5) 
# hiding turtle
animation.hideturtle()

# changing background color
animation.getscreen().bgcolor("black")

# color of the animation
animation.color("red")

for i in range(100):
	
	# drawing circle using circle function
	# by passing radius i
	animation.circle(i)

	# changing turtle face by 5 degree from it's
	# previous position after drawing a circle
	animation._rotate(5)
