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
    
def resumeMacro():
    global t1
    t1 = Thread(target=resume).start()

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
            if checkRGB():
                print("dir changed")

                if dir == 'a':
                    keyboard.release('d')
                else:
                    keyboard.release('a')

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


def resume():
    global dir, run, killThread
    print('resuming macro')
    # if moveMouseDown:
    mouse.move(0, 5, absolute=False, duration=0.2)
    dir = 'a'
    keyboard.press(dir)
    mouse.press(button='left')
    try:
        while run:
            if checkRGB():
                print("dir changed")

                if dir == 'a':
                    keyboard.release('d')
                else:
                    keyboard.release('a')

            if killThread:
                run = False
                break

            # print(round(time.time() - timestamp, 3))
    finally:
        print('macro stopped')
        killThread = False
        run=True
        keyboard.release('a')
        keyboard.release('d')
        mouse.release('left')


def checkRGB():
    global dir, resetViewTimestamp, rightTimestamp, leftTimestamp
    timestamp = time.time()

    useOldRange = False
    if useOldRange:
        screenshot = pyautogui.screenshot()
    else:
        screenshot = pyautogui.screenshot(region=(576,200, 768, 800))

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
            #print(f'time to parse image: {time.time() - timestamp}')
            return True

    Y, X = np.where(np.all(im == leftRGB, axis=2))
    if len(X) >= 1 and dir == 'd':
        dir = 'a'
        keyboard.release('d')
        keyboard.press(dir)
        #print(f'time to parse image: {time.time() - timestamp}')
        return True

    Y, X = np.where(np.all(im == rightRGB, axis=2))
    if len(X) >= 1 and dir == 'a':
        dir = 'd'
        keyboard.release('a')
        keyboard.press(dir)
        #print(f'time to parse image: {time.time() - timestamp}')
        return True
    #print(f'time to parse image: {time.time() - timestamp}')

    
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
    """
    try:
        t1.join()
    except:
        killThread = False
    """

    """
    global run
    run = False
    """
    
def raiseExcept():
    m = 1/0


class RGB():
    def __init__(self, name, rgb):
        self.name = name
        self.rgb = rgb


def init():
    try:
        packages()
    except:
        pg.install()

    # keyboard.add_hotkey('l', lambda: startmacro())
    print('macro init complete')
