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



if __name__=="__main__":
    my_funtion()  
    func2()


    def draw_f():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    
    bob = turtle.Turtle()
    bob.speed(2)  
    bob.pensize(3) 
    bob.shape("turtle")  
    bob.penup() 
    bob.goto(-100, 100)  
    bob.pendown()  
    bob.right(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(60)
    bob.backward(60)
    bob.right(90)
    bob.forward(40)
    bob.backward(40)
    bob.left(90)
    bob.forward(60)
    bob.right(90)
    bob.forward(60)
  
    bob.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_f()