from macro import Macro
import time

class Test(Macro):
    def __init__(self, name):
        super().__init__(name)
        self.init()

    def macro(self):
        timestamp = 0
        while self.running:
            if timestamp <= time.time():
                timestamp = time.time() + 4
                print(f"test {time.time()}")

    