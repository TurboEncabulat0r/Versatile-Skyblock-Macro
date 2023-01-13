from macros.macro import Macro
import time

class Potato(Macro):
    def __init__(self):
        super().__init__("potato")
        self.walkTime = 44.4
        self.timeStamp = 0
        self.dir = 'r'

    def on_start(self):
        self.press('mouse1', -1)

    def on_resume(self):
        self.press('mouse1', -1)
        if self.dir == 'r':
            self.press('d', -1)
        else:
            self.press('a', -1)

    def update(self):
        # swaps the direction that the macro is walking
        if self.timeStamp < time.time():
            self.release('a')
            self.release('d')

            if self.dir == 'l':
                self.dir = 'r'
                self.press('d', -1)
            else:
                self.dir = 'l'
                self.press('a', -1)
            self.timeStamp = time.time() + self.walkTime


    def goToFarm(self):
        self.resetPositon()
        self.press("d", 3)
        self.press("a", 0.7)
        self.moveMouse((0, -13), raw=True)


        