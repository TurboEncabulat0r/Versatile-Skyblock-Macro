import os

macros = []
modules = []

activeMacro = ''

def importAll():
  global macros, modules
  directory = 'macros'

  for filename in os.listdir(directory):
      f = os.path.join(directory, filename)
      if os.path.isfile(f):
          g = breakStr(filename)
          try:
              exec(f'from {directory} import {g}', globals())
              print(f'importing {g}')
              macros.append(g)
              exec(f'{g}.test()')
          except ZeroDivisionError:
              print('unknown error importing file')

            
          
def attemptRun(name):
  if name in macros:
    print('running file')
  else:
    print('file does not exist')
    return 'FNE'
    
  try:
    exec(f'{name}.startmacro()')
    activeMacro = name
    return 'S'
  except AttributeError:
    print('invalid file')
    return 'E'

def getAllMacros():
  return macros

def stopMacro():
  global activeMacro
  name = activeMacro
  
  if name in macros:
    print('stopping file')
  else:
    raise FileNotExist
    
  try:
    exec(f'{name}.stopmacro()')
    activeMacro = ''
    return 'S'
  except AttributeError:
    raise IncorrectFileFormat
  

def breakStr(text, returnCmd=False):
    if returnCmd:
        if text.find(".") != -1:
            cmd = text[0:text.find(".")]
            subcmd = text[text.find(".") + 1: len(text)]
            return (cmd, subcmd)
        else:
            return
    else:
        if text.find(".") != -1:
            cmd = text[0:text.find(".")]
            subcmd = text[text.find(".") + 1: len(text)]
            return cmd
        else:
            return


def getAllConfig():
  print('getting all cfg')
  config = []
  for i in macros:
    try:
      ret = eval(f'{i}.config()', globals())
      config.append([str(i), ret])
    except ImportError:
      print(f'unknown error while attemping to grab config at name "{i}"')
  return config

def updateAllCfg(cfg):
  print('updating cfg')
  print(cfg)
  for i in cfg:
    macro = i[0]
    config = i [1]
    print(f'updating config for {config}')
    exec(f'{macro}.updateCfg(config)')


def getMacroList():
  return macros


def getActiveMacro():
  return activeMacro

class FileNotExist(Exception):
  pass

class IncorrectFileFormat(Exception):
  pass