from PyUI.Screen import Screen
from PyUI.PageElements import *
class StartScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (255,220,220)) ##use the parents constructor
    def elementsToDisplay(self): #defines what elements will be on the page
        self.elements = [
            Label((150,65),500,500,"<3 HAPPY VALENTINES DAY <3", 50, (255,255,255))
    ]

class SecondScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (225,0,0))
    def elementsToDisplay(self):
        self.elements = [
            Label((150,65),500,500,"<3 HAPPY VALENTINES DAY <3", 50, (255,220,220))
        ]

class ThirdScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (225,255,255))
    def elementsToDisplay(self):
        self.elements = [
            Label((150,65),500,500,"<3 HAPPY VALENTINES DAY <3", 50, (255,0,0))
        ]
