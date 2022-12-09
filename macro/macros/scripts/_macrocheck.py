import numpy as np, pyautogui
from PIL import Image
import mouse, keyboard
import time

macroTripped = False
macroFlagReason = ''

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
        macroFlagReason = f'DetectedRgb{i}'
        
  except:
    print('error occured in anti macro check, stopping macro')
    macroFlagReason = f'Error'
    macroTripped = True
    releaseAllKeys()

def releaseAllKeys():
  keys = 'adws'
  mouse.release('left')
  for i in keys:
    keyboard.release(i)
  keyboard.press('escape')
  time.sleep(0.1)
  keyboard.release('escape')