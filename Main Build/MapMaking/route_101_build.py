
# Transitions
area[0][8] = tc.TransFromUnknown(area[0][8], True, False, 'n', 'oldale')
area[0][9] = tc.TransFromUnknown(area[0][9], True, False, 'n', 'oldale')
area[0][10] = tc.TransFromUnknown(area[0][10], True, False, 'n', 'oldale')
area[0][11] = tc.TransFromUnknown(area[0][11], True, False, 'n', 'oldale')

area[19][10] = tc.TransFromUnknown(area[19][10], True, False, 's', 'littleroot')
area[19][11] = tc.TransFromUnknown(area[19][11], True, False, 's', 'littleroot')

# Change so the player may route from the north and jump over
# "Interactables"
area[6][7] = tc.TileFromUnknown(area[6][7], False,False, 'n')
area[6][8] = tc.TileFromUnknown(area[6][8], False,False, 'n')
area[6][9] = tc.TileFromUnknown(area[6][9], False,False, 'n')
area[6][10] = tc.TileFromUnknown(area[6][10], False,False, 'n')

area[7][2] = tc.TileFromUnknown(area[7][2], False,False, 'n')
area[7][3] = tc.TileFromUnknown(area[7][3], False,False, 'n')
area[7][4] = tc.TileFromUnknown(area[7][4], False,False, 'n')
area[7][5] = tc.TileFromUnknown(area[7][5], False,False, 'n')

area[9][5] = tc.TileFromUnknown(area[9][5], False,True, '')

area[13][8] = tc.TileFromUnknown(area[13][8], False,False, 'n')
area[13][9] = tc.TileFromUnknown(area[13][9], False,False, 'n')
area[13][10] = tc.TileFromUnknown(area[13][10], False,False, 'n')
area[13][11] = tc.TileFromUnknown(area[13][11], False,False, 'n')


#area[6][6].unique_img = cv2.imread("..\\route101_unq_tiles\\" + str(area[6][6].pos[1]) + "," + str(area[6][6].pos[0]) + ".bmp")

#area[7][6].unique_img = cv2.imread("..\\route101_unq_tiles\\" + str(area[7][6].pos[1]) + "," + str(area[7][6].pos[0]) + ".bmp")

#area[9][5].unique_img = cv2.imread("..\\route101_unq_tiles\\" + str(area[9][5].pos[1]) + "," + str(area[9][5].pos[0]) + ".bmp")
