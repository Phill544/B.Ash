

# This script contains utility functions to do with data retrieved from emulator


# This only works if the data is DEFINITELY chars.
def HexValsToChars(data):

    # Remove any whitespace
    data = data.replace(" ","")

    # If string begins with '0x' remove it
    if data.startswith("0x"):
        data = data[2:]

    converted = ""
    
    for byte in chunker(data, 2):
        xHex = int(byte,16)
        xInt = xHex - 0x7a # 0x7a is the conversion value from pokemon encoding to ASCI


        if xHex == 255:
            break
        
        #converted += str(hex(xInt)[2:])
        converted += chr(xInt)

    return converted


#Converts data from little to big endian
def FlipDataEndian(data):

    if len(data) % 4 != 0:
        print("Trying to flip an uneven amount of bytes. CHECK FLIPDATAENDIAN")
        return

    byteLenth = len(data) / 2

    flippedData = ""
    currentPos = 0
    counter = 0

    while counter <= byteLenth:
        a = data[currentPos:currentPos+2]
        currentPos += 2
        b = data[currentPos:currentPos+2]
        currentPos +=2
        flippedData += b + a
        
        counter += 1

    return flippedData                         


#Use this when python is shortening your starting hex values. Ie if you need to read 4 values '003f' but it is being shortened to '3f'
def AddZeros(strVal):

    if strVal.startswith("0x"):
        strVal = strVal[2:]
    
    offset = len(strVal) % 4
    if offset != 0:
            return ("0"*(4-offset))+strVal
    else:
            return strVal
  

# A function that allows a string to be iterated over in chunks.
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
