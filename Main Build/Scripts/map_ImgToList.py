
###########################################################
# This script is used to convert a pixel map to a 2D list #
###########################################################


import cv2
import os
import Tile_Classes as tc
import copy

# RULES FOR MAKING AN AREA:
# Area must be a square shape

path = ""
while(os.path.isfile(path) == False):
    print("Give absolute path to image.")
    path = input()


img = cv2.imread(path)

WHITE = 255
BLACK = 0

dft_walkable = tc.Tile( (-1,-1), True, False)
dft_non_walkable = tc.Tile( (-1,-1), False, False)

area = []

for yindx,col in enumerate(img):
    row = []
    for xindx,pixel in enumerate(col):        
        if(pixel[0] == WHITE and pixel[1] == WHITE and pixel[2] == WHITE):
                #print("Walkable Tile Found")
                new_tile = copy.copy(dft_walkable)
                new_tile.pos = (xindx,yindx)
                row.append(new_tile)

                
        elif(pixel[0] == BLACK and pixel[1] == BLACK and pixel[2] == BLACK):
                #print("Non-Walkable Tile Found")
                new_tile = copy.copy(dft_non_walkable)
                new_tile.pos = (xindx,yindx)
                row.append(new_tile)

        else:
            print("Other type tile found, need manual creation at: " + str(xindx) + ", " + str(yindx))
            row.append((xindx,yindx))
            # Create none type in position and update it manually
    area.append(row)

for a in area:
    print(a)
    print()
                

# TODO: Automatically save the area in pickle format so it may be loaded elsewhere.
