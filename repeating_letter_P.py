import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("green")

# Create a Turtle object
pen = turtle.Turtle()
pen.speed(1)  # Set the drawing speed

# straightline_increment = 180
radius = 40
starting_position = pen.position()

for increment in range(100):
    # starting_point += 10
    print('the starting position' + str(pen.position()))
    pen.circle(radius, 180)
    pen.left(90)
    pen.forward(180)
    print('the last position' + str(pen.position()))
    # straightline_increment += 10
    # pen.up()
    pen.setposition(starting_position)



# Close the Turtle graphics window when clicked
screen.exitonclick()
