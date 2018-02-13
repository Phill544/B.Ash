import os # To find/save files. 
import win32gui # To find open windows and retrieve information (eg coords and size)
from PIL import ImageGrab # To take screenshots and save them to memory
import cv2 # TO convert the colours correctly
import numpy

print(os.getcwd())



"""

- Take Screenshot of window
- Find tiles of importance inside of window
- Run functions of tiles
- Maintain and update data about position in game world, e.g. On route XX
- Implement States that the bot will be in. i.e Currently training/returning to town/challenging next gym
- Choose next state based on goals.
- Able to identify and keep track of pokemon
- Able to at identify and complete battle state
- Able to use items
- Able to input into the game to change state and complete goals


"""
def StartEmulator():
    try:
        os.startfile(r"..\Emulator\VisualBoyAdvance-1.8.0-511.exe")
        print('[+] Emulator Started')
    except:
        print('[-] Error loading emulator.')

def ScreenShotWindow():
    window = win32gui.FindWindow("Afx:400000:0:0:900011:c8f0b35",None)
    rect = win32gui.GetClientRect(window)
    xstart, ystart = win32gui.ClientToScreen(window,(0,0))
    captureRect = (xstart, ystart, xstart + rect[2], ystart + rect[3])
    img = ImageGrab.grab(captureRect)    
    return img

def FindWindow():
    window = win32gui.FindWindow(None,"VisualBoyAdvance")
    return window

def GetScreenShot(window):
    rect = win32gui.GetClientRect(window)
    xstart, ystart = win32gui.ClientToScreen(window,(0,0))
    captureRect = (xstart, ystart, xstart + rect[2], ystart + rect[3])
    img = ImageGrab.grab(captureRect)
    img = numpy.asarray(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def GetScreenSnippit(window, xpos, ypos, width, height):
    rect = win32gui.GetClientRect(window)
    xstart, ystart = win32gui.ClientToScreen(window,(0,0))
    captureRect = (xstart + xpos, ystart + ypos, xstart + xpos + width, ystart + ypos + height)
    img = ImageGrab.grab(captureRect)
    img = numpy.asarray(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def FindWithWinSpy(classID):
    window = win32gui.FindWindow(str(classID),None)
    return window
                  

#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) THIS FIXES THE COLOUR ISSUES!
