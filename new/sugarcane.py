from macro import Macro
import time

class Sugarane(Macro):
    def __init__(self, name):
        super().__init__(name)
        self.forwardTime = 20
        self.backwardTime = 20

    def macro(self):
        while self.running:
            self.press("w", self.forwardTime)
            

