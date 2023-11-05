import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("green")

# Create a Turtle object
pen = turtle.Turtle()
pen.speed(1)  # Set the drawing speed

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        pen.forward(size)
        pen.left(90)

# Draw multiple squares of increasing sizes
for size in range(20, 101, 20):  # Adjust the range and step size as needed
    draw_square(size)
    pen.penup()
    pen.forward(20)  # Move the pen to the side for the next square
    pen.pendown()

# Close the Turtle graphics window when clicked
screen.exitonclick()
