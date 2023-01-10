import time
from threading import Thread
import keyboard as kb, pyautogui, mouse
import numpy as np
from PIL import Image

class MacroCheck:
    def __init__(self, name):
        self.name = name
        self.running = False
        self.thr = 0
        self.keys = []
        self.init()

    def releaseAllKeys(self):
        for i in self.keys:
            kb.release(i)

    def init(self):
        self.thr = Thread(target=self.check)
    
    def dispose(self):
        self.thr = None
        self.releaseAllKeys()

    def start(self):
        self.thr.start()

    def check():
        while True:
            #checks through all the rgb values of the screen
            return

    def __repr__(self):
        return f"Macro('{self.name}', '{self.key}', {self.delay}, {self.args})"



