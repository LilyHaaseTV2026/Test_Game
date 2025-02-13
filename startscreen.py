from PyUI.Screen import Screen
from PyUI.PageElements import *
class StartScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (75,50,170)) ##use the parents constructor
    def elementsToDisplay(self): #defines what elements will be on the page
        self.elements = [
            Label((50,50),100,100,"blue<3")
    ]
