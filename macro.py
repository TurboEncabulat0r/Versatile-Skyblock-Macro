import time, packages as pg


def packages():
    global mouse, pyautogui, keyboard, np, Image, pynput, kb
    import keyboard, pyautogui, mouse
    from pynput import keyboard as kb
    import numpy as np
    from PIL import Image


tolerance = 10

oldrightRGB = (106, 42, 101)
oldleftRGB = (62, 14, 14)

rightRGB = (72, 27, 76)
leftRGB = (52, 18, 17)

dir = 'a'
run = True
running = False


def startmacro():
    global dir, run, running

    if not running:

        running = True
        print('starting macro')
        mouse.move(0, 5, absolute=False, duration=0.2)
        mouse.press(button='left')
        keyboard.press(dir)
        startTime = time.time()
        count = 0

        while run:
            count += 1

            if checkRGB():
                print("dir changed")
                keyboard.press(dir)

                if dir == 'a':
                    keyboard.release('d')
                else:
                    keyboard.release('a')

                if count > 250:
                    keyboard.press('w')
                    time.sleep(0.1)
                    keyboard.release('w')
                    count = 0
    else:
        running = False
        print('stopping macro')


def checkRGB():
    global dir
    screenshot = pyautogui.screenshot()
    im = np.array(screenshot)

    Y, X = np.where(np.all(im == leftRGB, axis=2))
    if len(X) >= 1:
        dir = 'a'
        return True

    Y, X = np.where(np.all(im == rightRGB, axis=2))
    if len(X) >= 1:
        dir = 'd'
        return True

def swapDir():
    global dir
    print('switching dir')
    if dir == 'a':
        dir = 'd'
    else:
        dir = 'a'


def stopmacro():
    global run
    run = False
    print('macro stopped')


def on_press(key):
    print(type(key))
    print(key == kb.Key(char='l'))
    return ''
    if key == kb.Key(char='l'):
        startmacro()

    if key == kb.Key(char='k'):
        swapDir()

def on_release(key):
    pass

def init():
    try:
        packages()
    except:
        pg.install()

    #keyboard.add_hotkey('l', lambda: startmacro())
    print('macro init complete')

    
