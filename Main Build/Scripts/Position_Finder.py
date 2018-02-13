import os
import ImgSplit as IS
import TemplateMatch as TM # May not need if going down route of comparing hashes
import Tile_Classes as TC
import numpy as NP
import cv2
import ScreenGrab as SG
import _pickle as pickle
import hashlib # Used for finding out the player's direction

# Load the area map into memory
# Grab the emulator image and split it into tiles
# Compare each tile of the emulator to the "unique" tiles of the area map
# If match is found, calculate player's position based on play-tile distance

TILE_SIZE = 16

def Load_Area(dir):
    with open(dir, "rb") as file:
        area = pickle.load(file)
    return area

def Emulator_Split(img):
    
    img = IS.trim_top_pixels(img, 8)
    img = IS.trim_bottom_pixels(img, 8)
    return IS.Img_split_to_memory_grid(img)

def Compare_Emulator_To_pyGrid(pyGrid,emTiles):
    for row in pyGrid:
        for t in row:
            if isinstance(t.unique_img, NP.ndarray):  
                for rowIndx,emRow in enumerate(emTiles):
                    for tileIndx,emTile in enumerate(emRow):
                        match = TM.SingleMatch(emTile,t.unique_img)

                        if match == False:
                            continue
                        elif match == True:
                            print("Tile match found at: " + str(t.pos))
                            return [t.pos,(tileIndx,rowIndx)] #t.pos  is the map coords, the tuple is the screen pos
                        else:
                            return None

def FindPos(img, pyGrid, emTiles):

    World_And_Emu_Pos = Compare_Emulator_To_pyGrid(pyGrid, emTiles)

    if World_And_Emu_Pos == None:
        return None
    PlayerPos = PlayerToWorld(World_And_Emu_Pos) #Finding player's position in the world
    emPos = pyGridToWindow(World_And_Emu_Pos[1], TILE_SIZE)
    cv2.rectangle(img,(emPos[0],emPos[1] + 8) #Plus 8 because we cut off the top of the emulator window when doing tile calculations, so when drawing to the screen we need to offset the y axis by 8
                  ,(emPos[0] + TILE_SIZE, emPos[1] + TILE_SIZE + 8)
                  ,(0,255,255),2) 
    cv2.imshow('detected', img)
    cv2.waitKey(1)
    return PlayerPos

def pyGridToWindow(coords,scale):
    return (coords[0]*scale, coords[1]*scale)

def PlayerToWorld(uniquePosInfo):

    PLAYER_WINDOW_POS = (8,5) 

    uniqueTileWindow = uniquePosInfo[1]
    uniqueTileGrid = uniquePosInfo[0]

    windowPosDifference = (PLAYER_WINDOW_POS[0] - uniqueTileWindow[0], PLAYER_WINDOW_POS[1] - uniqueTileWindow[1])
    playerGridPos = (uniqueTileGrid[0] + windowPosDifference[0] - 1,uniqueTileGrid[1] + windowPosDifference[1] -1)
    #print("Player Grid Pos:" + str(playerGridPos))

    return playerGridPos

def FindPlayerFace(window_id):
    img = SG.GetScreenSnippit(window_id,115,74,10,4)
    imgHash = hashlib.md5(img.tostring()).hexdigest()

    dire = "..\\player_facing"
    playerFaces = []
    for obj in os.listdir(dire):
        if os.path.isfile(dire + "\\" + obj):
            if obj.endswith(".bmp"):
                playerFaces.append((obj,cv2.imread(dire+ "\\" +obj)))# Reads in pngs as grayscale
    
    for indx,f in enumerate(playerFaces):
        playerFaces[indx] = (f[0],hashlib.md5(f[1].tostring()).hexdigest())

    for faceHash in playerFaces:
        if faceHash[1] == imgHash:
            print("Player is facing: " + faceHash[0][0])
            return faceHash[0][0]
