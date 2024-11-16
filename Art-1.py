import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Background color
artist = turtle.Turtle()
artist.color("green")   # Tree color
artist.speed(0)         # Fastest drawing speed
artist.left(90)         # Start facing up
artist.penup()
artist.goto(0, -300)    # Starting position
artist.pendown()

# Function to draw a branch
def draw_branch(branch_length, angle):
    if branch_length > 5:  # Base case to stop recursion
        artist.forward(branch_length)
        artist.right(angle)         # Turn right for the new branch
        draw_branch(branch_length - 15, angle)  # Right branch
        artist.left(angle * 2)      # Turn left for the other branch
        draw_branch(branch_length - 15, angle)  # Left branch
        artist.right(angle)         # Return to the original angle
        artist.backward(branch_length)  # Move back to the previous branch

# Draw the tree
draw_branch(100, 20)  # Initial branch length and angle

# Hide the turtle and finish
artist.hideturtle()
turtle.done()
