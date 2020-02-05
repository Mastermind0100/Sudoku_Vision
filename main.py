import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image
from keras import models,layers
from keras.datasets import mnist
from keras.utils import to_categorical
import operator
import os
import platform
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filename', action='store', type=str, help='enter filename')
args = parser.parse_args()

filename = args.filename

arr_out = []
arr_result = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
model=load_model('fmodelwts.h5')

kernel = np.ones((1,1), np.uint8) 

img = cv2.imread(filename)
img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img2gray.copy(),(9,9),0)
th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

cnts,_ = cv2.findContours(th3,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
c = max(cnts, key = cv2.contourArea)

bottom_right, _ = max(enumerate([pt[0][0] + pt[0][1] for pt in c]), key=operator.itemgetter(1))
top_left, _ = min(enumerate([pt[0][0] + pt[0][1] for pt in c]), key=operator.itemgetter(1))
bottom_left, _ = min(enumerate([pt[0][0] - pt[0][1] for pt in c]), key=operator.itemgetter(1))
top_right, _ = max(enumerate([pt[0][0] - pt[0][1] for pt in c]), key=operator.itemgetter(1))

bottom_left = c[bottom_left][0]
bottom_right = c[bottom_right][0]
top_left = c[top_left][0]
top_right = c[top_right][0]

d1 = ((top_left[0]-top_right[0])**2 + (top_left[1]-top_right[1])**2)**(0.5)
d2 = ((top_left[0]-bottom_left[0])**2 + (top_left[1]-bottom_left[1])**2)**(0.5)
d3 = ((bottom_left[0]-bottom_right[0])**2 + (bottom_left[1]-bottom_right[1])**2)**(0.5)
d4 = ((bottom_right[0]-top_right[0])**2 + (bottom_right[1]-top_right[1])**2)**(0.5)

side = max([d1,d2,d3,d4])
src = np.array([top_left, top_right, bottom_right, bottom_left], dtype='float32')
dst = np.array([[0, 0], [side - 1, 0], [side - 1, side - 1], [0, side - 1]], dtype='float32')
m = cv2.getPerspectiveTransform(src, dst)
finimg = cv2.warpPerspective(img, m, (int(side), int(side)))

newimg = cv2.drawContours(img.copy(),c,-1,(0,255,0),2)

# cv2.imshow('contours', finimg)
# cv2.imwrite('square.png',finimg)


img = cv2.cvtColor(finimg,cv2.COLOR_BGR2GRAY)
rows,cols= img.shape

divr = rows//9
divc = cols//9
r = 0
c = 0

for i in range(0,9):
    for j in range(0,9):
        roi = img[r:r+divr,c:c+divc]
        c += divc
        # cv2.imshow('wassup',roi)
        # cv2.waitKey()
        _,test_image = cv2.threshold(roi,100,255,cv2.THRESH_BINARY)
        test_image = cv2.medianBlur(test_image.copy(),3)
        test_image = cv2.resize(test_image.copy(),(64,64),interpolation = cv2.INTER_AREA)
        cv2.resize(test_image,(64,64))
        # cv2.imshow('ineed2seedis',test_image)
        # cv2.waitKey()
        test_image=(image.img_to_array(test_image))/255
        test_image=np.expand_dims(test_image, axis = 0)
        result=model.predict(test_image)  
        np.reshape(result, 36)
        high = np.amax(test_image)
        low = np.amin(test_image)
        if high != low:
            maxval = np.amax(result)
            index = np.where(result == maxval)
            arr_out.append(arr_result[index[1][0]])
    r += divr
    c = 0

for i in range(len(arr_out)):
    if arr_out[i]== 'T':
        arr_out[i] = '0'

for i in range(len(arr_out)):
    arr_out[i] = int(arr_out[i])

print(arr_out)

with open('unsolved.txt', 'w') as f:
    for number in arr_out:
        f.write("%d\n" % number)

if platform.system() == 'Linux': 
    instructions = ['g++ sudoku.cpp','./a.out']
elif platform.system() == 'Windows':
    instructions = ['g++ sudoku.cpp','./a.exe']    

for command in instructions:
    os.system(command)