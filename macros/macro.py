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
            self.release(i)

    """
    press a key for a certain amount of time, input negative number for infinite time
    when macro is disposed keys will be released
    """
    def press(self, key, delay):
        if key == 'mouse1':
            mouse.press("left")
        elif key == 'mouse2':
            mouse.press("right")
        else:
            kb.press(key)

        self.keys.append(key)
        if delay <= 0:
            return

        time.sleep(delay)
        self.release(key)

    def release(self, key):
        if key in self.keys:
            if key == 'mouse1':
                mouse.release("left")
            elif key == 'mouse2':
                mouse.release("right")
            else:
                kb.release(key)

                self.keys.remove(key)

    def init(self):
        self.thr = Thread(target=self.macro)
    
    def dispose(self):
        self.running = False
        self.thr = None
        self.releaseAllKeys()
        print(f"macro {self.name} stopped, and disposed")

    def resume(self):
        self.paused = False
        self.on_resume()

    def start(self):
        if self.paused == False:
            try:
                self.thr.start()
            except:
                self.init()
                self.thr.start()

            self.running = True
        else:
            self.resume()

    
    def stop(self):
        print(f"stopping macro {self.name}")
        self.running = False
        self.dispose()

    def breakSequene(self):
        self.togglePause()
        self.releaseAllKeys()

        self.say("/bz")
        time.sleep(1)
        mouse.move(893, 550, absolute=True, duration=0.1)
        time.sleep(0.5)
        mouse.click()
        mouse.move(892, 452, absolute=True, duration=0.1)
        time.sleep(0.5)
        for i in range(3):
            mouse.click()
            time.sleep(0.3)
        self.press("esc", 0.1)

        time.sleep(10)
        self.say("/hub")
        time.sleep(1)
        breakTs = time.time() + (60 * 5)
        while time.time() < breakTs:
            # has a 1/10 chance of preforming an action
            if random.randint(0, 10) == 0:
                if random.randint(0, 1) == 0:
                    mouse.move(random.randint(-50, 50), random.randint(-50, 50), absolute=False, duration=5)
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

    def resetPositon(self):
        self.say("/hub")
        time.sleep(1)
        self.say("/is")
        self.press("shift", 1)

    def moveMouse(self, value, t=10, raw=False):
        #will move the mouse in a way that is friendly to the game because that shit is annoying
        # it will move it in a direction for an ammount of time
        x = value[0] * -1
        y = value[1] * -1
        if raw:
            mouse.move(x, y, absolute=False, duration=0.1)
        else:
            for i in range(t):
                mouse.move(mouse.get_position()[0] + x, mouse.get_position()[1] + y, absolute=True, duration=0)
                time.sleep(0.1)




    # says someting in chat
    def say(self, s):
        self.press("t", 0.1)
        kb.write(s)
        self.press("enter", 0.1)

    def togglePause(self):
        self.paused = not self.paused
        self.releaseAllKeys()
        print(f"macro {self.name} paused: {self.paused}")

    def write(self, text, delay=0.1):
        pyautogui.write(text, interval=delay)

    #overridable
    def on_pause(self):
        pass

    #overridable
    def on_resume(self):
        pass

    #overridable, will be called when the macro is started
    def on_start(self):
        print(f"macro {self.name} started")

    def macro(self):
        statsTS = 0
        deltaTimeTS = 0
        breakTS = 0
        self.goToFarm()
        self.on_start()
        while self.running:
            if not self.paused:

                if self.takeBreaks and time.time() > breakTS:
                    self.breakSequene()
                    breakTS = time.time() + (60 * self.BreakFrequency)

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