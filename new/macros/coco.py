import mouse
from macros.macro import Macro
import time

class Coco(Macro):
    def __init__(self):
        super().__init__("coco")
        self.walkTime = 14.2
        self.timeStamp = 0
        self.dir = 's'
        self.row = 0
        self.line = 0
        self.the = False


    def on_start(self):
        self.press('mouse1', -1)

    def on_resume(self):
        self.press('mouse1', -1)
        self.press(self.dir, -1)

    def walkToNextRow(self):
        if (self.row == 30):
            self.press('d', 20)
            self.row = 0
            return
        self.press('a', 0.29)
        self.press('w', 0.3)
        self.press('d', 0.2)

    def swapLines(self):
        self.press('a', 0.5)

    def update(self):
        # swaps the direction that the macro is walking
        if self.timeStamp < time.time():
            self.release('w')
            self.release('s')
            if self.the:
                if self.line == 0:
                    self.swapLines()
                    self.line = self.line + 1
                else:
                    self.walkToNextRow()
                    self.row = self.row + 1
                    self.line = 0
            else:
                self.the = True

            if self.dir == 'w':
                self.dir = 's'
            else:
                self.dir = 'w'

            self.press(self.dir, -1)
            self.timeStamp = time.time() + self.walkTime

    def __str__(self):
        return f"{super().__str__()} : row: {self.row} line: {self.line}"

