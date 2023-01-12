from macros.macro import Macro
import time

class Netherwart(Macro):
    def __init__(self):
        super().__init__("netherwart")
        self.walkTime = 80
        self.timeStamp = 0
        self.dir = 'l'

    def update(self):
        # swaps the direction that the macro is walking
        if self.timeStamp < time.time():
            self.releaseAllKeys()

            if self.dir == 'l':
                self.dir = 'r'
                self.press('d', -1)
            else:
                self.dir = 'l'
                self.press('a', -1)
            self.timeStamp = time.time() + self.walkTime
            
