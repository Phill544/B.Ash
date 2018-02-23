import hashlib
import os
from PIL import Image

# Black = Non-Walkable && Non-Interactable E.g Walls and Trees
# Red = Non-Walkable && Interactable E.g Signs and People
# White = Walkable && Non-Interactable E.g Floors
# Green = Walkable && Interactable E.g Grass
# Yellow = Walkable && Non-Interactable E.g Portals

BLACK = (0, 0, 0, 255)
RED = (255, 0, 0, 255)
WHITE = (255, 255, 255, 255)
GREEN = (24, 207, 0, 255)
YELLOW = (220, 217, 0, 255)

BlackTile = []
RedTile = []
WhiteTile = []
GreenTile = []
YellowTile = []

ALLLISTS = []

width = 24
height = 24
background = (0, 0, 0, 0)

image = Image.new("RGBA", (width, height), background)
pixels = image.load()

ColourList = [BLACK, RED, WHITE, GREEN, YELLOW]


def ListAndHashDirectory(BlackTilesDir, RedTilesDir, WhiteTilesDir, GreenTilesDir, YellowTilesDir):
    os.chdir(BlackTilesDir)
    print(os.getcwd())
    for filename in os.listdir(os.getcwd()):
        BlackTile.append(hashlib.md5(open(filename, 'rb').read()).hexdigest())

    os.chdir(RedTilesDir)
    print(os.getcwd())    
    for filename in os.listdir(os.getcwd()):
        RedTile.append(hashlib.md5(open(filename, 'rb').read()).hexdigest())

    os.chdir(WhiteTilesDir)
    print(os.getcwd())    
    for filename in os.listdir(os.getcwd()):
        WhiteTile.append(hashlib.md5(open(filename, 'rb').read()).hexdigest())

    os.chdir(GreenTilesDir)
    print(os.getcwd())    
    for filename in os.listdir(os.getcwd()):
        GreenTile.append(hashlib.md5(open(filename, 'rb').read()).hexdigest())

    os.chdir(YellowTilesDir)
    print(os.getcwd())    
    for filename in os.listdir(os.getcwd()):
        YellowTile.append(hashlib.md5(open(filename, 'rb').read()).hexdigest())

    os.chdir(r'C:\Users\Lazy\Desktop\Pathfindingtest\01_Littleroot\Tiles')
    Combinedlists(os.getcwd())

def Combinedlists(ALLTILESDIR):
    ColourCount = 0
    
    for filename in os.listdir(ALLTILESDIR):
        thing = (hashlib.md5(open(filename, 'rb').read()).hexdigest())
        
        for i in BlackTile:
            if thing in i:
                thing2 = filename.replace('.bmp','')
                thingo = int(thing2.split(',')[1])
                thingy = int(thing2.split(',')[0])
                pixels[thingo, thingy] = BLACK

        for i in RedTile:
            if thing in i:
                thing2 = filename.replace('.bmp','')
                thingo = int(thing2.split(',')[1])
                thingy = int(thing2.split(',')[0])
                pixels[thingo, thingy] = RED
        
        for i in WhiteTile:
            if thing in i:
                thing2 = filename.replace('.bmp','')
                thingo = int(thing2.split(',')[1])
                thingy = int(thing2.split(',')[0])
                pixels[thingo, thingy] = WHITE

        for i in GreenTile:
            if thing in i:
                thing2 = filename.replace('.bmp','')
                thingo = int(thing2.split(',')[1])
                thingy = int(thing2.split(',')[0])
                pixels[thingo, thingy] = GREEN

        for i in YellowTile:
            if thing in i:
                thing2 = filename.replace('.bmp','')
                thingo = int(thing2.split(',')[1])
                thingy = int(thing2.split(',')[0])
                pixels[thingo, thingy] = YELLOW
                
    os.chdir(r'C://Users//Lazy//Desktop')   
    image.save("image.png")
    
ListAndHashDirectory(r'C:\Users\Lazy\Desktop\Pathfindingtest\01_Littleroot\00_Walls',
                     r'C:\Users\Lazy\Desktop\Pathfindingtest\01_Littleroot\02_Interactables',
                     r'C:\Users\Lazy\Desktop\Pathfindingtest\01_Littleroot\01_Floors',
                     r'C:\Users\Lazy\Desktop\Pathfindingtest\01_Littleroot\04_AttackZones',
                     r'C:\Users\Lazy\Desktop\Pathfindingtest\01_Littleroot\03_Portals')
