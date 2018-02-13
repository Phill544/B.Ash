import sys
import hashlib
import cv2
import math
import os

# Splits image into 16x16 tiles and saves them to a relative folder to current working directory
def Img_split(img,dir):
    img_shape = img.shape
    TILE_SIZE = (16, 16)
    OFFSET = (16, 16)

    for i in range(int(math.ceil(img_shape[0]/(OFFSET[1] * 1.0)))):
        for j in range(int(math.ceil(img_shape[1]/(OFFSET[0] * 1.0)))):
            cropped_img = img[OFFSET[1]*i:min(OFFSET[1]*i+TILE_SIZE[1],
                                              img_shape[0]), OFFSET[0]*j:min(OFFSET[0]*j+TILE_SIZE[0], img_shape[1])]
            cv2.imwrite(dir + str(i) + ',' + str(j) + '.bmp', cropped_img)

# Splits an image into 16x16 tiles and returns them as a grid ( 2d list, grid[y][x])
def Img_split_to_memory_grid(img):
    img_shape = img.shape
    TILE_SIZE = (16, 16)
    OFFSET = (16, 16)
    tiles = []
    rows = []

    for i in range(int(math.ceil(img_shape[0]/(OFFSET[1] * 1.0)))):
        for j in range(int(math.ceil(img_shape[1]/(OFFSET[0] * 1.0)))):
            cropped_img = img[OFFSET[1]*i:min(OFFSET[1]*i+TILE_SIZE[1],
                                              img_shape[0]), OFFSET[0]*j:min(OFFSET[0]*j+TILE_SIZE[0], img_shape[1])]
            rows.append(cropped_img)
        tiles.append(rows)
        rows = []
    return tiles

# Splits an image into 16x16 tiles and returns them as a list
def Img_split_to_memory_list(img):
    img_shape = img.shape
    TILE_SIZE = (16, 16)
    OFFSET = (16, 16)
    tiles = []

    for i in range(int(math.ceil(img_shape[0]/(OFFSET[1] * 1.0)))):
        for j in range(int(math.ceil(img_shape[1]/(OFFSET[0] * 1.0)))):
            cropped_img = img[OFFSET[1]*i:min(OFFSET[1]*i+TILE_SIZE[1],
                                              img_shape[0]), OFFSET[0]*j:min(OFFSET[0]*j+TILE_SIZE[0], img_shape[1])]
            tiles.append(cropped_img)
    return tiles

# returns the input image minus the specified amount of pixels from the top of the image
def trim_top_pixels(img, amount):
    return img[amount:][0:]
# returns the input image minus the specified amount of pixels from the bottom of the image
def trim_bottom_pixels(img, amount):
    return img[0:][0:-amount]

# removes any identical images inside a folder, therefore keeping one copy
def remove_duplicates(dir):
    os.chdir(dir)
    unique = []
    filehash = ''
    for filename in os.listdir(dir):
        if os.path.isfile(filename):
            filehash = hashlib.md5(open(filename, 'rb').read()).hexdigest()
        if filehash not in unique:
            unique.append(filehash)
        else:
            os.remove(filename)

# removes all images that aren't unique to the folder, ie if there are two of the exact same images, both will be deleted
def keep_uniques(dir):
    
    olddir = os.getcwd()
    os.chdir(dir)
    
    files = {}
    filehash = ''

    for filename in os.listdir(dir):
        if os.path.isfile(filename):
            filehash = hashlib.md5(open(filename, 'rb').read()).hexdigest()
        if filehash not in files:
            files[filehash] = [filename]
        else:
            files[filehash].append(filename)

    pairs = []
    for k,v in files.items():
        pairs.append([k,v])

    for x in pairs:
        if(len(x[1]) > 1):
            for file in x[1]:
                os.remove(file)
    os.chdir(olddir)

# Returns a list of images which are unique to the input list, any images that have a matches are removed
def keep_uniques_memory(list_tiles): 
        
    files = {}
    filehash = ''

    for t in list_tiles:
        filehash = hashlib.md5(t.tobytes()).hexdigest()
        if filehash not in files:
            files[filehash] = [t]
        else:
            files[filehash].append(t)

    pairs = []
    for k,v in files.items():
        pairs.append([k,v])

    unique_tiles = []
    
    for x in pairs:
        if(len(x[1]) == 1):
            unique_tiles.append(x[1][0])
    return unique_tiles 
