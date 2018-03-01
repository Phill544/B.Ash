import MemoryReader as MR
import time #For testing purposes

class DataFinder():

    def __init__(self):
        self.mr = MR.MemoryReader()

        #TODO: Complile list of all areas.
        self.areas = {
            0x00 : "littleroot",
            0x01: "oldale",
            0x10 : "route_101"
            }

        #TODO: Find if bike gives same values
        self.facing = {
            0x00 : "UNKNOWN",
            0x01 : "south",
            0x02 : "north",
            0x03 : "west",
            0x04 : "east"
            }


    def FindYPos(self):
        PTR_LOC = 0x005B0604
        OFFSET = 0x25736

        ptr = self.mr.FindPointerData(PTR_LOC)
        data = self.mr.FindOffsetData(ptr, OFFSET, 1)

        return data[0]

    def FindXPos(self):
        PTR_LOC = 0x005B0604
        OFFSET = 0x25734

        ptr = self.mr.FindPointerData(PTR_LOC)
        data = self.mr.FindOffsetData(ptr, OFFSET, 1)

        return data[0]

    def FindCoords(self):
        x = self.FindXPos()
        y = self.FindYPos()

        return (x,y)

    def FindArea(self):
        PTR_LOC = 0x005B0604
        OFFSET = 0x2E83C

        ptr = self.mr.FindPointerData(PTR_LOC)
        data = self.mr.FindOffsetData(ptr, OFFSET, 1)

        return self.areas[data[0]]


    def FindFacing(self):
        PTR_LOC = 0x005B0600
        OFFSET = 0x48C0

        ptr = self.mr.FindPointerData(PTR_LOC)
        data = self.mr.FindOffsetData(ptr, OFFSET, 1)

        return self.facing[data[0]]

'''
print("Hit enter to start")
input()

df = DataFinder()

while True:
    time.sleep(1)
    print(df.FindCoords())
    print("The current area is: " + df.FindArea())
    print(" Player Facing: " + df.FindFacing())
   ''' 
