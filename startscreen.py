from PyUI.Screen import Screen
from PyUI.PageElements import *
import random
import time

class StartScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (124, 171, 247)) ##use the parents constructor
        self.state = {
            "displayText": " ",
            "moveTo": " ", 
            "imageMaybe" : " "
            
            }

    def elementsToDisplay(self): #defines what elements will be on the page
        self.elements = [
            Label((350, 250), 100, 100, self.state["displayText"], 50, (255,255,255)), RockButton(),PaperButton(),ScissorsButton(), #ShootButton(),
            Image((175, 525), 50, 50, './imgs/rock no backround.png'),  Image((362.5, 525), 75, 37.5, './imgs/paper no backround.png'),  
            Image((575, 525), 50, 50, './imgs/scisors no backround.png'),  #Image((662.5, 525), 75, 37.5, './imgs/boom no backround.png'),
            #WinButton(), LoseButton()
        ]

        if self.state["imageMaybe"] != " ":
            self.elements.append(Image((350, 125), 100, 100, self.state["imageMaybe"]))

def computerPlay():
    valuesRPS = {'rock' : 1, 'paper' : 2, 'scissors' : 3}
    compChoice = random.randint(valuesRPS['rock'], valuesRPS['scissors'])
    return compChoice


#(topLeftLoc: Any, width: Any, height: Any, text: Any, textColorRGB: Any = (0, 0, 0), backColorRGB: Any = (255, 255, 255)) -> Button
#(topLeftLoc: Any, width: Any, height: Any, text: Any, fontSize: int = 14, textColorRGB: Any = (0, 0, 0)) -> Label

class RockButton(Button):
    def __init__(self):
        super().__init__((150, 400), 100, 100, "Rock", (124, 171, 247))
        
    def onClick(self, screen): #override the onClick method to do our bidding, MUST TAKE SCREEN AS ARGUMENT
        screen.state["displayText"] = "Rock" #modifies the state of the screen
        screen.state['imageMaybe'] = './imgs/rock no backround.png'
        compChoice = computerPlay()
        if compChoice == 1:
            time.sleep(1)
            screen.state["moveTo"] = "Tie"
        if compChoice == 2:
            time.sleep(1)
            screen.state["moveTo"] = "LOSE"            
        if compChoice == 3:
            time.sleep(1)
            screen.state["moveTo"] = "WIN"

class PaperButton(Button):
    def __init__(self):
        super().__init__((350, 400), 100, 100, "Paper", (124, 171, 247))
        
    def onClick(self, screen): #override the onClick method to do our bidding, MUST TAKE SCREEN AS ARGUMENT
        screen.state["displayText"] = "Paper" #modifies the state of the screen
        screen.state['imageMaybe'] = './imgs/paper no backround.png'
        compChoice = computerPlay()

        if compChoice == 2:
            time.sleep(1)
            screen.state["moveTo"] = "Tie"
        if compChoice == 3:
            time.sleep(1)
            screen.state["moveTo"] = "LOSE"            
        if compChoice == 1:
            time.sleep(1)
            screen.state["moveTo"] = "WIN"

class ScissorsButton(Button):
    def __init__(self):
        super().__init__((550, 400), 100, 100, "Scissors", (124, 171, 247))
        
    def onClick(self, screen): #override the onClick method to do our bidding, MUST TAKE SCREEN AS ARGUMENT
        screen.state["displayText"] = "Scissors" #modifies the state of the screen
        screen.state['imageMaybe'] = './imgs/scisors no backround.png'
        compChoice = computerPlay()

        if compChoice == 3:
            time.sleep(1)
            screen.state["moveTo"] = "Tie"
        if compChoice == 1:
            time.sleep(1)
            screen.state["moveTo"] = "LOSE"            
        if compChoice == 2:
            time.sleep(1)
            screen.state["moveTo"] = "WIN"

class ShootButton(Button):
    def __init__(self):
        super().__init__((650, 400), 100, 100, "Shoot",(124, 171, 247))
        
    def onClick(self, screen): #override the onClick method to do our bidding, MUST TAKE SCREEN AS ARGUMENT
        screen.state["displayText"] = "Boom!!!" #modifies the state of the screen
        screen.state['imageMaybe'] = './imgs/boom no backround.png'

# class WinButton(Button):
#     def __init__(self):
#         super().__init__((100, 100), 100, 100, "Win!")
#     def onClick(self, screen):
#        screen.state["moveTo"] = "WIN"

# class LoseButton(Button):
#     def __init__(self):
#         super().__init__((600, 100), 100, 100, "Lose:(")
#     def onClick(self, screen):
#        screen.state["moveTo"] = "LOSE"






# playerChoice = 
# if compChoice == 1:
# RockButton(Button)
# if compChoice == 2:
# PaperButton(Button)
# if compChoice == 3:
# ScissorsButton(Button)

