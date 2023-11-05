# draws a unique shape of 4 P'S increasing in size
import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("green")

# Create a Turtle object
pen = turtle.Turtle()
pen.speed(1)  # Set the drawing speed

# Function to draw the letter "P"
def draw_p(size):
    pen.circle(size, 180)
    pen.left(90)
    pen.forward(180)
    # pen.left(90)

# Draw multiple "P" shapes of increasing sizes
for size in range(100):  # Adjust the range as needed
    draw_p(size)

# Close the Turtle graphics window when clicked
screen.exitonclick()
