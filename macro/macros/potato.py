import time
from threading import Thread
import keyboard, pyautogui, mouse
import numpy as np
from PIL import Image


# include all the rgb values that trigger the macrocheck
macroFlagRgb = [(106,86,51), (69, 69, 69)]


fixcameraRGB = (143, 81, 196)
rightRGB = (72, 27, 76)
leftRGB = (52, 18, 17)

doMacroCheck = True
moveMouseDown = True
devInfo = False


# dont touch these
dir = 'd'
run = True
running = False
killThread = False 
macroCheckRunning = False
resetViewTimestamp = 0
leftTimestamp = 0
rightTimestamp = 0
macroTripped = False

def startmacro():
    global t1, macrocheck
    t1 = Thread(target=macrostart).start()
    macrocheck = Thread(target=antiMacroCheck)
    
def resumeMacro():
    global t1, macrocheck
    t1 = Thread(target=resume).start()
    macrocheck = Thread(target=antiMacroCheck)

def macrostart():
    global dir, run, killThread, macrocheck
    print('starting macro')
    if doMacroCheck:
      macrocheck.start()
    else:
      macroCheckRunning = True
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


def resume(moveMouse=True):
    global dir, run, killThread
    print('resuming macro')
    if moveMouse:
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
        releaseAllKeys()


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
  

def antiMacroCheck():
  global macroFlagRgb, macroTripped, macroCheckRunning
  macroCheckRunning = True
  print('anit macro check now running')
  try:
    for i in macroFlagRgb:
      im = pyautogui.screenshot()
      Y, X = np.where(np.all(im == i, axis=2))
      if len(X) >= 1:
        macroTripped = True
        releaseAllKeys()
        stopmacro()
  except:
    print('error occured in anti macro check, stopping macro')
    macroTripped = True
    releaseAllKeys()
    stopmacro()


def releaseAllKeys():
  keys = 'adws'
  mouse.release('left')
  for i in keys:
    keyboard.release(i)
  keyboard.press('escape')
  time.sleep(0.1)
  keyboard.release('escape')

def test():
    print('potat')

def init():
    global macrocheck
    print('macro init complete')


def config():
  return {'startRGB':fixcameraRGB,
         'rightRGB':rightRGB,
         'leftRGB':leftRGB,
         'doMacroCheck':doMacroCheck,
         'macroCheckFlags':macroFlagRgb}
