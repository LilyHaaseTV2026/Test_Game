from PyUI.Window import Window
import random
##import the custom screens you made---
from startscreen import StartScreen
from winscreen import SecondScreen
from losescreen import LoseScreen
from tiescreen import TieScreen
##-------------------------------------


window = Window("Example App", (100,0,100)) ##Create the window to work with

##-----------------------------------
##Create Screen Objects for use------
startScreen = StartScreen(window)
secondScreen = SecondScreen(window)
loseScreen = LoseScreen(window)
tieScreen = TieScreen(window)

##-----------------------------------

screen = startScreen ##set screen to be the starting screen
#screen = secondScreen

#computer play
# valuesRPS = {'rock' : 1, 'paper' : 2, 'scissors' : 3}
# compChoice = random.randint(valuesRPS['rock'], valuesRPS['scissors'])
# if compChoice == 1:
#     print('rock')
# if compChoice == 2:
#     print('paper')
# if compChoice == 3:
#     print('scissors')
# print(compChoice)




while True: ##Game loop
    ##Enter code here to handle changes between screens---
    if screen.state.get("moveTo") == "WIN":
            screen = secondScreen
            screen.state.get("moveTo") == " "
    if screen.state.get("moveTo") == "WIN":
            screen = startScreen
            screen.state.get("moveTo") == " "
    if screen.state.get("moveTo") == "LOSE":
            screen = loseScreen
            screen.state.get("moveTo") == " "
    if screen.state.get("moveTo") == "LOSE":
            screen = startScreen
            screen.state.get("moveTo") == " "
    if screen.state.get("moveTo") == "Tie":
            screen = tieScreen
            screen.state.get("moveTo") == " "
    if screen.state.get("moveTo") == "Tie":
            screen = startScreen
            screen.state.get("moveTo") == " "
    window.checkForInput(screen) #checks for inputs on the screen
    window.update(screen) #updates the window to reflect the new screen
