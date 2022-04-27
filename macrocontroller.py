import os

macros = []
modules = []
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
    return 'S'
  except AttributeError:
    print('invalid file')
    return 'E'
    

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
  config = {}
  for i in macros:
    try:
      config += exec(f'{i}.config()')
    except:
      print(f'unknown error while attemping to grab config at name "{i}"')
  return config