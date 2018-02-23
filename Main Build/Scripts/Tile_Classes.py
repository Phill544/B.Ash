import cv2

###########################################################
# These classes are used as part of the pyGrids for       #
# a more accurate player movement.                        #
###########################################################

class Tile:
    # Basic Tile Class

    pos = (-1,-1)
    walkable = False
    interactable = False
    playerFace = ""
    unique_img = None #Takes an image


    def __init__(self, p , w, i, f = ""):
        self.pos = p
        self.walkable = w
        self.interactable = i
        self.playerFace = f

        #These four values are used for pathfinding
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None

    def tile_print(self):
        print("Position : " + str(self.pos))
        print("Walkable: " + str(self.walkable))
        print("Interactable: " + str(self.interactable))
        print("Player Direction: " + self.playerFace)

    def grab_uniq_img(self):
        return cv2.imread("..\\littleroot_tiles\\" + str(self.pos[1]-1) + "," + str(self.pos[0]-1) + ".bmp")

    #Definitions for pathfinding
    def __lt__(self, other):
        return(self.pos < other.pos)
    def __le__(self, other):
        return(self.pos <= other.pos)
    def __eq__(self, other):
        return(self.pos == other.pos)
    def __ne__(self, other):
        return(self.pos != other.pos)
    def __gt__(self, other):
        return(self.pos > other.pos)
    def __ge__(self, other):
        return(self.pos >= other.pos)

# A transition tile is a tile that when walked on, will change the player's
# current region.
class Transition(Tile):

    newArea = ""
    newCoord = (-1,-1)

    def __init__(self, p , w, i, f, a, c ):
        Tile.__init__(self, p , w, i, f)
        self.newArea = a
        self.newCoord = c

    #Definitions for pathfinding
    def __lt__(self, other):
        return(self.pos < other.pos)
    def __le__(self, other):
        return(self.pos <= other.pos)
    def __eq__(self, other):
        return(self.pos == other.pos)
    def __ne__(self, other):
        return(self.pos != other.pos)
    def __gt__(self, other):
        return(self.pos > other.pos)
    def __ge__(self, other):
        return(self.pos >= other.pos)

class Item(Tile):

    item_id = -1

    def __init__(self, p , w, i, f = "", _item_id = -1 ):
        Tile.__init__(self, p , w, i, f)
        self.item_id = _item_id

class Obstacle(Tile):
    ob_type = -1 # Each number is a different obstacle, e.g. a rocksmash rock may have an id of 2 and a cut tree may have id of 3

    def __init__(self, p , w, i, f = "", _ob_type = -1 ):
        Tile.__init__(self, p , w, i, f)
        self.ob_type = _ob_type
   

def TransFromUnknown(pos,walkable,interactable, facing, newArea, newCoord):    
    return Transition(pos, walkable, interactable, facing, newArea, newCoord)

def TileFromUnknown(pos,walkable,interactable, facing):
    return Tile(pos, walkable, interactable, facing)
