from PIL import Image, ImageTk
from tkinter import *
import tkinter as tkr
import PIL.ImageGrab
import pyautogui
import time
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Stop the print command from showing up in the console
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Start of Code
print("Welcome to the Ark Automated Fishing Service")
time.sleep(2)
print("Starting program")
time.sleep(2)

# Activates the print block function
#blockPrint()

print('39')
loop = 1

R = 255
G = 255
B = 255

colour = (R,G,B)

while loop == 1:
    print(colour)
    PressQ = PIL.ImageGrab.grab().load()[1181, 1016]  # Get the RGB value for the pixel at x=1181, y=1016 on your screen
    PressW = PIL.ImageGrab.grab().load()[1113, 868]  # Get the RGB value for the pixel at x=1113, y=868 on your screen
    PressA = PIL.ImageGrab.grab().load()[1162, 970]  # Get the RGB value for the pixel at x=1162, y=970 on your screen
    PressD = PIL.ImageGrab.grab().load()[1192, 906]  # Get the RGB value for the pixel at x=1192, y=906 on your screen
    PressZ = PIL.ImageGrab.grab().load()[1158, 973]  # Get the RGB value for the pixel at x=1158, y=973 on your screen
    PressX = PIL.ImageGrab.grab().load()[1167, 972]  # Get the RGB value for the pixel at x=1167, y=972 on your screen

    PressE = PIL.ImageGrab.grab().load()[1186, 998]  # Get the RGB value for the pixel at x=1186, y=998 on your screen
    PressS = PIL.ImageGrab.grab().load()[1161, 917]  # Get the RGB value for the pixel at x=1161, y=917 on your screen
    PressC = PIL.ImageGrab.grab().load()[1135, 918]  # Get the RGB value for the pixel at x=1135, y=918 on your screen

    print('55')

    while PressQ == colour:
        time.sleep(0.1)
        print('Press Q')
        pyautogui.keyDown("q")
        pyautogui.keyUp("q")
        continue

    while PressW == colour:
        time.sleep(0.1)
        print('Press W')
        pyautogui.keyDown("w")
        pyautogui.keyUp("w")
        continue

    while PressA == colour:
        time.sleep(0.1)
        print('Press A')
        pyautogui.keyDown("a")
        pyautogui.keyUp("a")
        continue

    while PressD == colour:
        time.sleep(0.1)
        print('Press D')
        pyautogui.keyDown("d")
        pyautogui.keyUp("d")
        continue

    while PressZ == colour:
        time.sleep(0.1)
        print('Press Z')
        pyautogui.keyDown("z")
        pyautogui.keyUp("z")
        continue

    while PressX == colour:
        time.sleep(0.1)
        print('Press X')
        pyautogui.keyDown("x")
        pyautogui.keyUp("x")
        continue


    while PressE == colour and PressA != colour and PressZ != colour and PressW != colour and PressX != colour and PressD != colour:
        time.sleep(0.1)
        print('Press E')
        pyautogui.keyDown("e")
        pyautogui.keyUp("e")
        continue

    while PressS == colour and PressZ != colour and PressW != colour and PressX != colour:
        time.sleep(0.1)
        print('Press S')
        pyautogui.keyDown("s")
        pyautogui.keyUp("s")
        continue

    while PressC == colour and PressQ != colour and PressD != colour:
        time.sleep(0.1)
        print('Press C')
        pyautogui.keyDown("c")
        pyautogui.keyUp("c")
        continue
