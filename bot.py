import discord
from discord.ext import commands
import subcommands as sub
import random 

bot = commands.bot(command_prefix='.')

token = ''


@bot.event
async def on_ready():
  print("bot ready")
  print(f'logged in as {bot.user.name}')

  
@bot.command(name='dc')
async def dc(ctx):
  await ctx.send("attempting to disconnect")
  sub.disconnect()

@bot.command(name='hub')
async def hub(ctx):
  await ctx.send('going to hub')
  sub.goToHub()
  
@bot.command(name='is')
async def is(ctx):
  await ctx.send('going to is')
  sub.goToIs()

@bot.command(name='say')
async def say(ctx):
  imp = ctx.content
  if inp.find(" ") != -1:
    cmd = inp[0:inp.find(" ")]
    subcmd = inp[inp.find(" ") + 1: len(inp)]
    sub.say(subcmd)
    
  else:
    await ctx.send("error, you need to add a message to say. ex '.say your mom'")

@bot.command(name='startFarming')
async def startFarming(ctx):
  await ctx.send('attempting to start farming')
  sub.startFarming()
  
@bot.command(name='farmCycle')
async def farmCycle(ctx):
  await ctx.send('attempting a full farming cycle')
  sub.fullFarmCycle()

  
@bot.command(name='walkleft')
async def walkleft(ctx):
  imp = ctx.content
  if inp.find(" ") != -1:
    cmd = inp[0:inp.find(" ")]
    subcmd = inp[inp.find(" ") + 1: len(inp)]
    
    sub.walk('left', subcmd)
    
  else:
    await ctx.send("error, you need to add the ammount of seconds you want to walk. ex '.walkleft 2'")

@bot.command(name='walkright')
async def walkright(ctx):
  imp = ctx.content
  if inp.find(" ") != -1:
    cmd = inp[0:inp.find(" ")]
    subcmd = inp[inp.find(" ") + 1: len(inp)]
    
    sub.walk('right', subcmd)
    
  else:
    await ctx.send("error, you need to add the ammount of seconds you want to walk. ex '.walkright 2'")
    
@bot.command(name='walkforward')
async def walkforward(ctx):
  imp = ctx.content
  if inp.find(" ") != -1:
    cmd = inp[0:inp.find(" ")]
    subcmd = inp[inp.find(" ") + 1: len(inp)]
    
    sub.walk('up', subcmd)
    
  else:
    await ctx.send("error, you need to add the ammount of seconds you want to walk. ex '.walkforward 2'")
    
@bot.command(name='walkback')
async def walkback(ctx):
  imp = ctx.content
  if inp.find(" ") != -1:
    cmd = inp[0:inp.find(" ")]
    subcmd = inp[inp.find(" ") + 1: len(inp)]
    
    sub.walk('back', subcmd)
    
  else:
    await ctx.send("error, you need to add the ammount of seconds you want to walk. ex '.walkback 2'")
    
@bot.command()
async def test(ctx):
  ctx.send(f'gaming, {random.uniform(0.100, 0.400)}ms')
"""
WIP i wish make this where you type 'walk left 2'
@bot.command(name='walk')
async def walk(ctx):
    imp = ctx.content
  if inp.find(" ") != -1:
    cmd = inp[0:inp.find(" ")]
    subcmd = inp[inp.find(" ") + 1: len(inp)]
    
    
  else:
    await ctx.send("error, you need to add a direction to walk. ex '.say your mom'")
"""

if __name__ == '__main__':
  bot.run(token)
