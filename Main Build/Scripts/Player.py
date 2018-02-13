
class Player:

    # pos # player's pos on current map
    #facing # Vales can be 'n', 's', 'e', 'w', or ''
    #currentArea

    def __init__(self, _pos = (-1,-1), _facing = "", area = ""):
        self.pos = _pos
        self.facing = _facing
        self.currentArea = area

    def printInfo(self):
        print("Current area: " + self.currentArea)
        print("Current position: " + str(self.pos))
        print("Direction facing: " + self.facing)

