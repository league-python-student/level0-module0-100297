import random
import turtle

# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def getNextColor(i):
    return colors[i % len(colors)]

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('black')
    window.setup(width=0.75, height=0.9, startx=0, starty=0)

    colors = ('red', 'black','blue', 'black','green', 'black','white', 'black','purple','black')

    # Make a new turtle
    Zach = turtle.Turtle()
    # Make the turtle shape 'turtle', .shape('turtle')
    Zach.shape('turtle')
    # Set the turtle speed to max (0)
    Zach.speed(0)
    # Set the turtle width to 1
    Zach.width = 1
    # Create a variable to hold the number of sides in a pentagon
    psides = 10
    # Create a variable to be the angle of 360 divided by the sides variable
    pangle = 360/psides
    # Use a for loop to repeat ALL the following lines of code 360 times. 
    for i in range(360):
        # If the loop variable (i) is equal to 100, set the turtle width to 2
        if i == 100:
            turtle.width = 2
        # If the loop variable (i) is equal to 200, set the turtle width to 3
        if i == 200:
            turtle.width = 3
        # Use the getNextColor function to set the turtle pencolor,
        # *hint .pencolor(getNextColor(i)) 
        Zach.pencolor(getNextColor(i))
        # Move the turtle forward by the loop variable, *hint .forward(i)
        Zach.forward(i)
        # Turn the turtle to the right by the angle variable + 1
        Zach.right(pangle + 1)
    # Hide your turtle so you can see the pattern.
        Zach.hideturtle()
    # Check the pattern against the picture in the recipe. If it matches, you are done!

    # Variations:
    # *Make the pattern really huge
    # *Change the colors
    # *Experiment with different shapes

    # Call the turtle.done() method
    turtle.done()