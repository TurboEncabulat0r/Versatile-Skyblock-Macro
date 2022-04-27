import configparser

config = configparser.ConfigParser()

class Config():
  def __init__(self, token, RGB, sendReports, devInfo):
    self.token = token
    self.RGB = RGB
    self.sendReports = sendReports
    self.devInfo = devInfo


def write(cfg):
  config['MAIN SETTINGS'] = {'token': cfg.token,
                        'RGB': cfg.RGB,
                        'sendReports': cfg.sendReports,
                        'devInfo': cfg.devInfo}
  
  with open('config.ini', 'w') as configfile:
    config.write(configfile)
                        
def read():
  cfg = Config()
  
  settings = configparser.ConfigParser()
  settings.read('config.ini')
  for i in range(3):
    try:
      cfg.token = str(settings['token'])
      cfg.RGB = tuple(settings['RGB'])
      cfg.sendReports = bool(settings['sendReports'])
      cfg.devInfo = bool(settings['devInfo'])
    except:
      print('error with config file')
      print('writing config file and trying again')
      write()
  
  return cfg