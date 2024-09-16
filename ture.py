from turtle import Turtle, exitonclick

def draw_square(turtle, side_length):
    # Draw a square
    turtle.penup()
    turtle.goto(-side_length / 2, side_length / 2)  # Move to the starting position
    turtle.pendown()
    turtle.color("red")  # Set the color for the square
    turtle.begin_fill()
    
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)  # Turn 90 degrees to create the square
    
    turtle.end_fill()

def draw_shapes():
    bob = Turtle()
    bob.speed()
    bob.pensize()
    bob.shape("turtle")
    
    draw_square(bob, 100)  # Draw a square with sides of 100 units

    bob.hideturtle()

if __name__ == "__main__":
    draw_shapes()
    exitonclick()