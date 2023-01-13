import configparser
import macrocontroller as controller

config = configparser.ConfigParser()

class Config():
  def __init__(self, token, sendReports, macros):
    self.token = token
    self.sendReports = sendReports
    self.macros = macros


def write(cfg):
  config['SETTINGS'] = {'token': 'token',
                        'sendReports': 'sendReports'}
  
  for i in cfg:
   config[i[0]] = i[1]

  
  with open('config.ini', 'w') as configfile:
    config.write(configfile)
                        
def read():
  cfg = Config(0, 0, 0)
  
  config = configparser.ConfigParser()
  config.read('config.ini')

  settings = config['SETTINGS']
  
  try:
    cfg.token = str(settings['token'])
    cfg.sendReports = bool(settings['sendReports'])


    return cfg
  except ImportError:
    print('error with config file')
  