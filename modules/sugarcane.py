import keyboard as kb
import time
from threading import Thread

run = True
killThreads = False

completed = [False, False, False, False]

def cycle():
    global run, killThreads, completed
    try:
        while run:
            if not completed[0]:
                t1 = Thread(target=pressForSeconds, args=(['w', 'a'], 4, 0)).start()
            elif not completed[1]:
                t1 = Thread(target=pressForSeconds, args=(['w'], 2, 1)).start()
            elif not completed[2]:
                t1 = Thread(target=pressForSeconds, args=(['s', 'a'], 4, 2)).start()
            elif not completed[3]:
                t1 = Thread(target=pressForSeconds, args=(['d'], 3, 3)).start()

            if all(completed):
                for i in range(len(completed)):
                    completed[i] = False

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

def pressForSeconds(key, delay, ind):
    global completed
    for i in key:
        kb.press(i)

    time.sleep(delay)

    for i in key:
        kb.press(i)
    completed[ind] = True

t2 = Thread(target=cycle).start()
time.sleep(3)
killThreads = True
