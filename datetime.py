import os
import subprocess
from time import sleep
from sys import platform as _platform

def DateTime():
    print('')
    print("     --     Anime no Sekai     --     ")
    print('')
    print("                ©2020                 ")
    print('')
    print('')
    print('')
    print("Detected operating system (platform):", _platform)
    print('')
    print('')
    print('')
    print('')
    print('')
    start = input("Do you want to start? ")
    if start == "uncleared":
        if _platform == "darwin" or _platform == "linux" or _platform == "linux2":
            unix_uncleared()
        elif _platform == "win32" or _platform == "win64":
            print("Sorry, I do not support Windows yet.")
            print("Bye!")
            sleep(1)
            quit()
        else:
            print("Sorry, I do not support your operating system yet.")
            print("Bye〜!")
            sleep(1)
            quit()
    else:
        if _platform == "darwin" or _platform == "linux" or _platform == "linux2":
            unix()
        elif _platform == "win32" or _platform == "win64":
            print("Sorry, I do not support Windows yet.")
            print("Bye!")
            sleep(1)
            quit()
        else:
            print("Sorry, I do not support your operating system yet.")
            print("Bye〜!")
            sleep(1)
            quit()

def unix():
    while True:
        previousResult = "undefined"
        result = subprocess.check_output("date", shell=True, universal_newlines=True)
        if result != previousResult:
            clear = os.system('clear')
            print(result)
            continue
        else:
            previousResult = subprocess.check_output("date", shell=True, universal_newlines=True)
            sleep(.1)
            continue

def unix_uncleared():
    while True:
        print(subprocess.check_output("date", shell=True, universal_newlines=True))


#Runs the program
run = DateTime()