from PyUI.Window import Window
##import the custom screens you made---
from startscreen import StartScreen, SecondScreen, ThirdScreen
##-------------------------------------


window = Window("Example App", (100,0,100)) ##Create the window to work with

##Create Screen Objects for use------
startScreen = StartScreen(window)
secondScreen = SecondScreen(window)
thirdScreen = ThirdScreen(window)
##-----------------------------------

screen = startScreen ##set screen to be the starting screen
screen2 = secondScreen
screen3 = thirdScreen
loopCounter = 1
while True: ##Game loop
    ##Enter code here to handle changes between screens---
    # if loopCounter == 1:
    #     window.checkForInput(screen) #checks for inputs on the screen
    #     screen.update() #updates the screen
    #     window.update(screen) #updates the window to reflect the new screen

    # if loopCounter ==2:
    #     window.checkForInput(screen2) #checks for inputs on the screen
    #     screen.update() #updates the screen
    #     window.update(screen2) #updates the window to reflect the new screen

    # if loopCounter == 3:
    #     window.checkForInput(screen3) #checks for inputs on the screen
    #     screen.update() #updates the screen
    #     window.update(screen3) #updates the window to reflect the new screen
    ##----------------------------------------------------
    loopCounter+=1
    window.checkForInput(screen) #checks for inputs on the screen
    screen.update() #updates the screen
    window.update(screen) #updates the window to reflect the new screen
