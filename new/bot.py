import keyboard as kb
from scripts import subcommands as sub
import configmanager
import macrocontroller as controller
from macros.sugarcane import Sugarcane
from macros.netherwart import Netherwart
from macros.potato import Potato
from macros.coco import Coco

config = configmanager.read()

m = [Sugarcane(), Netherwart(), Potato(), Coco()]

mcontroller = controller.MacroController(m)


macros = ["sugarcane", 'netherwart', 'potato', 'coco']

hotkey = "b"


selectedMacro = 'coco'

hkey = None
def setHotKey():
    global hkey
    if hkey == None:
        hkey = kb.add_hotkey(hotkey, runMacro)
    else:
        kb.remove_all_hotkeys()
        hkey = kb.add_hotkey(hotkey, runMacro)


def printStatus():
    print(f"""
    --Cauldron Macro Engine v0.3.4(manual)--

    registered commands:
    help - displays this list
    select - selects a macro (1 arg)
    hotkey - sets hotkey to run macro (1 arg)
    getAllMacros - prints a list of all macros
    
    extra:
    to run macro press the hotkey '{hotkey}'
    the macro is currently set to '{selectedMacro}'
    you can change this by running the 'select' command
    """)

macroRunning = False
def runMacro():
    global macroRunning

    try:
        if not macroRunning:
            print("[MACRO] manually invoking macro")
            mcontroller.runMacro(selectedMacro)
            macroRunning = True
        else:
            mcontroller.stopMacro()
            macroRunning = False

    except controller.MacroAlreadyRunningException:
        print("error - macro already running!")


def lookForCmds():
    global selectedMacro, hotkey
    while True:
        inp = input(">> ")

        args = sub.breakString(inp, " ")
        if args[0] == 'select':

            if len(args) > 1:
                if args[1] in macros:
                    selectedMacro = args[1]
                else:
                    print("error - macro not recognised, use getAllMacros to get a list of all macros")

            else:
                print("error - please enter a macro to select")
        elif args[0] == 'help':
            printStatus()
        elif args[0] == 'hotkey':
            if len(args) > 1:
                if len(args[1]) == 1:
                    hotkey = args[1]
                    setHotKey()
            else:
                print("error - please enter a key")

        elif args[0] == "getAllMacros":
            print(mcontroller.getAllMacros())

        else:
            print("error - command not recognised use 'help'")



def run():
    setHotKey()
    printStatus()
    lookForCmds()
