from PyUI.Window import Window
##import the custom screens you made---
from startscreen import StartScreen
##-------------------------------------


window = Window("Example App", (100,0,100)) ##Create the window to work with

##Create Screen Objects for use------
startScreen = StartScreen(window)

##-----------------------------------

screen = startScreen ##set screen to be the starting screen

loopCounter = 1
while True: ##Game loop
    ##Enter code here to handle changes between screens---
    loopCounter+=1
    window.checkForInput(screen) #checks for inputs on the screen
    window.update(screen) #updates the window to reflect the new screen
