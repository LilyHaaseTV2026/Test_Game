from PyUI.Screen import Screen
from PyUI.PageElements import *
class SecondScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (0,0,0)) ##use the parents constructor
        self.state = {
            "displayText" : " You Won!",
            "moveTo" : " " 
            }
    def elementsToDisplay(self): #defines what elements will be on the page
        self.elements = [
            Label((350, 250), 100, 100, self.state["displayText"], 50, (255,255,255)), AgainButton()
        ]

class AgainButton(Button):
    def __init__(self):
        super().__init__((100, 100), 100, 100, '''Game''', (0,0,0))
        
    def onClick(self, screen): #override the onClick method to do our bidding, MUST TAKE SCREEN AS ARGUMENT
        screen.state["moveTo"] = "WIN" #modifies the state of the screen

