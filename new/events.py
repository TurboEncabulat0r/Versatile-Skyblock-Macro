import discord
from discord.ext import commands
from threading import Thread
import time
bot = 'd'
channel = 968713627584589845


class BotNotInitError(Exception):
  pass

class Event(object):
  def __init__(self, text, delay):
    self.text = text
    self.delay = delay

    self.killThreads = False
    
  def sequence(self):
    
    while True:
      time.sleep(self.delay)
      if not self.killThreads:
        sendEvent(self.text)
      else:
        break
        
  def start(self):
    self.killThreads = False
    t1 = Thread(target=self.sequence).start()
    
  def stop(self):
    self.killThreads = True
    

async def sendEvent(text):
  if not bot == 'd':
    ch = bot.get_channel(channel)
  
    await ch.send(text)
  else:
    raise BotNotInitError


def init(b):
  global bot
  bot = b