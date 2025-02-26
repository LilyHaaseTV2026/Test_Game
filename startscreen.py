from PyUI.Screen import Screen
from PyUI.PageElements import *
class StartScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (83, 137, 181)) ##use the parents constructor
        self.state = {
            "displayText": " ",
            "moveTo": " ", 
            "imageMaybe" : " "
            }

    def elementsToDisplay(self): #defines what elements will be on the page
        self.elements = [
            Label((350, 250), 100, 100, self.state["displayText"], 50, (255,255,255)), RockButton(),PaperButton(),ScissorsButton(), ShootButton(),
            Image((75, 525), 50, 50, './imgs/rock no backround.png'),  Image((262.5, 525), 75, 37.5, './imgs/paper no backround.png'),  
            Image((475, 525), 50, 50, './imgs/scisors no backround.png'),  Image((662.5, 525), 75, 37.5, './imgs/boom no backround.png'),
            WinButton()
        ]

        if self.state["imageMaybe"] != " ":
            self.elements.append(Image((350, 125), 100, 100, self.state["imageMaybe"]))

#(topLeftLoc: Any, width: Any, height: Any, text: Any, textColorRGB: Any = (0, 0, 0), backColorRGB: Any = (255, 255, 255)) -> Button
#(topLeftLoc: Any, width: Any, height: Any, text: Any, fontSize: int = 14, textColorRGB: Any = (0, 0, 0)) -> Label

class RockButton(Button):
    def __init__(self):
        super().__init__((50, 400), 100, 100, "Rock", (83, 137, 181))
        
    def onClick(self, screen): #override the onClick method to do our bidding, MUST TAKE SCREEN AS ARGUMENT
        screen.state["displayText"] = "Rock" #modifies the state of the screen
        screen.state['imageMaybe'] = './imgs/rock no backround.png'

class PaperButton(Button):
    def __init__(self):
        super().__init__((250, 400), 100, 100, "Paper", (83, 137, 181))
        
    def onClick(self, screen): #override the onClick method to do our bidding, MUST TAKE SCREEN AS ARGUMENT
        screen.state["displayText"] = "Paper" #modifies the state of the screen
        screen.state['imageMaybe'] = './imgs/paper no backround.png'

class ScissorsButton(Button):
    def __init__(self):
        super().__init__((450, 400), 100, 100, "Scissors", (83, 137, 181))
        
    def onClick(self, screen): #override the onClick method to do our bidding, MUST TAKE SCREEN AS ARGUMENT
        screen.state["displayText"] = "Scissors" #modifies the state of the screen
        screen.state['imageMaybe'] = './imgs/scisors no backround.png'

class ShootButton(Button):
    def __init__(self):
        super().__init__((650, 400), 100, 100, "Shoot",(83, 137, 181))
        
    def onClick(self, screen): #override the onClick method to do our bidding, MUST TAKE SCREEN AS ARGUMENT
        screen.state["displayText"] = "Boom!!!" #modifies the state of the screen
        screen.state['imageMaybe'] = './imgs/boom no backround.png'

class WinButton(Button):
    def __init__(self):
        super().__init__((100, 100), 100, 100, "Win!")
    def onClick(self, screen):
       screen.state["moveTo"] = "WIN"
