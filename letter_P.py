"""
Drawing letter P using turtle
"""

import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("green")
  
# Create a Turtle object
pen = turtle.Turtle()
pen.speed(1)  # setset the drawing speed

#  for you to draw the letter p you draw a semi circle first then a straight line going downwards
radius = 60

print('the starting position' + str(pen.position()))  # 
pen.circle(radius, 180)   # draw the semi circle first
pen.left(90)   # then turn left at 90 deegrees i.e. a right angle turn
pen.forward(180)  # then this draws a straight line
print('the last position' + str(pen.position()))


# Close the Turtle graphics window when clicked
screen.exitonclick()
