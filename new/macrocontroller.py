
class MacroController:
    def __init__(self, m=[]):
        self.macros = m
        self.isRunning = False
        self.currentMacro = None

    def runMacroByIndex(self, index):
        if not self.isRunning:
            if index < len(self.macros):
                print(f"invoking macro {self.macros[index].name}")
                self.macros[index].start()
                self.isRunning = True
                self.currentMacro = self.macros[index]
                return self.macros[index]
            raise MacroNotRegisteredException
        raise MacroAlreadyRunningException
    
    def runMacro(self, macro):
        if not self.isRunning:
            for i in self.macros:
                if i.name == macro:
                    i.start()
                    self.isRunning = True
                    self.currentMacro = i
                    return i

            raise MacroNotRegisteredException
        raise MacroAlreadyRunningException

    def register(self, macro):
        self.macros.append(macro)

    def stopMacro(self):
        if self.isRunning:
            self.currentMacro.stop()
            self.isRunning = False
            return
        raise MacroNotRunningException

    def resumeMacro(self):
        if self.isRunning:
            self.currentMacro.resume()
            return
        raise MacroNotRunningException

    def pauseMacro(self):
        if self.isRunning:
            self.currentMacro.pause()
            return
        raise MacroNotRunningException

    def getAllMacros(self):
        return self.macros

    def getMacroTime(self):
        if self.isRunning:
            return self.currentMacro.getTime()
        raise MacroNotRunningException

class MacroNotRunningException(Exception):
    pass
    
class MacroAlreadyRunningException(Exception):
    pass

class MacroNotRegisteredException(Exception):
    pass

