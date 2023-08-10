
class MacroController:
    def __init__(self, m=[]):
        self.macros = m
        self.running = False
        self.macroRunning = None

    def runMacroByIndex(self, index):
        if not self.macroRunning:
            if index < len(self.macros):
                print(f"invoking macro {self.macros[index].name}")
                self.macros[index].start()
                self.running = True
                self.macroRunning = self.macros[index]
                return self.macros[index]
            raise MacroNotRegisteredException
        raise MacroAlreadyRunningException
    
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

    def resumeMacro(self):
        if self.macroRunning:
            self.macroRunning.resume()
            return
        raise MacroNotRunningException

    def pauseMacro(self):
        if self.macroRunning:
            self.macroRunning.pause()
            return
        raise MacroNotRunningException

    def getAllMacros(self):
        return self.macros

    def getMacroTime(self):
        if self.macroRunning:
            return self.macroRunning.getTime()
        raise MacroNotRunningException

class MacroNotRunningException(Exception):
    pass
    
class MacroAlreadyRunningException(Exception):
    pass

class MacroNotRegisteredException(Exception):
    pass

