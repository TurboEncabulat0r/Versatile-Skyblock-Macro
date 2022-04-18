import keyboard as kb
import mouse
import time
import macro
from modules import netherwart as nw

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
    newDirCorrection = False

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

def resumeFarming():
    macro.init()
    macro.resumeMacro()


def fullFarmCycle():
    goToHub()
    time.sleep(1.2)
    goToIs()

    time.sleep(0.4)
    kb.press('shift')
    time.sleep(0.8)
    kb.release('shift')
    walkToFarm()
    startFarming()
    print('macro process started')


def say(text):
    openChat()
    type(text)
    pressEnter()


def disconnect():
    kb.press('escape')
    time.sleep(0.1)
    kb.release('escape')
    mouse.move(0, 40, absolute=False, duration=0.15)
    mouse.click('left')


def stopmacro():
    macro.stopmacro()


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

def accepttrade():
    time.sleep(5)
    kb.press('t')
    time.sleep(0.2)
    kb.release('t')

    kb.write('/trade whitelisted14')
    time.sleep(0.2)

    kb.press('enter')
    time.sleep(0.2)
    kb.release('enter')
    
def pressKey(key, delay=0.15):
    kb.press(key)
    time.sleep(delay)
    kb.release(key)
    
def openinv():
    pressKey('e')

def fixFarming():
    mouse.press('left')

def netherwart():
    nw.init()
    nw.resumeMacro()

def mouseMove(dir, amm=5):
    if dir == 'up':
        mouse.move(0, amm * -1, absolute=False, delay=0.2)
        return 'mouse moved ' + dir + ' by ' + amm
    elif dir == 'down':
        mouse.move(0, amm, absolute=False, delay=0.2)
        return 'mouse moved ' + dir + ' by ' + amm
    else:
        return 'mouse failed to move, enter a valid direction'

def breakCommand(text, returnCmd=False):
    if returnCmd:
        if text.find(" ") != -1:
            cmd = text[0:text.find(" ")]
            subcmd = text[text.find(" ") + 1: len(text)]
            return (cmd, subcmd)
        else:
            return ''
    else:
        if text.find(" ") != -1:
            cmd = text[0:text.find(" ")]
            subcmd = text[text.find(" ") + 1: len(text)]
            return subcmd
        else:
            return ''
"""
if __name__ == '__main__':
  goToHub()
  goToIs()
  walkToFarm()
  startFarming()
  kb.wait('p')
 """
