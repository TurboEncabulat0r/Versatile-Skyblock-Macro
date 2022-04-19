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
  
  cfg.token = settings['token']
  cfg.RGB = tuple(settings['RGB'])
  cfg.sendReports = bool(settings['sendReports'])
  cfg.devInfo = bool(settings['devInfo'])
  return cfg
