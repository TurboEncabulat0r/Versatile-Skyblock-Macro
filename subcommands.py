import keyboard as kb
import mouse
import time 
import macro

def openChat():
  kb.press('t')
  time.sleep(0.05)
  kb.release('t')
  time.sleep(0.1)

def type(text, delay=0.04):
  for i in range(len(text)):
    kb.press(text[i])
    time.sleep(delay)
    kb.release(text[i])

def pressEnter():
  kb.press('enter')
  time.sleep(0.1)
  kb.release('enter')
  

def goToIs():
  openChat()
  type('/is')
  pressEnter()

def goToHub():
  openChat()
  type('/hub')
  pressEnter()
 
def walkToFarm():
  newDirCorrection = True
  
  if newDirCorrection:
    walk('left', 2)
    time.sleep(0.1)
    walk('right', 1)
    time.sleep(0.1)
    walk('left', .8)
    time.sleep(0.25)
    walk('right', 0.8)
    walk('left', 1.5)
  else:
    kb.press('a')
    time.sleep(1.3)
    kb.release('a')
  
  
def startFarming():
    macro.init()
    macro.startmacro()

    
def fullFarmCycle():
  goToHub()
  time.sleep(1.2)
  goToIs()

  time.sleep(0.4)
  kb.press('shift')
  time.sleep(0.2)
  kb.release('shift')
  walkToFarm()
  startFarming()
  kb.wait('p')

  
def say(text):
  openChat()
  type(text)
  pressEnter()
  
  
def disconnect():
  kb.press('escape')
  time.sleep(0.1)
  kb.release('escape')
  mouse.move(0, 10, absolute=False, duration=0.1)
  mouse.click('left')

  
def walk(dir, duration):
  if dir == 'left':
    key = 'a'
  elif dir == 'right':
    key = 'd'
  elif dir == 'up':
    key = 'w'
  elif dir == 'back':
    key = 's'
  else:
    print('key not recognised')
  
  kb.press(key)
  time.sleep(duration)
  kb.release(key)
  
  
"""
if __name__ == '__main__':
  goToHub()
  goToIs()
  walkToFarm()
  startFarming()
  kb.wait('p')
 """
