import os
import sys

packages = [
    'pyautogui',
    'keyboard',
    'numpy',
    'pillow',
    'pynput',
    'mouse'
]


def install():
    while True:
        inp = input("Error initialising, packages missing, would you them to be automatically installed(Y or N)")
        if inp == "Y" or inp == 'y':
            print('installing packages')
            for i in packages:
                os.system(f'python -m pip install {i}')
        elif inp == "N" or inp == 'n':
            print("a restart of the macro is required")
            input('press enter to exit')
            sys.exit(0)
        else:
            print('invalid input')
