from PyUI.Screen import Screen
from PyUI.PageElements import *
class StartScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (255,220,220)) ##use the parents constructor
        self.state = {
            "displayText": "Hello"
        }

    def elementsToDisplay(self): #defines what elements will be on the page
        self.elements = [
            Label((150,65),500,500,self.state["displayText"], 50, (255,255,255)), Button((350, 150), 50, 50, '<3', (255,220,200), (255, 255, 255))
            #(topLeftLoc: Any, width: Any, height: Any, text: Any, textColorRGB: Any = (0, 0, 0), backColorRGB: Any = (255, 255, 255)) -> Button
            #(topLeftLoc: Any, width: Any, height: Any, text: Any, fontSize: int = 14, textColorRGB: Any = (0, 0, 0)) -> Label
            #"<3 HAPPY VALENTINES DAY <3"

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

class HelloButton(Button):
    def __init__(self):
        super().__init__((200, 200), 100, 100, "Hello")
        
    def onClick(self, screen): #override the onClick method to do our bidding, MUST TAKE SCREEN AS ARGUMENT
        screen.state["displayText"] = "World" #modifies the state of the screen