

# Transition Areas
area[0][11] = tc.TransFromUnknown(area[0][11], True, False, 'n', 'route_101')
area[0][10] = tc.TransFromUnknown(area[0][10], True, False, 'n', 'route_101')
area[8][5] = tc.TransFromUnknown(area[8][5], True, False, 'n', 'male_room')
area[8][14] = tc.TransFromUnknown(area[8][14], True, False, 'n', 'female_room')
area[16][7] = tc.TransFromUnknown(area[16][7], True, False, 'n', "lab")


# Interactive Tiles
area[8][7] = tc.TileFromUnknown(area[8][7], False,True, 'swn')
area[8][12] = tc.TileFromUnknown(area[8][12], False,True, 'sen')
area[13][15] = tc.TileFromUnknown(area[13][15], False, True, "")
area[17][6] = tc.TileFromUnknown(area[17][6], False, True, 'ewn')



# Unique Tiles
#area[16][7].unique_img = cv2.imread("..\\littleroot_tiles\\" + str(area[16][7].pos[1]) + "," + str(area[16][7].pos[0]-1) + ".bmp")
