from macro import Macro
import time

class Test(Macro):
    def __init__(self, name):
        super().__init__(name)
        self.init()

    def update(self):
        print(f"test {time.time()}")

    