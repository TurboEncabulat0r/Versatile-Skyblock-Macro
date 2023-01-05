
class MacroController():
    def __init__(self):
        self.macros = []
        self.running = False
        self.macroRunning = None
    
    def runMacro(self, macro):
        for i in self.macros:
            if i.name == macro:
                i.start()
                self.running = True
                self.macroRunning = i
                return i

        raise MacroNotRegisteredException

    def register(self, macro):
        self.macros.append(macro)

    def stopMacro(self):
        self.macroRunning.stop()
        self.running = False
    


class MacroNotRegisteredException(Exception):
    pass

