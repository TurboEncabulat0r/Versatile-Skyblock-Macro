from macros.macro import Macro
import time

class Sugarcane(Macro):
    def __init__(self):
        super().__init__("Sugarcane")
        self.walkTime = 5
        self.walkingForward = False
        self.timestamp = 0
        self.swaps = 0

    def update(self):
        if self.timestamp <= time.time():
            self.swaps += 1
            self.nextRow()
            self.releaseAllKeys()
            self.timestamp = time.time() + self.walkTime
            self.walkingForward = not self.walkingForward
            if self.walkingForward:
                self.press("w", -1)
                self.press('a', -1)
            else:
                self.press("s", -1)
                self.press('d', -1)

    def nextRow(self):
        self.releaseAllKeys()
        if self.walkingForward:
            self.press("d", -1)
            self.press("w", 3)
        else:
            self.press("d", -1)
            self.press("s", 3)

    def getData(self):
        dir = ''
        if self.walkingForward:
            dir = "forward"
        else:
            dir = "backward"

        return {"direction " : dir,
        "walk timestamp " : self.timestamp,
        "swaps " : self.swaps,
        "paused " : self.paused,
        "delta time " : self.deltaTime}

    def on_resume(self):
        t = time.time() - self.pauseTimestamp
        self.timestamp += t

    def on_pause(self):
        self.pauseTimestamp = time.time()