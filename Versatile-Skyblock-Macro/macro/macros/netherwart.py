import time
from threading import Thread
#import keyboard, pyautogui, mouse
import numpy as np
from PIL import Image
#from .. import events
macroFlagRgb = [(106,86,51)]

# all of these values can be changed


fixcameraRGB = (143, 81, 196)
rightRGB = (84, 59, 16)
leftRGB = (29, 52, 39)

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
attempted = False
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

    dir = 'a'
    keyboard.press(dir)
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
    dir = 'a'
    keyboard.press(dir)
    mouse.press(button='left')
    timestamp = time.time()
    try:
        while run:
            if checkRGB():
                timestamp = time.time()
                print("dir changed")

                if dir == 'a':
                    keyboard.release('d')
                else:
                    keyboard.release('a')

            if time.time() - timestamp >= getSec(1.5) and not attempted:
                attempted = True
                swapDir()
                events.sendEvent('macro has been paused for a large ammout of time, attempting to switch directions')
            elif time.time() - timestamp >= getSec(4):
                #events.sendEvent('macro has been paused for too long(not detecting blocks) stopping macro for safty')
                stopmacro()
                print('stopping macro due to timeout')

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

def getSec(min):
    return min * 60


def stopmacro():
    global killThread, t1
    killThread = True
  

def antiMacroCheck():
  global macroFlagRgb, macroTripped, macroCheckRunning
  macroCheckRunning = True
  print('anit macro check now running')
  try:
    for i in macroFlagRgb:
      screenshot = pyautogui.screenshot(region=(576,200, 768, 800))
      im = np.array(screenshot)
      Y, X = np.where(np.all(im == i, axis=2))
      if len(X) >= 1:
        print(f'macro tripped on rgb {i}')
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
    print('wart')

def init():
    global macrocheck
    print('macro init complete')


def config():
  print('returning cfg')
  return {'rightRGB':rightRGB,
         'leftRGB':leftRGB,
         'doMacroCheck':doMacroCheck,
         'macroCheckFlags':macroFlagRgb}

def updateCfg(cfg):
  global rightRGB, leftRGB, doMacroCheck, macroFlagRgb
  rightRGB = cfg['rightRGB']
  leftRGB = cfg['leftRGB']
  doMacroCheck = cfg['doMacroCheck']
  macroFlagRgb = cfg['macroCheckFlags']    