import os
import sys

packages = [
    'pyautogui',
    'keyboard',
    'numpy',
    'pillow',
    'pynput',
    'mouse',
    'discord',
    'discord.ext'
]


def install():
    while True:
        inp = input("Error initialising, packages missing, would you them to be automatically installed(Y or N)")
        if inp == "Y" or inp == 'y':
            print('installing packages')
            for i in packages:
                os.system(f'python -m pip install {i}')
            os.system('cls')
            print('a restart of the macro is required to finish this')
            input('press enter to exit')
        elif inp == "N" or inp == 'n':
            print("the packages are required to run the macro, if you wish to install them manually a list of them are in 'packages.py'")
            input('press enter to exit')
            sys.exit(0)
        else:
            print('invalid input')
