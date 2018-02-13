import cv2 # To compare images
import numpy as np # To aid cv2
import os # for going through directories

def TemplateTest(image):

    screenshot = np.asarray(image,dtype=np.uint8) # "dtype=np.uint8" is needed as it treats the pillow screenshot as the correct colours
    
    img_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    template_g = cv2.imread("..\Areas\\Towns\\littleroot\\ID_overworld.png", 0) #read in as grayscale
    w,h = template_g.shape[::-1]

    res = cv2.matchTemplate(img_gray, template_g, cv2.TM_CCOEFF_NORMED)
    threshold = 0.90
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(screenshot,pt,(pt[0]+w, pt[1]+h),(0,255,255),2)
        cv2.imshow('detected', screenshot)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Use this function for calling from other modules.
def GrabAreas():
    lAreas = {}
    currentPath = "..\\Areas"
    __GrabAreas(lAreas, currentPath)
    return lAreas


# Never use this function unless you consult with Phill
def __GrabAreas(areas, currentPath):
    for obj in os.listdir(currentPath):
        if os.path.isfile(currentPath + "\\" + obj):
            if obj.endswith(".png"):
                areas[obj] = cv2.imread(currentPath+ "\\" +obj , 0)# Reads in templates are grayscale
        if os.path.isdir(currentPath + "\\" + obj):
            __GrabAreas(areas,currentPath + "\\" + obj)

def MatchAreasDraw(screenshot, templates):
    
    img_np = np.asarray(screenshot,dtype=np.uint8)
    img_gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    for templ_name,template in templates.items():
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        loc = np.where(res >= threshold)

        if loc[0].size > 0:
            print("Current area is: " + templ_name[:-4])
            w,h = template.shape[::-1]
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_np,pt,(pt[0]+w, pt[1]+h),(0,255,255),2)
                cv2.imshow('detected', img_np)
                cv2.waitKey(1)
                return True
            
def MatchArea(screenshot, templates):
    
    img_np = np.asarray(screenshot,dtype=np.uint8)
    img_gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    for templ_name,template in templates.items():
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        loc = np.where(res >= threshold)

        if loc[0].size > 0:
            print("Current area is: " + templ_name[:-4])
            return templ_name[:-4]
    return None

def SingleMatch(img,template, _threshold = 0.99):

    # Make this WAY more efficient if I store the images as grayscale by default
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        
    if len(template.shape) == 3:
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = _threshold
    loc = np.where(res >= threshold)

    # May need to be changed to size == 1 if comparing an template to a tiled image
    if loc[0].size > 0:
        return True
    else:
        return False
