import os # To find/save files. 
import win32gui # To find open windows and retrieve information (eg coords and size)
from PIL import ImageGrab # To take screenshots and save them to memory
import cv2 # TO convert the colours correctly
import numpy

###########################################################
# This script is used to start, find, and get screenshots #
# of the emulator window.                                 #
###########################################################



# TODO: Move this function to a more accurate module.
def StartEmulator():
    try:
        os.startfile(r"..\Emulator\VisualBoyAdvance-1.8.0-511.exe")
        print('[+] Emulator Started')
    except:
        print('[-] Error loading emulator.')

# Depreciated function, do not use.
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


# Takes a screenshot of the window.
def GetScreenShot(window):
    rect = win32gui.GetClientRect(window)
    xstart, ystart = win32gui.ClientToScreen(window,(0,0))
    captureRect = (xstart, ystart, xstart + rect[2], ystart + rect[3])
    img = ImageGrab.grab(captureRect)
    img = numpy.asarray(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


# Takes a snippit of the window starting at the xpos and ypos, and going for the height/width
def GetScreenSnippit(window, xpos, ypos, width, height):
    rect = win32gui.GetClientRect(window)
    xstart, ystart = win32gui.ClientToScreen(window,(0,0))
    captureRect = (xstart + xpos, ystart + ypos, xstart + xpos + width, ystart + ypos + height)
    img = ImageGrab.grab(captureRect)
    img = numpy.asarray(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


# Depreciated function, do not use.
def FindWithWinSpy(classID):
    window = win32gui.FindWindow(str(classID),None)
    return window
                  

#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) THIS FIXES THE COLOUR ISSUES!
