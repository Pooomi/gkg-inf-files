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
KEY_CODE_UP = 38
KEY_CODE_DOWN = 40
KEY_CODE_ENTER = 10

# Constant settings
frameSize = 500

# General properties
points = 0
highScore = 0
lastKey = None
name = ""
dangerzone = 10
numberOfStones = 0
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

def onKeyPressed(key):
   global lastKey
   
   print key.getKeyCode # gibt aus, welche Taste gedrückt wurde
   if  key.getKeyCode () == KEY_CODE_LEFT:
      lastKey = key.getKeyCode ()
   elif key.getKeyCode ()== KEY_CODE_RIGHT:
      lastKey = key.getKeyCode ()
   elif key.getKeyCode () == KEY_CODE_UP:
      lastKey = key.getKeyCode ()
   elif key.getKeyCode () == KEY_CODE_DOWN:
      lastKey = key.getKeyCode ()
   elif key.getKeyCode() == KEY_CODE_ENTER:
      lastKey = key.getKeyCode()
   TurnSnakeTurtle() #Ruft Funktion auf, mit der die Turtle gedreht wird
   
# wir bestimmen, dass der Computer weiss, welche Taste zuletzt gedrückt wurde. (lastKey)


def TurnSnakeTurtle(): # Es wird jeweils getestet, in welche Taste zuletzt gedrückt wurde und ob die Turtle nicht in die entgegengesetzte Richtung schaut.
   #Dann wird die Ausrichtung entsprechend neu gesetzt
   global lastKey
   print lastKey
   if lastKey == KEY_CODE_LEFT and snakeTurtle.heading()!=90: 
      snakeTurtle.setHeading(-90)
   elif lastKey == KEY_CODE_RIGHT and snakeTurtle.heading()!=-90:
      snakeTurtle.setHeading(90)
   elif lastKey == KEY_CODE_UP and snakeTurtle.heading()!=180:
      snakeTurtle.setHeading(0)
   elif lastKey == KEY_CODE_DOWN and snakeTurtle.heading()!=0:
      snakeTurtle.setHeading(180)
      
#Funktion, mit der die SnakeTurtle gedreht wird
#
# FUNCTIONS ON SPECIFIC TURTLES
#

# Checks whether the snake (turtle) is alive or not.
# We have to find out the position of the turtle.
# Then we check if the turtle touches a stone or the main frame (blue square).
# Returns True or False.
def snakeTurtleIsAlive():
   global frameSize  
   if snakeTurtle.getX()> frameSize/2 -15:
      snakeTurtle.hideTurtle()
      return False
   elif snakeTurtle.getX()< -frameSize/2 +15:
      snakeTurtle.hideTurtle()
      return False
   elif snakeTurtle.getY()> frameSize/2 -15:
      snakeTurtle.hideTurtle()
      return False
   elif snakeTurtle.getY()< -frameSize/2 +15:
      snakeTurtle.hideTurtle()
      return False
   
   for i in range(numberOfStones):
      dist = snakeTurtle.distance(stoneTurtles[i])
      if dist < dangerzone :
         return False
      
   eatApple()
   return True


#
# GENERAL METHODS
#



# Waits until a name is entered by a dialog.
# It saves the name to the global variable name.
def waitForInputName():
    global name # we want to change the value

    name = input ("enter name")
    # Todo: Put code here and remove this line <---------------------

    print "Name entered: " + name # Remove this if you want

# Todo: Put functions here and remove this line <---------------------

#
# FUNCTIONS TO CREATE TURTLES
#
def createSnake():
   global snakeTurtle
   snakeTurtle = Turtle(tf, "snake.png", keyPressed = onKeyPressed)
   snakeTurtle.setPos(0,0)
   snakeTurtle.penUp()
def createApple():
   global appleTurtle
   appleTurtle = Turtle(tf, "apple.png")
   appleTurtle.setRandomPos(0.9*frameSize, 0.9*frameSize)
   appleTurtle.setColor("red")
def createFrame():
   global frameTurtle
   frameTurtle = Turtle(tf)
   frameTurtle.setPos(250,-250)
   frameTurtle.hideTurtle()
   repeat 4:
      frameTurtle.forward(frameSize)
      frameTurtle.left(90)

def createStone():
   global numberOfStones
   global stoneTurtles
   stone = Turtle(tf, "stone.png") #Erstellt neuen Stein
   stone.setRandomPos(0.9*frameSize, 0.9*frameSize) #Platziert neuen Stein zufällig
   stoneTurtles.append(stone) #neuer stein wird zum Stein-Array hinzugefügt
   numberOfStones += 1 #erhöht die Anzahl Steine

def frissApple(): #wenn ein Apfel gefressen werden soll (eatApple() testet, ob dies passiert)
   global appleTurtle
   global points
   appleTurtle.setRandomPos(0.9*frameSize, 0.9*frameSize) #Es muss kein neuer Apfel erstellt werden, man kann einfach eine neue zufällige position setzen
   points += 1 #Punktzahl wird erhöht
   playTone("a''",50,instrument="xylophone") #Hoher Ton abgespielt
   createStone()
   
   
def eatApple(): #Testet, ob sich die Turtle nahe genug (<dangerzone) beim Apfel befindet und wenn ja, ruft frissApple(), um den Apfel zu fressen
   global appleTurtle
   global snakeTurtle
   dist = snakeTurtle.distance(appleTurtle)
   if dist < dangerzone :
      frissApple()

#
# MAIN METHODS
#

# The function to play the game.
# Reset some stuff first, like the snake turtle, points, etc.
def play():

   global points # we want to change the value

   print "Play function started" # Remove this if you want

   createSnake()
   createApple()
    # Reset the snake and apple turtles by defining new ones and placing them in the frame

    # Reset the points and display them
    # Todo: Put code here and remove this line <---------------------

   i = 0
   isAlive = True
   while (isAlive): # Run the game while the snake is alive
      #while True:
         snakeTurtle.forward(10)
         # Turn, move the snake here
        # Todo: Put code here and remove this line <---------------------
        # Check if the snake is still alive
         isAlive = snakeTurtleIsAlive()
         i = i + 1
   
   playTone([("F#", 70),("C", 300)],instrument="trumpet")
   print "game over"
   print "your points are: ", points
   print "press enter to play again"
   playagain()
   
    # The game is over now
    # Todo: Put code here and remove this line <---------------------

# The main function.
# Set up stuff here that stays alive for the whole application.
# Create the frame (turtle), ask for the user name etc.

def playagain(): # diese funktion wird 
   global numberOfStones
   global stoneTurtles
   global points
   while True:
      if lastKey == KEY_CODE_ENTER:
         appleTurtle.hideTurtle() #wir müssen den bestehenden Apfel entfernen, weil in play() ein neuer entsteht.
         snakeTurtle.hideTurtle() #Wir wolen keine Leichen auf dem Spielfeld ;)
         for i in range(numberOfStones):
            stoneTurtles[i].hideTurtle() #Alle Stone-Turtles werden verborgen
         stoneTurtles = [] #Stone-Turtle array wird zurückgesetzt, um keine Unsichtbaren Hindernisse zu haben
         numberOfStones = 0    #Anzahl Steine Auf 0
         points = 0
         play()
      
      
   
def main():

    print "Main function started" # Remove this if you want

    # Wait until a name is input
    waitForInputName();   
    createFrame() # draw the frame

    # Start the actual game
    play()
   
   
         


#############
# MAIN CODE #
#############


# Only call the main function here.
# Put all general functionality into the main function.
main()


# No code here! Everything goes in main, play or other functions!
