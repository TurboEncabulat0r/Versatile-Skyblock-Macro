
class MacroController():
    def __init__(self):
        self.macros = []
        self.running = False
        self.macroRunning = None
    
    def runMacro(self, macro):
        if not self.macroRunning:
            for i in self.macros:
                if i.name == macro:
                    i.start()
                    self.running = True
                    self.macroRunning = i
                    return i

            raise MacroNotRegisteredException
        raise MacroAlreadyRunningException

    def register(self, macro):
        self.macros.append(macro)

    def stopMacro(self):
        if self.macroRunning:
            self.macroRunning.stop()
            self.running = False
            return
        raise MacroNotRunningException

class MacroNotRunningException(Exception):
    pass
    
class MacroAlreadyRunningException(Exception):
    pass

class MacroNotRegisteredException(Exception):
    pass

