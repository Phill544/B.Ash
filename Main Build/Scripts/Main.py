# Main file for pyMon
# Run this to start the bot.

import ScreenGrab as SG
import TemplateMatch as TM
import ImgSplit as IS
import Position_Finder as PF
import numpy as NP
import time
import Player
import Overworld_Movement as om

import random # JUST FOR TESTING PURPOSES

SG.StartEmulator()
listAreas = TM.GrabAreas()

print("Emulator Starting-- Please Wait.")
time.sleep(1) # Makes script wait to ensure that it can find the handle -- May need to increase this value depending on slow computers
window_id = SG.FindWindow()
input("Once you load the rom press Enter to Continue")

time.sleep(3)

image = SG.GetScreenShot(window_id)

littleroot = PF.Load_Area("..\\littleroot_pyMap.pkl")
player = Player.Player()
emTiles = PF.Emulator_Split(image)
player.pos = PF.FindPos(image, littleroot, emTiles)

player.facing = PF.FindPlayerFace(window_id)

player.printInfo()

"""while(True):    
    image = SG.GetScreenShot(window)
    player.currentArea = TM.MatchArea(image,listAreas)
    image = NP.asarray(image,dtype=NP.uint8)
    emTiles = PF.Emulator_Split(image)
    player.pos = PF.FindPos(image, littleroot, emTiles)
    player.printInfo()"""
movement = om.Overworld_Movement(player, littleroot, window_id)
endPoints = [(9,18),(7,10),(16,10)]
previousChoice = (7,10)

while True:

    dest = random.choice(endPoints)
    while dest == previousChoice:
        dest = random.choice(endPoints)
    movement.set_endPos(dest)
    print("Moving to: " + str(dest))
    previousChoice = dest
    movement.Route_Player()


