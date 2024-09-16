from turtle import Turtle, exitonclick

def draw_balloon(turtle, radius, balloon_color, string_length):
    # Draw the balloon (circle)
    turtle.penup()
    turtle.goto(0, -radius)  # Position the turtle to start drawing the balloon
    turtle.pendown()
    turtle.color(balloon_color)  # Set the color of the balloon
    turtle.begin_fill()
    turtle.circle(radius)  # Draw the balloon
    turtle.end_fill()
    
    # Draw the balloon string
    turtle.penup()
    turtle.goto(0, -radius)  # Move to the bottom of the balloon
    turtle.pendown()
    turtle.color("black")  # Set the color of the string
    turtle.right(90)
    turtle.forward(string_length)  # Draw the string
    
    # Draw a small oval or circle at the end of the string
    turtle.penup()
    turtle.goto(0, -radius - string_length)  # Move to the end of the string
    turtle.pendown()
    turtle.color("black")  # Set the color for the end of the string
    turtle.begin_fill()
    turtle.circle(5)  # Draw a small circle at the end of the string
    turtle.end_fill()

def draw_shapes():
    bob = Turtle()
    bob.speed(2)
    bob.pensize(2)
    bob.shape("turtle")
    
    draw_balloon(bob, 50, "red", 150)  # Draw a balloon with radius 50, color red, and string length 150

    bob.hideturtle()

if __name__ == "__main__":
    draw_shapes()
    exitonclick()