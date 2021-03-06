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

# Activates the print block function
blockPrint()

R, G, B = 255, 255, 255, 

colour = (R,G,B)

from PIL import ImageGrab
from pyautogui import keyDown, keyUp
from time import sleep, perf_counter

while 1:
    start = perf_counter()
    # Get the RGB value for the pixel at the given coordinates on your screen
    Point1, Point2, Point3, Point4, Point5 = \
    ImageGrab.grab().load()[1162, 968], \
    ImageGrab.grab().load()[1162, 925], \
    ImageGrab.grab().load()[1167, 998], \
    ImageGrab.grab().load()[1179, 923], \
    ImageGrab.grab().load()[1138, 997]

    if Point1 != colour and Point2 != colour and Point3 == colour and Point4 == colour and Point5 != colour:
        sleep(.1)
        print('Press Q')
        keyDown("q") # Simulate a key press for the letter Q
        keyUp("q")
        pass

    if Point1 != colour and Point2 == colour and Point3 != colour and Point4 == colour and Point5 == colour:
        sleep(.1)
        print('Press W')
        keyDown("w") # Simulate a key press for the letter W
        keyUp("w")
        pass

    if Point1 == colour:
        sleep(.1)
        print('Press A')
        keyDown("a") # Simulate a key press for the letter A
        keyUp("a")
        pass

    if Point1 != colour and Point2 != colour and Point3 == colour and Point4 == colour and Point5 == colour:
        sleep(.1)
        print('Press D')
        keyDown("d") # Simulate a key press for the letter D
        keyUp("d")
        pass

    if Point1 != colour and Point2 == colour and Point3 == colour and Point4 != colour and Point5 == colour:
        sleep(.1)
        print('Press Z')
        keyDown("z") # Simulate a key press for the letter Z
        keyUp("z")
        pass

    if Point1 != colour and Point2 == colour and Point3 != colour and Point4 != colour and Point5 == colour:
        sleep(.1)
        print('Press X')
        keyDown("x") # Simulate a key press for the letter X
        keyUp("x")
        pass


    if Point1 != colour and Point2 == colour and Point3 == colour and Point4 == colour and Point5 == colour:
        sleep(.1)
        print('Press E')
        keyDown("e") # Simulate a key press for the letter E
        keyUp("e")
        pass

    if Point1 != colour and Point2 == colour and Point3 == colour and Point4 != colour and Point5 != colour:
        sleep(.1)
        print('Press S')
        keyDown("s") # Simulate a key press for the letter S
        keyUp("s")
        pass

    if Point1 != colour and Point2 != colour and Point3 == colour and Point4 != colour and Point5 != colour:
        sleep(.1)
        print('Press C')
        keyDown("c") # Simulate a key press for the letter C
        keyUp("c")
        pass
    end = perf_counter()
    print (end - start)
