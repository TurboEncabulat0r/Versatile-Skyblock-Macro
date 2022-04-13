import io, time, random
import subcommands as sub
from threading import Thread
import packages as pac

def packages():
    global discord, commands
    import discord
    from discord.ext import commands
    import keyboard, pyautogui, mouse
    from pynput import keyboard as kb
    import numpy as np
    from PIL import Image

bot = commands.Bot(command_prefix='.')

token = 'OTYyODY0OTE5MzQxMDQ3ODkw.YlNv1Q.MDvppJ1GryCnzzMdOZcN4eSbRzU'
starttime = 0

thread1 = 0

@bot.event
async def on_ready():
    print("bot ready")
    print(f'logged in as {bot.user.name}')


@bot.command(name='dc', brief='disconnects from server')
async def dc(ctx):
    await ctx.send("attempting to disconnect")
    sub.disconnect()


@bot.command(name='tohub', brief='sends the player to hub')
async def tohub(ctx):
    await ctx.send('going to hub')
    sub.goToHub()


@bot.command(name='tois', brief='sends the player to the is')
async def tois(ctx):
    await ctx.send('going to is')
    sub.goToIs()


@bot.command(name='say', brief='says anything in minecraft chat')
async def say(ctx, *, content)):
    imp = ctx.message.content
    if imp.find(" ") != -1:
        cmd = imp[0:imp.find(" ")]
        subcmd = imp[imp.find(" ") + 1: len(imp)]
        sub.say(subcmd)

    else:
        await ctx.send("error, you need to add a message to say. ex '.say your mom'")


@bot.command(name='startFarming', brief='forces to start farming, use farmcycle instead')
async def startFarming(ctx):
    global starttime, thread1
    await ctx.send('attempting to start farming')
    starttime = time.time()
    thread1 = Thread(target=sub.startFarming).start()


@bot.command(name='farmcycle', brief='cycles the macro, resets the view and starts farming')
async def farmcycle(ctx):
    global starttime, thread1
    await ctx.send('attempting a full farming cycle')
    starttime = time.time()
    thread1 = Thread(target=sub.fullFarmCycle).start()


@bot.command(name='walkleft', brief='make the character walk left')
async def walkleft(ctx):
    imp = ctx.message.content
    if imp.find(" ") != -1:
        cmd = imp[0:imp.find(" ")]
        subcmd = imp[imp.find(" ") + 1: len(imp)]

        sub.walk('left', subcmd)

    else:
        await ctx.send("error, you need to add the ammount of seconds you want to walk. ex '.walkleft 2'")


@bot.command(name='walkright', brief='make the character walk right')
async def walkright(ctx, *, content):
    imp = ctx.message.content
    if imp.find(" ") != -1:
        cmd = imp[0:imp.find(" ")]
        subcmd = imp[imp.find(" ") + 1: len(imp)]

        sub.walk('right', subcmd)

    else:
        await ctx.send("error, you need to add the ammount of seconds you want to walk. ex '.walkright 2'")


@bot.command(name='walkforward',brief='make the character walk forwards')
async def walkforward(ctx:
    imp = ctx.message.content
    if imp.find(" ") != -1:
        cmd = imp[0:imp.find(" ")]
        subcmd = imp[imp.find(" ") + 1: len(imp)]

        sub.walk('up', subcmd)

    else:
        await ctx.send("error, you need to add the ammount of seconds you want to walk. ex '.walkforward 2'")


@bot.command(name='walkback', brief='make the character walk backwards')
async def walkback(ctx):
    imp = ctx.messgae.content
    if imp.find(" ") != -1:
        cmd = imp[0:imp.find(" ")]
        subcmd = imp[imp.find(" ") + 1: len(imp)]

        sub.walk('back', subcmd)

    else:
        await ctx.send("error, you need to add the ammount of seconds you want to walk. ex '.walkback 2'")


@bot.command(name='sc', brief='takes a screenshot and sends it')
async def sc(ctx):
    image = pyautogui.screenshot()
    with io.BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))

                      
@bot.command(name='runtime', brief='tells you how long the macro has been running for')
async def runtime(ctx):
    if starttime != 0:
        if time.time() - starttime < 60:
            await ctx.send(f'the macro has been running for {time.time() - starttime} sec')
        elif time.time() - starttime < 3600:
            await ctx.send(f'the macro has been running for {(time.time() - starttime)/60} min')
        else:
            await ctx.send(f'the macro has been running for {((time.time() - starttime)/60)/60} hours')
    else:
        await ctx.send(f'the macro is currently not running')

                      
@bot.command(name='stop', brief='stops the macro')
async def stop(ctx):
    sub.stopmacro()
    await ctx.send('macro stopped')


@bot.command(name='test', brief='dev stuff')
async def test(ctx):
    await ctx.send(f'gaming, {random.uniform(0.100, 0.400)}ms')


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
    try:
        packages()
    except:
        pac.install()
                      
    bot.run(token)
