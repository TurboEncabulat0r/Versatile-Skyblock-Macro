import time, packages as pg
import asyncio
from threading import Thread
def packages():
    global mouse, pyautogui, keyboard, np, Image, pynput, kb
    import keyboard, pyautogui, mouse
    from pynput import keyboard as kb
    import numpy as np
    from PIL import Image

#all of these values can be changed
oldrightRGB = (106, 42, 101)
oldleftRGB = (62, 14, 14)

fixcameraRGB = (143, 81, 196)
rightRGB = (72, 27, 76)
leftRGB = (52, 18, 17)

moveMouseDown = True
devInfo = False


# dont touch these
dir = 'd'
run = True
running = False
killThread = False 
resetViewTimestamp = 0
leftTimestamp = 0
rightTimestamp = 0

def startmacro():
    global t1
    t1 = Thread(target=macrostart).start()
    


def macrostart():
    global dir, run, killThread
    print('starting macro')
    #if moveMouseDown:
    #   mouse.move(0, 5, absolute=False, duration=0.2)
        
    mouse.press(button='left')
    startTime = time.time()
    count = 0
    try:
        while run:
            count += 1
            timestamp = time.time()
            if checkRGB():
                print("dir changed")

                if dir == 'a':
                    keyboard.release('d')
                else:
                    keyboard.release('a')

                if count > 250:
                    keyboard.press('w')
                    time.sleep(0.1)
                    keyboard.release('w')
                    count = 0
                    
            if killThread:
                run = False
                keyboard.release('a')
                keyboard.release('d')
                mouse.release('left')
                break
                    
            #print(round(time.time() - timestamp, 3))
    finally:
        print('macro stopped')
        killThread = False


def checkRGB():
    global dir, resetViewTimestamp, rightTimestamp, leftTimestamp
    screenshot = pyautogui.screenshot()
    im = np.array(screenshot)

    if resetViewTimestamp < time.time():
        Y, X = np.where(np.all(im == fixcameraRGB, axis=2))
        if len(X) >= 1:
            oldDir = dir
            swapDir()
            keyboard.release(oldDir)
            keyboard.press(dir)
            mouse.move(0, 5, absolute=False, duration=0.2)
            resetViewTimestamp = time.time() + 20

    Y, X = np.where(np.all(im == leftRGB, axis=2))
    if len(X) >= 1:
        dir = 'a'
        keyboard.release('d')
        keyboard.press(dir)

        return True

    Y, X = np.where(np.all(im == rightRGB, axis=2))
    if len(X) >= 1:
        dir = 'd'
        keyboard.release('a')
        keyboard.press(dir)

        return True

    
def rgbCheck(rgblist):
    for i in rgblist:
        print('wip')

    
def swapDir():
    global dir
    print('switching dir')
    if dir == 'a':
        dir = 'd'
    else:
        dir = 'a'


def stopmacro():
    global killThread, t1
    killThread = True
    #t1.join()

    """
    global run
    run = False
    """
    
def raiseExcept():
    m = 1/0

def on_press(key):
    print(type(key))
    print(key == kb.Key(char='l'))
    return ''
    if key == kb.Key(char='l'):
        startmacro()

    if key == kb.Key(char='k'):
        swapDir()

        
class RGB():
    def __init__(self, name, rgb):
        self.name = name
        self.rgb = rgb


def on_release(key):
    pass

def init():
    try:
        packages()
    except:
        pg.install()

    # keyboard.add_hotkey('l', lambda: startmacro())
    print('macro init complete')
