import keyboard as kb
import time
import mouse
from threading import Thread

rows = 30

forwardTime = 30
backtime = 30
rightTime = 5
leftTime = 5

run = True
killThreads = False
row = 0
completed = [False, False, False, False]
pressed = [False, False, False, False]

def cycle():
    global run, killThreads, completed
    try:
        mouse.press('left')
        while run:
            if not completed[0] and not pressed[0]:
                t1 = Thread(target=pressForSeconds, args=(['w', 'a'], forwardTime, 0)).start()
            elif not completed[1] and not pressed[1]:
                t1 = Thread(target=pressForSeconds, args=(['w'], rightTime, 1)).start()
            elif not completed[2] and not pressed[2]:
                t1 = Thread(target=pressForSeconds, args=(['s', 'a'], backTime, 2)).start()
            elif not completed[3] and not pressed[3]:
                t1 = Thread(target=pressForSeconds, args=(['d'], rightTime, 3)).start()

            if all(completed):
                for i in range(len(completed)):
                    completed[i] = False
                    row += 1

            if killThreads:
                run = False
                break
                
            print('frame')
    finally:
        print('macro stopped')

        
def releaseKeys():
    keys = 'wasd'
    for i in keys:
         kb.release(i)
            
    mouse.release('left')

            
def pressForSeconds(key, delay, ind):
    global completed, pressed
    pressed[ind] = True
    for i in key:
        kb.press(i)

    time.sleep(delay)

    for i in key:
        kb.press(i)
        
    pressed[ind] = False
    completed[ind] = True

def startMacro():
    t2 = Thread(target=cycle).start()

def stopMacro():
    killThreads = True
    run = True
    releaseKeys()
