import time
import os
from threading import Thread

lines = []
updateSpeed = 0.5
killThreads = False
def start():
  Thread(_startPrinting).start()

def _startPrinting():
  global killThreads, lines
  while True:
    if killThreads:
      break
    for i in lines:
      print(i)
    time.sleep(updateSpeed)

def updateLines(lst):
  global lines
  lines = lst

def appendLines(obj):
  global lines
  lines.append(obj)

def clear():
  os.system('cls')

def stop():
  global killThreads
  killThreads = True