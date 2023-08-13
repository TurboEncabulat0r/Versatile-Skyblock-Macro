import bot
import os

packages = ["mouse", "keyboard", "numpy", "pillow", "pyautogui"]

while True:
    try:
        bot.run()
    except ImportError:
        input("error - packages not installed, press enter to install...")
        for i in packages:
            os.system(f"pip install {i}")
    except Exception as error:
        print("critical error please send log.txt to turbo and restart the program")
        with open("log.txt", "w") as f:
            f.write(str(error))


