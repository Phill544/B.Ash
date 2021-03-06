import _pickle as pickle
import Tile_Classes as tc
import Player
import Position_Finder as pf
import ctypes
import time
import DirectKeys as dk
import Pathfinding
import TemplateMatch as tm
import ScreenGrab as sg
import ImgSplit as IS
import os
import cv2

###########################################################
# This script contains the movement class                 #
###########################################################

##############################
# How the class functions:
##############################
# Find the tile destination.
# Find current position
# Calculate AStar route
# Move player to tiles on the route based off of current facing and position
##############################
# Class inputs:
##############################
# _player = Instance of the player - See Player.py for more info.
# _area = A 2D list of tiles from the current map space.
# _window_id = The current windows id for the emulator.
##############################

class Overworld_Movement():

    def __init__(self, _player, _area, _window_id):
        self.player = _player
        self.area = _area
        self.window_id = _window_id
        self.PLAYER_TILE_POS = (7,4) #Center tile for emulator window
        self.TILE_SIZE = 16
        self.npcs = self.LoadAreaNPCs()
        self.TrimNpcShape()

    # Sets the destination position of the player.
    def set_endPos(self,coord):
        self.endPos = coord

    # The main function for this class. Route player attempts to move the player
    # to their current destination.
    def Route_Player(self):
        aStar = Pathfinding.AStar(self.area, self.area[self.player.pos[1]][self.player.pos[0]], self.area[self.endPos[1]][self.endPos[0]])
        self.route = aStar.process()

        while len(self.route) > 0:
            nextMove = self.route.pop()
            self.move_player(nextMove)
            time.sleep(0.1)

            

    # The function responsible for choosing which direction the player takes to get to their next position.
    def move_player(self,nextMove):
        # Calculate next position to move
        # face player in correct position
        # EXTRA: LOOK AT TILE TO BE MOVED AT, IF NPC IS THERE, WAIT SOME TIME
        if self.player.pos[0] < nextMove[0] and self.player.pos[1] == nextMove[1]:
            self.Move_Right()            
        elif self.player.pos[0] > nextMove[0] and self.player.pos[1] == nextMove[1]:
            self.Move_Left()
            
        elif self.player.pos[1] < nextMove[1] and self.player.pos[0] == nextMove[0]:
            self.Move_Down()            
        elif self.player.pos[1] > nextMove[1] and self.player.pos[0] == nextMove[0]:
            self.Move_Up()
            
        time.sleep(0.1) # Approx time it takes for player to move one time

    def Move_Right(self):
        if self.player.facing != 'e':
            dk.Button_RIGHT()
            print("Rotating player: RIGHT")
            self.player.facing = 'e'
        self.CheckNextSquare(self.player.facing)
        dk.Button_RIGHT()
        self.player.pos = (self.player.pos[0] + 1, self.player.pos[1]) # Increase X pos
        print("Moving player: RIGHT")

    def Move_Left(self):
        if self.player.facing != 'w':
            dk.Button_LEFT()
            print("Rotating player: LEFT")
            self.player.facing = 'w'
        self.CheckNextSquare(self.player.facing)
        dk.Button_LEFT()
        self.player.pos = (self.player.pos[0] - 1, self.player.pos[1]) # Decrease X pos
        print("Moving player: LEFT")

    def Move_Down(self):
        if self.player.facing != 's':
            dk.Button_DOWN()
            print("Rotating player: DOWN")
            self.player.facing = 's'
        self.CheckNextSquare(self.player.facing)
        dk.Button_DOWN()
        self.player.pos = (self.player.pos[0], self.player.pos[1] + 1) # Increase Y pos
        print("Moving player: DOWN")        

    def Move_Up(self):
        if self.player.facing != 'n':
            dk.Button_UP()
            print("Rotating player: UP")
            self.player.facing = 'n'
        self.CheckNextSquare(self.player.facing)
        dk.Button_UP()
        self.player.pos = (self.player.pos[0], self.player.pos[1] - 1) # Decrease Y pos
        print("Moving player: UP")


        
    # Checks the tile in font of the player to see whether there is an npc.
    # TODO: Make this code nicer.
    # TODO: Change the code so that it will check to see whether there is a npc in front, but also diagonal to the player
    def CheckNextSquare(self, facing):
        player_Tile = (self.PLAYER_TILE_POS[0]*self.TILE_SIZE,(self.PLAYER_TILE_POS[1]*self.TILE_SIZE) + 7) # Because we ignore first 8 tiles in y-axis
        print(str(player_Tile))
        print("Checking tile to the: " + self.player.facing)
        waitForMove = False
        if facing == 'n':
            # check north square of player            
            while self.CheckXTiles((player_Tile[0],player_Tile[1] - self.TILE_SIZE)):
                waitForMove = True
            if waitForMove:
                time.sleep(0.2)
                self.Route_Player()
            
        elif facing == 's':
            # check south square of player
            while self.CheckXTiles((player_Tile[0],player_Tile[1] + self.TILE_SIZE)):
                waitForMove = True
            if waitForMove:
                time.sleep(0.2)
                self.Route_Player()
        
        elif facing == 'e':
            # check east square of player
            while self.CheckYTiles((player_Tile[0] + self.TILE_SIZE, player_Tile[1])):
                waitForMove = True
            if waitForMove:
                time.sleep(0.2)
                self.Route_Player()
        
        elif facing == 'w':
            # check west square of player
            while self.CheckYTiles((player_Tile[0] - self.TILE_SIZE, player_Tile[1])):
                waitForMove = True
            if waitForMove:
                time.sleep(0.2)
                self.Route_Player()


    # Loads the known npcs to watch out for when checking if a tile is empty
    def LoadAreaNPCs(self):
        areaName = "..\\littleroot_moveables"
        npcs = []
        for obj in os.listdir(areaName):
            if os.path.isfile(areaName + "\\" + obj):
                if obj.endswith(".png"):
                    npcs.append(cv2.imread(areaName+ "\\" +obj , 0))# Reads in pngs as grayscale
        return npcs



    # Checks of the next tile contains a known npc
    def CheckNpcTile(self, tile):
        for npc in self.npcs:
            if tm.SingleMatch(tile, npc, 0.40): # using the tile as the template in this case as the tile is always 16x16 and the npcs may not be
                return True
        return False


    # Trims the img of the npc so they are one tile high.            
    def TrimNpcShape(self):
        for indx,npc in enumerate(self.npcs):
            height = npc.shape[0] #height
            if height > 16: # Size of a standard tile
                self.npcs[indx] = IS.trim_top_pixels(npc, height - 16)






    # EXPERIMENTAL CODE
    # Checks the 3 tiles in front of the player. (Front and diagonal)
    def CheckXTiles(self,midCoords):
        #print(" Check 1x")
        tile = sg.GetScreenSnippit(self.window_id, midCoords[0], midCoords[1], self.TILE_SIZE, self.TILE_SIZE)        
        if self.CheckNpcTile(tile):
            return True
        #Below commented out as it doesn't work in conjunction with the low accuracy tile check
        """print(" Check 2x")
        tile = sg.GetScreenSnippit(self.window_id, midCoords[0] + self.TILE_SIZE, midCoords[1], self.TILE_SIZE, self.TILE_SIZE)
        if self.CheckNpcTile(tile):
            return True
        print(" Check 3x")
        tile = sg.GetScreenSnippit(self.window_id, midCoords[0] - self.TILE_SIZE, midCoords[1], self.TILE_SIZE, self.TILE_SIZE)
        if self.CheckNpcTile(tile):
            return True"""
        return False

    def CheckYTiles(self,midCoords):
        #print(" Check 1y")
        tile = sg.GetScreenSnippit(self.window_id, midCoords[0], midCoords[1], self.TILE_SIZE, self.TILE_SIZE)
        if self.CheckNpcTile(tile):
            return True
        #Below commented out as it doesn't work in conjunction with the low accuracy tile check
        """print(" Check 2y")
        tile = sg.GetScreenSnippit(self.window_id, midCoords[0], midCoords[1], self.TILE_SIZE + self.TILE_SIZE, self.TILE_SIZE)
        if self.CheckNpcTile(tile):
            return True
        print(" Check 3y")
        tile = sg.GetScreenSnippit(self.window_id, midCoords[0], midCoords[1] - self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
        if self.CheckNpcTile(tile):
            return True"""
        return False
        
