from macros.macro import Macro
import time
# row 32
class Sugarcane(Macro):
    def __init__(self):
        super().__init__("sugarcane")
        self.walkTime = 7
        self.dir = 'r'
        self.timeStamp = 0
        self.swaps = 0
        self.row = 0
        self.pauseTimestamp = 0

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
        if self.timeStamp < self.time():
            if self.row == 31:
                self.press('w', 11)
                self.press('d', 11)
                self.row = 0


            self.row += 1
            print(f"row: {self.row}")


            self.release('s')
            self.release('a')

            if self.dir == 'l':
                self.dir = 'r'
                self.press('a', -1)
            else:
                self.dir = 'l'
                self.press('s', -1)
            self.timeStamp = self.time() + self.walkTime

    def on_resume(self):
        t = time.time() - self.pauseTimestamp
        self.timeStamp += t

    def on_pause(self):
        self.pauseTimestamp = time.time()