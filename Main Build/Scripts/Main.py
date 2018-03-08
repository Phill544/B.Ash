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
import PlayerInfo
import PartyInfo

import random # JUST FOR TESTING PURPOSES

SG.StartEmulator()
listAreas = TM.GrabAreas()

print("Emulator Starting-- Please Wait.")
time.sleep(1) # Makes script wait to ensure that it can find the handle -- May need to increase this value depending on slow computers
window_id = SG.FindWindow()
input("Once you load the rom press Enter to Continue")


playerInfo = PlayerInfo.PlayerInfo()
pi = PartyInfo.PartyInfo()
opi = PartyInfo.OpponentPartyInfo()

worldLocation = playerInfo.FindArea()


location = PF.Load_Area("..\\" + worldLocation + "_pyMap.pkl")


player = Player.Player()
player.pos = playerInfo.FindCoords()
player.currentArea = worldLocation
player.facing = playerInfo.FindFacing()

player.printInfo()


input("Ready to try transitioning. Press enter and select the emulator within 3 seconds to continue")
time.sleep(3)

movement = om.Overworld_Movement(playerInfo, pi, opi)

movement.SetEndPos((10,0))
movement.RoutePlayer()

while True:
    print("Input the X-coord, then the Y-Coord")
    x = input()
    y = input()
    movement.SetEndPos((int(x),int(y)))
    time.sleep(1)
    movement.RoutePlayer()

'''time.sleep(2)

movement.TransitionToArea()

player.pos = pinfo.FindCoords()
worldLocation = pinfo.FindArea()
player.currentArea = worldLocation
player.facing = pinfo.FindFacing()

movement.player = player

movement.set_endPos((9,1))
movement.Route_Player()'''

