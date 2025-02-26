from PyUI.Window import Window
##import the custom screens you made---
from startscreen import StartScreen
from winscreen import SecondScreen
##-------------------------------------


window = Window("Example App", (100,0,100)) ##Create the window to work with

##-----------------------------------
##Create Screen Objects for use------
startScreen = StartScreen(window)
secondScreen = SecondScreen(window)

##-----------------------------------

screen = startScreen ##set screen to be the starting screen
#screen = secondScreen

while True: ##Game loop
    ##Enter code here to handle changes between screens---
    if screen.state.get("moveTo") == "WIN":
            screen = secondScreen
            screen.state.get("moveTo") == " "
    if screen.state.get("moveTo") == "WIN":
            screen = startScreen
            screen.state.get("moveTo") == " "
    window.checkForInput(screen) #checks for inputs on the screen
    window.update(screen) #updates the window to reflect the new screen
