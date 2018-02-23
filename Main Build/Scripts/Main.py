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

worldLocation = None
areas = TM.GrabAreas()

print("Please move around until a location is detected")

while worldLocation == None:
    image = SG.GetScreenShot(window_id)
    worldLocation = TM.MatchArea(image,areas)


print("Location detected at: " + worldLocation)
input("Press enter and select the emulator within 3 seconds to continue")
time.sleep(3)

location = PF.Load_Area("..\\" + worldLocation + "_pyMap.pkl")
player = Player.Player()
emTiles = PF.Emulator_Split(image)
player.pos = PF.FindPos(image, location, emTiles)

player.facing = PF.FindPlayerFace(window_id)

player.printInfo()

input("Ready to try transitioning. Press enter and select the emulator within 3 seconds to continue")
time.sleep(3)

player.pos = (9,7)

movement = om.Overworld_Movement(player, location, window_id)

movement.set_endPos((12,0))
movement.Route_Player()

time.sleep(2)

movement.TransitionToArea()

movement.set_endPos((10,1))
movement.Route_Player()



'''
movement = om.Overworld_Movement(player, location, window_id)
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

'''
