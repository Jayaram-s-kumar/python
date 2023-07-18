import turtle

# Create a turtle instance
my_turtle = turtle.Turtle()

# Set the turtle speed and shape
# my_turtle.speed(3)
# my_turtle.shape("turtle")

# Move the turtle to starting position
my_turtle.penup()
my_turtle.goto(-100, 0)
my_turtle.pendown()

# Draw the star pattern
for _ in range(5):
    my_turtle.forward(200)
    my_turtle.right(144)

# Hide the turtle
my_turtle.hideturtle()

# Exit on click
turtle.exitonclick()
