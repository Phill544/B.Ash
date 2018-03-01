import MemoryReader as MR
import time #For testing purposes

class DataFinder():

    def __init__(self):
        self.mr = MR.MemoryReader()


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

print("Hit enter to start")
input()

df = DataFinder()

while True:
    time.sleep(1)
    print(df.FindCoords())
    
