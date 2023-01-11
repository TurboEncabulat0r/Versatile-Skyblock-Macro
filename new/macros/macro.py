import time
from threading import Thread
import keyboard as kb, pyautogui
import numpy as np
from PIL import Image
from macros.macrocheck import MacroCheck
import mouse, random

class Macro:
    def __init__(self, name):
        self.name = name
        self.thr = 0
        self.running = False
        self.keys = []
        self.stats = {}
        self.paused = False
        self.deltaTime = 0
        self.doMacroCheck = False
        self.takeBreaks = True
        self.BreakFrequency = 45
        if self.doMacroCheck:
            self.macroCheck = MacroCheck()
        else:
            self.macroCheck = None
        self.init()

    def releaseAllKeys(self):
        for i in self.keys:
            kb.release(i)

    """
    press a key for a certain amount of time, input negative number for infinite time
    when macro is disposed keys will be released
    """
    def press(self, key, delay):
        self.keys.append(key)
        kb.press(key)
        if delay <= 0:
            return

        time.sleep(delay)
        kb.release(key)
        self.keys.remove(key)

    def release(self, key):
        kb.release(key)
        try:
            self.keys.remove(key)
        except:
            pass

    def init(self):
        self.thr = Thread(target=self.macro)
    
    def dispose(self):
        self.running = False
        self.thr = None
        self.releaseAllKeys()
        print(f"macro {self.name} stopped, and disposed")

    def resume(self):
        self.paused = False

    def start(self):
        if self.paused == False:
            self.running = True
            self.thr.start()
        else:
            self.resume()
    
    def stop(self):
        print(f"stopping macro {self.name}")
        self.running = False
        self.dispose()

    def doBreakSequene(self):
        self.togglePause()
        self.releaseAllKeys()

        self.write("/bz")
        time.sleep(1)
        mouse.move(0, 0, absolute=True, duration=0.1)
        time.sleep(0.5)
        mouse.click()
        mouse.move(0, 0, absolute=True, duration=0.1)
        time.sleep(0.5)
        for i in range(3):
            mouse.click()
            time.sleep(0.3)
        self.press("esc", 0.1)
        time.sleep(10)
        self.write("/hub")
        time.sleep(1)
        breakTs = time.time() + (60 * 5)
        while time.time() < breakTs:
            # has a 1/10 chance of preforming an action
            if random.randint(0, 10) == 0:
                if random.randint(0, 1) == 0:
                    mouse.move(random.randint(-50, 50), random.randint(-50, 50), absolute=True, duration=5)
                    time.sleep(0.5)
                    for i in range(random.randint(1, 5)):
                        mouse.click()
                        time.sleep(0.1)
                else:
                    # moves in a random direction for a random amount of time
                    self.press(random.choice(["w", "a", "s", "d"]), random.randint(1, 5))
                    time.sleep(0.5)
                    mouse.click()

        self.releaseAllKeys()
        self.goToFarm()
        self.togglePause()


    #must be overriden, it will move the player to the farm
    def goToFarm(self):
        pass
        
    def togglePause(self):
        self.paused = not self.paused

    def write(self, text, delay=0.1):
        pyautogui.write(text, interval=delay)

    #overridable
    def on_pause(self):
        pass

    #overridable
    def on_resume(self):
        pass

    def macro(self):
        statsTS = 0
        deltaTimeTS = 0
        while self.running:
            if not self.paused:
                deltaTimeTS = time.time()

                if statsTS <= time.time():
                    statsTS = time.time() + 4
                    self.stats = self.getStats()


                self.update()
                self.deltaTime = time.time() - deltaTimeTS

    #this method should be overriden by the child class
    # will be called every iteration of the macro and is called after getStats
    def update(self):
        print("this is an empty macro object")

    def getStats(self):
        # this method will use a library to grab the stats from neu and pars them for data
        # it will then return them as an object or json dictionary
        # the stats can be then post processed for data like potatos per minuite or money/min
        
        # this should be rarly called as this method will be expensive
        pass
    
    def scanImage(self, image, rgb):
        im = np.array(image)
        Y, X = np.where(np.all(im == rgb, axis=2))
        return len(X) >= 1
    
    def screenshot(self, pos1, pos2):
        return pyautogui.screenshot(region=(pos1[0], pos1[1], pos2[0], pos2[1]))

    def __repr__(self):
        return f"Macro('{self.name}')"



class MacroAlreadyRunningException(Exception):
    pass