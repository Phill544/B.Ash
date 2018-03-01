from ctypes import *
from ctypes.wintypes import *

import psutil


# Create MemoryReader object

# For pointers:
# Call FindData(*memory_address*,4)  ---- where memory address is the address of the pointer, and 4 is beacuse there are 4 bytes to a pointer
# This will return the memory address for the value you want.
# Flip the address so that d4 c3 b2 a1 --> a1 b2 c3 d4.
# Add the offset to the new memory address eg:
# newAddress = 0x04de8b00
# offset = 25736 (This is a hex value)
# dataLocation = newAddress + offset == 0x4e0e236
# Finally, call FindData(dataLocation, *size of data*) to retrieve the value you want
# Where size of data is the size in bytes of the data you need. 

class MemoryReader():

    def __init__(self):
        self.pid = self.FindPid()


    def FindPid(self):
        PROCNAME = "VisualBoyAdvance.exe"

        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:  
                print(proc)                
                return proc.pid
            
        #If the function hasn't returned by now, no emulator was found.
        print("Visual Boy Emulator not detected! Please ensure you have it running and restart the script. \n")
        print("If it is running but not being detected, ensure that the file name for the emulator is exactly \"VisualBoyAdvance.exe\" ")

    # Takes a hex memory location and returns data (in bytes) at that position. Where length is the amount of data in bytes
    def FindData(self, address, length):

        if self.pid == None:
            print("process id has not been found! Ensure emulator is running before calling this function.")
            return False

        
        OpenProcess = windll.kernel32.OpenProcess
        ReadProcessMemory = windll.kernel32.ReadProcessMemory
        CloseHandle = windll.kernel32.CloseHandle
        PROCESS_ALL_ACCESS = 0x1F0FFF

        data = create_string_buffer(length)

        processHandle = OpenProcess(PROCESS_ALL_ACCESS, False, int(self.pid))
        ReadProcessMemory(processHandle, address, data, length, 0)
        CloseHandle(processHandle)

        return data.raw



    def FlipHexString(self,value):
        return "".join(reversed([value[i:i+2] for i in range(0, len(value), 2)]))




    def FindPointerData(self, address):
        rawData = self.FindData(address, 4)
        flip = self.FlipHexString(rawData.hex())
        return int(flip,16)



    def FindOffsetData(self, address, offset, size):
        loc = address + offset
        ans = self.FindData(loc,size)
        return ans
