import mouse, keyboard as kb
import pyautogui, time
from threading import Thread
run = True
killThreads = False
forwardTime = 24
backTime = 30

def startmacro():
  global t1
  t1 = Thread(target=cycle).start()


def cycle():
  while run:
    pressForSeconds(['w', 'a'], forwardTime)
    pressForSeconds('w', 2)
    pressForSeconds(['s', 'a'], backTime)
    pressForSeconds('d', 3)


def pressForSeconds(key, delay):
  if len(key) == 1:
    kb.press(key)
    time.sleep(delay)
    kb.press(key)
  elif len(key) > 1 and type(key) == list:

    for i in key:
      kb.press(i)

    time.sleep(delay)

    for i in key:
      kb.press(i)
