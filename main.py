import keyboard as kb
import mouse
import time 


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
  time.sleep(0.3)
  kb.release('enter')
  

def goToIs:
  openChat()
  type('/is')
  pressEnter()

def goToHub():
  openChat()
  type('/hub')
  pressEnter()
 
def walkToFarm():
  kb.press('a')
  time.sleep(1.3)
  kb.release('a')
  
def startFarming():
  try:
    import macro
    
    macro.init()
    macro.startMacro()
  except:
    print('unknown error, unable to start macro')



if __name__ == '__main__':
  goToHub()
  goToIs()
  walkToFarm()
  startFarming()
  kb.wait('p')
