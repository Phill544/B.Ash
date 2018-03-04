import MemoryReader as MR
import ByteUtilFunctions as util

class Pokemon():

    def __init__(self, pokemon_data):

        # Dictionary of data names and their lengths in bytes
        self.dataSizes = {
            "P_VALUE"           : 4,
            "OT_ID"             : 4,
            "NICKNAME"          : 10,
            "LANGUAGE"          : 2,
            "OT_NAME"           : 7,
            "MARKINGS"          : 1,
            "CHECKSUM"          : 2,
            "?????"             : 2,
            "DATA"              : 48,
            "STATUS_CONDITION"  : 4,
            "LEVEL"             : 1,
            "POKERUS_REMAINING" : 1,
            "CURRENT_HP"        : 2,
            "TOTAL_HP"          : 2,
            "ATTACK"            : 2,
            "DEFENSE"           : 2,
            "SPEED"             : 2,
            "SP.ATTACK"         : 2,
            "SP.DEFENSE"        : 2
            }
        
        
        self.init_pokemon(pokemon_data)



    def init_pokemon(self,data):

        data = data.replace(" ","")

        if len(data) != 200:
            print("Pokemon needs 100 bytes of data to initialise")
            return
        
        bytePos = 0

        dataSize = self.dataSizes["P_VALUE"] * 2 # x2 because the bytes are two characters
        rawVal = data[bytePos:bytePos + dataSize]
        self.p_value = util.FlipDataEndian(rawVal)
        bytePos += dataSize 

        dataSize = self.dataSizes["OT_ID"] * 2 
        rawVal = data[bytePos:bytePos + dataSize]
        self.ot_id = util.FlipDataEndian(rawVal)
        bytePos += dataSize

        dataSize = self.dataSizes["NICKNAME"] * 2 
        encodedName = data[bytePos:bytePos + dataSize]
        self.nickname = util.HexValsToChars(encodedName)
        bytePos += dataSize

        dataSize = self.dataSizes["LANGUAGE"] * 2 
        rawVal = data[bytePos:bytePos + dataSize]
        self.lang = util.FlipDataEndian(rawVal)
        bytePos += dataSize

        dataSize = self.dataSizes["OT_NAME"] * 2 
        encodedName = data[bytePos:bytePos + dataSize]
        self.ot_name = util.HexValsToChars(encodedName)
        bytePos += dataSize

        dataSize = self.dataSizes["MARKINGS"] * 2
        self.markings = data[bytePos:bytePos + dataSize]
        bytePos += dataSize 

        dataSize = self.dataSizes["CHECKSUM"] * 2 
        rawVal = data[bytePos:bytePos + dataSize]
        self.checksum = util.FlipDataEndian(rawVal)
        bytePos += dataSize

        dataSize = self.dataSizes["?????"] * 2 
        rawVal = data[bytePos:bytePos + dataSize]
        self.unknown = util.FlipDataEndian(rawVal)
        bytePos += dataSize

        dataSize = self.dataSizes["DATA"] * 2
        self.data_substructure = DataSubstructure(
            self.p_value,
            self.ot_id,
            data[bytePos:bytePos + dataSize])
        bytePos += dataSize 
        
        dataSize = self.dataSizes["STATUS_CONDITION"] * 2 
        rawVal = data[bytePos:bytePos + dataSize]
        self.status = util.FlipDataEndian(rawVal)
        bytePos += dataSize

        dataSize = self.dataSizes["LEVEL"] * 2 
        self.level = int(data[bytePos:bytePos + dataSize],16)
        bytePos += dataSize

        dataSize = self.dataSizes["POKERUS_REMAINING"] * 2 
        self.pokerus_remaining = data[bytePos:bytePos + dataSize]
        bytePos += dataSize

        dataSize = self.dataSizes["CURRENT_HP"] * 2 
        rawVal = data[bytePos:bytePos + dataSize]
        self.current_hp = int(util.FlipDataEndian(rawVal), 16)
        bytePos += dataSize

        dataSize = self.dataSizes["TOTAL_HP"] * 2 
        rawVal = data[bytePos:bytePos + dataSize]
        self.total_hp = int(util.FlipDataEndian(rawVal), 16)
        bytePos += dataSize

        dataSize = self.dataSizes["ATTACK"] * 2 
        rawVal = data[bytePos:bytePos + dataSize]
        self.attack = int(util.FlipDataEndian(rawVal), 16)
        bytePos += dataSize

        dataSize = self.dataSizes["DEFENSE"] * 2 
        rawVal = data[bytePos:bytePos + dataSize]
        self.defense = int(util.FlipDataEndian(rawVal), 16)
        bytePos += dataSize

        dataSize = self.dataSizes["SPEED"] * 2 
        rawVal = data[bytePos:bytePos + dataSize]
        self.speed = int(util.FlipDataEndian(rawVal), 16)
        bytePos += dataSize

        dataSize = self.dataSizes["SP.ATTACK"] * 2 
        rawVal = data[bytePos:bytePos + dataSize]
        self.spA = int(util.FlipDataEndian(rawVal), 16)
        bytePos += dataSize

        dataSize = self.dataSizes["SP.DEFENSE"] * 2 
        rawVal = data[bytePos:bytePos + dataSize]
        self.spD = int(util.FlipDataEndian(rawVal), 16)
        bytePos += dataSize


    def print_basic_data(self):
        print("********************************")
        print("Pokemon Basic Details")
        print("Nickname: " + self.nickname)
        print("Pokemon ID: " + str(self.data_substructure.species))
        print("P_Value: " + self.p_value)
        print("SubStruct Order: " + self.data_substructure.structure_order[self.data_substructure.order])
        print("Original Trainer ID: " + self.ot_id)
        print("Level: " + str(self.level))
        print("Current HP: " + str(self.current_hp))
        print("Total HP: " + str(self.total_hp))
        print("Held Item ID: " + str(self.data_substructure.held_item))
        print("Total Exp: " + str(self.data_substructure.experience))
        print("Moves: ")
        print("Move 1 ID: " + str(self.data_substructure.move1) + " Remaining Uses: " + str(self.data_substructure.pp1))
        print("Move 2 ID: " + str(self.data_substructure.move2) + " Remaining Uses: " + str(self.data_substructure.pp2))
        print("Move 3 ID: " + str(self.data_substructure.move3) + " Remaining Uses: " + str(self.data_substructure.pp3))
        print("Move 4 ID: " + str(self.data_substructure.move4) + " Remaining Uses: " + str(self.data_substructure.pp4))              
        print("********************************")



class DataSubstructure():

    def __init__(self, pVal, ot_id , data):

        self.structure_order = {
             0  :    "GAEM",  1  :    "GAME",
             2  :    "GEAM",  3  :    "GEMA",
             4  :    "GMAE",  5  :    "GMEA",
             6  :    "AGEM",  7  :    "AGME",
             8  :    "AEGM",  9  :    "AEMG",
            10  :    "AMGE", 11  :    "AMEG",
            12  :    "EGAM", 13  :    "EGMA",
            14  :    "EAGM", 15  :    "EAMG",
            16  :    "EMGA", 17  :    "EMAG",
            18  :    "MGAE", 19  :    "MGEA",
            20  :    "MAGE", 21  :    "MAEG",
            22  :    "MEGA", 23  :    "MEAG",
            }

        self.pVal = pVal
        self.ot_id  = ot_id


        self.FindOrder()
        self.FindKey()

        self.CalculateData(data)

    def FindOrder(self):
        self.order = int(self.pVal,16) % 24


    def FindKey(self):
        self.key = (int(self.pVal, 16) ^ int(self.ot_id, 16))
   
        

        
    def CalculateData(self, data):
        
        #Figure out which substructure is being read at for each loop
        #Read 4 bytes at a time,
        #flip them to big endian
        #XOR with key
        #Profit

        orderStr = self.structure_order[self.order]
        bytePos = 0

        for char in orderStr:

            if char == 'G':
                #decode as growth
                self.DecodeGrowth(data[bytePos:bytePos + 24]) # 24 Because 12 bytes takes 24 characters
            elif char == 'A':
                #decode as attacks
                self.DecodeAttacks(data[bytePos:bytePos + 24])
            elif char == 'E':
                #Decode as Evs
                self.DecodeEVsAndCond(data[bytePos:bytePos + 24])
            elif char == 'M':
                # Decode as Miscellaneous
                self.DecodeMisc(data[bytePos:bytePos + 24])

            bytePos += 24 # Increment bytePos so that next iteration it is reading the correct bytes
        

    def DecodeGrowth(self, data):

        self.species, self.held_item = self.DecodeDuo(data[0:8])
        self.experience = self.DecodeSingle(data[8:16])
        
        flippedVal = util.FlipDataEndian(data)
        decodedVal = hex((self.key ^ int(flippedVal, 16)))[2:]
        decodedVal = util.AddZeros(decodedVal) 
        self.pp_bonuses = int(decodedVal[0:2],16)
        self.friendship = int(decodedVal[2:4],16)
        unknown = int(decodedVal[4:8],16) # This has an unknown use. Therefore isn't recorded.




    def DecodeAttacks(self, data):
        self.move1 ,self.move2 = self.DecodeDuo(data[0:8])
        self.move3 ,self.move4 = self.DecodeDuo(data[8:16])
        
        self.pp1, self.pp2, self.pp3, self.pp4 = self.DecodeQuad(data[16:24])


    def DecodeEVsAndCond(self, data):

        self.ev_hp, self.ev_atk, self.ev_def, self.ev_spd = self.DecodeQuad(data[0:8])
        self.ev_sAtk, self.ev_sDef, self.coolness, self.beauty = self.DecodeQuad(data[0:8])
        self.cuteness, self.smartness, self.toughness, self.feel = self.DecodeQuad(data[0:8])                                                                            
                                                                            

    def DecodeMisc(self, data):

        flippedVal = util.FlipDataEndian(data)
        decodedVal = hex((self.key ^ int(flippedVal, 16)))[2:]
        decodedVal = util.AddZeros(decodedVal)

        self.pokerus_status = int(decodedVal[0:2],16)
        self.met_location = int(decodedVal[2:4],16)
        self.origins_info = int(decodedVal[4:8],16)

        self.iv_egg_ability = self.DecodeSingle(data[8:16])
        self.ribbons_and_obedience = self.DecodeSingle(data[16:24])
               


    def DecodeDuo(self,rawVal):
        flippedVal = util.FlipDataEndian(rawVal)
        decodedVal = hex(self.key ^ int(flippedVal, 16))[2:]
        
        #Make sure the isn't any zeros missing off the front
        if len(decodedVal) != 8:
            decodedVal = ("0"*(8-len(decodedVal))) + decodedVal         
        return (int(decodedVal[0:4],16),int(decodedVal[4:8],16))

    #PP results may be returned in the wrong order?
    def DecodeQuad(self,rawVal):
        flippedVal = util.FlipDataEndian(rawVal)
        decodedVal = hex((self.key ^ int(flippedVal, 16)))[2:]
        if len(decodedVal) != 8:
            decodedVal = ("0"*(8-len(decodedVal))) + decodedVal
            
        # Moves seem to need to be sent out of order so that move order: 2143. Probably something to do with little endian byte type
        return [ int(decodedVal[2:4],16), int(decodedVal[0:2],16),
                 int(decodedVal[6:8],16),int(decodedVal[4:6],16)]        


    def DecodeSingle(self, rawVal):
        flippedVal = util.FlipDataEndian(rawVal)
        decodedVal = hex((self.key ^ int(flippedVal, 16)))[2:]
        if len(decodedVal) != 8:
            decodedVal = ("0"*(8-len(decodedVal))) + decodedVal  
        rearrangedVal = decodedVal[4:8] + decodedVal[0:4]
        return int(rearrangedVal,16)        


    
        

class PartyInfo():

    def __init__(self):

        self.PTR_LOC = 0x005AF940
        self.pos1_offset = 0x4360
        self.pos2_offset = 0x43C4
        self.pos3_offset = 0x4428
        self.pos4_offset = 0x448C
        self.pos5_offset = 0x44F0
        self.pos6_offset = 0x4554

        self.mr = MR.MemoryReader()
        self.base_ptr = self.mr.FindPointerData(self.PTR_LOC)

        self.UpdateParty()

    def UpdateParty(self):

        self.poke1 = Pokemon(self.mr.FindOffsetData(self.base_ptr, self.pos1_offset, 100).hex())
        self.poke2 = Pokemon(self.mr.FindOffsetData(self.base_ptr, self.pos2_offset, 100).hex())

    def Print_Info(self):
        self.poke1.print_basic_data()
        self.poke2.print_basic_data()
