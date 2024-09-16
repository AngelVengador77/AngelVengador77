def my_funtion ():
    print("So close, no matter how far")
    print("Couldn't be much more from the heart")
    print("Forever trusting who we are")
    print("And nothing else matters")
    print("Never opened myself this way")
    print("Life is ours, we live it our way")
    print("All these words, I don't just say")
    print("And nothing else matters")
    
    
def func2():
    print("Trust I seek and I find in you")
    print("Every day for us something new")
    print("Open mind for a different view")
    print("And nothing else matters")
    print("Never cared for what they do")
    print("Never cared for what they know")
    print("But I know")

def func3():
print("So close, no matter how far")
print("It couldn't be much more from the heart")
print("Forever trusting who we are")
print("And nothing else matters")
print("Never cared for what they do")
print("Never cared for what they know")
print("But I know")



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
    bob.speed(2)
    bob.pensize(3)
    bob.shape("turtle")
    
    draw_square(bob, 100)  # Draw a square with sides of 100 units

    bob.hideturtle()

if __name__ == "__main__":
    draw_shapes()
    exitonclick()






balon 


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