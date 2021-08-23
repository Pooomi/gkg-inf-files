################################
#                              #
# SNAKE.PY                     #
#                              #
# Author:  Andreas Aeschlimann #
# Date:    26 October 2020     #
#                              #
################################

###########
# IMPORTS #
###########


from gturtle import *


#####################
# GLOBAL PROPERTIES #
#####################


# Key codes
KEY_CODE_LEFT = 37

KEY_CODE_RIGHT = 39

KEY_CODE_UP =38

KEY_CODE_DOWN = 40

KEY_CODE_ENTER = 10

# Constant settings
frameSize = 500

# General properties
points = 0
highScore = 0
lastKey = None
name = ""

# Turtle properties
tf = TurtleFrame()
snakeTurtle = None
frameTurtle = None
appleTurtle = None
stoneTurtles = []


#############
# FUNCTIONS #
#############


#
# FUNCTIONS TO DRAW SHAPES WITH TURTLES
#
def   onKeyPressed(e):
    global lastKey  
    print e.getKeyCode()
    if  e.getKeyCode() == KEY_CODE_LEFT and snakeTurtle.heading ()!=90:     
        lastKey = e.getKeyCode()
    elif e.getKeyCode()== KEY_CODE_RIGHT and snakeTurtle.heading ()!=-90:     
        lastKey = e.getKeyCode()
    elif e.getKeyCode()== KEY_CODE_UP and snakeTurtle.heading ()!=180:     
        lastKey = e.getKeyCode()
    elif e.getKeyCode() == KEY_CODE_DOWN and snakeTurtle.heading ()!=0:     
        lastKey = e.getKeyCode()
        
def MovementCreationOfSnake ():
    global lastKey
    print lastKey
    if lastKey == KEY_CODE_LEFT:
        snakeTurtle.setHeading (-90)
    elif lastKey == KEY_CODE_RIGHT:
        snakeTurtle.setHeading (90)
    elif lastKey == KEY_CODE_DOWN:
        snakeTurtle.setHeading (180)
    elif lastKey == KEY_CODE_UP:
        snakeTurtle.setHeading (0)   
        

# Todo: Put functions here and remove this line <---------------------

#
# FUNCTIONS ON SPECIFIC TURTLES
#

# Checks whether the snake (turtle) is alive or not.
# We have to find out the position of the turtle.
# Then we check if the turtle touches a stone or the main frame (blue square).
# Returns True or False.
def snakeTurtleIsAlive():
    # Todo: Put code here and remove this line <---------------------
    # Tip: Use if / else - conditions
    # Write "return False" if the turtle is dead, otherwise write "return True"

    return True

# Todo: Put functions here and remove this line <---------------------

#
# GENERAL METHODS
#


# Waits until a name is entered by a dialog.
# It saves the name to the global variable name.

def InPutNameCreation():
    global name # we want to change the value
    name = "Anonymous"
    input ("Enter Name")

 

    print "Name entered: " + name
    name = "Anonymous"
    # Todo: Put code here and remove this line <---------------------

    print "Name entered: " + name # Remove this if you want

# Todo: Put functions here and remove this line <---------------------

#
# FUNCTIONS TO CREATE TURTLES
#


def SnakeCreation():
   global snakeTurtle
   snakeTurtle = Turtle(tf, "snake.png", keyPressed = onKeyPressed)
   snakeTurtle.setPos(0,0)
   snakeTurtle.penUp()
def AppleCreation():
   appleTurtle = Turtle(tf)
   appleTurtle.setRandomPos(0.9*frameSize, 0.9*frameSize)
   appleTurtle.setColor("red")
   
   
def FrameCreation():
   global frameTurtle
   frameTurtle = Turtle(tf)
   frameTurtle.setPos(250,-250)
   frameTurtle.hideTurtle()
   repeat 4:
      frameTurtle.forward(500)
      frameTurtle.left(90)

def snakeTurtleIsAlive():
#    print "Koordinaten", snakeTurtle.getX(), snakeTurtle.getY()
    if snakeTurtle.getX()+5 < 235 and snakeTurtle.getX()-5 > -235 and snakeTurtle.getY()+5 < 235 and snakeTurtle.getY()-5 >-235:
        snakeTurtle.forward(11)
        MovementCreationOfSnake()
        
        return True  
    
    
    else:
        return False   


    

    



# Todo: Put functions here and remove this line <---------------------

#
# MAIN METHODS
#

# The function to play the game.
# Reset some stuff first, like the snake turtle, points, etc.
def play():
       
    global points # we want to change the value
    print "Play function started" # Remove this if you want
    # Reset the snake and apple turtles
    # Todo: Put code here and remove this line <---------------------

    # Reset the points and display them
    # Todo: Put code here and remove this line <---------------------
    SnakeCreation ()
    AppleCreation ()
    i = 0
    isAlive = True
    
    while (isAlive): # Run the game while the snake is alive



        # Check if the snake is still alive
        isAlive = snakeTurtleIsAlive()

        i = i + 1
    

    
        
    
   

          

 


    # The game is over now
    # Todo: Put code here and remove this line <---------------------

# The main function.
# Set up stuff here that stays alive for the whole application.
# Create the frame (turtle), ask for the user name etc.







#main()#################






#    print "Main function started" # Remove this if you want

    # Wait until a name is input
#waitForInputName();

#createmyFrame()



#drawing the frame
    # createFrameTurtle() <- You could write a function with this name

    # Start the actual game
#play()



#############
# MAIN CODE #
#############
def main():
    InPutNameCreation();
    FrameCreation()
    play()

# Only call the main function here.
# Put all general functionality into the main function.
main()



# No code here! Everything goes in main, play or other functions!