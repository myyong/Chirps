#from __future__ import print_function
from PIL import Image
import numpy as np


url = "/Users/myong/Documents/workspace/Python/Chirps/data/africa_daily/tifs/p25/2016/chirps-v2.0.2016.01.01.tif"
im = Image.open(url)

#print(im.format, im.size, im.mode)

def printarray():
    imarray = np.array(im)
    print (imarray.shape)
#     for row in range(imarray.shape[0]):
#         for col in range(imarray.shape[1]):
#             if (imarray[row][col] > 0):
#                 print("Row: %i Col: %i Value: %i" % (row, col, imarray[row][col]))

def maxValue(imarray): 
    maxvalue = 0
    for row in range(imarray.shape[0]):
        for col in range(imarray.shape[1]):
            aValue = max(imarray[row][col])
            if (aValue > maxvalue):
                maxvalue = aValue
    return maxvalue
                
            
def modifyarray():
    newim = im.convert('RGB')
    newimarray = np.array(newim)
    maxValueOfIm = maxValue(newimarray)    
    for row in range(newimarray.shape[0]):
        for col in range(newimarray.shape[1]):
            if (max(newimarray[row][col]) > 0):
                currentValue = newimarray[row][col][0]
                newValue = (currentValue/maxValueOfIm)*255
                newimarray[row][col] = [0,0,newValue]
    img2 = Image.fromarray(newimarray, mode='RGB')
    img2.show()
    
modifyarray()
print (max([1,0,0]))
